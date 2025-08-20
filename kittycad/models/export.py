from typing import List

from ..models.export_file import ExportFile
from .base import KittyCadBaseModel


class Export(KittyCadBaseModel):
    """The response from the `Export` endpoint."""

    files: List[ExportFile]
