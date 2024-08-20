
from pydantic import BaseModel, ConfigDict

from ..models.jetstream_api_stats import JetstreamApiStats


class JetstreamStats(BaseModel):
    """Jetstream statistics."""

    accounts: int = 0

    api: JetstreamApiStats = {"errors": 0, "inflight": 0, "total": 0}

    ha_assets: int = 0

    memory: int = 0

    reserved_memory: int = 0

    reserved_store: int = 0

    store: int = 0

    model_config = ConfigDict(protected_namespaces=())
