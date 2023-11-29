from typing import Optional

from pydantic import BaseModel



class LeafNode(BaseModel):
    """Leaf node information."""

    auth_timeout: Optional[int] = None

    host: Optional[str] = None

    port: Optional[int] = None

    tls_timeout: Optional[int] = None
