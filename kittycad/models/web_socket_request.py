from typing import Dict, List, Literal, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.client_metrics import ClientMetrics
from ..models.modeling_cmd import ModelingCmd
from ..models.modeling_cmd_id import ModelingCmdId
from ..models.modeling_cmd_req import ModelingCmdReq
from ..models.rtc_ice_candidate_init import RtcIceCandidateInit
from ..models.rtc_session_description import RtcSessionDescription
from .base import KittyCadBaseModel


class OptionTrickleIce(KittyCadBaseModel):
    """The trickle ICE candidate request."""

    candidate: RtcIceCandidateInit

    type: Literal["trickle_ice"] = "trickle_ice"


class OptionSdpOffer(KittyCadBaseModel):
    """The SDP offer request."""

    offer: RtcSessionDescription

    type: Literal["sdp_offer"] = "sdp_offer"


class OptionModelingCmdReq(KittyCadBaseModel):
    """The modeling command request."""

    cmd: ModelingCmd

    cmd_id: ModelingCmdId

    type: Literal["modeling_cmd_req"] = "modeling_cmd_req"


class OptionModelingCmdBatchReq(KittyCadBaseModel):
    """A sequence of modeling requests. If any request fails, following requests will not be tried."""

    batch_id: ModelingCmdId

    requests: List[ModelingCmdReq]

    responses: bool = False

    type: Literal["modeling_cmd_batch_req"] = "modeling_cmd_batch_req"


class OptionPing(KittyCadBaseModel):
    """The client-to-server Ping to ensure the WebSocket stays alive."""

    type: Literal["ping"] = "ping"


class OptionMetricsResponse(KittyCadBaseModel):
    """The response to a metrics collection request from the server."""

    metrics: ClientMetrics

    type: Literal["metrics_response"] = "metrics_response"


class OptionDebug(KittyCadBaseModel):
    """Return information about the connected instance"""

    type: Literal["debug"] = "debug"


class OptionHeaders(KittyCadBaseModel):
    """Authentication header request."""

    headers: Dict[str, str]

    type: Literal["headers"] = "headers"


WebSocketRequest = RootModel[
    Annotated[
        Union[
            OptionTrickleIce,
            OptionSdpOffer,
            OptionModelingCmdReq,
            OptionModelingCmdBatchReq,
            OptionPing,
            OptionMetricsResponse,
            OptionDebug,
            OptionHeaders,
        ],
        Field(discriminator="type"),
    ]
]
