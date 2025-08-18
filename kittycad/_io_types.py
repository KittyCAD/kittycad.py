"""Shared type aliases for file I/O operations in the KittyCAD SDK.

This module defines the type unions that make file operations Pythonic by accepting
multiple input types (paths, file objects, bytes, iterators) and normalizing them
internally.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import IO, AsyncIterable, Callable, Iterable, Union

# Path-like types (PEP 519 compliant)
PathType = Union[str, Path, os.PathLike[str]]

# Bytes-like types
BytesLike = Union[bytes, bytearray, memoryview]

# What users can pass as "the thing to upload" (sync)
SyncUpload = Union[
    PathType,  # File path as string, Path, or os.PathLike
    IO[bytes],  # File-like object (open file, BytesIO, etc.)
    BytesLike,  # Raw bytes/bytearray/memoryview
    Iterable[bytes],  # Iterator of byte chunks for streaming
]

# What users can pass as "the thing to upload" (async)
AsyncUpload = Union[
    PathType,  # File path as string, Path, or os.PathLike
    IO[bytes],  # File-like object (open file, BytesIO, etc.)
    BytesLike,  # Raw bytes/bytearray/memoryview
    AsyncIterable[bytes],  # Async iterator of byte chunks for streaming
]

# What users can pass as "where to download to" (sync)
SyncDownload = Union[
    PathType,  # File path to write to
    IO[bytes],  # File-like object to write to
    None,  # Return bytes directly
]

# Progress callback type
ProgressCallback = Callable[[int, int | None], None]  # (bytes_sent, total_bytes)

# Content type override
ContentType = str

# Filename override
Filename = str
