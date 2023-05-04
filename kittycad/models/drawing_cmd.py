from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.drawing_cmd_id import DrawingCmdId
from ..types import UNSET, Unset

J = TypeVar("J", bound="DrawCircle")


@attr.s(auto_attribs=True)
class DrawCircle:
    center: Union[Unset, List[float]] = UNSET
    radius: Union[Unset, float] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        center: Union[Unset, List[float]] = UNSET
        if not isinstance(self.center, Unset):
            center = self.center
        radius = self.radius

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if center is not UNSET:
            field_dict["center"] = center
        if radius is not UNSET:
            field_dict["radius"] = radius

        return field_dict

    @classmethod
    def from_dict(cls: Type[J], src_dict: Dict[str, Any]) -> J:
        d = src_dict.copy()
        center = cast(List[float], d.pop("center", UNSET))

        radius = d.pop("radius", UNSET)

        draw_circle = cls(
            center=center,
            radius=radius,
        )

        draw_circle.additional_properties = d
        return draw_circle

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


V = TypeVar("V", bound="Extrude")


@attr.s(auto_attribs=True)
class Extrude:
    distance: Union[Unset, float] = UNSET
    sketch: Union[Unset, DrawingCmdId] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        distance = self.distance
        if not isinstance(self.sketch, Unset):
            sketch = self.sketch

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if distance is not UNSET:
            field_dict["distance"] = distance
        if sketch is not UNSET:
            field_dict["sketch"] = sketch

        return field_dict

    @classmethod
    def from_dict(cls: Type[V], src_dict: Dict[str, Any]) -> V:
        d = src_dict.copy()
        distance = d.pop("distance", UNSET)

        _sketch = d.pop("sketch", UNSET)
        sketch: Union[Unset, DrawingCmdId]
        if isinstance(_sketch, Unset):
            sketch = UNSET
        else:
            sketch = DrawingCmdId(_sketch)

        extrude = cls(
            distance=distance,
            sketch=sketch,
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


DrawingCmd = Union[DrawCircle, Extrude]
