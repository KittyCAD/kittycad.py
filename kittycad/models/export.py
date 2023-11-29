from typing import List

from pydantic import BaseModel

from ..models.export_file import ExportFile


class Export(BaseModel):
    """The response from the `Export` endpoint."""

    files: List[ExportFile]
