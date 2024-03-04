from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.jetstream_api_stats import JetstreamApiStats


class JetstreamStats(BaseModel):
    """Jetstream statistics."""

    accounts: Optional[int] = None

    api: Optional[JetstreamApiStats] = None

    ha_assets: Optional[int] = None

    memory: Optional[int] = None

    reserved_memory: Optional[int] = None

    reserved_store: Optional[int] = None

    store: Optional[int] = None

    model_config = ConfigDict(protected_namespaces=())
