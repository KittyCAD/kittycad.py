from typing import List

from ..models.kcl_file import KclFile
from ..models.safe_filepath import SafeFilepath
from .base import KittyCadBaseModel


class KclProject(KittyCadBaseModel):
    """A KCL project."""

    entrypoint: SafeFilepath

    files: List[KclFile]
