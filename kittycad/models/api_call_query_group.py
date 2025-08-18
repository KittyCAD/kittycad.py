from .base import KittyCadBaseModel


class ApiCallQueryGroup(KittyCadBaseModel):
    """A response for a query on the API call table that is grouped by something."""

    count: int

    query: str
