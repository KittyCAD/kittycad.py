from typing import List, Literal, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated

from ..models.ice_server import IceServer
from ..models.ok_modeling_cmd_response import OkModelingCmdResponse
from ..models.raw_file import RawFile
from ..models.rtc_ice_candidate_init import RtcIceCandidateInit
from ..models.rtc_session_description import RtcSessionDescription


class IceServerInfoData(BaseModel):
    """"""

    ice_servers: List[IceServer]

    model_config = ConfigDict(protected_namespaces=())


class ice_server_info(BaseModel):
    """Information about the ICE servers."""

    data: IceServerInfoData

    type: Literal["ice_server_info"] = "ice_server_info"

    model_config = ConfigDict(protected_namespaces=())


class TrickleIceData(BaseModel):
    """"""

    candidate: RtcIceCandidateInit

    model_config = ConfigDict(protected_namespaces=())


class trickle_ice(BaseModel):
    """The trickle ICE candidate response."""

    data: TrickleIceData

    type: Literal["trickle_ice"] = "trickle_ice"

    model_config = ConfigDict(protected_namespaces=())


class SdpAnswerData(BaseModel):
    """"""

    answer: RtcSessionDescription

    model_config = ConfigDict(protected_namespaces=())


class sdp_answer(BaseModel):
    """The SDP answer response."""

    data: SdpAnswerData

    type: Literal["sdp_answer"] = "sdp_answer"

    model_config = ConfigDict(protected_namespaces=())


class ModelingData(BaseModel):
    """"""

    modeling_response: OkModelingCmdResponse

    model_config = ConfigDict(protected_namespaces=())


class modeling(BaseModel):
    """The modeling command response."""

    data: ModelingData

    type: Literal["modeling"] = "modeling"

    model_config = ConfigDict(protected_namespaces=())


class ExportData(BaseModel):
    """"""

    files: List[RawFile]

    model_config = ConfigDict(protected_namespaces=())


class export(BaseModel):
    """The exported files."""

    data: ExportData

    type: Literal["export"] = "export"

    model_config = ConfigDict(protected_namespaces=())


class MetricsRequestData(BaseModel):
    """"""

    model_config = ConfigDict(protected_namespaces=())


class metrics_request(BaseModel):
    """Request a collection of metrics, to include WebRTC."""

    data: MetricsRequestData

    type: Literal["metrics_request"] = "metrics_request"

    model_config = ConfigDict(protected_namespaces=())


OkWebSocketResponseData = RootModel[
    Annotated[
        Union[
            ice_server_info,
            trickle_ice,
            sdp_answer,
            modeling,
            export,
            metrics_request,
        ],
        Field(discriminator="type"),
    ]
]
