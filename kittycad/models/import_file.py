from .base import KittyCadBaseModel


class ImportFile(KittyCadBaseModel):
    """File to import into the current scene."""

    data: bytes

    path: str
