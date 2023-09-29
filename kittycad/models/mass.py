from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.unit_mass import UnitMass
from ..types import UNSET, Unset

NY = TypeVar("NY", bound="Mass")

@attr.s(auto_attribs=True)
class Mass:
	""" The mass response. """ # noqa: E501
	mass:  Union[Unset, float] = UNSET
	output_unit: Union[Unset, UnitMass] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		mass = self.mass
		if not isinstance(self.output_unit, Unset):
			output_unit = self.output_unit

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if mass is not UNSET:
			field_dict['mass'] = mass
		if output_unit is not UNSET:
			field_dict['output_unit'] = output_unit

		return field_dict

	@classmethod
	def from_dict(cls: Type[NY], src_dict: Dict[str, Any]) -> NY:
		d = src_dict.copy()
		mass = d.pop("mass", UNSET)

		_output_unit = d.pop("output_unit", UNSET)
		output_unit: Union[Unset, UnitMass]
		if isinstance(_output_unit, Unset):
			output_unit = UNSET
		else:
			output_unit = _output_unit # type: ignore[arg-type]


		mass = cls(
			mass= mass,
			output_unit= output_unit,
		)

		mass.additional_properties = d
		return mass

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
