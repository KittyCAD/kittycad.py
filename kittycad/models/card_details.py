from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.payment_method_card_checks import PaymentMethodCardChecks
from ..types import UNSET, Unset

B = TypeVar("B", bound="CardDetails")


@attr.s(auto_attribs=True)
class CardDetails:
    """The card details of a payment method."""  # noqa: E501

    brand: Union[Unset, str] = UNSET
    checks: Union[Unset, PaymentMethodCardChecks] = UNSET
    country: Union[Unset, str] = UNSET
    exp_month: Union[Unset, int] = UNSET
    exp_year: Union[Unset, int] = UNSET
    fingerprint: Union[Unset, str] = UNSET
    funding: Union[Unset, str] = UNSET
    last4: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        brand = self.brand
        if not isinstance(self.checks, Unset):
            checks = self.checks
        country = self.country
        exp_month = self.exp_month
        exp_year = self.exp_year
        fingerprint = self.fingerprint
        funding = self.funding
        last4 = self.last4

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if brand is not UNSET:
            field_dict["brand"] = brand
        if checks is not UNSET:
            field_dict["checks"] = checks
        if country is not UNSET:
            field_dict["country"] = country
        if exp_month is not UNSET:
            field_dict["exp_month"] = exp_month
        if exp_year is not UNSET:
            field_dict["exp_year"] = exp_year
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if funding is not UNSET:
            field_dict["funding"] = funding
        if last4 is not UNSET:
            field_dict["last4"] = last4

        return field_dict

    @classmethod
    def from_dict(cls: Type[B], src_dict: Dict[str, Any]) -> B:
        d = src_dict.copy()
        brand = d.pop("brand", UNSET)

        _checks = d.pop("checks", UNSET)
        checks: Union[Unset, PaymentMethodCardChecks]
        if isinstance(_checks, Unset):
            checks = UNSET
        else:
            checks = PaymentMethodCardChecks(_checks)

        country = d.pop("country", UNSET)

        exp_month = d.pop("exp_month", UNSET)

        exp_year = d.pop("exp_year", UNSET)

        fingerprint = d.pop("fingerprint", UNSET)

        funding = d.pop("funding", UNSET)

        last4 = d.pop("last4", UNSET)

        card_details = cls(
            brand=brand,
            checks=checks,
            country=country,
            exp_month=exp_month,
            exp_year=exp_year,
            fingerprint=fingerprint,
            funding=funding,
            last4=last4,
        )

        card_details.additional_properties = d
        return card_details

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
