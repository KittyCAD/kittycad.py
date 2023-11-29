from typing import Optional

from pydantic import BaseModel



class JetstreamConfig(BaseModel):
    """Jetstream configuration."""

    domain: Optional[str] = None

    max_memory: Optional[int] = None

    max_storage: Optional[int] = None

    store_dir: Optional[str] = None
