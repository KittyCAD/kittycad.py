from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.unit_volume import UnitVolume
from ..types import UNSET, Unset

FC = TypeVar("FC", bound="Volume")

@attr.s(auto_attribs=True)
class Volume:
	""" The volume response. """ # noqa: E501
	output_unit: Union[Unset, UnitVolume] = UNSET
	volume:  Union[Unset, float] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.output_unit, Unset):
			output_unit = self.output_unit
		volume = self.volume

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if output_unit is not UNSET:
			field_dict['output_unit'] = output_unit
		if volume is not UNSET:
			field_dict['volume'] = volume

		return field_dict

	@classmethod
	def from_dict(cls: Type[FC], src_dict: Dict[str, Any]) -> FC:
		d = src_dict.copy()
		_output_unit = d.pop("output_unit", UNSET)
		output_unit: Union[Unset, UnitVolume]
		if isinstance(_output_unit, Unset):
			output_unit = UNSET
		else:
			output_unit = _output_unit # type: ignore[arg-type]

		volume = d.pop("volume", UNSET)


		volume = cls(
			output_unit= output_unit,
			volume= volume,
		)

		volume.additional_properties = d
		return volume

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
