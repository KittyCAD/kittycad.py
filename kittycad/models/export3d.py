from typing import List

from ..models.export_file import ExportFile
from .base import KittyCadBaseModel


class Export3d(KittyCadBaseModel):
    """The response from the `Export3d` endpoint."""

    files: List[ExportFile]
