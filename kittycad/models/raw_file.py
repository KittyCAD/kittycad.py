from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

UY = TypeVar("UY", bound="RawFile")

@attr.s(auto_attribs=True)
class RawFile:
	""" A raw file with unencoded contents to be passed over binary websockets. """ # noqa: E501
	contents: Union[Unset, List[int]] = UNSET
	name: Union[Unset, str] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		contents: Union[Unset, List[int]] = UNSET
		if not isinstance(self.contents, Unset):
			contents = self.contents
		name = self.name

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if contents is not UNSET:
			field_dict['contents'] = contents
		if name is not UNSET:
			field_dict['name'] = name

		return field_dict

	@classmethod
	def from_dict(cls: Type[UY], src_dict: Dict[str, Any]) -> UY:
		d = src_dict.copy()
		contents = cast(List[int], d.pop("contents", UNSET))

		name = d.pop("name", UNSET)


		raw_file = cls(
			contents= contents,
			name= name,
		)

		raw_file.additional_properties = d
		return raw_file

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
