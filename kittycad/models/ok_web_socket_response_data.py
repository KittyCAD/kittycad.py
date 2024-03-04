import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.ice_server import IceServer



class IceServerInfoData(BaseModel):
    """"""
    
    
    ice_servers: List[IceServer]
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.ice_server import IceServer



class ice_server_info(BaseModel):
    """Information about the ICE servers."""
    
    
    data: IceServerInfoData
    
    
    
    type: Literal["ice_server_info"] = "ice_server_info"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.rtc_ice_candidate_init import RtcIceCandidateInit



class TrickleIceData(BaseModel):
    """"""
    
    
    candidate: RtcIceCandidateInit
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.rtc_ice_candidate_init import RtcIceCandidateInit



class trickle_ice(BaseModel):
    """The trickle ICE candidate response."""
    
    
    data: TrickleIceData
    
    
    
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



class SdpAnswerData(BaseModel):
    """"""
    
    
    answer: RtcSessionDescription
    
    

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



class sdp_answer(BaseModel):
    """The SDP answer response."""
    
    
    data: SdpAnswerData
    
    
    
    type: Literal["sdp_answer"] = "sdp_answer"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.ok_modeling_cmd_response import OkModelingCmdResponse



class ModelingData(BaseModel):
    """"""
    
    
    modeling_response: OkModelingCmdResponse
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.ok_modeling_cmd_response import OkModelingCmdResponse



class modeling(BaseModel):
    """The modeling command response."""
    
    
    data: ModelingData
    
    
    
    type: Literal["modeling"] = "modeling"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.raw_file import RawFile



class ExportData(BaseModel):
    """"""
    
    
    files: List[RawFile]
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.raw_file import RawFile



class export(BaseModel):
    """The exported files."""
    
    
    data: ExportData
    
    
    
    type: Literal["export"] = "export"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class MetricsRequestData(BaseModel):
    """"""
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class metrics_request(BaseModel):
    """Request a collection of metrics, to include WebRTC."""
    
    
    data: MetricsRequestData
    
    
    
    type: Literal["metrics_request"] = "metrics_request"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class PongData(BaseModel):
    """"""
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class pong(BaseModel):
    """Pong response to a Ping message."""
    
    
    data: PongData
    
    
    
    type: Literal["pong"] = "pong"
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
from typing import Dict, Any, Union, Type, TypeVar
from pydantic import RootModel, Field

from typing_extensions import Annotated




OkWebSocketResponseData = RootModel[Annotated[Union[
        
        ice_server_info,
        
        trickle_ice,
        
        sdp_answer,
        
        modeling,
        
        export,
        
        metrics_request,
        
        pong,
        
    ], Field(discriminator='type')]]

