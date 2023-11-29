from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from pydantic import BaseModel, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema

from ..models.client_metrics import ClientMetrics
from ..models.modeling_cmd import ModelingCmd
from ..models.modeling_cmd_id import ModelingCmdId
from ..models.modeling_cmd_req import ModelingCmdReq
from ..models.rtc_ice_candidate_init import RtcIceCandidateInit
from ..models.rtc_session_description import RtcSessionDescription


class trickle_ice(BaseModel):
    """The trickle ICE candidate request."""

    candidate: RtcIceCandidateInit

    type: str = "trickle_ice"


class sdp_offer(BaseModel):
    """The SDP offer request."""

    offer: RtcSessionDescription

    type: str = "sdp_offer"


class modeling_cmd_req(BaseModel):
    """The modeling command request."""

    cmd: ModelingCmd

    cmd_id: ModelingCmdId

    type: str = "modeling_cmd_req"


class modeling_cmd_batch_req(BaseModel):
    """A sequence of modeling requests. If any request fails, following requests will not be tried."""

    requests: List[ModelingCmdReq]

    type: str = "modeling_cmd_batch_req"


class ping(BaseModel):
    """The client-to-server Ping to ensure the WebSocket stays alive."""

    type: str = "ping"


class metrics_response(BaseModel):
    """The response to a metrics collection request from the server."""

    metrics: ClientMetrics

    type: str = "metrics_response"


GY = TypeVar("GY", bound="WebSocketRequest")


@attr.s(auto_attribs=True)
class WebSocketRequest:

    """The websocket messages the server receives."""

    type: Union[
        trickle_ice,
        sdp_offer,
        modeling_cmd_req,
        modeling_cmd_batch_req,
        ping,
        metrics_response,
    ]

    def __init__(
        self,
        type: Union[
            trickle_ice,
            sdp_offer,
            modeling_cmd_req,
            modeling_cmd_batch_req,
            ping,
            metrics_response,
        ],
    ):
        self.type = type

    def model_dump(self) -> Dict[str, Any]:
        if isinstance(self.type, trickle_ice):
            WI: trickle_ice = self.type
            return WI.model_dump()
        elif isinstance(self.type, sdp_offer):
            YR: sdp_offer = self.type
            return YR.model_dump()
        elif isinstance(self.type, modeling_cmd_req):
            XK: modeling_cmd_req = self.type
            return XK.model_dump()
        elif isinstance(self.type, modeling_cmd_batch_req):
            OB: modeling_cmd_batch_req = self.type
            return OB.model_dump()
        elif isinstance(self.type, ping):
            QQ: ping = self.type
            return QQ.model_dump()
        elif isinstance(self.type, metrics_response):
            WX: metrics_response = self.type
            return WX.model_dump()

        raise Exception("Unknown type")

    @classmethod
    def from_dict(cls: Type[GY], d: Dict[str, Any]) -> GY:
        if d.get("type") == "trickle_ice":
            QL: trickle_ice = trickle_ice(**d)
            return cls(type=QL)
        elif d.get("type") == "sdp_offer":
            ME: sdp_offer = sdp_offer(**d)
            return cls(type=ME)
        elif d.get("type") == "modeling_cmd_req":
            EB: modeling_cmd_req = modeling_cmd_req(**d)
            return cls(type=EB)
        elif d.get("type") == "modeling_cmd_batch_req":
            VK: modeling_cmd_batch_req = modeling_cmd_batch_req(**d)
            return cls(type=VK)
        elif d.get("type") == "ping":
            ZC: ping = ping(**d)
            return cls(type=ZC)
        elif d.get("type") == "metrics_response":
            BE: metrics_response = metrics_response(**d)
            return cls(type=BE)

        raise Exception("Unknown type")

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls,
            handler(
                Union[
                    trickle_ice,
                    sdp_offer,
                    modeling_cmd_req,
                    modeling_cmd_batch_req,
                    ping,
                    metrics_response,
                ]
            ),
        )
