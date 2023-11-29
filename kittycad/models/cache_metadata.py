
from pydantic import BaseModel



class CacheMetadata(BaseModel):
    """Metadata about our cache.

    This is mostly used for internal purposes and debugging."""

    ok: bool
