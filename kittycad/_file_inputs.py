"""File input normalization helpers for the KittyCAD SDK.

This module provides utilities to normalize various file input types into
consistent file-like objects that can be used with HTTPX multipart uploads
and raw binary uploads.
"""

from __future__ import annotations

import io
import mimetypes
from pathlib import Path
from typing import IO, Optional, Tuple, cast

from ._io_types import SyncUpload


def _open_if_path(
    upload: SyncUpload,
) -> Tuple[IO[bytes], bool, Optional[str]]:
    """Normalize any upload input to (file_obj, should_close, filename).

    Args:
        upload: Any acceptable upload input

    Returns:
        A tuple of (file_object, should_close, filename)
        - file_object: A file-like object ready for reading
        - should_close: Whether we opened the file and should close it
        - filename: The filename if available (for multipart uploads)

    Note:
        Only close files that we opened. Don't close user-provided file objects.
    """
    # Handle path-like objects
    if isinstance(upload, (str, Path)) or hasattr(upload, "__fspath__"):
        path = Path(str(upload))  # Convert to str first for Path constructor
        filename = path.name
        file_obj = open(path, "rb")
        return file_obj, True, filename

    # Handle bytes-like objects
    if isinstance(upload, (bytes, bytearray, memoryview)):
        bytes_obj: IO[bytes] = io.BytesIO(bytes(upload))
        return bytes_obj, False, None

    # Handle iterables (streaming)
    if hasattr(upload, "__iter__") and not hasattr(upload, "read"):
        # Convert iterator to BytesIO for now
        # In a full implementation, this would be optimized for streaming
        chunks = []
        for chunk in upload:
            if isinstance(chunk, bytes):
                chunks.append(chunk)
            else:
                raise TypeError(f"Iterator must yield bytes, got {type(chunk)}")

        data = b"".join(chunks)
        iter_obj: IO[bytes] = io.BytesIO(data)
        return iter_obj, False, None

    # Handle file-like objects (already open)
    if hasattr(upload, "read"):
        filename_attr = getattr(upload, "name", None)
        if filename_attr and not isinstance(filename_attr, str):
            filename_attr = None  # Don't use non-string names
        return cast(IO[bytes], upload), False, filename_attr

    raise TypeError(f"Unsupported upload type: {type(upload)}")


def _get_content_type(
    filename: Optional[str] = None,
    content: Optional[bytes] = None,
    override: Optional[str] = None,
) -> str:
    """Guess content type from filename or content.

    Args:
        filename: Optional filename to guess from
        content: Optional content bytes to analyze
        override: Explicit content type override

    Returns:
        Content type string
    """
    if override:
        return override

    # Try to guess from filename first
    if filename:
        content_type, _ = mimetypes.guess_type(filename)
        if content_type:
            return content_type

    # Try to detect from content for common formats
    if content:
        # Check for common binary formats by magic bytes
        if content.startswith(b"\x89PNG\r\n\x1a\n"):
            return "image/png"
        elif content.startswith(b"\xff\xd8\xff"):
            return "image/jpeg"
        elif content.startswith(b"GIF8"):
            return "image/gif"
        elif content.startswith(b"\x00\x00\x00\x20ftyp"):
            return "video/mp4"
        elif content.startswith(b"%PDF"):
            return "application/pdf"
        elif content.startswith(b"PK\x03\x04"):
            return "application/zip"

    # Default to binary
    return "application/octet-stream"


def _should_use_multipart(
    upload: SyncUpload,
    filename: Optional[str] = None,
    content_type: Optional[str] = None,
    force_multipart: bool = False,
) -> bool:
    """Determine if upload should use multipart/form-data vs raw binary.

    Args:
        upload: The upload input
        filename: Optional filename
        content_type: Optional content type
        force_multipart: Force multipart even without filename

    Returns:
        True if should use multipart, False for raw binary

    Note:
        - Use multipart when we have a filename (file upload semantics)
        - Use multipart when explicitly forced
        - Use raw binary for bytes/streams without filename (data upload semantics)
    """
    if force_multipart:
        return True

    # If we have a filename, prefer multipart (file upload semantics)
    if filename:
        return True

    # For path-like objects, always use multipart
    if isinstance(upload, (str, Path)) or hasattr(upload, "__fspath__"):
        return True

    # For bytes-like without filename, use raw binary (data semantics)
    if isinstance(upload, (bytes, bytearray, memoryview)):
        return False

    # For file objects, check if they have a name
    if hasattr(upload, "read"):
        obj_filename = getattr(upload, "name", None)
        if obj_filename and isinstance(obj_filename, str):
            return True

    # Default to raw binary for iterators and unnamed objects
    return False


def _peek_file_content(file_obj: IO[bytes], peek_size: int = 512) -> bytes:
    """Peek at the beginning of a file without consuming it.

    Args:
        file_obj: File-like object to peek at
        peek_size: Number of bytes to peek

    Returns:
        The peeked bytes

    Note:
        This function ensures the file position is restored after peeking.
    """
    if not hasattr(file_obj, "seek") or not hasattr(file_obj, "tell"):
        # Can't seek, just return empty
        return b""

    current_pos = file_obj.tell()
    try:
        content = file_obj.read(peek_size)
        file_obj.seek(current_pos)
        return content
    except (OSError, io.UnsupportedOperation):
        # Reset position and return empty if seeking fails
        try:
            file_obj.seek(current_pos)
        except (OSError, io.UnsupportedOperation):
            pass
        return b""


def prepare_upload_input(
    upload: SyncUpload,
    filename: Optional[str] = None,
    content_type: Optional[str] = None,
    force_multipart: bool = False,
) -> Tuple[IO[bytes], bool, Optional[str], str, bool]:
    """Prepare any upload input for HTTP requests.

    Args:
        upload: Any acceptable upload input type
        filename: Override filename (for multipart)
        content_type: Override content type
        force_multipart: Force multipart even without filename

    Returns:
        Tuple of (file_obj, should_close, filename, content_type, use_multipart)

    Example:
        >>> from io import BytesIO
        >>> file_obj, should_close, filename, content_type, use_multipart = prepare_upload_input(
        ...     BytesIO(b"image data")
        ... )
        >>> # Use file_obj for upload, close if should_close is True
    """
    # Normalize the input
    file_obj, should_close, detected_filename = _open_if_path(upload)

    # Use provided filename or detected filename
    final_filename = filename or detected_filename

    # Peek at content for type detection if needed
    content_sample = (
        _peek_file_content(file_obj)
        if not content_type and hasattr(file_obj, "read")
        else b""
    )

    # Determine content type
    final_content_type = _get_content_type(
        filename=final_filename, content=content_sample, override=content_type
    )

    # Decide on upload method
    use_multipart = _should_use_multipart(
        upload=upload,
        filename=final_filename,
        content_type=final_content_type,
        force_multipart=force_multipart,
    )

    return file_obj, should_close, final_filename, final_content_type, use_multipart
