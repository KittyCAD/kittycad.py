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
