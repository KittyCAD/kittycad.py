from typing import List

from pydantic import BaseModel, ConfigDict

from ..models.export_file import ExportFile


class Export2d(BaseModel):
    """The response from the `Export2d` endpoint."""

    files: List[ExportFile]

    model_config = ConfigDict(protected_namespaces=())
