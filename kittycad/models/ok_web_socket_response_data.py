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


class OptionIceServerInfoData(BaseModel):
    """"""

    ice_servers: List[IceServer]

    model_config = ConfigDict(protected_namespaces=())


class OptionIceServerInfo(BaseModel):
    """Information about the ICE servers."""

    data: OptionIceServerInfoData

    type: Literal["option_ice_server_info"] = "option_ice_server_info"

    model_config = ConfigDict(protected_namespaces=())


class OptionTrickleIceData(BaseModel):
    """"""

    candidate: RtcIceCandidateInit

    model_config = ConfigDict(protected_namespaces=())


class OptionTrickleIce(BaseModel):
    """The trickle ICE candidate response."""

    data: OptionTrickleIceData

    type: Literal["option_trickle_ice"] = "option_trickle_ice"

    model_config = ConfigDict(protected_namespaces=())


class OptionSdpAnswerData(BaseModel):
    """"""

    answer: RtcSessionDescription

    model_config = ConfigDict(protected_namespaces=())


class OptionSdpAnswer(BaseModel):
    """The SDP answer response."""

    data: OptionSdpAnswerData

    type: Literal["option_sdp_answer"] = "option_sdp_answer"

    model_config = ConfigDict(protected_namespaces=())


class OptionModelingData(BaseModel):
    """"""

    modeling_response: OkModelingCmdResponse

    model_config = ConfigDict(protected_namespaces=())


class OptionModeling(BaseModel):
    """The modeling command response."""

    data: OptionModelingData

    type: Literal["option_modeling"] = "option_modeling"

    model_config = ConfigDict(protected_namespaces=())


class OptionModelingBatchData(BaseModel):
    """"""

    responses: Dict[str, BatchResponse]

    model_config = ConfigDict(protected_namespaces=())


class OptionModelingBatch(BaseModel):
    """Response to a ModelingBatch."""

    data: OptionModelingBatchData

    type: Literal["option_modeling_batch"] = "option_modeling_batch"

    model_config = ConfigDict(protected_namespaces=())


class OptionExportData(BaseModel):
    """"""

    files: List[RawFile]

    model_config = ConfigDict(protected_namespaces=())


class OptionExport(BaseModel):
    """The exported files."""

    data: OptionExportData

    type: Literal["option_export"] = "option_export"

    model_config = ConfigDict(protected_namespaces=())


class OptionMetricsRequestData(BaseModel):
    """"""

    model_config = ConfigDict(protected_namespaces=())


class OptionMetricsRequest(BaseModel):
    """Request a collection of metrics, to include WebRTC."""

    data: OptionMetricsRequestData

    type: Literal["option_metrics_request"] = "option_metrics_request"

    model_config = ConfigDict(protected_namespaces=())


class OptionModelingSessionDataData(BaseModel):
    """"""

    session: ModelingSessionData

    model_config = ConfigDict(protected_namespaces=())


class OptionModelingSessionData(BaseModel):
    """Data about the Modeling Session (application-level)."""

    data: OptionModelingSessionDataData

    type: Literal["option_modeling_session_data"] = "option_modeling_session_data"

    model_config = ConfigDict(protected_namespaces=())


class OptionPongData(BaseModel):
    """"""

    model_config = ConfigDict(protected_namespaces=())


class OptionPong(BaseModel):
    """Pong response to a Ping message."""

    data: OptionPongData

    type: Literal["option_pong"] = "option_pong"

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
