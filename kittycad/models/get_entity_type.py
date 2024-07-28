import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.entity_type import EntityType
from .base64data import Base64Data


class GetEntityType(BaseModel):
    """The response from the `GetEntityType` command."""

    entity_type: EntityType

    model_config = ConfigDict(protected_namespaces=())
