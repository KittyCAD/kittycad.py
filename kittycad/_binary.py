"""Raw binary upload helpers for the KittyCAD SDK.

This module provides utilities for uploading raw binary data (application/octet-stream)
without multipart encoding, which is useful for APIs that expect raw file content.
"""

from __future__ import annotations

from typing import IO, Any, Dict, Optional, cast

import httpx

from ._file_inputs import prepare_upload_input
from ._io_types import ProgressCallback, SyncUpload
from ._progress import wrap_with_progress


def create_binary_upload(
    file_input: SyncUpload,
    content_type: Optional[str] = None,
    progress_callback: Optional[ProgressCallback] = None,
) -> tuple[bytes, str]:
    """Create a binary upload from file input.

    Args:
        file_input: The file content (path, file object, bytes, etc.)
        content_type: Override content type (defaults to application/octet-stream)
        progress_callback: Optional progress tracking callback

    Returns:
        Tuple of (binary_data, content_type)

    Example:
        >>> from io import BytesIO
        >>> data, content_type = create_binary_upload(BytesIO(b"image data"))
        >>> # response = httpx.post(url, content=data, headers={"Content-Type": content_type})
    """
    # Prepare the file input (force non-multipart)
    file_obj, should_close, _, detected_content_type, _ = prepare_upload_input(
        upload=file_input, content_type=content_type, force_multipart=False
    )

    try:
        # Wrap with progress tracking if requested
        if progress_callback and hasattr(file_obj, "read"):
            wrapped_file_obj = wrap_with_progress(
                file_obj=file_obj, progress_callback=progress_callback, for_reading=True
            )
            if hasattr(wrapped_file_obj, "read"):
                file_obj = cast(IO[bytes], wrapped_file_obj)

        # Read all data
        if hasattr(file_obj, "read"):
            binary_data = file_obj.read()
        else:
            raise TypeError(f"Object does not support reading: {type(file_obj)}")

        # Use provided content type or detected type, fallback to octet-stream
        final_content_type = (
            content_type or detected_content_type or "application/octet-stream"
        )

        return binary_data, final_content_type

    finally:
        # Clean up if we opened the file
        if should_close and hasattr(file_obj, "close"):
            try:
                file_obj.close()
            except Exception:
                pass


def create_binary_stream(
    file_input: SyncUpload,
    content_type: Optional[str] = None,
    progress_callback: Optional[ProgressCallback] = None,
    chunk_size: int = 8192,
):
    """Create a streaming binary upload from file input.

    Args:
        file_input: The file content (path, file object, bytes, etc.)
        content_type: Override content type (defaults to application/octet-stream)
        progress_callback: Optional progress tracking callback
        chunk_size: Size of chunks to read when streaming

    Returns:
        Tuple of (stream_generator, content_type, cleanup_func)

    Example:
        >>> from io import BytesIO
        >>> stream, content_type, cleanup = create_binary_stream(BytesIO(b"large file data"))
        >>> try:
        ...     # Use stream and content_type for HTTP request
        ...     pass
        ... finally:
        ...     cleanup()
    """
    # Handle iterators specially for streaming (but not strings/paths)
    if (
        hasattr(file_input, "__iter__")
        and not hasattr(file_input, "read")
        and not isinstance(file_input, (str, bytes, bytearray, memoryview))
        and not hasattr(file_input, "__fspath__")
    ):
        # For iterators, pass them through directly for streaming
        def iterator_stream_generator():
            """Generator that yields chunks from the iterator."""
            for chunk in file_input:
                if isinstance(chunk, bytes):
                    yield chunk
                else:
                    raise TypeError(f"Iterator must yield bytes, got {type(chunk)}")

        def iterator_cleanup_func():
            # Nothing to clean up for iterators
            pass

        final_content_type = content_type or "application/octet-stream"
        return iterator_stream_generator(), final_content_type, iterator_cleanup_func

    # Prepare the file input for non-iterators
    file_obj, should_close, _, detected_content_type, _ = prepare_upload_input(
        upload=file_input, content_type=content_type, force_multipart=False
    )

    # Wrap with progress tracking if requested
    if progress_callback and hasattr(file_obj, "read"):
        wrapped_file_obj = wrap_with_progress(
            file_obj=file_obj, progress_callback=progress_callback, for_reading=True
        )
        if hasattr(wrapped_file_obj, "read"):
            file_obj = cast(IO[bytes], wrapped_file_obj)

    def stream_generator():
        """Generator that yields chunks of the file."""
        try:
            while True:
                if hasattr(file_obj, "read"):
                    chunk = file_obj.read(chunk_size)
                    if not chunk:
                        break
                    yield chunk
                else:
                    break
        except Exception:
            # If streaming fails, clean up and re-raise
            cleanup_func()
            raise

    def cleanup_func():
        """Clean up resources."""
        if should_close and hasattr(file_obj, "close"):
            try:
                file_obj.close()
            except Exception:
                pass

    # Use provided content type or detected type, fallback to octet-stream
    final_content_type = (
        content_type or detected_content_type or "application/octet-stream"
    )

    return stream_generator(), final_content_type, cleanup_func


class BinaryUploadContext:
    """Context manager for binary uploads with automatic cleanup.

    Example:
        >>> from io import BytesIO
        >>> with BinaryUploadContext(BytesIO(b"test data")) as upload:
        ...     # Use upload.data and upload.headers for HTTP request
        ...     pass
    """

    def __init__(
        self,
        file_input: SyncUpload,
        content_type: Optional[str] = None,
        progress_callback: Optional[ProgressCallback] = None,
        stream: bool = False,
        chunk_size: int = 8192,
    ):
        """Initialize the binary upload context.

        Args:
            file_input: The file content (path, file object, bytes, etc.)
            content_type: Override content type
            progress_callback: Optional progress tracking callback
            stream: Whether to use streaming (True) or load all data (False)
            chunk_size: Size of chunks when streaming
        """
        self.file_input = file_input
        self.content_type = content_type
        self.progress_callback = progress_callback
        self.stream = stream
        self.chunk_size = chunk_size
        self.data: Optional[Any] = None
        self.headers: Dict[str, str] = {}
        self._cleanup_func = None

    def __enter__(self):
        """Prepare the binary upload."""
        if self.stream:
            # Use streaming approach
            stream_gen, content_type, cleanup_func = create_binary_stream(
                file_input=self.file_input,
                content_type=self.content_type,
                progress_callback=self.progress_callback,
                chunk_size=self.chunk_size,
            )
            self.data = stream_gen
            self._cleanup_func = cleanup_func
        else:
            # Load all data at once
            data, content_type = create_binary_upload(
                file_input=self.file_input,
                content_type=self.content_type,
                progress_callback=self.progress_callback,
            )
            self.data = data

        self.headers = {"Content-Type": content_type}
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Clean up resources."""
        if self._cleanup_func:
            self._cleanup_func()
        return None


def upload_file_binary(
    client: httpx.Client,
    url: str,
    file_input: SyncUpload,
    method: str = "POST",
    content_type: Optional[str] = None,
    progress_callback: Optional[ProgressCallback] = None,
    stream: bool = False,
    chunk_size: int = 8192,
    **request_kwargs,
) -> httpx.Response:
    """Upload a file as raw binary data with automatic cleanup.

    Args:
        client: HTTPX client to use for the request
        url: URL to upload to
        file_input: The file content (path, file object, bytes, etc.)
        method: HTTP method (default: POST)
        content_type: Override content type
        progress_callback: Optional progress tracking callback
        stream: Whether to use streaming upload
        chunk_size: Size of chunks when streaming
        **request_kwargs: Additional arguments for the HTTP request

    Returns:
        The HTTP response

    Example:
        >>> from io import BytesIO
        >>> import httpx
        >>> response = upload_file_binary(
        ...     client=httpx.Client(),
        ...     url="https://example.com/upload-binary",
        ...     file_input=BytesIO(b"file data"),
        ... )
    """
    with BinaryUploadContext(
        file_input=file_input,
        content_type=content_type,
        progress_callback=progress_callback,
        stream=stream,
        chunk_size=chunk_size,
    ) as upload:
        # Make the request with binary content
        response = client.request(
            method=method,
            url=url,
            content=upload.data,
            headers={**upload.headers, **request_kwargs.pop("headers", {})},
            **request_kwargs,
        )
        return response


async def upload_file_binary_async(
    client: httpx.AsyncClient,
    url: str,
    file_input: SyncUpload,
    method: str = "POST",
    content_type: Optional[str] = None,
    progress_callback: Optional[ProgressCallback] = None,
    stream: bool = False,
    chunk_size: int = 8192,
    **request_kwargs,
) -> httpx.Response:
    """Async version of upload_file_binary.

    Args:
        client: Async HTTPX client to use for the request
        url: URL to upload to
        file_input: The file content (path, file object, bytes, etc.)
        method: HTTP method (default: POST)
        content_type: Override content type
        progress_callback: Optional progress tracking callback
        stream: Whether to use streaming upload
        chunk_size: Size of chunks when streaming
        **request_kwargs: Additional arguments for the HTTP request

    Returns:
        The HTTP response
    """
    with BinaryUploadContext(
        file_input=file_input,
        content_type=content_type,
        progress_callback=progress_callback,
        stream=stream,
        chunk_size=chunk_size,
    ) as upload:
        # Make the async request with binary content
        response = await client.request(
            method=method,
            url=url,
            content=upload.data,
            headers={**upload.headers, **request_kwargs.pop("headers", {})},
            **request_kwargs,
        )
        return response


def prepare_binary_headers(
    content_type: Optional[str] = None,
    content_length: Optional[int] = None,
    additional_headers: Optional[Dict[str, str]] = None,
) -> Dict[str, str]:
    """Prepare headers for binary uploads.

    Args:
        content_type: Content type for the upload
        content_length: Content length if known
        additional_headers: Additional headers to include

    Returns:
        Dictionary of headers for the request
    """
    headers = {}

    if content_type:
        headers["Content-Type"] = content_type
    else:
        headers["Content-Type"] = "application/octet-stream"

    if content_length is not None:
        headers["Content-Length"] = str(content_length)

    if additional_headers:
        headers.update(additional_headers)

    return headers
