
from pydantic import BaseModel

from ..models.error_code import ErrorCode


class ApiError(BaseModel):
    """An error."""

    error_code: ErrorCode

    message: str
