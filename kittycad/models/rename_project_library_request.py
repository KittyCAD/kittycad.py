from .base import KittyCadBaseModel


class RenameProjectLibraryRequest(KittyCadBaseModel):
    """Request to rename a cloud project library."""

    expected_revision: str

    name: str
