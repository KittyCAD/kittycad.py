
from pydantic import BaseModel, ConfigDict



class JetstreamConfig(BaseModel):
    """Jetstream configuration."""

    domain: str = ""

    max_memory: int = 0

    max_storage: int = 0

    store_dir: str = ""

    model_config = ConfigDict(protected_namespaces=())
