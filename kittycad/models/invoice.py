import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.currency import Currency
from ..models.invoice_status import InvoiceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Invoice")


@attr.s(auto_attribs=True)
class Invoice:
    """ """
    amount_due: Union[Unset, int] = UNSET
    amount_paid: Union[Unset, int] = UNSET
    amount_remaining: Union[Unset, int] = UNSET
    attempt_count: Union[Unset, int] = UNSET
    attempted: Union[Unset, bool] = False
    created_at: Union[Unset, datetime.datetime] = UNSET
    currency: Union[Unset, Currency] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    invoice_pdf: Union[Unset, str] = UNSET
    invoice_url: Union[Unset, str] = UNSET
    from ..models.invoice_line_item import InvoiceLineItem
    lines: Union[Unset, List[InvoiceLineItem]] = UNSET
    metadata: Union[Unset, Any] = UNSET
    number: Union[Unset, str] = UNSET
    paid: Union[Unset, bool] = False
    receipt_number: Union[Unset, str] = UNSET
    statement_descriptor: Union[Unset, str] = UNSET
    status: Union[Unset, InvoiceStatus] = UNSET
    subtotal: Union[Unset, int] = UNSET
    tax: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount_due = self.amount_due
        amount_paid = self.amount_paid
        amount_remaining = self.amount_remaining
        attempt_count = self.attempt_count
        attempted = self.attempted
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()
        currency: Union[Unset, str] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.value
        description = self.description
        id = self.id
        invoice_pdf = self.invoice_pdf
        invoice_url = self.invoice_url
        from ..models.invoice_line_item import InvoiceLineItem
        lines: Union[Unset, List[InvoiceLineItem]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = self.lines
        metadata = self.metadata
        number = self.number
        paid = self.paid
        receipt_number = self.receipt_number
        statement_descriptor = self.statement_descriptor
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value
        subtotal = self.subtotal
        tax = self.tax
        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_due is not UNSET:
            field_dict['amount_due'] = amount_due
        if amount_paid is not UNSET:
            field_dict['amount_paid'] = amount_paid
        if amount_remaining is not UNSET:
            field_dict['amount_remaining'] = amount_remaining
        if attempt_count is not UNSET:
            field_dict['attempt_count'] = attempt_count
        if attempted is not UNSET:
            field_dict['attempted'] = attempted
        if created_at is not UNSET:
            field_dict['created_at'] = created_at
        if currency is not UNSET:
            field_dict['currency'] = currency
        if description is not UNSET:
            field_dict['description'] = description
        if id is not UNSET:
            field_dict['id'] = id
        if invoice_pdf is not UNSET:
            field_dict['invoice_pdf'] = invoice_pdf
        if invoice_url is not UNSET:
            field_dict['invoice_url'] = invoice_url
        if lines is not UNSET:
            field_dict['lines'] = lines
        if metadata is not UNSET:
            field_dict['metadata'] = metadata
        if number is not UNSET:
            field_dict['number'] = number
        if paid is not UNSET:
            field_dict['paid'] = paid
        if receipt_number is not UNSET:
            field_dict['receipt_number'] = receipt_number
        if statement_descriptor is not UNSET:
            field_dict['statement_descriptor'] = statement_descriptor
        if status is not UNSET:
            field_dict['status'] = status
        if subtotal is not UNSET:
            field_dict['subtotal'] = subtotal
        if tax is not UNSET:
            field_dict['tax'] = tax
        if total is not UNSET:
            field_dict['total'] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount_due = d.pop("amount_due", UNSET)

        amount_paid = d.pop("amount_paid", UNSET)

        amount_remaining = d.pop("amount_remaining", UNSET)

        attempt_count = d.pop("attempt_count", UNSET)

        attempted = d.pop("attempted", UNSET)

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

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        invoice_pdf = d.pop("invoice_pdf", UNSET)

        invoice_url = d.pop("invoice_url", UNSET)

        from ..models.invoice_line_item import InvoiceLineItem
        lines = cast(List[InvoiceLineItem], d.pop("lines", UNSET))

        metadata = d.pop("metadata", UNSET)
        number = d.pop("number", UNSET)

        paid = d.pop("paid", UNSET)

        receipt_number = d.pop("receipt_number", UNSET)

        statement_descriptor = d.pop("statement_descriptor", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, InvoiceStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = InvoiceStatus(_status)

        subtotal = d.pop("subtotal", UNSET)

        tax = d.pop("tax", UNSET)

        total = d.pop("total", UNSET)

        invoice = cls(
            amount_due=amount_due,
            amount_paid=amount_paid,
            amount_remaining=amount_remaining,
            attempt_count=attempt_count,
            attempted=attempted,
            created_at=created_at,
            currency=currency,
            description=description,
            id=id,
            invoice_pdf=invoice_pdf,
            invoice_url=invoice_url,
            lines=lines,
            metadata=metadata,
            number=number,
            paid=paid,
            receipt_number=receipt_number,
            statement_descriptor=statement_descriptor,
            status=status,
            subtotal=subtotal,
            tax=tax,
            total=total,
        )

        invoice.additional_properties = d
        return invoice

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
