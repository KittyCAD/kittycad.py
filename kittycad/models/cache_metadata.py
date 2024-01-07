
from pydantic import BaseModel, ConfigDict



class CacheMetadata(BaseModel):
    """Metadata about our cache.

    This is mostly used for internal purposes and debugging."""

    ok: bool

    model_config = ConfigDict(protected_namespaces=())
