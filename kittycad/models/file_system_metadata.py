
from pydantic import BaseModel



class FileSystemMetadata(BaseModel):
    """Metadata about our file system.

    This is mostly used for internal purposes and debugging."""

    ok: bool
