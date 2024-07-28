import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.error_code import ErrorCode
from .base64data import Base64Data


class ApiError(BaseModel):
    """An error."""

    error_code: ErrorCode

    message: str

    model_config = ConfigDict(protected_namespaces=())
