import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class euclidean(BaseModel):
    """Euclidean Distance."""
    
    
    type: Literal["euclidean"] = "euclidean"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.global_axis import GlobalAxis



class on_axis(BaseModel):
    """The distance between objects along the specified axis"""
    
    
    axis: GlobalAxis
    
    
    
    type: Literal["on_axis"] = "on_axis"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
from typing import Dict, Any, Union, Type, TypeVar
from pydantic import RootModel, Field

from typing_extensions import Annotated




DistanceType = RootModel[Annotated[Union[
        
        euclidean,
        
        on_axis,
        
    ], Field(discriminator='type')]]

