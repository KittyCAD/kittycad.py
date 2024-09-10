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

    type: Literal["option_trickle_ice"] = "option_trickle_ice"

    model_config = ConfigDict(protected_namespaces=())


class OptionSdpOffer(BaseModel):
    """The SDP offer request."""

    offer: RtcSessionDescription

    type: Literal["option_sdp_offer"] = "option_sdp_offer"

    model_config = ConfigDict(protected_namespaces=())


class OptionModelingCmdReq(BaseModel):
    """The modeling command request."""

    cmd: ModelingCmd

    cmd_id: ModelingCmdId

    type: Literal["option_modeling_cmd_req"] = "option_modeling_cmd_req"

    model_config = ConfigDict(protected_namespaces=())


class OptionModelingCmdBatchReq(BaseModel):
    """A sequence of modeling requests. If any request fails, following requests will not be tried."""

    batch_id: ModelingCmdId

    requests: List[ModelingCmdReq]

    responses: bool = False

    type: Literal["option_modeling_cmd_batch_req"] = "option_modeling_cmd_batch_req"

    model_config = ConfigDict(protected_namespaces=())


class OptionPing(BaseModel):
    """The client-to-server Ping to ensure the WebSocket stays alive."""

    type: Literal["option_ping"] = "option_ping"

    model_config = ConfigDict(protected_namespaces=())


class OptionMetricsResponse(BaseModel):
    """The response to a metrics collection request from the server."""

    metrics: ClientMetrics

    type: Literal["option_metrics_response"] = "option_metrics_response"

    model_config = ConfigDict(protected_namespaces=())


class OptionHeaders(BaseModel):
    """Authentication header request."""

    headers: Dict[str, str]

    type: Literal["option_headers"] = "option_headers"

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
