
from pydantic import BaseModel, ConfigDict



class MetaClusterInfo(BaseModel):
    """Jetstream statistics."""

    cluster_size: int = 0

    leader: str = ""

    name: str = ""

    model_config = ConfigDict(protected_namespaces=())
