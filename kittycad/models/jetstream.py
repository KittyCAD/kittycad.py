from pydantic import BaseModel, ConfigDict

from ..models.jetstream_config import JetstreamConfig
from ..models.jetstream_stats import JetstreamStats
from ..models.meta_cluster_info import MetaClusterInfo


class Jetstream(BaseModel):
    """Jetstream information."""

    config: JetstreamConfig = {
        "domain": "",
        "max_memory": 0,
        "max_storage": 0,
        "store_dir": "",
    }  # type: ignore

    meta: MetaClusterInfo = {"cluster_size": 0, "leader": "", "name": ""}  # type: ignore

    stats: JetstreamStats = {
        "accounts": 0,
        "api": {"errors": 0, "inflight": 0, "total": 0},
        "ha_assets": 0,
        "memory": 0,
        "reserved_memory": 0,
        "reserved_store": 0,
        "store": 0,
    }  # type: ignore

    model_config = ConfigDict(protected_namespaces=())
