import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class JetstreamConfig(BaseModel):
    """Jetstream configuration."""

    domain: Optional[str] = None

    max_memory: Optional[int] = None

    max_storage: Optional[int] = None

    store_dir: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
