from typing import Dict, List, Literal, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.batch_response import BatchResponse
from ..models.ice_server import IceServer
from ..models.modeling_session_data import ModelingSessionData
from ..models.ok_modeling_cmd_response import OkModelingCmdResponse
from ..models.raw_file import RawFile
from ..models.rtc_ice_candidate_init import RtcIceCandidateInit
from ..models.rtc_session_description import RtcSessionDescription
from .base import KittyCadBaseModel


class IceServerInfoData(KittyCadBaseModel):
    """"""

    ice_servers: List[IceServer]


class OptionIceServerInfo(KittyCadBaseModel):
    """Information about the ICE servers."""

    data: IceServerInfoData

    type: Literal["ice_server_info"] = "ice_server_info"


class TrickleIceData(KittyCadBaseModel):
    """"""

    candidate: RtcIceCandidateInit


class OptionTrickleIce(KittyCadBaseModel):
    """The trickle ICE candidate response."""

    data: TrickleIceData

    type: Literal["trickle_ice"] = "trickle_ice"


class SdpAnswerData(KittyCadBaseModel):
    """"""

    answer: RtcSessionDescription


class OptionSdpAnswer(KittyCadBaseModel):
    """The SDP answer response."""

    data: SdpAnswerData

    type: Literal["sdp_answer"] = "sdp_answer"


class ModelingData(KittyCadBaseModel):
    """"""

    modeling_response: OkModelingCmdResponse


class OptionModeling(KittyCadBaseModel):
    """The modeling command response."""

    data: ModelingData

    type: Literal["modeling"] = "modeling"


class ModelingBatchData(KittyCadBaseModel):
    """"""

    responses: Dict[str, BatchResponse]


class OptionModelingBatch(KittyCadBaseModel):
    """Response to a ModelingBatch."""

    data: ModelingBatchData

    type: Literal["modeling_batch"] = "modeling_batch"


class ExportData(KittyCadBaseModel):
    """"""

    files: List[RawFile]


class OptionExport(KittyCadBaseModel):
    """The exported files."""

    data: ExportData

    type: Literal["export"] = "export"


class MetricsRequestData(KittyCadBaseModel):
    """"""


class OptionMetricsRequest(KittyCadBaseModel):
    """Request a collection of metrics, to include WebRTC."""

    data: MetricsRequestData

    type: Literal["metrics_request"] = "metrics_request"


class ModelingSessionDataData(KittyCadBaseModel):
    """"""

    session: ModelingSessionData


class OptionModelingSessionData(KittyCadBaseModel):
    """Data about the Modeling Session (application-level)."""

    data: ModelingSessionDataData

    type: Literal["modeling_session_data"] = "modeling_session_data"


class PongData(KittyCadBaseModel):
    """"""


class OptionPong(KittyCadBaseModel):
    """Pong response to a Ping message."""

    data: PongData

    type: Literal["pong"] = "pong"


class DebugData(KittyCadBaseModel):
    """"""

    name: str


class OptionDebug(KittyCadBaseModel):
    """Information about the connected instance"""

    data: DebugData

    type: Literal["debug"] = "debug"


OkWebSocketResponseData = RootModel[
    Annotated[
        Union[
            OptionIceServerInfo,
            OptionTrickleIce,
            OptionSdpAnswer,
            OptionModeling,
            OptionModelingBatch,
            OptionExport,
            OptionMetricsRequest,
            OptionModelingSessionData,
            OptionPong,
            OptionDebug,
        ],
        Field(discriminator="type"),
    ]
]
