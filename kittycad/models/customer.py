import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.currency import Currency
from ..models.new_address import NewAddress
from ..types import UNSET, Unset

M = TypeVar("M", bound="Customer")


@attr.s(auto_attribs=True)
class Customer:
    """The resource representing a payment "Customer"."""  # noqa: E501

    address: Union[Unset, NewAddress] = UNSET
    balance: Union[Unset, float] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    currency: Union[Unset, Currency] = UNSET
    delinquent: Union[Unset, bool] = False
    email: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    metadata: Union[Unset, Any] = UNSET
    name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.address, Unset):
            address = self.address
        balance = self.balance
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()
        if not isinstance(self.currency, Unset):
            currency = self.currency
        delinquent = self.delinquent
        email = self.email
        id = self.id
        metadata = self.metadata
        name = self.name
        phone = self.phone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if balance is not UNSET:
            field_dict["balance"] = balance
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if currency is not UNSET:
            field_dict["currency"] = currency
        if delinquent is not UNSET:
            field_dict["delinquent"] = delinquent
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: Type[M], src_dict: Dict[str, Any]) -> M:
        d = src_dict.copy()
        _address = d.pop("address", UNSET)
        address: Union[Unset, NewAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = NewAddress(_address)

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

        phone = d.pop("phone", UNSET)

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
