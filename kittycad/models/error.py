from typing import Optional

from pydantic import BaseModel



class Error(BaseModel):
    """Error information from a response."""

    error_code: Optional[str] = None

    message: str

    request_id: str
