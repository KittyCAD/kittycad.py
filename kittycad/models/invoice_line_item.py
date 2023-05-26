from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.currency import Currency
from ..types import UNSET, Unset

Y = TypeVar("Y", bound="InvoiceLineItem")


@attr.s(auto_attribs=True)
class InvoiceLineItem:
    """An invoice line item."""  # noqa: E501

    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, Currency] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    invoice_item: Union[Unset, str] = UNSET
    metadata: Union[Unset, Any] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        if not isinstance(self.currency, Unset):
            currency = self.currency
        description = self.description
        id = self.id
        invoice_item = self.invoice_item
        metadata = self.metadata

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if invoice_item is not UNSET:
            field_dict["invoice_item"] = invoice_item
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[Y], src_dict: Dict[str, Any]) -> Y:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, Currency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = Currency(_currency)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        invoice_item = d.pop("invoice_item", UNSET)

        metadata = d.pop("metadata", UNSET)

        invoice_line_item = cls(
            amount=amount,
            currency=currency,
            description=description,
            id=id,
            invoice_item=invoice_item,
            metadata=metadata,
        )

        invoice_line_item.additional_properties = d
        return invoice_line_item

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
