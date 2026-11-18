from typing import Optional

from .base import KittyCadBaseModel


class ExecutionJobOutput(KittyCadBaseModel):
    """An output path or glob to collect after execution."""

    path: str

    required: Optional[bool] = True
