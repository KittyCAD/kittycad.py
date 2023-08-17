from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rtc_ice_candidate_type import RtcIceCandidateType
from ..models.rtc_ice_protocol import RtcIceProtocol
from ..types import UNSET, Unset

LJ = TypeVar("LJ", bound="RtcIceCandidate")


@attr.s(auto_attribs=True)
class RtcIceCandidate:
    """ICECandidate represents a ice candidate"""  # noqa: E501

    address: Union[Unset, str] = UNSET
    component: Union[Unset, int] = UNSET
    foundation: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    priority: Union[Unset, int] = UNSET
    protocol: Union[Unset, RtcIceProtocol] = UNSET
    related_address: Union[Unset, str] = UNSET
    related_port: Union[Unset, int] = UNSET
    stats_id: Union[Unset, str] = UNSET
    tcp_type: Union[Unset, str] = UNSET
    typ: Union[Unset, RtcIceCandidateType] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address
        component = self.component
        foundation = self.foundation
        port = self.port
        priority = self.priority
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol
        related_address = self.related_address
        related_port = self.related_port
        stats_id = self.stats_id
        tcp_type = self.tcp_type
        if not isinstance(self.typ, Unset):
            typ = self.typ

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if component is not UNSET:
            field_dict["component"] = component
        if foundation is not UNSET:
            field_dict["foundation"] = foundation
        if port is not UNSET:
            field_dict["port"] = port
        if priority is not UNSET:
            field_dict["priority"] = priority
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if related_address is not UNSET:
            field_dict["related_address"] = related_address
        if related_port is not UNSET:
            field_dict["related_port"] = related_port
        if stats_id is not UNSET:
            field_dict["stats_id"] = stats_id
        if tcp_type is not UNSET:
            field_dict["tcp_type"] = tcp_type
        if typ is not UNSET:
            field_dict["typ"] = typ

        return field_dict

    @classmethod
    def from_dict(cls: Type[LJ], src_dict: Dict[str, Any]) -> LJ:
        d = src_dict.copy()
        address = d.pop("address", UNSET)

        component = d.pop("component", UNSET)

        foundation = d.pop("foundation", UNSET)

        port = d.pop("port", UNSET)

        priority = d.pop("priority", UNSET)

        _protocol = d.pop("protocol", UNSET)
        protocol: Union[Unset, RtcIceProtocol]
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = _protocol  # type: ignore[arg-type]

        related_address = d.pop("related_address", UNSET)

        related_port = d.pop("related_port", UNSET)

        stats_id = d.pop("stats_id", UNSET)

        tcp_type = d.pop("tcp_type", UNSET)

        _typ = d.pop("typ", UNSET)
        typ: Union[Unset, RtcIceCandidateType]
        if isinstance(_typ, Unset):
            typ = UNSET
        else:
            typ = _typ  # type: ignore[arg-type]

        rtc_ice_candidate = cls(
            address=address,
            component=component,
            foundation=foundation,
            port=port,
            priority=priority,
            protocol=protocol,
            related_address=related_address,
            related_port=related_port,
            stats_id=stats_id,
            tcp_type=tcp_type,
            typ=typ,
        )

        rtc_ice_candidate.additional_properties = d
        return rtc_ice_candidate

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
