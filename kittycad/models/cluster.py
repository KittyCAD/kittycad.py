from typing import List, Optional

from pydantic import BaseModel, ConfigDict



class Cluster(BaseModel):
    """Cluster information."""

    addr: Optional[str] = None

    auth_timeout: Optional[int] = None

    cluster_port: Optional[int] = None

    name: Optional[str] = None

    tls_timeout: Optional[int] = None

    urls: Optional[List[str]] = None

    model_config = ConfigDict(protected_namespaces=())
