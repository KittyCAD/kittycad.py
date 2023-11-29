from typing import List, Literal, Union

from pydantic import BaseModel, Field, RootModel
from typing_extensions import Annotated

from ..models.client_metrics import ClientMetrics
from ..models.modeling_cmd import ModelingCmd
from ..models.modeling_cmd_id import ModelingCmdId
from ..models.modeling_cmd_req import ModelingCmdReq
from ..models.rtc_ice_candidate_init import RtcIceCandidateInit
from ..models.rtc_session_description import RtcSessionDescription


class trickle_ice(BaseModel):
    """The trickle ICE candidate request."""

    candidate: RtcIceCandidateInit

    type: Literal["trickle_ice"] = "trickle_ice"


class sdp_offer(BaseModel):
    """The SDP offer request."""

    offer: RtcSessionDescription

    type: Literal["sdp_offer"] = "sdp_offer"


class modeling_cmd_req(BaseModel):
    """The modeling command request."""

    cmd: ModelingCmd

    cmd_id: ModelingCmdId

    type: Literal["modeling_cmd_req"] = "modeling_cmd_req"


class modeling_cmd_batch_req(BaseModel):
    """A sequence of modeling requests. If any request fails, following requests will not be tried."""

    requests: List[ModelingCmdReq]

    type: Literal["modeling_cmd_batch_req"] = "modeling_cmd_batch_req"


class ping(BaseModel):
    """The client-to-server Ping to ensure the WebSocket stays alive."""

    type: Literal["ping"] = "ping"


class metrics_response(BaseModel):
    """The response to a metrics collection request from the server."""

    metrics: ClientMetrics

    type: Literal["metrics_response"] = "metrics_response"


WebSocketRequest = RootModel[
    Annotated[
        Union[
            trickle_ice,
            sdp_offer,
            modeling_cmd_req,
            modeling_cmd_batch_req,
            ping,
            metrics_response,
        ],
        Field(discriminator="type"),
    ]
]
