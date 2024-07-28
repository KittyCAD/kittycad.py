import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class SelectWithPoint(BaseModel):
    """The response from the `SelectWithPoint` command."""

    entity_id: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
