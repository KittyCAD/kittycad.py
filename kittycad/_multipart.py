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
        >>> encoder = create_multipart_upload(
        ...     file_param="file",
        ...     file_input="/path/to/file.png",
        ...     progress_callback=lambda bytes_sent, total: print(f"{bytes_sent}/{total}")
        ... )
        >>> response = httpx.post(url, content=encoder.to_string(),
        ...                      headers=encoder.content_type)
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
    file_tuple = (detected_filename, file_obj, detected_content_type)

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
        # Fallback - create a simple dict that works with httpx
        encoder = fields  # type: ignore[assignment]

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
        >>> files = create_files_dict(
        ...     file_param="file",
        ...     file_input="/path/to/file.png"
        ... )
        >>> response = httpx.post(url, files=files)
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
    file_tuple = (detected_filename, file_obj, detected_content_type)

    files_dict = {file_param: file_tuple}

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
        >>> with MultipartUploadContext("file", "/path/to/file.png") as upload:
        ...     response = httpx.post(url, files=upload.files)
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
        >>> response = upload_file_multipart(
        ...     client=httpx.Client(),
        ...     url="https://api.zoo.dev/upload",
        ...     file_param="file",
        ...     file_input="/path/to/file.png",
        ...     progress_callback=lambda sent, total: print(f"{sent}/{total}")
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
