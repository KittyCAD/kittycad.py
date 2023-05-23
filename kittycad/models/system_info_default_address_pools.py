from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

Y = TypeVar("Y", bound="SystemInfoDefaultAddressPools")


@attr.s(auto_attribs=True)
class SystemInfoDefaultAddressPools:
    base: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        base = self.base
        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base is not UNSET:
            field_dict["base"] = base
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: Type[Y], src_dict: Dict[str, Any]) -> Y:
        d = src_dict.copy()
        base = d.pop("base", UNSET)

        size = d.pop("size", UNSET)

        system_info_default_address_pools = cls(
            base=base,
            size=size,
        )

        system_info_default_address_pools.additional_properties = d
        return system_info_default_address_pools

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
