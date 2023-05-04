from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.new_address import NewAddress
from ..types import UNSET, Unset

X = TypeVar("X", bound="BillingInfo")


@attr.s(auto_attribs=True)
class BillingInfo:
    """The billing information for payments."""  # noqa: E501

    address: Union[Unset, NewAddress] = UNSET
    name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.address, Unset):
            address = self.address
        name = self.name
        phone = self.phone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: Type[X], src_dict: Dict[str, Any]) -> X:
        d = src_dict.copy()
        _address = d.pop("address", UNSET)
        address: Union[Unset, NewAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = NewAddress(_address)

        name = d.pop("name", UNSET)

        phone = d.pop("phone", UNSET)

        billing_info = cls(
            address=address,
            name=name,
            phone=phone,
        )

        billing_info.additional_properties = d
        return billing_info

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
