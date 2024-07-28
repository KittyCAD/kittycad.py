import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class Gateway(BaseModel):
    """Gateway information."""

    auth_timeout: Optional[int] = None

    host: Optional[str] = None

    name: Optional[str] = None

    port: Optional[int] = None

    tls_timeout: Optional[int] = None

    model_config = ConfigDict(protected_namespaces=())
