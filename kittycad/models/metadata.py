
from pydantic import BaseModel, ConfigDict

from ..models.cache_metadata import CacheMetadata
from ..models.connection import Connection
from ..models.environment import Environment
from ..models.file_system_metadata import FileSystemMetadata


class Metadata(BaseModel):
    """Metadata about our currently running server.

    This is mostly used for internal purposes and debugging."""

    cache: CacheMetadata

    environment: Environment

    fs: FileSystemMetadata

    git_hash: str

    pubsub: Connection

    model_config = ConfigDict(protected_namespaces=())
