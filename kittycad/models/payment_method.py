import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.billing_info import BillingInfo
from ..models.card_details import CardDetails
from ..models.payment_method_type import PaymentMethodType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentMethod")


@attr.s(auto_attribs=True)
class PaymentMethod:
    """ """
    billing_info: Union[Unset, BillingInfo] = UNSET
    card: Union[Unset, CardDetails] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
