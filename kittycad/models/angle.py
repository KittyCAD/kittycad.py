from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.unit_angle import UnitAngle
from ..types import UNSET, Unset

GO = TypeVar("GO", bound="Angle")

@attr.s(auto_attribs=True)
class Angle:
	""" An angle, with a specific unit. """ # noqa: E501
	unit: Union[Unset, UnitAngle] = UNSET
	value:  Union[Unset, float] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.unit, Unset):
			unit = self.unit
		value = self.value

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if unit is not UNSET:
			field_dict['unit'] = unit
		if value is not UNSET:
			field_dict['value'] = value

		return field_dict

	@classmethod
	def from_dict(cls: Type[GO], src_dict: Dict[str, Any]) -> GO:
		d = src_dict.copy()
		_unit = d.pop("unit", UNSET)
		unit: Union[Unset, UnitAngle]
		if isinstance(_unit, Unset):
			unit = UNSET
		else:
			unit = _unit # type: ignore[arg-type]

		value = d.pop("value", UNSET)


		angle = cls(
			unit= unit,
			value= value,
		)

		angle.additional_properties = d
		return angle

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
