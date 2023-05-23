import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.uuid import Uuid
from ..types import UNSET, Unset

N = TypeVar("N", bound="CustomerBalance")


@attr.s(auto_attribs=True)
class CustomerBalance:
    """A balance for a user.

    This holds information about the financial balance for the user."""  # noqa: E501

    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    monthly_credits_remaining: Union[Unset, float] = UNSET
    pre_pay_cash_remaining: Union[Unset, float] = UNSET
    pre_pay_credits_remaining: Union[Unset, float] = UNSET
    total_due: Union[Unset, float] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user_id: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()
        id = self.id
        monthly_credits_remaining = self.monthly_credits_remaining
        pre_pay_cash_remaining = self.pre_pay_cash_remaining
        pre_pay_credits_remaining = self.pre_pay_credits_remaining
        total_due = self.total_due
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if monthly_credits_remaining is not UNSET:
            field_dict["monthly_credits_remaining"] = monthly_credits_remaining
        if pre_pay_cash_remaining is not UNSET:
            field_dict["pre_pay_cash_remaining"] = pre_pay_cash_remaining
        if pre_pay_credits_remaining is not UNSET:
            field_dict["pre_pay_credits_remaining"] = pre_pay_credits_remaining
        if total_due is not UNSET:
            field_dict["total_due"] = total_due
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[N], src_dict: Dict[str, Any]) -> N:
        d = src_dict.copy()
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _id = d.pop("id", UNSET)
        id: Union[Unset, Uuid]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = Uuid(_id)

        monthly_credits_remaining = d.pop("monthly_credits_remaining", UNSET)

        pre_pay_cash_remaining = d.pop("pre_pay_cash_remaining", UNSET)

        pre_pay_credits_remaining = d.pop("pre_pay_credits_remaining", UNSET)

        total_due = d.pop("total_due", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user_id = d.pop("user_id", UNSET)

        customer_balance = cls(
            created_at=created_at,
            id=id,
            monthly_credits_remaining=monthly_credits_remaining,
            pre_pay_cash_remaining=pre_pay_cash_remaining,
            pre_pay_credits_remaining=pre_pay_credits_remaining,
            total_due=total_due,
            updated_at=updated_at,
            user_id=user_id,
        )

        customer_balance.additional_properties = d
        return customer_balance

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
