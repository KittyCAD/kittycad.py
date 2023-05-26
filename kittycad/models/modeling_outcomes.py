from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

H = TypeVar("H", bound="ModelingOutcomes")


@attr.s(auto_attribs=True)
class ModelingOutcomes:
    """The result from a batch of modeling commands."""  # noqa: E501

    outcomes: Union[Unset, Any] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        outcomes = self.outcomes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if outcomes is not UNSET:
            field_dict["outcomes"] = outcomes

        return field_dict

    @classmethod
    def from_dict(cls: Type[H], src_dict: Dict[str, Any]) -> H:
        d = src_dict.copy()
        outcomes = d.pop("outcomes", UNSET)

        modeling_outcomes = cls(
            outcomes=outcomes,
        )

        modeling_outcomes.additional_properties = d
        return modeling_outcomes

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
