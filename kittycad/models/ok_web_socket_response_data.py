from typing import Dict, List, Literal, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated

from ..models.batch_response import BatchResponse
from ..models.ice_server import IceServer
from ..models.modeling_session_data import ModelingSessionData
from ..models.ok_modeling_cmd_response import OkModelingCmdResponse
from ..models.raw_file import RawFile
from ..models.rtc_ice_candidate_init import RtcIceCandidateInit
from ..models.rtc_session_description import RtcSessionDescription


class IceServerInfoData(BaseModel):
    """"""

    ice_servers: List[IceServer]

    model_config = ConfigDict(protected_namespaces=())


class OptionIceServerInfo(BaseModel):
    """Information about the ICE servers."""

    data: IceServerInfoData

    type: Literal["ice_server_info"] = "ice_server_info"

    model_config = ConfigDict(protected_namespaces=())


class TrickleIceData(BaseModel):
    """"""

    candidate: RtcIceCandidateInit

    model_config = ConfigDict(protected_namespaces=())


class OptionTrickleIce(BaseModel):
    """The trickle ICE candidate response."""

    data: TrickleIceData

    type: Literal["trickle_ice"] = "trickle_ice"

    model_config = ConfigDict(protected_namespaces=())


class SdpAnswerData(BaseModel):
    """"""

    answer: RtcSessionDescription

    model_config = ConfigDict(protected_namespaces=())


class OptionSdpAnswer(BaseModel):
    """The SDP answer response."""

    data: SdpAnswerData

    type: Literal["sdp_answer"] = "sdp_answer"

    model_config = ConfigDict(protected_namespaces=())


class ModelingData(BaseModel):
    """"""

    modeling_response: OkModelingCmdResponse

    model_config = ConfigDict(protected_namespaces=())


class OptionModeling(BaseModel):
    """The modeling command response."""

    data: ModelingData

    type: Literal["modeling"] = "modeling"

    model_config = ConfigDict(protected_namespaces=())


class ModelingBatchData(BaseModel):
    """"""

    responses: Dict[str, BatchResponse]

    model_config = ConfigDict(protected_namespaces=())


class OptionModelingBatch(BaseModel):
    """Response to a ModelingBatch."""

    data: ModelingBatchData

    type: Literal["modeling_batch"] = "modeling_batch"

    model_config = ConfigDict(protected_namespaces=())


class ExportData(BaseModel):
    """"""

    files: List[RawFile]

    model_config = ConfigDict(protected_namespaces=())


class OptionExport(BaseModel):
    """The exported files."""

    data: ExportData

    type: Literal["export"] = "export"

    model_config = ConfigDict(protected_namespaces=())


class MetricsRequestData(BaseModel):
    """"""

    model_config = ConfigDict(protected_namespaces=())


class OptionMetricsRequest(BaseModel):
    """Request a collection of metrics, to include WebRTC."""

    data: MetricsRequestData

    type: Literal["metrics_request"] = "metrics_request"

    model_config = ConfigDict(protected_namespaces=())


class ModelingSessionDataData(BaseModel):
    """"""

    session: ModelingSessionData

    model_config = ConfigDict(protected_namespaces=())


class OptionModelingSessionData(BaseModel):
    """Data about the Modeling Session (application-level)."""

    data: ModelingSessionDataData

    type: Literal["modeling_session_data"] = "modeling_session_data"

    model_config = ConfigDict(protected_namespaces=())


class PongData(BaseModel):
    """"""

    model_config = ConfigDict(protected_namespaces=())


class OptionPong(BaseModel):
    """Pong response to a Ping message."""

    data: PongData

    type: Literal["pong"] = "pong"

    model_config = ConfigDict(protected_namespaces=())


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
        ],
        Field(discriminator="type"),
    ]
]
