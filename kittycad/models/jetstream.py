from typing import Optional

from pydantic import BaseModel

from ..models.jetstream_config import JetstreamConfig
from ..models.jetstream_stats import JetstreamStats
from ..models.meta_cluster_info import MetaClusterInfo


class Jetstream(BaseModel):
    """Jetstream information."""

    config: Optional[JetstreamConfig] = None

    meta: Optional[MetaClusterInfo] = None

    stats: Optional[JetstreamStats] = None
