from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

C = TypeVar("C", bound="PaymentMethodCardChecks")


@attr.s(auto_attribs=True)
class PaymentMethodCardChecks:
    """Card checks."""  # noqa: E501

    address_line1_check: Union[Unset, str] = UNSET
    address_postal_code_check: Union[Unset, str] = UNSET
    cvc_check: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address_line1_check = self.address_line1_check
        address_postal_code_check = self.address_postal_code_check
        cvc_check = self.cvc_check

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_line1_check is not UNSET:
            field_dict["address_line1_check"] = address_line1_check
        if address_postal_code_check is not UNSET:
            field_dict["address_postal_code_check"] = address_postal_code_check
        if cvc_check is not UNSET:
            field_dict["cvc_check"] = cvc_check

        return field_dict

    @classmethod
    def from_dict(cls: Type[C], src_dict: Dict[str, Any]) -> C:
        d = src_dict.copy()
        address_line1_check = d.pop("address_line1_check", UNSET)

        address_postal_code_check = d.pop("address_postal_code_check", UNSET)

        cvc_check = d.pop("cvc_check", UNSET)

        payment_method_card_checks = cls(
            address_line1_check=address_line1_check,
            address_postal_code_check=address_postal_code_check,
            cvc_check=cvc_check,
        )

        payment_method_card_checks.additional_properties = d
        return payment_method_card_checks

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
