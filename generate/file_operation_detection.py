"""File operation detection utilities for API endpoints.

This module provides utilities to detect when API endpoints involve file operations
(uploads or downloads) and determine the appropriate file handling strategy.
"""

from typing import Any, Dict, List, Optional


def is_file_upload_endpoint(endpoint: dict) -> bool:
    """Detect if an endpoint accepts file uploads.

    Args:
        endpoint: OpenAPI endpoint specification

    Returns:
        True if endpoint accepts file uploads
    """
    if "requestBody" not in endpoint:
        return False

    request_body = endpoint["requestBody"]
    if "content" not in request_body:
        return False

    content_types = request_body["content"].keys()

    # Check for file upload content types
    file_upload_types = {
        "multipart/form-data",
        "application/octet-stream",
        "image/*",
        "video/*",
        "audio/*",
        "application/pdf",
        "application/zip",
        "text/plain",  # Sometimes used for file uploads
    }

    for content_type in content_types:
        if content_type in file_upload_types:
            return True

        # Check for wildcard matches
        if content_type.startswith(("image/", "video/", "audio/", "application/")):
            return True

    return False


def is_file_download_endpoint(endpoint: dict) -> bool:
    """Detect if an endpoint returns file downloads.

    Args:
        endpoint: OpenAPI endpoint specification

    Returns:
        True if endpoint returns file downloads
    """
    if "responses" not in endpoint:
        return False

    responses = endpoint["responses"]

    # Check successful response codes (2xx)
    for status_code, response in responses.items():
        if not str(status_code).startswith("2"):
            continue

        if "content" not in response:
            continue

        content_types = response["content"].keys()

        # Check for file download content types
        file_download_types = {
            "application/octet-stream",
            "image/*",
            "video/*",
            "audio/*",
            "application/pdf",
            "application/zip",
            "text/plain",
            "text/csv",
            "application/json",  # Sometimes used for file downloads
        }

        for content_type in content_types:
            if content_type in file_download_types:
                return True

            # Check for wildcard matches
            if content_type.startswith(
                ("image/", "video/", "audio/", "application/", "text/")
            ):
                # Exclude typical API response types
                if content_type not in {"application/json", "text/html"}:
                    return True

    return False


def get_upload_content_types(endpoint: dict) -> List[str]:
    """Get content types that indicate file uploads.

    Args:
        endpoint: OpenAPI endpoint specification

    Returns:
        List of content types for file uploads
    """
    if "requestBody" not in endpoint:
        return []

    request_body = endpoint["requestBody"]
    if "content" not in request_body:
        return []

    content_types = list(request_body["content"].keys())

    # Filter for file-related content types
    file_content_types = []
    for content_type in content_types:
        if content_type in {
            "multipart/form-data",
            "application/octet-stream",
        } or content_type.startswith(("image/", "video/", "audio/", "application/")):
            file_content_types.append(content_type)

    return file_content_types


def get_download_content_types(endpoint: dict) -> List[str]:
    """Get content types that indicate file downloads.

    Args:
        endpoint: OpenAPI endpoint specification

    Returns:
        List of content types for file downloads
    """
    if "responses" not in endpoint:
        return []

    file_content_types = []
    responses = endpoint["responses"]

    # Check successful response codes (2xx)
    for status_code, response in responses.items():
        if not str(status_code).startswith("2"):
            continue

        if "content" not in response:
            continue

        content_types = list(response["content"].keys())

        for content_type in content_types:
            if content_type in {
                "application/octet-stream",
            } or content_type.startswith(
                ("image/", "video/", "audio/", "text/", "application/")
            ):
                # Exclude typical API response types
                if content_type not in {"application/json", "text/html"}:
                    if content_type not in file_content_types:
                        file_content_types.append(content_type)

    return file_content_types


def determine_upload_strategy(endpoint: dict) -> Optional[str]:
    """Determine the best upload strategy for an endpoint.

    Args:
        endpoint: OpenAPI endpoint specification

    Returns:
        'multipart', 'binary', or None
    """
    content_types = get_upload_content_types(endpoint)

    if not content_types:
        return None

    # Prefer multipart for form-data
    if "multipart/form-data" in content_types:
        return "multipart"

    # Use binary for octet-stream or specific file types
    if "application/octet-stream" in content_types:
        return "binary"

    # For other file types, prefer binary unless multiple fields are expected
    if any(
        ct.startswith(("image/", "video/", "audio/", "application/"))
        for ct in content_types
    ):
        return "binary"

    return None


def determine_download_strategy(endpoint: dict) -> Optional[str]:
    """Determine the best download strategy for an endpoint.

    Args:
        endpoint: OpenAPI endpoint specification

    Returns:
        'streaming', 'bytes', or None
    """
    content_types = get_download_content_types(endpoint)

    if not content_types:
        return None

    # Always use streaming for downloads to handle large files
    return "streaming"


def extract_file_parameter_info(endpoint: dict, data: dict) -> Dict[str, Any]:
    """Extract information about file parameters in an endpoint.

    Args:
        endpoint: OpenAPI endpoint specification
        data: Full OpenAPI specification data

    Returns:
        Dictionary with file parameter information
    """
    info: Dict[str, Any] = {
        "has_file_upload": False,
        "has_file_download": False,
        "upload_strategy": None,
        "download_strategy": None,
        "upload_content_types": [],
        "download_content_types": [],
        "file_parameters": [],
    }

    # Check for uploads
    info["has_file_upload"] = is_file_upload_endpoint(endpoint)
    if info["has_file_upload"]:
        info["upload_strategy"] = determine_upload_strategy(endpoint)
        info["upload_content_types"] = get_upload_content_types(endpoint)

    # Check for downloads
    info["has_file_download"] = is_file_download_endpoint(endpoint)
    if info["has_file_download"]:
        info["download_strategy"] = determine_download_strategy(endpoint)
        info["download_content_types"] = get_download_content_types(endpoint)

    # Extract file parameter details from multipart schemas
    if (
        info["has_file_upload"]
        and "multipart/form-data" in info["upload_content_types"]
    ):
        info["file_parameters"] = _extract_multipart_file_params(endpoint, data)

    return info


def _extract_multipart_file_params(endpoint: dict, data: dict) -> List[Dict[str, Any]]:
    """Extract file parameters from multipart/form-data schema.

    Args:
        endpoint: OpenAPI endpoint specification
        data: Full OpenAPI specification data

    Returns:
        List of file parameter dictionaries
    """
    file_params: List[Dict[str, Any]] = []

    if "requestBody" not in endpoint:
        return file_params

    request_body = endpoint["requestBody"]
    if "content" not in request_body:
        return file_params

    content = request_body["content"]
    if "multipart/form-data" not in content:
        return file_params

    multipart_content = content["multipart/form-data"]
    if "schema" not in multipart_content:
        return file_params

    schema = multipart_content["schema"]

    # Handle $ref schemas
    if "$ref" in schema:
        ref_name = schema["$ref"].replace("#/components/schemas/", "")
        if ref_name in data.get("components", {}).get("schemas", {}):
            schema = data["components"]["schemas"][ref_name]

    # Extract file parameters from properties
    if "properties" in schema:
        for param_name, param_schema in schema["properties"].items():
            param_info = _analyze_parameter_for_file(param_name, param_schema)
            if param_info:
                file_params.append(param_info)

    return file_params


def _analyze_parameter_for_file(
    param_name: str, param_schema: dict
) -> Optional[Dict[str, Any]]:
    """Analyze a parameter to determine if it's a file parameter.

    Args:
        param_name: Parameter name
        param_schema: Parameter schema

    Returns:
        File parameter info or None
    """
    # Check for explicit file format
    if param_schema.get("format") == "binary":
        return {
            "name": param_name,
            "type": "file",
            "format": "binary",
            "required": False,  # Will be updated by caller
        }

    # Check for string type with binary format
    if param_schema.get("type") == "string":
        if param_schema.get("format") in {"binary", "byte"}:
            return {
                "name": param_name,
                "type": "file",
                "format": param_schema.get("format"),
                "required": False,
            }

    # Check parameter name patterns
    file_param_patterns = {
        "file",
        "files",
        "upload",
        "attachment",
        "document",
        "image",
        "photo",
        "video",
        "audio",
    }

    if any(pattern in param_name.lower() for pattern in file_param_patterns):
        return {
            "name": param_name,
            "type": "file",
            "format": "inferred",
            "required": False,
        }

    return None


def should_use_file_helpers(endpoint: dict) -> bool:
    """Determine if an endpoint should use the new file helper functions.

    Args:
        endpoint: OpenAPI endpoint specification

    Returns:
        True if endpoint should use file helpers
    """
    return is_file_upload_endpoint(endpoint) or is_file_download_endpoint(endpoint)


def get_required_file_imports(endpoint: dict) -> List[str]:
    """Get list of file handling imports needed for an endpoint.

    Args:
        endpoint: OpenAPI endpoint specification

    Returns:
        List of import statements needed
    """
    imports = []

    if is_file_upload_endpoint(endpoint):
        upload_strategy = determine_upload_strategy(endpoint)
        if upload_strategy == "multipart":
            imports.extend(
                [
                    "from kittycad._multipart import upload_file_multipart, upload_file_multipart_async",
                    "from kittycad._io_types import SyncUpload, ProgressCallback",
                ]
            )
        elif upload_strategy == "binary":
            imports.extend(
                [
                    "from kittycad._binary import upload_file_binary, upload_file_binary_async",
                    "from kittycad._io_types import SyncUpload, ProgressCallback",
                ]
            )

    if is_file_download_endpoint(endpoint):
        imports.extend(
            [
                "from kittycad._downloads import stream_download, stream_download_async",
                "from kittycad._io_types import SyncDownload, ProgressCallback",
            ]
        )

    return imports
