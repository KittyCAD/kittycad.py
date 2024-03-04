import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.axis_direction_pair import AxisDirectionPair



class System(BaseModel):
    """Co-ordinate system definition.

The `up` axis must be orthogonal to the `forward` axis.

See [cglearn.eu] for background reading.

[cglearn.eu](https://cglearn.eu/pub/computer-graphics/introduction-to-geometry#material-coordinate-systems-1)"""
    
    
    forward: AxisDirectionPair
    
    
    
    up: AxisDirectionPair
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )