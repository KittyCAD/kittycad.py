from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.currency import Currency
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceLineItem")


@attr.s(auto_attribs=True)
class InvoiceLineItem:
    """ """
    amount: Union[Unset, int] = UNSET
    currency: Union[Unset, Currency] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    invoice_item: Union[Unset, str] = UNSET
