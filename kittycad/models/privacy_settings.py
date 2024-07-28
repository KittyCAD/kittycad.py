import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class PrivacySettings(BaseModel):
    """Privacy settings for an org or user."""

    can_train_on_data: bool

    model_config = ConfigDict(protected_namespaces=())
