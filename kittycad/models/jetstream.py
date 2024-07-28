import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.jetstream_config import JetstreamConfig
from ..models.jetstream_stats import JetstreamStats
from ..models.meta_cluster_info import MetaClusterInfo
from .base64data import Base64Data


class Jetstream(BaseModel):
    """Jetstream information."""

    config: Optional[JetstreamConfig] = None

    meta: Optional[MetaClusterInfo] = None

    stats: Optional[JetstreamStats] = None

    model_config = ConfigDict(protected_namespaces=())
