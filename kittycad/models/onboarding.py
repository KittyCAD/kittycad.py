from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

P = TypeVar("P", bound="Onboarding")


@attr.s(auto_attribs=True)
class Onboarding:
    """Onboarding details"""  # noqa: E501

    first_call_from__their_machine_date: Union[Unset, str] = UNSET
    first_litterbox_execute_date: Union[Unset, str] = UNSET
    first_token_date: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_call_from__their_machine_date = self.first_call_from__their_machine_date
        first_litterbox_execute_date = self.first_litterbox_execute_date
        first_token_date = self.first_token_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_call_from__their_machine_date is not UNSET:
            field_dict[
                "first_call_from_their_machine_date"
            ] = first_call_from__their_machine_date
        if first_litterbox_execute_date is not UNSET:
            field_dict["first_litterbox_execute_date"] = first_litterbox_execute_date
        if first_token_date is not UNSET:
            field_dict["first_token_date"] = first_token_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[P], src_dict: Dict[str, Any]) -> P:
        d = src_dict.copy()
        first_call_from__their_machine_date = d.pop(
            "first_call_from_their_machine_date", UNSET
        )

        first_litterbox_execute_date = d.pop("first_litterbox_execute_date", UNSET)

        first_token_date = d.pop("first_token_date", UNSET)

        onboarding = cls(
            first_call_from__their_machine_date=first_call_from__their_machine_date,
            first_litterbox_execute_date=first_litterbox_execute_date,
            first_token_date=first_token_date,
        )

        onboarding.additional_properties = d
        return onboarding

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
