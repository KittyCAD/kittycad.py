from typing import Dict, List, Literal, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated

from ..models.client_metrics import ClientMetrics
from ..models.modeling_cmd import ModelingCmd
from ..models.modeling_cmd_id import ModelingCmdId
from ..models.modeling_cmd_req import ModelingCmdReq
from ..models.rtc_ice_candidate_init import RtcIceCandidateInit
from ..models.rtc_session_description import RtcSessionDescription


class OptionTrickleIce(BaseModel):
    """The trickle ICE candidate request."""

    candidate: RtcIceCandidateInit

    type: Literal["trickle_ice"] = "trickle_ice"

    model_config = ConfigDict(protected_namespaces=())


class OptionSdpOffer(BaseModel):
    """The SDP offer request."""

    offer: RtcSessionDescription

    type: Literal["sdp_offer"] = "sdp_offer"

    model_config = ConfigDict(protected_namespaces=())


class OptionModelingCmdReq(BaseModel):
    """The modeling command request."""

    cmd: ModelingCmd

    cmd_id: ModelingCmdId

    type: Literal["modeling_cmd_req"] = "modeling_cmd_req"

    model_config = ConfigDict(protected_namespaces=())


class OptionModelingCmdBatchReq(BaseModel):
    """A sequence of modeling requests. If any request fails, following requests will not be tried."""

    batch_id: ModelingCmdId

    requests: List[ModelingCmdReq]

    responses: bool = False

    type: Literal["modeling_cmd_batch_req"] = "modeling_cmd_batch_req"

    model_config = ConfigDict(protected_namespaces=())


class OptionPing(BaseModel):
    """The client-to-server Ping to ensure the WebSocket stays alive."""

    type: Literal["ping"] = "ping"

    model_config = ConfigDict(protected_namespaces=())


class OptionMetricsResponse(BaseModel):
    """The response to a metrics collection request from the server."""

    metrics: ClientMetrics

    type: Literal["metrics_response"] = "metrics_response"

    model_config = ConfigDict(protected_namespaces=())


class OptionHeaders(BaseModel):
    """Authentication header request."""

    headers: Dict[str, str]

    type: Literal["headers"] = "headers"

    model_config = ConfigDict(protected_namespaces=())


WebSocketRequest = RootModel[
    Annotated[
        Union[
            OptionTrickleIce,
            OptionSdpOffer,
            OptionModelingCmdReq,
            OptionModelingCmdBatchReq,
            OptionPing,
            OptionMetricsResponse,
            OptionHeaders,
        ],
        Field(discriminator="type"),
    ]
]
