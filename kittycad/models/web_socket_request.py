from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.client_metrics import ClientMetrics
from ..models.modeling_cmd import ModelingCmd
from ..models.modeling_cmd_id import ModelingCmdId
from ..models.rtc_ice_candidate_init import RtcIceCandidateInit
from ..models.rtc_session_description import RtcSessionDescription
from ..types import UNSET, Unset

ZI = TypeVar("ZI", bound="trickle_ice")


@attr.s(auto_attribs=True)
class trickle_ice:
    """The trickle ICE candidate request."""  # noqa: E501

    candidate: Union[Unset, RtcIceCandidateInit] = UNSET
    type: str = "trickle_ice"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.candidate, Unset):
            candidate = self.candidate
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if candidate is not UNSET:
            field_dict["candidate"] = candidate.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[ZI], src_dict: Dict[str, Any]) -> ZI:
        d = src_dict.copy()
        _candidate = d.pop("candidate", UNSET)
        candidate: Union[Unset, RtcIceCandidateInit]
        if isinstance(_candidate, Unset):
            candidate = UNSET
        else:
            candidate = _candidate  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        trickle_ice = cls(
            candidate=candidate,
            type=type,
        )

        trickle_ice.additional_properties = d
        return trickle_ice

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


CZ = TypeVar("CZ", bound="sdp_offer")


@attr.s(auto_attribs=True)
class sdp_offer:
    """The SDP offer request."""  # noqa: E501

    offer: Union[Unset, RtcSessionDescription] = UNSET
    type: str = "sdp_offer"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.offer, Unset):
            offer = self.offer
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offer is not UNSET:
            field_dict["offer"] = offer.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[CZ], src_dict: Dict[str, Any]) -> CZ:
        d = src_dict.copy()
        _offer = d.pop("offer", UNSET)
        offer: Union[Unset, RtcSessionDescription]
        if isinstance(_offer, Unset):
            offer = UNSET
        else:
            offer = _offer  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        sdp_offer = cls(
            offer=offer,
            type=type,
        )

        sdp_offer.additional_properties = d
        return sdp_offer

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


OE = TypeVar("OE", bound="modeling_cmd_req")


@attr.s(auto_attribs=True)
class modeling_cmd_req:
    """The modeling command request."""  # noqa: E501

    cmd: Union[Unset, ModelingCmd] = UNSET
    cmd_id: Union[Unset, ModelingCmdId] = UNSET
    type: str = "modeling_cmd_req"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.cmd, Unset):
            cmd = self.cmd
        if not isinstance(self.cmd_id, Unset):
            cmd_id = self.cmd_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cmd is not UNSET:
            field_dict["cmd"] = cmd.to_dict()
        if cmd_id is not UNSET:
            field_dict["cmd_id"] = cmd_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[OE], src_dict: Dict[str, Any]) -> OE:
        d = src_dict.copy()
        _cmd = d.pop("cmd", UNSET)
        cmd: Union[Unset, ModelingCmd]
        if isinstance(_cmd, Unset):
            cmd = UNSET
        else:
            cmd = _cmd  # type: ignore[arg-type]

        _cmd_id = d.pop("cmd_id", UNSET)
        cmd_id: Union[Unset, ModelingCmdId]
        if isinstance(_cmd_id, Unset):
            cmd_id = UNSET
        else:
            cmd_id = _cmd_id  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        modeling_cmd_req = cls(
            cmd=cmd,
            cmd_id=cmd_id,
            type=type,
        )

        modeling_cmd_req.additional_properties = d
        return modeling_cmd_req

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


QC = TypeVar("QC", bound="modeling_cmd_batch_req")


@attr.s(auto_attribs=True)
class modeling_cmd_batch_req:
    """A sequence of modeling requests. If any request fails, following requests will not be tried."""  # noqa: E501

    from ..models.modeling_cmd_req import ModelingCmdReq

    requests: Union[Unset, List[ModelingCmdReq]] = UNSET
    type: str = "modeling_cmd_batch_req"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.modeling_cmd_req import ModelingCmdReq

        requests: Union[Unset, List[ModelingCmdReq]] = UNSET
        if not isinstance(self.requests, Unset):
            requests = self.requests
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if requests is not UNSET:
            field_dict["requests"] = requests
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[QC], src_dict: Dict[str, Any]) -> QC:
        d = src_dict.copy()
        from ..models.modeling_cmd_req import ModelingCmdReq

        requests = cast(List[ModelingCmdReq], d.pop("requests", UNSET))

        type = d.pop("type", UNSET)

        modeling_cmd_batch_req = cls(
            requests=requests,
            type=type,
        )

        modeling_cmd_batch_req.additional_properties = d
        return modeling_cmd_batch_req

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


JJ = TypeVar("JJ", bound="ping")


@attr.s(auto_attribs=True)
class ping:
    """The client-to-server Ping to ensure the WebSocket stays alive."""  # noqa: E501

    type: str = "ping"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[JJ], src_dict: Dict[str, Any]) -> JJ:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        ping = cls(
            type=type,
        )

        ping.additional_properties = d
        return ping

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


OD = TypeVar("OD", bound="metrics_response")


@attr.s(auto_attribs=True)
class metrics_response:
    """The response to a metrics collection request from the server."""  # noqa: E501

    metrics: Union[Unset, ClientMetrics] = UNSET
    type: str = "metrics_response"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metrics is not UNSET:
            field_dict["metrics"] = metrics.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[OD], src_dict: Dict[str, Any]) -> OD:
        d = src_dict.copy()
        _metrics = d.pop("metrics", UNSET)
        metrics: Union[Unset, ClientMetrics]
        if isinstance(_metrics, Unset):
            metrics = UNSET
        else:
            metrics = _metrics  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        metrics_response = cls(
            metrics=metrics,
            type=type,
        )

        metrics_response.additional_properties = d
        return metrics_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


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

    def to_dict(self) -> Dict[str, Any]:
        if isinstance(self.type, trickle_ice):
            ZY: trickle_ice = self.type
            return ZY.to_dict()
        elif isinstance(self.type, sdp_offer):
            GJ: sdp_offer = self.type
            return GJ.to_dict()
        elif isinstance(self.type, modeling_cmd_req):
            GM: modeling_cmd_req = self.type
            return GM.to_dict()
        elif isinstance(self.type, modeling_cmd_batch_req):
            ZA: modeling_cmd_batch_req = self.type
            return ZA.to_dict()
        elif isinstance(self.type, ping):
            ZW: ping = self.type
            return ZW.to_dict()
        elif isinstance(self.type, metrics_response):
            DS: metrics_response = self.type
            return DS.to_dict()

        raise Exception("Unknown type")

    @classmethod
    def from_dict(cls: Type[GY], d: Dict[str, Any]) -> GY:
        if d.get("type") == "trickle_ice":
            GW: trickle_ice = trickle_ice()
            GW.from_dict(d)
            return cls(type=GW)
        elif d.get("type") == "sdp_offer":
            QU: sdp_offer = sdp_offer()
            QU.from_dict(d)
            return cls(type=QU)
        elif d.get("type") == "modeling_cmd_req":
            XU: modeling_cmd_req = modeling_cmd_req()
            XU.from_dict(d)
            return cls(type=XU)
        elif d.get("type") == "modeling_cmd_batch_req":
            BC: modeling_cmd_batch_req = modeling_cmd_batch_req()
            BC.from_dict(d)
            return cls(type=BC)
        elif d.get("type") == "ping":
            MX: ping = ping()
            MX.from_dict(d)
            return cls(type=MX)
        elif d.get("type") == "metrics_response":
            ZQ: metrics_response = metrics_response()
            ZQ.from_dict(d)
            return cls(type=ZQ)

        raise Exception("Unknown type")
