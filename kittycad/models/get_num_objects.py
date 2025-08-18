from .base import KittyCadBaseModel


class GetNumObjects(KittyCadBaseModel):
    """The response from the `GetNumObjects` command."""

    num_objects: int
