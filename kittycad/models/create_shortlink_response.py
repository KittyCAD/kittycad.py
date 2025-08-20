from .base import KittyCadBaseModel


class CreateShortlinkResponse(KittyCadBaseModel):
    """Response from creating a shortlink."""

    key: str

    url: str
