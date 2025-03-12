from typing import List

from pydantic import BaseModel, ConfigDict

from ..models.export_file import ExportFile


class Export3d(BaseModel):
    """The response from the `Export3d` endpoint."""

    files: List[ExportFile]

    model_config = ConfigDict(protected_namespaces=())
