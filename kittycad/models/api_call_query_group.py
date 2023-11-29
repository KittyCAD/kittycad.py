
from pydantic import BaseModel



class ApiCallQueryGroup(BaseModel):
    """A response for a query on the API call table that is grouped by something."""

    count: int

    query: str
