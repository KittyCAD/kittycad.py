from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.axis_direction_pair import AxisDirectionPair
from ..types import UNSET, Unset

FW = TypeVar("FW", bound="System")


@attr.s(auto_attribs=True)
class System:
    """Co-ordinate system definition.

    The `up` axis must be orthogonal to the `forward` axis.

    See [cglearn.eu] for background reading.

    [cglearn.eu](https://cglearn.eu/pub/computer-graphics/introduction-to-geometry#material-coordinate-systems-1)
    """  # noqa: E501

    forward: Union[Unset, AxisDirectionPair] = UNSET
    up: Union[Unset, AxisDirectionPair] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        forward: Union[Unset, AxisDirectionPair] = UNSET
        if not isinstance(self.forward, Unset):
            forward = self.forward
        up: Union[Unset, AxisDirectionPair] = UNSET
        if not isinstance(self.up, Unset):
            up = self.up

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if forward is not UNSET:
            _forward: AxisDirectionPair = cast(AxisDirectionPair, forward)
            field_dict["forward"] = _forward.to_dict()
        if up is not UNSET:
            _up: AxisDirectionPair = cast(AxisDirectionPair, up)
            field_dict["up"] = _up.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[FW], src_dict: Dict[str, Any]) -> FW:
        d = src_dict.copy()
        _forward = d.pop("forward", UNSET)
        forward: Union[Unset, AxisDirectionPair]
        if isinstance(_forward, Unset):
            forward = UNSET
        if _forward is None:
            forward = UNSET
        else:
            forward = AxisDirectionPair.from_dict(_forward)

        _up = d.pop("up", UNSET)
        up: Union[Unset, AxisDirectionPair]
        if isinstance(_up, Unset):
            up = UNSET
        if _up is None:
            up = UNSET
        else:
            up = AxisDirectionPair.from_dict(_up)

        system = cls(
            forward=forward,
            up=up,
        )

        system.additional_properties = d
        return system

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
