import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.address import Address
from ..models.currency import Currency
from ..models.phone_number import PhoneNumber
from ..types import UNSET, Unset

T = TypeVar("T", bound="Customer")


@attr.s(auto_attribs=True)
class Customer:
    """ """
    address: Union[Unset, Address] = UNSET
    balance: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    currency: Union[Unset, Currency] = UNSET
    delinquent: Union[Unset, bool] = False
    email: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    metadata: Union[Unset, Any] = UNSET
    name: Union[Unset, str] = UNSET
    phone: Union[Unset, PhoneNumber] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address: Union[Unset, str] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.value
        balance = self.balance
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()
        currency: Union[Unset, str] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.value
        delinquent = self.delinquent
        email = self.email
        id = self.id
        metadata = self.metadata
        name = self.name
        phone: Union[Unset, str] = UNSET
        if not isinstance(self.phone, Unset):
            phone = self.phone.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict['address'] = address
        if balance is not UNSET:
            field_dict['balance'] = balance
        if created_at is not UNSET:
            field_dict['created_at'] = created_at
        if currency is not UNSET:
            field_dict['currency'] = currency
        if delinquent is not UNSET:
            field_dict['delinquent'] = delinquent
        if email is not UNSET:
            field_dict['email'] = email
        if id is not UNSET:
            field_dict['id'] = id
        if metadata is not UNSET:
            field_dict['metadata'] = metadata
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

        balance = d.pop("balance", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, Currency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = Currency(_currency)

        delinquent = d.pop("delinquent", UNSET)

        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        metadata = d.pop("metadata", UNSET)
        name = d.pop("name", UNSET)

        _phone = d.pop("phone", UNSET)
        phone: Union[Unset, PhoneNumber]
        if isinstance(_phone, Unset):
            phone = UNSET
        else:
            phone = PhoneNumber(_phone)

        customer = cls(
            address=address,
            balance=balance,
            created_at=created_at,
            currency=currency,
            delinquent=delinquent,
            email=email,
            id=id,
            metadata=metadata,
            name=name,
            phone=phone,
        )

        customer.additional_properties = d
        return customer

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
