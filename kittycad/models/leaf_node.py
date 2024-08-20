
from pydantic import BaseModel, ConfigDict



class LeafNode(BaseModel):
    """Leaf node information."""

    auth_timeout: int = 0

    host: str = ""

    port: int = 0

    tls_timeout: int = 0

    model_config = ConfigDict(protected_namespaces=())
