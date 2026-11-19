from typing import Optional

from ..models.execution_log_stream import ExecutionLogStream
from .base import KittyCadBaseModel


class ExecutionLogResponse(KittyCadBaseModel):
    """Binary-safe log page with explicit availability and incomplete-tail evidence."""

    available: bool

    complete: bool

    data_base64: str

    failure_code: Optional[str] = None

    next_offset: int

    offset: int

    state: str

    stored_bytes: Optional[int] = None

    stream: ExecutionLogStream

    truncated: bool
