from typing import Optional

from pydantic import BaseModel



class MetaClusterInfo(BaseModel):
    """Jetstream statistics."""

    cluster_size: Optional[int] = None

    leader: Optional[str] = None

    name: Optional[str] = None
