from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

OM = TypeVar("OM", bound="ImportFiles")

@attr.s(auto_attribs=True)
class ImportFiles:
	""" Data from importing the files """ # noqa: E501
	object_id: Union[Unset, str] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		object_id = self.object_id

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if object_id is not UNSET:
			field_dict['object_id'] = object_id

		return field_dict

	@classmethod
	def from_dict(cls: Type[OM], src_dict: Dict[str, Any]) -> OM:
		d = src_dict.copy()
		object_id = d.pop("object_id", UNSET)


		import_files = cls(
			object_id= object_id,
		)

		import_files.additional_properties = d
		return import_files

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
