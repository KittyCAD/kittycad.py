from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.point3d import Point3d
from ..models.unit_length import UnitLength
from ..types import UNSET, Unset

HK = TypeVar("HK", bound="CenterOfMass")

@attr.s(auto_attribs=True)
class CenterOfMass:
	""" The center of mass response. """ # noqa: E501
	center_of_mass: Union[Unset, Point3d] = UNSET
	output_unit: Union[Unset, UnitLength] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.center_of_mass, Unset):
			center_of_mass = self.center_of_mass
		if not isinstance(self.output_unit, Unset):
			output_unit = self.output_unit

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if center_of_mass is not UNSET:
			field_dict['center_of_mass'] = center_of_mass
		if output_unit is not UNSET:
			field_dict['output_unit'] = output_unit

		return field_dict

	@classmethod
	def from_dict(cls: Type[HK], src_dict: Dict[str, Any]) -> HK:
		d = src_dict.copy()
		_center_of_mass = d.pop("center_of_mass", UNSET)
		center_of_mass: Union[Unset, Point3d]
		if isinstance(_center_of_mass, Unset):
			center_of_mass = UNSET
		else:
			center_of_mass = _center_of_mass # type: ignore[arg-type]

		_output_unit = d.pop("output_unit", UNSET)
		output_unit: Union[Unset, UnitLength]
		if isinstance(_output_unit, Unset):
			output_unit = UNSET
		else:
			output_unit = _output_unit # type: ignore[arg-type]


		center_of_mass = cls(
			center_of_mass= center_of_mass,
			output_unit= output_unit,
		)

		center_of_mass.additional_properties = d
		return center_of_mass

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
