import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.rtc_ice_candidate_init import RtcIceCandidateInit



class trickle_ice(BaseModel):
    """The trickle ICE candidate request."""
    
    
    candidate: RtcIceCandidateInit
    
    
    
    type: Literal["trickle_ice"] = "trickle_ice"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.rtc_session_description import RtcSessionDescription



class sdp_offer(BaseModel):
    """The SDP offer request."""
    
    
    offer: RtcSessionDescription
    
    
    
    type: Literal["sdp_offer"] = "sdp_offer"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.modeling_cmd import ModelingCmd


from ..models.modeling_cmd_id import ModelingCmdId



class modeling_cmd_req(BaseModel):
    """The modeling command request."""
    
    
    cmd: ModelingCmd
    
    
    
    cmd_id: ModelingCmdId
    
    
    
    type: Literal["modeling_cmd_req"] = "modeling_cmd_req"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.modeling_cmd_req import ModelingCmdReq



class modeling_cmd_batch_req(BaseModel):
    """A sequence of modeling requests. If any request fails, following requests will not be tried."""
    
    
    requests: List[ModelingCmdReq]
    
    
    
    type: Literal["modeling_cmd_batch_req"] = "modeling_cmd_batch_req"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class ping(BaseModel):
    """The client-to-server Ping to ensure the WebSocket stays alive."""
    
    
    type: Literal["ping"] = "ping"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.client_metrics import ClientMetrics



class metrics_response(BaseModel):
    """The response to a metrics collection request from the server."""
    
    
    metrics: ClientMetrics
    
    
    
    type: Literal["metrics_response"] = "metrics_response"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
from typing import Dict, Any, Union, Type, TypeVar
from pydantic import RootModel, Field

from typing_extensions import Annotated




WebSocketRequest = RootModel[Annotated[Union[
        
        trickle_ice,
        
        sdp_offer,
        
        modeling_cmd_req,
        
        modeling_cmd_batch_req,
        
        ping,
        
        metrics_response,
        
    ], Field(discriminator='type')]]

