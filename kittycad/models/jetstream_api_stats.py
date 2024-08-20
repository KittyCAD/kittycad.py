
from pydantic import BaseModel, ConfigDict



class JetstreamApiStats(BaseModel):
    """Jetstream API statistics."""

    errors: int = 0

    inflight: int = 0

    total: int = 0

    model_config = ConfigDict(protected_namespaces=())
