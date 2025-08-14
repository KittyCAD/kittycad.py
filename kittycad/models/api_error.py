from pydantic import BaseModel, ConfigDict

from ..models.error_code import ErrorCode


class Apierror(BaseModel):
    """An error."""

    error_code: ErrorCode

    message: str

    model_config = ConfigDict(protected_namespaces=())
