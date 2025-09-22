"""Multipart upload helpers for the KittyCAD SDK.

This module provides utilities for creating multipart/form-data uploads
with proper file handling, content type detection, and progress tracking.
"""

from __future__ import annotations

from typing import IO, Any, Dict, Optional, Union, cast

import httpx
import httpx._multipart

from ._file_inputs import prepare_upload_input
from ._io_types import ProgressCallback, SyncUpload
from ._progress import wrap_with_progress


class MultipartDict(dict):
    """Custom dict that can store cleanup info as attributes."""

    pass


def _resolve_multipart_filename(
    field_name: str, detected_filename: Optional[str]
) -> Optional[str]:
    """Choose the filename to send in a multipart part.

    - If the field name encodes a relative path (contains a path separator),
      use it so servers that key by filename receive the intended path.
    - Otherwise, fall back to the detected/basename filename.
    """
    if "/" in field_name or "\\" in field_name:
        return field_name
    # Keep None for bytes/streams with no inherent filename
    return detected_filename


def create_multipart_upload(
    file_param: str,
    file_input: SyncUpload,
    filename: Optional[str] = None,
    content_type: Optional[str] = None,
    progress_callback: Optional[ProgressCallback] = None,
    additional_fields: Optional[Dict[str, Any]] = None,
) -> Any:
    """Create a multipart upload encoder for file uploads.

    Args:
        file_param: The parameter name for the file in the multipart data
        file_input: The file content (path, file object, bytes, etc.)
        filename: Override filename for the upload
        content_type: Override content type
        progress_callback: Optional progress tracking callback
        additional_fields: Additional form fields to include

    Returns:
        A configured multipart encoder ready for upload

    Example:
        >>> from io import BytesIO
        >>> # encoder = create_multipart_upload(
        >>> #     file_param="file",
        >>> #     file_input=BytesIO(b"image data"),
        >>> # )
        >>> # response = httpx.post(url, content=encoder.to_string(), headers=encoder.content_type)
    """
    # Prepare the file input
    file_obj, should_close, detected_filename, detected_content_type, use_multipart = (
        prepare_upload_input(
            upload=file_input,
            filename=filename,
            content_type=content_type,
            force_multipart=True,  # Always use multipart for this function
        )
    )

    # Wrap with progress tracking if requested
    if progress_callback and hasattr(file_obj, "read"):
        wrapped_file_obj = wrap_with_progress(
            file_obj=file_obj, progress_callback=progress_callback, for_reading=True
        )
        file_obj = cast(IO[bytes], wrapped_file_obj)

    # Create the file tuple for multipart
    # Format: (filename, file_obj, content_type)
    use_filename = _resolve_multipart_filename(file_param, detected_filename)
    file_tuple = (use_filename, file_obj, detected_content_type)

    # Build the fields dictionary
    fields = {file_param: file_tuple}

    # Add any additional fields
    if additional_fields:
        fields.update(additional_fields)

    # Create the multipart encoder
    try:
        from httpx._multipart import MultipartEncoder  # type: ignore[attr-defined]

        encoder = MultipartEncoder(fields=fields)
    except (AttributeError, ImportError):
        # Fallback - create a simple dict-like that supports attribute storage
        encoder = MultipartDict(fields)

    # Store cleanup info on the encoder for later use
    encoder._kittycad_file_obj = file_obj
    encoder._kittycad_should_close = should_close

    return encoder


def create_files_dict(
    file_param: str,
    file_input: SyncUpload,
    filename: Optional[str] = None,
    content_type: Optional[str] = None,
    progress_callback: Optional[ProgressCallback] = None,
) -> Dict[str, Any]:
    """Create a files dictionary for HTTPX requests.

    This is an alternative to create_multipart_upload that works with
    HTTPX's built-in files parameter.

    Args:
        file_param: The parameter name for the file
        file_input: The file content (path, file object, bytes, etc.)
        filename: Override filename for the upload
        content_type: Override content type
        progress_callback: Optional progress tracking callback

    Returns:
        A files dictionary suitable for httpx.post(files=...)

    Example:
        >>> from io import BytesIO
        >>> files = create_files_dict(
        ...     file_param="file",
        ...     file_input=BytesIO(b"image data")
        ... )
        >>> # response = httpx.post(url, files=files)
    """
    # Prepare the file input
    file_obj, should_close, detected_filename, detected_content_type, use_multipart = (
        prepare_upload_input(
            upload=file_input,
            filename=filename,
            content_type=content_type,
            force_multipart=True,
        )
    )

    # Wrap with progress tracking if requested
    if progress_callback and hasattr(file_obj, "read"):
        wrapped_file_obj = wrap_with_progress(
            file_obj=file_obj, progress_callback=progress_callback, for_reading=True
        )
        file_obj = cast(IO[bytes], wrapped_file_obj)

    # Create the file tuple
    # HTTPX expects: (filename, file_obj, content_type)
    use_filename = _resolve_multipart_filename(file_param, detected_filename)
    file_tuple = (use_filename, file_obj, detected_content_type)

    files_dict = MultipartDict({file_param: file_tuple})

    # Store cleanup info for later use
    setattr(files_dict, "_kittycad_file_obj", file_obj)
    setattr(files_dict, "_kittycad_should_close", should_close)

    return files_dict


def cleanup_multipart_upload(
    encoder_or_files: Union[Any, Dict[str, Any]],
) -> None:
    """Clean up resources after a multipart upload.

    Args:
        encoder_or_files: The encoder or files dict returned from create_multipart_upload/create_files_dict
    """
    if (
        hasattr(encoder_or_files, "_kittycad_should_close")
        and encoder_or_files._kittycad_should_close
    ):
        file_obj = getattr(encoder_or_files, "_kittycad_file_obj", None)
        if file_obj and hasattr(file_obj, "close"):
            try:
                file_obj.close()
            except Exception:
                pass  # Ignore errors during cleanup


class MultipartUploadContext:
    """Context manager for multipart uploads with automatic cleanup.

    Example:
        >>> from io import BytesIO
        >>> with MultipartUploadContext("file", BytesIO(b"image data")) as upload:
        ...     # response = httpx.post(url, files=upload.files)
        ...     pass
    """

    def __init__(
        self,
        file_param: str,
        file_input: SyncUpload,
        filename: Optional[str] = None,
        content_type: Optional[str] = None,
        progress_callback: Optional[ProgressCallback] = None,
        use_encoder: bool = False,
        additional_fields: Optional[Dict[str, Any]] = None,
    ):
        """Initialize the multipart upload context.

        Args:
            file_param: The parameter name for the file
            file_input: The file content (path, file object, bytes, etc.)
            filename: Override filename for the upload
            content_type: Override content type
            progress_callback: Optional progress tracking callback
            use_encoder: Whether to use MultipartEncoder (True) or files dict (False)
            additional_fields: Additional form fields (only used with encoder)
        """
        self.file_param = file_param
        self.file_input = file_input
        self.filename = filename
        self.content_type = content_type
        self.progress_callback = progress_callback
        self.use_encoder = use_encoder
        self.additional_fields = additional_fields
        self._upload_obj: Optional[Union[Any, Dict[str, Any]]] = None
        self.encoder: Optional[Any] = None
        self.files: Optional[Dict[str, Any]] = None

    def __enter__(self):
        """Create the multipart upload object."""
        if self.use_encoder:
            self._upload_obj = create_multipart_upload(
                file_param=self.file_param,
                file_input=self.file_input,
                filename=self.filename,
                content_type=self.content_type,
                progress_callback=self.progress_callback,
                additional_fields=self.additional_fields,
            )
            self.encoder = self._upload_obj
            self.files = None
        else:
            self._upload_obj = create_files_dict(
                file_param=self.file_param,
                file_input=self.file_input,
                filename=self.filename,
                content_type=self.content_type,
                progress_callback=self.progress_callback,
            )
            self.files = self._upload_obj
            self.encoder = None

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Clean up the multipart upload resources."""
        if self._upload_obj:
            cleanup_multipart_upload(self._upload_obj)
        return None


def upload_file_multipart(
    client: httpx.Client,
    url: str,
    file_param: str,
    file_input: SyncUpload,
    method: str = "POST",
    filename: Optional[str] = None,
    content_type: Optional[str] = None,
    progress_callback: Optional[ProgressCallback] = None,
    additional_fields: Optional[Dict[str, Any]] = None,
    **request_kwargs,
) -> httpx.Response:
    """Upload a file using multipart/form-data with automatic cleanup.

    Args:
        client: HTTPX client to use for the request
        url: URL to upload to
        file_param: Parameter name for the file
        file_input: The file content (path, file object, bytes, etc.)
        method: HTTP method (default: POST)
        filename: Override filename for the upload
        content_type: Override content type
        progress_callback: Optional progress tracking callback
        additional_fields: Additional form fields to include
        **request_kwargs: Additional arguments for the HTTP request

    Returns:
        The HTTP response

    Example:
        >>> from io import BytesIO
        >>> import httpx
        >>> response = upload_file_multipart(
        ...     client=httpx.Client(),
        ...     url="https://example.com/upload",
        ...     file_param="file",
        ...     file_input=BytesIO(b"image data"),
        ... )
    """
    with MultipartUploadContext(
        file_param=file_param,
        file_input=file_input,
        filename=filename,
        content_type=content_type,
        progress_callback=progress_callback,
        additional_fields=additional_fields,
    ) as upload:
        # Make the request with files
        response = client.request(
            method=method, url=url, files=upload.files, **request_kwargs
        )
        return response


async def upload_file_multipart_async(
    client: httpx.AsyncClient,
    url: str,
    file_param: str,
    file_input: SyncUpload,
    method: str = "POST",
    filename: Optional[str] = None,
    content_type: Optional[str] = None,
    progress_callback: Optional[ProgressCallback] = None,
    additional_fields: Optional[Dict[str, Any]] = None,
    **request_kwargs,
) -> httpx.Response:
    """Async version of upload_file_multipart.

    Args:
        client: Async HTTPX client to use for the request
        url: URL to upload to
        file_param: Parameter name for the file
        file_input: The file content (path, file object, bytes, etc.)
        method: HTTP method (default: POST)
        filename: Override filename for the upload
        content_type: Override content type
        progress_callback: Optional progress tracking callback
        additional_fields: Additional form fields to include
        **request_kwargs: Additional arguments for the HTTP request

    Returns:
        The HTTP response
    """
    with MultipartUploadContext(
        file_param=file_param,
        file_input=file_input,
        filename=filename,
        content_type=content_type,
        progress_callback=progress_callback,
        additional_fields=additional_fields,
    ) as upload:
        # Make the async request with files
        response = await client.request(
            method=method, url=url, files=upload.files, **request_kwargs
        )
        return response


class JsonMultipartDict(dict):
    """Custom dict that can store cleanup info as attributes."""

    pass


def create_json_multipart_upload(
    json_body: Any,
    file_attachments: Optional[Dict[str, SyncUpload]] = None,
    json_field_name: str = "body",
    progress_callback: Optional[ProgressCallback] = None,
) -> Dict[str, Any]:
    """Create a multipart upload with JSON body + file attachments.

    This follows the Rust SDK pattern where multipart endpoints get:
    - A JSON body as a form field (default name: "body")
    - File attachments as separate form fields

    Args:
        json_body: The JSON body object (will be serialized)
        file_attachments: Dict of {field_name: file_input} for attachments
        json_field_name: Name of the JSON body field (default: "body")
        progress_callback: Optional progress tracking callback

    Returns:
        Files dict suitable for httpx.post(files=...)

    Example:
        >>> from io import BytesIO
        >>> files = create_json_multipart_upload(
        ...     json_body={"prompt": "Create a cube", "project_name": "test"},
        ...     file_attachments={"file1": BytesIO(b"kcl data"), "file2": BytesIO(b"more kcl data")},
        ... )
        >>> # response = httpx.post(url, files=files)
    """
    files_dict = JsonMultipartDict()

    # Add JSON body as a text part with application/json content type
    import json

    if hasattr(json_body, "model_dump"):
        # Pydantic model
        json_content = json_body.model_dump_json()
    elif hasattr(json_body, "dict"):
        # Pydantic v1 model
        json_content = json.dumps(json_body.dict())
    else:
        # Regular dict or other serializable object
        json_content = json.dumps(json_body)

    # Create the JSON part with proper content type
    files_dict[json_field_name] = (
        f"{json_field_name}.json",
        json_content,
        "application/json",
    )

    # Add file attachments
    if file_attachments:
        for field_name, file_input in file_attachments.items():
            file_obj, should_close, detected_filename, detected_content_type, _ = (
                prepare_upload_input(
                    upload=file_input,
                    force_multipart=True,
                )
            )

            # Wrap with progress tracking if requested
            if progress_callback and hasattr(file_obj, "read"):
                wrapped_file_obj = wrap_with_progress(
                    file_obj=file_obj,
                    progress_callback=progress_callback,
                    for_reading=True,
                )
                file_obj = cast(IO[bytes], wrapped_file_obj)

            # Create the file tuple: (filename, file_obj, content_type)
            files_dict[field_name] = (
                _resolve_multipart_filename(field_name, detected_filename),
                file_obj,
                detected_content_type,
            )

            # Store cleanup info
            setattr(files_dict, f"_kittycad_file_obj_{field_name}", file_obj)
            setattr(files_dict, f"_kittycad_should_close_{field_name}", should_close)

    return files_dict


def cleanup_json_multipart_upload(files_dict: Dict[str, Any]) -> None:
    """Clean up resources from a JSON multipart upload.

    Args:
        files_dict: The files dict returned from create_json_multipart_upload
    """
    # Look for cleanup attributes that were stored
    for attr_name in dir(files_dict):
        if attr_name.startswith("_kittycad_file_obj_"):
            field_name = attr_name.replace("_kittycad_file_obj_", "")
            should_close_attr = f"_kittycad_should_close_{field_name}"

            if hasattr(files_dict, should_close_attr):
                should_close = getattr(files_dict, should_close_attr)
                if should_close:
                    file_obj = getattr(files_dict, attr_name)
                    if file_obj and hasattr(file_obj, "close"):
                        try:
                            file_obj.close()
                        except Exception:
                            pass  # Ignore errors during cleanup


class JsonMultipartUploadContext:
    """Context manager for JSON + file multipart uploads with automatic cleanup.

    Example:
        >>> from io import BytesIO
        >>> with JsonMultipartUploadContext(
        ...     json_body={"prompt": "Create a cube"},
        ...     file_attachments={"file1": BytesIO(b"kcl data")}
        ... ) as upload:
        ...     # response = httpx.post(url, files=upload.files)
        ...     pass
    """

    def __init__(
        self,
        json_body: Any,
        file_attachments: Optional[Dict[str, SyncUpload]] = None,
        json_field_name: str = "body",
        progress_callback: Optional[ProgressCallback] = None,
    ):
        """Initialize the JSON multipart upload context.

        Args:
            json_body: The JSON body object (will be serialized)
            file_attachments: Dict of {field_name: file_input} for attachments
            json_field_name: Name of the JSON body field (default: "body")
            progress_callback: Optional progress tracking callback
        """
        self.json_body = json_body
        self.file_attachments = file_attachments
        self.json_field_name = json_field_name
        self.progress_callback = progress_callback
        self.files: Optional[Dict[str, Any]] = None

    def __enter__(self):
        """Create the multipart upload object."""
        self.files = create_json_multipart_upload(
            json_body=self.json_body,
            file_attachments=self.file_attachments,
            json_field_name=self.json_field_name,
            progress_callback=self.progress_callback,
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Clean up the multipart upload resources."""
        if self.files:
            cleanup_json_multipart_upload(self.files)
        return None


def upload_json_multipart(
    client: httpx.Client,
    url: str,
    json_body: Any,
    file_attachments: Optional[Dict[str, SyncUpload]] = None,
    method: str = "POST",
    json_field_name: str = "body",
    progress_callback: Optional[ProgressCallback] = None,
    **request_kwargs,
) -> httpx.Response:
    """Upload JSON body + file attachments using multipart/form-data.

    Args:
        client: HTTPX client to use for the request
        url: URL to upload to
        json_body: The JSON body object (will be serialized)
        file_attachments: Dict of {field_name: file_input} for attachments
        method: HTTP method (default: POST)
        json_field_name: Name of the JSON body field (default: "body")
        progress_callback: Optional progress tracking callback
        **request_kwargs: Additional arguments for the HTTP request

    Returns:
        The HTTP response

    Example:
        >>> from io import BytesIO
        >>> import httpx
        >>> response = upload_json_multipart(
        ...     client=httpx.Client(),
        ...     url="https://example.com/upload",
        ...     json_body={"prompt": "Create a cube", "project_name": "test"},
        ...     file_attachments={"file1": BytesIO(b"kcl data")},
        ... )
    """
    with JsonMultipartUploadContext(
        json_body=json_body,
        file_attachments=file_attachments,
        json_field_name=json_field_name,
        progress_callback=progress_callback,
    ) as upload:
        # Make the request with files
        response = client.request(
            method=method, url=url, files=upload.files, **request_kwargs
        )
        return response


async def upload_json_multipart_async(
    client: httpx.AsyncClient,
    url: str,
    json_body: Any,
    file_attachments: Optional[Dict[str, SyncUpload]] = None,
    method: str = "POST",
    json_field_name: str = "body",
    progress_callback: Optional[ProgressCallback] = None,
    **request_kwargs,
) -> httpx.Response:
    """Async version of upload_json_multipart.

    Args:
        client: Async HTTPX client to use for the request
        url: URL to upload to
        json_body: The JSON body object (will be serialized)
        file_attachments: Dict of {field_name: file_input} for attachments
        method: HTTP method (default: POST)
        json_field_name: Name of the JSON body field (default: "body")
        progress_callback: Optional progress tracking callback
        **request_kwargs: Additional arguments for the HTTP request

    Returns:
        The HTTP response
    """
    with JsonMultipartUploadContext(
        json_body=json_body,
        file_attachments=file_attachments,
        json_field_name=json_field_name,
        progress_callback=progress_callback,
    ) as upload:
        # Make the async request with files
        response = await client.request(
            method=method, url=url, files=upload.files, **request_kwargs
        )
        return response
