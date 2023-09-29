from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

US = TypeVar("US", bound="Color")

@attr.s(auto_attribs=True)
class Color:
	""" An RGBA color """ # noqa: E501
	a:  Union[Unset, float] = UNSET
	b:  Union[Unset, float] = UNSET
	g:  Union[Unset, float] = UNSET
	r:  Union[Unset, float] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		a = self.a
		b = self.b
		g = self.g
		r = self.r

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if a is not UNSET:
			field_dict['a'] = a
		if b is not UNSET:
			field_dict['b'] = b
		if g is not UNSET:
			field_dict['g'] = g
		if r is not UNSET:
			field_dict['r'] = r

		return field_dict

	@classmethod
	def from_dict(cls: Type[US], src_dict: Dict[str, Any]) -> US:
		d = src_dict.copy()
		a = d.pop("a", UNSET)

		b = d.pop("b", UNSET)

		g = d.pop("g", UNSET)

		r = d.pop("r", UNSET)


		color = cls(
			a= a,
			b= b,
			g= g,
			r= r,
		)

		color.additional_properties = d
		return color

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
