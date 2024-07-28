import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.cache_metadata import CacheMetadata
from ..models.connection import Connection
from ..models.environment import Environment
from ..models.file_system_metadata import FileSystemMetadata
from .base64data import Base64Data


class Metadata(BaseModel):
    """Metadata about our currently running server.

    This is mostly used for internal purposes and debugging."""

    cache: CacheMetadata

    environment: Environment

    fs: FileSystemMetadata

    git_hash: str

    pubsub: Connection

    model_config = ConfigDict(protected_namespaces=())
