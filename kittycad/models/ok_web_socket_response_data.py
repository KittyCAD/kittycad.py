from typing import List, Union

from pydantic import BaseModel, RootModel

from ..models.ice_server import IceServer
from ..models.ok_modeling_cmd_response import OkModelingCmdResponse
from ..models.raw_file import RawFile
from ..models.rtc_ice_candidate_init import RtcIceCandidateInit
from ..models.rtc_session_description import RtcSessionDescription


class IceServerInfoData(BaseModel):
    """"""

    ice_servers: List[IceServer]


class ice_server_info(BaseModel):
    """Information about the ICE servers."""

    data: IceServerInfoData

    type: str = "ice_server_info"


class TrickleIceData(BaseModel):
    """"""

    candidate: RtcIceCandidateInit


class trickle_ice(BaseModel):
    """The trickle ICE candidate response."""

    data: TrickleIceData

    type: str = "trickle_ice"


class SdpAnswerData(BaseModel):
    """"""

    answer: RtcSessionDescription


class sdp_answer(BaseModel):
    """The SDP answer response."""

    data: SdpAnswerData

    type: str = "sdp_answer"


class ModelingData(BaseModel):
    """"""

    modeling_response: OkModelingCmdResponse


class modeling(BaseModel):
    """The modeling command response."""

    data: ModelingData

    type: str = "modeling"


class ExportData(BaseModel):
    """"""

    files: List[RawFile]


class export(BaseModel):
    """The exported files."""

    data: ExportData

    type: str = "export"


class MetricsRequestData(BaseModel):
    """"""


class metrics_request(BaseModel):
    """Request a collection of metrics, to include WebRTC."""

    data: MetricsRequestData

    type: str = "metrics_request"


OkWebSocketResponseData = RootModel[
    Union[
        ice_server_info,
        trickle_ice,
        sdp_answer,
        modeling,
        export,
        metrics_request,
    ]
]
