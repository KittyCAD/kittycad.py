import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class UpdateUser(BaseModel):
    """The user-modifiable parts of a User."""

    company: Optional[str] = None

    discord: Optional[str] = None

    first_name: Optional[str] = None

    github: Optional[str] = None

    image: str

    last_name: Optional[str] = None

    phone: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
