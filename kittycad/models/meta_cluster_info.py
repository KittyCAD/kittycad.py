import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class MetaClusterInfo(BaseModel):
    """Jetstream statistics."""

    cluster_size: Optional[int] = None

    leader: Optional[str] = None

    name: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
