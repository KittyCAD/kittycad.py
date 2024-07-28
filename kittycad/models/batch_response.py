import datetime
from typing import Any, Dict, List, Literal, Optional, Type, TypeVar, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict, Field, RootModel
from pydantic_extra_types.phone_numbers import PhoneNumber
from typing_extensions import Annotated

from ..models.api_error import ApiError
from ..models.ok_modeling_cmd_response import OkModelingCmdResponse
from .base64data import Base64Data


class response(BaseModel):
    """Response to the modeling command."""

    model_config = ConfigDict(protected_namespaces=())


class errors(BaseModel):
    """Errors that occurred during the modeling command."""

    model_config = ConfigDict(protected_namespaces=())


BatchResponse = RootModel[
    Union[
        response,
        errors,
    ]
]
