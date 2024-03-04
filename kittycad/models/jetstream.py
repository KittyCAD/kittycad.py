import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.jetstream_config import JetstreamConfig


from ..models.meta_cluster_info import MetaClusterInfo


from ..models.jetstream_stats import JetstreamStats



class Jetstream(BaseModel):
    """Jetstream information."""
    
    
    config: Optional[JetstreamConfig] = None
    
    
    
    meta: Optional[MetaClusterInfo] = None
    
    
    
    stats: Optional[JetstreamStats] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )