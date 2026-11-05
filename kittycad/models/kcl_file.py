from ..models.safe_filepath import SafeFilepath
from .base import KittyCadBaseModel


class KclFile(KittyCadBaseModel):
    """A file in a KCL project."""

    contents: bytes

    path: SafeFilepath
