from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.address import Address
from ..models.phone_number import PhoneNumber
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingInfo")


@attr.s(auto_attribs=True)
class BillingInfo:
    """ """
    address: Union[Unset, Address] = UNSET
    name: Union[Unset, str] = UNSET
    phone: Union[Unset, PhoneNumber] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address: Union[Unset, str] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.value
        name = self.name
        phone: Union[Unset, str] = UNSET
        if not isinstance(self.phone, Unset):
            phone = self.phone.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict['address'] = address
        if name is not UNSET:
            field_dict['name'] = name
        if phone is not UNSET:
            field_dict['phone'] = phone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _address = d.pop("address", UNSET)
        address: Union[Unset, Address]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address(_address)

        name = d.pop("name", UNSET)

        _phone = d.pop("phone", UNSET)
        phone: Union[Unset, PhoneNumber]
        if isinstance(_phone, Unset):
            phone = UNSET
        else:
            phone = PhoneNumber(_phone)

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
