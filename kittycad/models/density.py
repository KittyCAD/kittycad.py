from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.unit_density import UnitDensity
from ..types import UNSET, Unset

CE = TypeVar("CE", bound="Density")

@attr.s(auto_attribs=True)
class Density:
	""" The density response. """ # noqa: E501
	density:  Union[Unset, float] = UNSET
	output_unit: Union[Unset, UnitDensity] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		density = self.density
		if not isinstance(self.output_unit, Unset):
			output_unit = self.output_unit

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if density is not UNSET:
			field_dict['density'] = density
		if output_unit is not UNSET:
			field_dict['output_unit'] = output_unit

		return field_dict

	@classmethod
	def from_dict(cls: Type[CE], src_dict: Dict[str, Any]) -> CE:
		d = src_dict.copy()
		density = d.pop("density", UNSET)

		_output_unit = d.pop("output_unit", UNSET)
		output_unit: Union[Unset, UnitDensity]
		if isinstance(_output_unit, Unset):
			output_unit = UNSET
		else:
			output_unit = _output_unit # type: ignore[arg-type]


		density = cls(
			density= density,
			output_unit= output_unit,
		)

		density.additional_properties = d
		return density

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
