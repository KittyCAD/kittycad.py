"""Progress tracking utilities for file uploads and downloads.

This module provides utilities for tracking progress during file operations,
including callback-based progress reporting and wrapper classes for monitoring
bytes transferred.
"""

from __future__ import annotations

import io
from typing import IO, Callable, Optional, Union


class ProgressTrackingReader:
    """A wrapper that tracks bytes read from a file-like object.

    This class wraps any file-like object and calls a progress callback
    as bytes are read, enabling progress tracking for uploads.
    """

    def __init__(
        self,
        file_obj: IO[bytes],
        progress_callback: Optional[Callable[[int, Optional[int]], None]] = None,
        total_size: Optional[int] = None,
    ):
        """Initialize the progress tracking reader.

        Args:
            file_obj: The file-like object to wrap
            progress_callback: Optional callback(bytes_read, total_size)
            total_size: Optional total size for percentage calculations
        """
        self._file_obj = file_obj
        self._progress_callback = progress_callback
        self._total_size = total_size
        self._bytes_read = 0

        # Try to determine total size if not provided
        if self._total_size is None:
            self._total_size = self._get_total_size()

    def _get_total_size(self) -> Optional[int]:
        """Try to determine the total size of the file object."""
        try:
            if hasattr(self._file_obj, "seek") and hasattr(self._file_obj, "tell"):
                current_pos = self._file_obj.tell()
                self._file_obj.seek(0, io.SEEK_END)
                size = self._file_obj.tell()
                self._file_obj.seek(current_pos)
                return size
        except (OSError, io.UnsupportedOperation):
            pass

        # Try to get size from stat if it's a real file
        if hasattr(self._file_obj, "fileno"):
            try:
                import os

                stat = os.fstat(self._file_obj.fileno())
                return stat.st_size
            except (OSError, AttributeError):
                pass

        return None

    def read(self, size: int = -1) -> bytes:
        """Read bytes and update progress."""
        data = self._file_obj.read(size)
        if data:
            self._bytes_read += len(data)
            if self._progress_callback:
                self._progress_callback(self._bytes_read, self._total_size)
        return data

    def readline(self, size: int = -1) -> bytes:
        """Read a line and update progress."""
        data = self._file_obj.readline(size)
        if data:
            self._bytes_read += len(data)
            if self._progress_callback:
                self._progress_callback(self._bytes_read, self._total_size)
        return data

    def readlines(self, hint: int = -1) -> list[bytes]:
        """Read lines and update progress."""
        lines = self._file_obj.readlines(hint)
        if lines:
            total_bytes = sum(len(line) for line in lines)
            self._bytes_read += total_bytes
            if self._progress_callback:
                self._progress_callback(self._bytes_read, self._total_size)
        return lines

    def __getattr__(self, name):
        """Delegate other attributes to the wrapped file object."""
        return getattr(self._file_obj, name)

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        if hasattr(self._file_obj, "__exit__"):
            return self._file_obj.__exit__(exc_type, exc_val, exc_tb)
        return None


class ProgressTrackingWriter:
    """A wrapper that tracks bytes written to a file-like object.

    This class wraps any file-like object and calls a progress callback
    as bytes are written, enabling progress tracking for downloads.
    """

    def __init__(
        self,
        file_obj: IO[bytes],
        progress_callback: Optional[Callable[[int, Optional[int]], None]] = None,
        total_size: Optional[int] = None,
    ):
        """Initialize the progress tracking writer.

        Args:
            file_obj: The file-like object to wrap
            progress_callback: Optional callback(bytes_written, total_size)
            total_size: Optional total size for percentage calculations
        """
        self._file_obj = file_obj
        self._progress_callback = progress_callback
        self._total_size = total_size
        self._bytes_written = 0

    def write(self, data: bytes) -> int:
        """Write bytes and update progress."""
        written = self._file_obj.write(data)
        self._bytes_written += written
        if self._progress_callback:
            self._progress_callback(self._bytes_written, self._total_size)
        return written

    def writelines(self, lines) -> None:
        """Write lines and update progress."""
        for line in lines:
            self.write(line)

    def __getattr__(self, name):
        """Delegate other attributes to the wrapped file object."""
        return getattr(self._file_obj, name)

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        if hasattr(self._file_obj, "__exit__"):
            return self._file_obj.__exit__(exc_type, exc_val, exc_tb)
        return None


def create_progress_callback(
    description: str = "Transfer", show_percentage: bool = True, show_speed: bool = True
) -> Callable[[int, Optional[int]], None]:
    """Create a simple console progress callback.

    Args:
        description: Description to show (e.g., "Uploading", "Downloading")
        show_percentage: Whether to show percentage complete
        show_speed: Whether to show transfer speed

    Returns:
        A progress callback function suitable for use with progress tracking classes

    Example:
        >>> progress = create_progress_callback("Uploading file")
        >>> # progress will print: "Uploading file: 1024/2048 bytes (50%) [1.2 MB/s]"
    """
    import time

    start_time = time.time()
    last_bytes = 0
    last_time = start_time

    def progress_callback(bytes_transferred: int, total_bytes: Optional[int]) -> None:
        nonlocal last_bytes, last_time

        current_time = time.time()

        # Build progress message
        parts = [f"{description}: {bytes_transferred:,} bytes"]

        if total_bytes:
            parts.append(f"/{total_bytes:,}")
            if show_percentage:
                percentage = (bytes_transferred / total_bytes) * 100
                parts.append(f" ({percentage:.1f}%)")

        # Calculate and show speed
        if show_speed and current_time > last_time:
            time_diff = current_time - last_time
            bytes_diff = bytes_transferred - last_bytes
            speed = bytes_diff / time_diff

            # Format speed in human-readable units
            if speed >= 1024 * 1024:
                speed_str = f"{speed / (1024 * 1024):.1f} MB/s"
            elif speed >= 1024:
                speed_str = f"{speed / 1024:.1f} KB/s"
            else:
                speed_str = f"{speed:.1f} B/s"

            parts.append(f" [{speed_str}]")

        # Print with carriage return to overwrite previous line
        print("".join(parts), end="\r", flush=True)

        last_bytes = bytes_transferred
        last_time = current_time

        # Print newline when complete
        if total_bytes and bytes_transferred >= total_bytes:
            print()  # Move to next line when complete

    return progress_callback


def wrap_with_progress(
    file_obj: IO[bytes],
    progress_callback: Optional[Callable[[int, Optional[int]], None]] = None,
    total_size: Optional[int] = None,
    for_reading: bool = True,
) -> Union[IO[bytes], ProgressTrackingReader, ProgressTrackingWriter]:
    """Wrap a file object with progress tracking.

    Args:
        file_obj: The file-like object to wrap
        progress_callback: Optional progress callback function
        total_size: Optional total size for percentage calculations
        for_reading: True for upload progress, False for download progress

    Returns:
        A progress-tracking wrapper around the file object
    """
    if not progress_callback:
        return file_obj

    if for_reading:
        return ProgressTrackingReader(file_obj, progress_callback, total_size)
    else:
        return ProgressTrackingWriter(file_obj, progress_callback, total_size)
