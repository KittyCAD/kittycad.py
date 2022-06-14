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
