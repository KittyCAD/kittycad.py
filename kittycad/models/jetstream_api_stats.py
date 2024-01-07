from typing import Optional

from pydantic import BaseModel, ConfigDict



class JetstreamApiStats(BaseModel):
    """Jetstream API statistics."""

    errors: Optional[int] = None

    inflight: Optional[int] = None

    total: Optional[int] = None

    model_config = ConfigDict(protected_namespaces=())
