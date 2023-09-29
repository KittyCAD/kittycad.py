from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

CF = TypeVar("CF", bound="ImportFile")

@attr.s(auto_attribs=True)
class ImportFile:
	""" File to import into the current model """ # noqa: E501
	data: Union[Unset, List[int]] = UNSET
	path: Union[Unset, str] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		data: Union[Unset, List[int]] = UNSET
		if not isinstance(self.data, Unset):
			data = self.data
		path = self.path

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if data is not UNSET:
			field_dict['data'] = data
		if path is not UNSET:
			field_dict['path'] = path

		return field_dict

	@classmethod
	def from_dict(cls: Type[CF], src_dict: Dict[str, Any]) -> CF:
		d = src_dict.copy()
		data = cast(List[int], d.pop("data", UNSET))

		path = d.pop("path", UNSET)


		import_file = cls(
			data= data,
			path= path,
		)

		import_file.additional_properties = d
		return import_file

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
