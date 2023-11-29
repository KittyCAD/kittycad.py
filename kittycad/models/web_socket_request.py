from typing import List, Union

from pydantic import BaseModel, RootModel

from ..models.client_metrics import ClientMetrics
from ..models.modeling_cmd import ModelingCmd
from ..models.modeling_cmd_id import ModelingCmdId
from ..models.modeling_cmd_req import ModelingCmdReq
from ..models.rtc_ice_candidate_init import RtcIceCandidateInit
from ..models.rtc_session_description import RtcSessionDescription


class trickle_ice(BaseModel):
    """The trickle ICE candidate request."""

    candidate: RtcIceCandidateInit

    type: str = "trickle_ice"


class sdp_offer(BaseModel):
    """The SDP offer request."""

    offer: RtcSessionDescription

    type: str = "sdp_offer"


class modeling_cmd_req(BaseModel):
    """The modeling command request."""

    cmd: ModelingCmd

    cmd_id: ModelingCmdId

    type: str = "modeling_cmd_req"


class modeling_cmd_batch_req(BaseModel):
    """A sequence of modeling requests. If any request fails, following requests will not be tried."""

    requests: List[ModelingCmdReq]

    type: str = "modeling_cmd_batch_req"


class ping(BaseModel):
    """The client-to-server Ping to ensure the WebSocket stays alive."""

    type: str = "ping"


class metrics_response(BaseModel):
    """The response to a metrics collection request from the server."""

    metrics: ClientMetrics

    type: str = "metrics_response"


WebSocketRequest = RootModel[
    Union[
        trickle_ice,
        sdp_offer,
        modeling_cmd_req,
        modeling_cmd_batch_req,
        ping,
        metrics_response,
    ]
]
