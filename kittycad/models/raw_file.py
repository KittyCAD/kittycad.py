import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class RawFile(BaseModel):
    """A raw file with unencoded contents to be passed over binary websockets. When raw files come back for exports it is sent as binary/bson, not text/json."""

    contents: bytes

    name: str

    model_config = ConfigDict(protected_namespaces=())
