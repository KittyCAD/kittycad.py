import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.billing_info import BillingInfo
from ..models.card_details import CardDetails
from ..models.payment_method_type import PaymentMethodType
from ..types import UNSET, Unset

CT = TypeVar("CT", bound="PaymentMethod")


@attr.s(auto_attribs=True)
class PaymentMethod:
    """A payment method."""  # noqa: E501

    billing_info: Union[Unset, BillingInfo] = UNSET
    card: Union[Unset, CardDetails] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    metadata: Union[Unset, Dict[str, str]] = UNSET
    type: Union[Unset, PaymentMethodType] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        billing_info: Union[Unset, BillingInfo] = UNSET
        if not isinstance(self.billing_info, Unset):
            billing_info = self.billing_info
        card: Union[Unset, CardDetails] = UNSET
        if not isinstance(self.card, Unset):
            card = self.card
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()
        id = self.id
        metadata = self.metadata

        type: Union[Unset, PaymentMethodType] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_info is not UNSET:
            _billing_info: BillingInfo = cast(BillingInfo, billing_info)
            field_dict["billing_info"] = _billing_info.to_dict()
        if card is not UNSET:
            _card: CardDetails = cast(CardDetails, card)
            field_dict["card"] = _card.to_dict()
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[CT], src_dict: Dict[str, Any]) -> CT:
        d = src_dict.copy()
        _billing_info = d.pop("billing_info", UNSET)
        billing_info: Union[Unset, BillingInfo]
        if isinstance(_billing_info, Unset):
            billing_info = UNSET
        if _billing_info is None:
            billing_info = UNSET
        else:
            billing_info = BillingInfo.from_dict(_billing_info)

        _card = d.pop("card", UNSET)
        card: Union[Unset, CardDetails]
        if isinstance(_card, Unset):
            card = UNSET
        if _card is None:
            card = UNSET
        else:
            card = CardDetails.from_dict(_card)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        id = d.pop("id", UNSET)

        metadata = d.pop("metadata", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, PaymentMethodType]
        if isinstance(_type, Unset):
            type = UNSET
        if _type is None:
            type = UNSET
        else:
            type = _type

        payment_method = cls(
            billing_info=billing_info,
            card=card,
            created_at=created_at,
            id=id,
            metadata=metadata,
            type=type,
        )

        payment_method.additional_properties = d
        return payment_method

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
