from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

C = TypeVar("C", bound="PluginsInfo")


@attr.s(auto_attribs=True)
class PluginsInfo:
    """Available plugins per type.

    **Note**: Only unmanaged (V1) plugins are included in this list. V1 plugins are \"lazily\" loaded, and are not returned in this list if there is no resource using the plugin."""  # noqa: E501

    authorization: Union[Unset, List[str]] = UNSET
    log: Union[Unset, List[str]] = UNSET
    network: Union[Unset, List[str]] = UNSET
    volume: Union[Unset, List[str]] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authorization: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorization, Unset):
            authorization = self.authorization
        log: Union[Unset, List[str]] = UNSET
        if not isinstance(self.log, Unset):
            log = self.log
        network: Union[Unset, List[str]] = UNSET
        if not isinstance(self.network, Unset):
            network = self.network
        volume: Union[Unset, List[str]] = UNSET
        if not isinstance(self.volume, Unset):
            volume = self.volume

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorization is not UNSET:
            field_dict["authorization"] = authorization
        if log is not UNSET:
            field_dict["log"] = log
        if network is not UNSET:
            field_dict["network"] = network
        if volume is not UNSET:
            field_dict["volume"] = volume

        return field_dict

    @classmethod
    def from_dict(cls: Type[C], src_dict: Dict[str, Any]) -> C:
        d = src_dict.copy()
        authorization = cast(List[str], d.pop("authorization", UNSET))

        log = cast(List[str], d.pop("log", UNSET))

        network = cast(List[str], d.pop("network", UNSET))

        volume = cast(List[str], d.pop("volume", UNSET))

        plugins_info = cls(
            authorization=authorization,
            log=log,
            network=network,
            volume=volume,
        )

        plugins_info.additional_properties = d
        return plugins_info

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
