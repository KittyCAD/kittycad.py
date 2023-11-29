from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from pydantic import BaseModel, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema

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


GY = TypeVar("GY", bound="OkWebSocketResponseData")


@attr.s(auto_attribs=True)
class OkWebSocketResponseData:

    """The websocket messages this server sends."""

    type: Union[
        ice_server_info,
        trickle_ice,
        sdp_answer,
        modeling,
        export,
        metrics_request,
    ]

    def __init__(
        self,
        type: Union[
            ice_server_info,
            trickle_ice,
            sdp_answer,
            modeling,
            export,
            metrics_request,
        ],
    ):
        self.type = type

    def model_dump(self) -> Dict[str, Any]:
        if isinstance(self.type, ice_server_info):
            VY: ice_server_info = self.type
            return VY.model_dump()
        elif isinstance(self.type, trickle_ice):
            MC: trickle_ice = self.type
            return MC.model_dump()
        elif isinstance(self.type, sdp_answer):
            BR: sdp_answer = self.type
            return BR.model_dump()
        elif isinstance(self.type, modeling):
            OK: modeling = self.type
            return OK.model_dump()
        elif isinstance(self.type, export):
            OP: export = self.type
            return OP.model_dump()
        elif isinstance(self.type, metrics_request):
            LV: metrics_request = self.type
            return LV.model_dump()

        raise Exception("Unknown type")

    @classmethod
    def from_dict(cls: Type[GY], d: Dict[str, Any]) -> GY:
        if d.get("type") == "ice_server_info":
            DW: ice_server_info = ice_server_info(**d)
            return cls(type=DW)
        elif d.get("type") == "trickle_ice":
            AV: trickle_ice = trickle_ice(**d)
            return cls(type=AV)
        elif d.get("type") == "sdp_answer":
            WM: sdp_answer = sdp_answer(**d)
            return cls(type=WM)
        elif d.get("type") == "modeling":
            MU: modeling = modeling(**d)
            return cls(type=MU)
        elif d.get("type") == "export":
            WW: export = export(**d)
            return cls(type=WW)
        elif d.get("type") == "metrics_request":
            II: metrics_request = metrics_request(**d)
            return cls(type=II)

        raise Exception("Unknown type")

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls,
            handler(
                Union[
                    ice_server_info,
                    trickle_ice,
                    sdp_answer,
                    modeling,
                    export,
                    metrics_request,
                ]
            ),
        )
