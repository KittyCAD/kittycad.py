from ..models.error_code import ErrorCode
from .base import KittyCadBaseModel


class ApiError(KittyCadBaseModel):
    """An error."""

    error_code: ErrorCode

    message: str
