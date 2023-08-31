from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.modeling_outcome import ModelingOutcome
from ..types import UNSET, Unset

SC = TypeVar("SC", bound="ModelingOutcomes")


@attr.s(auto_attribs=True)
class ModelingOutcomes:
    """The result from a batch of modeling commands."""  # noqa: E501

    from ..models.modeling_outcome import ModelingOutcome

    outcomes: Union[Unset, Dict[str, ModelingOutcome]] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        outcomes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.outcomes, Unset):
            new_dict: Dict[str, Any] = {}
            for key, value in self.outcomes.items():
                new_dict[key] = value.to_dict()
            outcomes = new_dict

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if outcomes is not UNSET:
            field_dict["outcomes"] = outcomes

        return field_dict

    @classmethod
    def from_dict(cls: Type[SC], src_dict: Dict[str, Any]) -> SC:
        d = src_dict.copy()
        _outcomes = d.pop("outcomes", UNSET)
        if isinstance(_outcomes, Unset):
            outcomes = UNSET
        else:
            new_map: Dict[str, ModelingOutcome] = {}
            for k, v in _outcomes.items():
                new_map[k] = ModelingOutcome.from_dict(v)  # type: ignore
            outcomes = new_map  # type: ignore

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
