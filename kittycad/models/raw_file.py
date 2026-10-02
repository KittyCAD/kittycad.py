from .base import KittyCadBaseModel


class RawFile(KittyCadBaseModel):
    """A raw file with unencoded contents.

    See the command that emits this type for its response encoding."""

    contents: bytes

    name: str
