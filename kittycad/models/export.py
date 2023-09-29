from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

ET = TypeVar("ET", bound="Export")

@attr.s(auto_attribs=True)
class Export:
	""" The response from the `Export` endpoint. """ # noqa: E501
	from ..models.export_file import ExportFile
	files: Union[Unset, List[ExportFile]] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		from ..models.export_file import ExportFile
		files: Union[Unset, List[ExportFile]] = UNSET
		if not isinstance(self.files, Unset):
			files = self.files

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if files is not UNSET:
			field_dict['files'] = files

		return field_dict

	@classmethod
	def from_dict(cls: Type[ET], src_dict: Dict[str, Any]) -> ET:
		d = src_dict.copy()
		from ..models.export_file import ExportFile
		files = cast(List[ExportFile], d.pop("files", UNSET))


		export = cls(
			files= files,
		)

		export.additional_properties = d
		return export

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
