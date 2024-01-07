
from pydantic import BaseModel, ConfigDict



class FileSystemMetadata(BaseModel):
    """Metadata about our file system.

    This is mostly used for internal purposes and debugging."""

    ok: bool

    model_config = ConfigDict(protected_namespaces=())
