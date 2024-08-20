from typing import List, Optional

from pydantic import BaseModel, ConfigDict



class Cluster(BaseModel):
    """Cluster information."""

    addr: Optional[str] = None

    auth_timeout: int = 0

    cluster_port: int = 0

    name: str = ""

    tls_timeout: int = 0

    urls: List[str] = []

    model_config = ConfigDict(protected_namespaces=())
