from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.unit_area import UnitArea
from ..types import UNSET, Unset

FA = TypeVar("FA", bound="SurfaceArea")

@attr.s(auto_attribs=True)
class SurfaceArea:
	""" The surface area response. """ # noqa: E501
	output_unit: Union[Unset, UnitArea] = UNSET
	surface_area:  Union[Unset, float] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.output_unit, Unset):
			output_unit = self.output_unit
		surface_area = self.surface_area

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if output_unit is not UNSET:
			field_dict['output_unit'] = output_unit
		if surface_area is not UNSET:
			field_dict['surface_area'] = surface_area

		return field_dict

	@classmethod
	def from_dict(cls: Type[FA], src_dict: Dict[str, Any]) -> FA:
		d = src_dict.copy()
		_output_unit = d.pop("output_unit", UNSET)
		output_unit: Union[Unset, UnitArea]
		if isinstance(_output_unit, Unset):
			output_unit = UNSET
		else:
			output_unit = _output_unit # type: ignore[arg-type]

		surface_area = d.pop("surface_area", UNSET)


		surface_area = cls(
			output_unit= output_unit,
			surface_area= surface_area,
		)

		surface_area.additional_properties = d
		return surface_area

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
