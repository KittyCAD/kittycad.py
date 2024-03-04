import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.plan_interval import PlanInterval



class flat(BaseModel):
    """A flat price that we publicly list."""
    
    
    interval: PlanInterval
    
    
    
    price: float
    
    
    
    type: Literal["flat"] = "flat"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.plan_interval import PlanInterval



class per_user(BaseModel):
    """A per user price that we publicly list."""
    
    
    interval: PlanInterval
    
    
    
    price: float
    
    
    
    type: Literal["per_user"] = "per_user"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class enterprise(BaseModel):
    """Enterprise: The price is not listed and the user needs to contact sales."""
    
    
    type: Literal["enterprise"] = "enterprise"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
from typing import Dict, Any, Union, Type, TypeVar
from pydantic import RootModel, Field

from typing_extensions import Annotated




SubscriptionTierPrice = RootModel[Annotated[Union[
        
        flat,
        
        per_user,
        
        enterprise,
        
    ], Field(discriminator='type')]]

