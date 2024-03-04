import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class individual(BaseModel):
    """A subscription tier that can be applied to individuals only."""
    
    
    type: Literal["individual"] = "individual"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class organization(BaseModel):
    """An subscription tier that can be applied to organizations only."""
    
    
    saml_sso: bool
    
    
    
    type: Literal["organization"] = "organization"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
from typing import Dict, Any, Union, Type, TypeVar
from pydantic import RootModel, Field

from typing_extensions import Annotated




SubscriptionTierType = RootModel[Annotated[Union[
        
        individual,
        
        organization,
        
    ], Field(discriminator='type')]]

