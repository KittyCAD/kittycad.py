from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.modeling_cmd_id import ModelingCmdId
from ..types import UNSET, Unset

T = TypeVar("T", bound="Extrude")


@attr.s(auto_attribs=True)
class Extrude:
    """Command for extruding a solid."""  # noqa: E501

    distance: Union[Unset, float] = UNSET
    target: Union[Unset, ModelingCmdId] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        distance = self.distance
        if not isinstance(self.target, Unset):
            target = self.target

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if distance is not UNSET:
            field_dict["distance"] = distance
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        distance = d.pop("distance", UNSET)

        _target = d.pop("target", UNSET)
        target: Union[Unset, ModelingCmdId]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = ModelingCmdId(_target)

        extrude = cls(
            distance=distance,
            target=target,
        )

        extrude.additional_properties = d
        return extrude

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
