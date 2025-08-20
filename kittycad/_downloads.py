"""Streaming download helpers for the KittyCAD SDK.

This module provides utilities for downloading files with progress tracking,
streaming to disk, and flexible output options (file path, file object, or return bytes).
"""

from __future__ import annotations

from pathlib import Path
from typing import IO, Optional, Union, cast

import httpx

from ._io_types import ProgressCallback, SyncDownload
from ._progress import wrap_with_progress


def download_to_file(
    response: httpx.Response,
    output: SyncDownload,
    progress_callback: Optional[ProgressCallback] = None,
    chunk_size: int = 8192,
    overwrite: bool = False,
) -> Optional[bytes]:
    """Download response content to a file or return as bytes.

    Args:
        response: HTTPX response to download from
        output: Where to save the content (path, file object, or None for bytes)
        progress_callback: Optional progress tracking callback
        chunk_size: Size of chunks to read/write
        overwrite: Whether to overwrite existing files

    Returns:
        Downloaded bytes if output is None, otherwise None

    Example:
        >>> import httpx
        >>> response = httpx.get("https://example.com/download/file.pdf")
        >>> download_to_file(response, "/tmp/downloaded.pdf", overwrite=True)
        >>>
        >>> # Or get bytes directly
        >>> data = download_to_file(response, None)
    """
    # Determine total size from headers
    total_size = None
    content_length = response.headers.get("content-length")
    if content_length:
        try:
            total_size = int(content_length)
        except ValueError:
            pass

    if output is None:
        # Return bytes directly
        if progress_callback:
            bytes_downloaded = 0
            chunks = []

            for chunk in response.iter_bytes(chunk_size):
                chunks.append(chunk)
                bytes_downloaded += len(chunk)
                progress_callback(bytes_downloaded, total_size)

            return b"".join(chunks)
        else:
            return response.content

    # Handle path-like output
    if isinstance(output, (str, Path)) or hasattr(output, "__fspath__"):
        path = Path(output)

        # Check if file exists and overwrite is False
        if path.exists() and not overwrite:
            raise FileExistsError(f"File {path} already exists and overwrite=False")

        # Create parent directories if needed
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "wb") as file_obj:
            _download_to_file_obj(
                response=response,
                file_obj=file_obj,
                progress_callback=progress_callback,
                total_size=total_size,
                chunk_size=chunk_size,
            )
            return None

    # Handle file-like output
    elif hasattr(output, "write"):
        _download_to_file_obj(
            response=response,
            file_obj=output,
            progress_callback=progress_callback,
            total_size=total_size,
            chunk_size=chunk_size,
        )
        return None

    else:
        raise TypeError(f"Unsupported output type: {type(output)}")


def _download_to_file_obj(
    response: httpx.Response,
    file_obj: IO[bytes],
    progress_callback: Optional[ProgressCallback],
    total_size: Optional[int],
    chunk_size: int,
) -> None:
    """Download response content to a file object."""
    # Wrap file object with progress tracking if requested
    if progress_callback:
        wrapped_file_obj = wrap_with_progress(
            file_obj=file_obj,
            progress_callback=progress_callback,
            total_size=total_size,
            for_reading=False,  # We're writing to the file
        )
        if hasattr(wrapped_file_obj, "write"):
            file_obj = cast(IO[bytes], wrapped_file_obj)

    # Stream the download
    for chunk in response.iter_bytes(chunk_size):
        file_obj.write(chunk)


def stream_download(
    client: httpx.Client,
    url: str,
    output: SyncDownload,
    method: str = "GET",
    progress_callback: Optional[ProgressCallback] = None,
    chunk_size: int = 8192,
    overwrite: bool = False,
    **request_kwargs,
) -> Optional[bytes]:
    """Download a file with streaming and progress tracking.

    Args:
        client: HTTPX client to use for the request
        url: URL to download from
        output: Where to save (path, file object, or None for bytes)
        method: HTTP method (default: GET)
        progress_callback: Optional progress tracking callback
        chunk_size: Size of chunks to read/write
        overwrite: Whether to overwrite existing files
        **request_kwargs: Additional arguments for the HTTP request

    Returns:
        Downloaded bytes if output is None, otherwise None

    Example:
        >>> import httpx
        >>> client = httpx.Client()
        >>> # stream_download(
        >>> #     client=client,
        >>> #     url="https://example.com/download/large_file.bin",
        >>> #     output="/tmp/large_file.bin",
        >>> # )
    """
    with client.stream(method, url, **request_kwargs) as response:
        response.raise_for_status()

        return download_to_file(
            response=response,
            output=output,
            progress_callback=progress_callback,
            chunk_size=chunk_size,
            overwrite=overwrite,
        )


async def stream_download_async(
    client: httpx.AsyncClient,
    url: str,
    output: SyncDownload,
    method: str = "GET",
    progress_callback: Optional[ProgressCallback] = None,
    chunk_size: int = 8192,
    overwrite: bool = False,
    **request_kwargs,
) -> Optional[bytes]:
    """Async version of stream_download.

    Args:
        client: Async HTTPX client to use for the request
        url: URL to download from
        output: Where to save (path, file object, or None for bytes)
        method: HTTP method (default: GET)
        progress_callback: Optional progress tracking callback
        chunk_size: Size of chunks to read/write
        overwrite: Whether to overwrite existing files
        **request_kwargs: Additional arguments for the HTTP request

    Returns:
        Downloaded bytes if output is None, otherwise None
    """
    async with client.stream(method, url, **request_kwargs) as response:
        response.raise_for_status()

        # For async, we need to manually iterate since download_to_file is sync
        total_size = None
        content_length = response.headers.get("content-length")
        if content_length:
            try:
                total_size = int(content_length)
            except ValueError:
                pass

        if output is None:
            # Return bytes directly
            if progress_callback:
                bytes_downloaded = 0
                chunks = []

                async for chunk in response.aiter_bytes(chunk_size):
                    chunks.append(chunk)
                    bytes_downloaded += len(chunk)
                    progress_callback(bytes_downloaded, total_size)

                return b"".join(chunks)
            else:
                return await response.aread()

        # Handle path-like output
        if isinstance(output, (str, Path)) or hasattr(output, "__fspath__"):
            path = Path(output)

            if path.exists() and not overwrite:
                raise FileExistsError(f"File {path} already exists and overwrite=False")

            path.parent.mkdir(parents=True, exist_ok=True)

            with open(path, "wb") as file_obj:
                await _download_to_file_obj_async(
                    response=response,
                    file_obj=file_obj,
                    progress_callback=progress_callback,
                    total_size=total_size,
                    chunk_size=chunk_size,
                )

        # Handle file-like output
        elif hasattr(output, "write"):
            await _download_to_file_obj_async(
                response=response,
                file_obj=output,
                progress_callback=progress_callback,
                total_size=total_size,
                chunk_size=chunk_size,
            )

        else:
            raise TypeError(f"Unsupported output type: {type(output)}")

        return None


async def _download_to_file_obj_async(
    response: httpx.Response,
    file_obj: IO[bytes],
    progress_callback: Optional[ProgressCallback],
    total_size: Optional[int],
    chunk_size: int,
) -> None:
    """Async version of _download_to_file_obj."""
    # Wrap file object with progress tracking if requested
    if progress_callback:
        wrapped_file_obj = wrap_with_progress(
            file_obj=file_obj,
            progress_callback=progress_callback,
            total_size=total_size,
            for_reading=False,
        )
        if hasattr(wrapped_file_obj, "write"):
            file_obj = cast(IO[bytes], wrapped_file_obj)

    # Stream the download async
    async for chunk in response.aiter_bytes(chunk_size):
        file_obj.write(chunk)


class DownloadContext:
    """Context manager for downloads with automatic cleanup and error handling.

    Example:
        >>> import httpx
        >>> client = httpx.Client()
        >>> # with DownloadContext(client, "https://example.com/file.bin", "/tmp/file.bin") as download:
        >>> #     download.start()  # Downloads the file
    """

    def __init__(
        self,
        client: Union[httpx.Client, httpx.AsyncClient],
        url: str,
        output: SyncDownload,
        method: str = "GET",
        progress_callback: Optional[ProgressCallback] = None,
        chunk_size: int = 8192,
        overwrite: bool = False,
        **request_kwargs,
    ):
        """Initialize the download context.

        Args:
            client: HTTPX client to use
            url: URL to download from
            output: Where to save the content
            method: HTTP method (default: GET)
            progress_callback: Optional progress tracking callback
            chunk_size: Size of chunks to read/write
            overwrite: Whether to overwrite existing files
            **request_kwargs: Additional arguments for the HTTP request
        """
        self.client = client
        self.url = url
        self.output = output
        self.method = method
        self.progress_callback = progress_callback
        self.chunk_size = chunk_size
        self.overwrite = overwrite
        self.request_kwargs = request_kwargs
        self.result: Optional[bytes] = None

    def __enter__(self):
        """Enter the download context."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the download context."""
        # Could add cleanup logic here if needed
        return None

    def start(self) -> Optional[bytes]:
        """Start the download."""
        if isinstance(self.client, httpx.AsyncClient):
            raise RuntimeError("Use start_async() for AsyncClient")

        self.result = stream_download(
            client=self.client,
            url=self.url,
            output=self.output,
            method=self.method,
            progress_callback=self.progress_callback,
            chunk_size=self.chunk_size,
            overwrite=self.overwrite,
            **self.request_kwargs,
        )
        return self.result

    async def start_async(self) -> Optional[bytes]:
        """Start the async download."""
        if not isinstance(self.client, httpx.AsyncClient):
            raise RuntimeError("Use start() for sync Client")

        self.result = await stream_download_async(
            client=self.client,
            url=self.url,
            output=self.output,
            method=self.method,
            progress_callback=self.progress_callback,
            chunk_size=self.chunk_size,
            overwrite=self.overwrite,
            **self.request_kwargs,
        )
        return self.result


def get_filename_from_response(
    response: httpx.Response, fallback: str = "download"
) -> str:
    """Extract filename from response headers.

    Args:
        response: HTTPX response
        fallback: Fallback filename if none found in headers

    Returns:
        Filename from Content-Disposition header or fallback

    Example:
        >>> import httpx
        >>> response = httpx.get("https://example.com/download/file")
        >>> filename = get_filename_from_response(response, "unknown.bin")
    """
    # Try to get filename from Content-Disposition header
    content_disposition = response.headers.get("content-disposition", "")

    if "filename=" in content_disposition:
        # Extract filename from header
        parts = content_disposition.split("filename=")
        if len(parts) > 1:
            filename = parts[1].strip()
            # Remove quotes if present
            if filename.startswith('"') and filename.endswith('"'):
                filename = filename[1:-1]
            if filename:
                return filename

    # Try to get filename from URL
    try:
        from urllib.parse import urlparse

        path = urlparse(str(response.url)).path
        if path and "/" in path:
            url_filename = path.split("/")[-1]
            if url_filename and "." in url_filename:
                return url_filename
    except Exception:
        pass

    return fallback
