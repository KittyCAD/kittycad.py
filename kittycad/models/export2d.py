from typing import List

from ..models.export_file import ExportFile
from .base import KittyCadBaseModel


class Export2d(KittyCadBaseModel):
    """The response from the `Export2d` endpoint."""

    files: List[ExportFile]
