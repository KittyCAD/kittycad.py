from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

DE = TypeVar("DE", bound="ice_server_info")


@attr.s(auto_attribs=True)
class ice_server_info:
    """Information about the ICE servers."""  # noqa: E501

    data: Union[Unset, Any] = UNSET
    type: str = "ice_server_info"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[DE], src_dict: Dict[str, Any]) -> DE:
        d = src_dict.copy()
        data = d.pop("data", UNSET)
        type = d.pop("type", UNSET)

        ice_server_info = cls(
            data=data,
            type=type,
        )

        ice_server_info.additional_properties = d
        return ice_server_info

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


PU = TypeVar("PU", bound="trickle_ice")


@attr.s(auto_attribs=True)
class trickle_ice:
    """The trickle ICE candidate response."""  # noqa: E501

    data: Union[Unset, Any] = UNSET
    type: str = "trickle_ice"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[PU], src_dict: Dict[str, Any]) -> PU:
        d = src_dict.copy()
        data = d.pop("data", UNSET)
        type = d.pop("type", UNSET)

        trickle_ice = cls(
            data=data,
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


AP = TypeVar("AP", bound="sdp_answer")


@attr.s(auto_attribs=True)
class sdp_answer:
    """The SDP answer response."""  # noqa: E501

    data: Union[Unset, Any] = UNSET
    type: str = "sdp_answer"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[AP], src_dict: Dict[str, Any]) -> AP:
        d = src_dict.copy()
        data = d.pop("data", UNSET)
        type = d.pop("type", UNSET)

        sdp_answer = cls(
            data=data,
            type=type,
        )

        sdp_answer.additional_properties = d
        return sdp_answer

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


AA = TypeVar("AA", bound="modeling")


@attr.s(auto_attribs=True)
class modeling:
    """The modeling command response."""  # noqa: E501

    data: Union[Unset, Any] = UNSET
    type: str = "modeling"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[AA], src_dict: Dict[str, Any]) -> AA:
        d = src_dict.copy()
        data = d.pop("data", UNSET)
        type = d.pop("type", UNSET)

        modeling = cls(
            data=data,
            type=type,
        )

        modeling.additional_properties = d
        return modeling

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


MH = TypeVar("MH", bound="export")


@attr.s(auto_attribs=True)
class export:
    """The exported files."""  # noqa: E501

    data: Union[Unset, Any] = UNSET
    type: str = "export"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[MH], src_dict: Dict[str, Any]) -> MH:
        d = src_dict.copy()
        data = d.pop("data", UNSET)
        type = d.pop("type", UNSET)

        export = cls(
            data=data,
            type=type,
        )

        export.additional_properties = d
        return export

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


OL = TypeVar("OL", bound="metrics_request")


@attr.s(auto_attribs=True)
class metrics_request:
    """Request a collection of metrics, to include WebRTC."""  # noqa: E501

    data: Union[Unset, Any] = UNSET
    type: str = "metrics_request"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[OL], src_dict: Dict[str, Any]) -> OL:
        d = src_dict.copy()
        data = d.pop("data", UNSET)
        type = d.pop("type", UNSET)

        metrics_request = cls(
            data=data,
            type=type,
        )

        metrics_request.additional_properties = d
        return metrics_request

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

    def to_dict(self) -> Dict[str, Any]:
        if isinstance(self.type, ice_server_info):
            WA: ice_server_info = self.type
            return WA.to_dict()
        elif isinstance(self.type, trickle_ice):
            EP: trickle_ice = self.type
            return EP.to_dict()
        elif isinstance(self.type, sdp_answer):
            JY: sdp_answer = self.type
            return JY.to_dict()
        elif isinstance(self.type, modeling):
            BZ: modeling = self.type
            return BZ.to_dict()
        elif isinstance(self.type, export):
            NL: export = self.type
            return NL.to_dict()
        elif isinstance(self.type, metrics_request):
            MI: metrics_request = self.type
            return MI.to_dict()

        raise Exception("Unknown type")

    @classmethod
    def from_dict(cls: Type[GY], d: Dict[str, Any]) -> GY:
        if d.get("type") == "ice_server_info":
            LA: ice_server_info = ice_server_info()
            LA.from_dict(d)
            return cls(type=LA)
        elif d.get("type") == "trickle_ice":
            CJ: trickle_ice = trickle_ice()
            CJ.from_dict(d)
            return cls(type=CJ)
        elif d.get("type") == "sdp_answer":
            FE: sdp_answer = sdp_answer()
            FE.from_dict(d)
            return cls(type=FE)
        elif d.get("type") == "modeling":
            NB: modeling = modeling()
            NB.from_dict(d)
            return cls(type=NB)
        elif d.get("type") == "export":
            TJ: export = export()
            TJ.from_dict(d)
            return cls(type=TJ)
        elif d.get("type") == "metrics_request":
            KS: metrics_request = metrics_request()
            KS.from_dict(d)
            return cls(type=KS)

        raise Exception("Unknown type")
