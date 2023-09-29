from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.axis import Axis
from ..models.direction import Direction
from ..types import UNSET, Unset

AH = TypeVar("AH", bound="AxisDirectionPair")

@attr.s(auto_attribs=True)
class AxisDirectionPair:
	""" An [`Axis`] paired with a [`Direction`]. """ # noqa: E501
	axis: Union[Unset, Axis] = UNSET
	direction: Union[Unset, Direction] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.axis, Unset):
			axis = self.axis
		if not isinstance(self.direction, Unset):
			direction = self.direction

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if axis is not UNSET:
			field_dict['axis'] = axis
		if direction is not UNSET:
			field_dict['direction'] = direction

		return field_dict

	@classmethod
	def from_dict(cls: Type[AH], src_dict: Dict[str, Any]) -> AH:
		d = src_dict.copy()
		_axis = d.pop("axis", UNSET)
		axis: Union[Unset, Axis]
		if isinstance(_axis, Unset):
			axis = UNSET
		else:
			axis = _axis # type: ignore[arg-type]

		_direction = d.pop("direction", UNSET)
		direction: Union[Unset, Direction]
		if isinstance(_direction, Unset):
			direction = UNSET
		else:
			direction = _direction # type: ignore[arg-type]


		axis_direction_pair = cls(
			axis= axis,
			direction= direction,
		)

		axis_direction_pair.additional_properties = d
		return axis_direction_pair

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
