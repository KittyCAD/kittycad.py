from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.curve_type import CurveType
from ..types import UNSET, Unset

PJ = TypeVar("PJ", bound="CurveGetType")

@attr.s(auto_attribs=True)
class CurveGetType:
	""" The response from the `CurveGetType` command. """ # noqa: E501
	curve_type: Union[Unset, CurveType] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.curve_type, Unset):
			curve_type = self.curve_type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if curve_type is not UNSET:
			field_dict['curve_type'] = curve_type

		return field_dict

	@classmethod
	def from_dict(cls: Type[PJ], src_dict: Dict[str, Any]) -> PJ:
		d = src_dict.copy()
		_curve_type = d.pop("curve_type", UNSET)
		curve_type: Union[Unset, CurveType]
		if isinstance(_curve_type, Unset):
			curve_type = UNSET
		else:
			curve_type = _curve_type # type: ignore[arg-type]


		curve_get_type = cls(
			curve_type= curve_type,
		)

		curve_get_type.additional_properties = d
		return curve_get_type

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
