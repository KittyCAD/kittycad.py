from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

FS = TypeVar("FS", bound="PathGetCurveUuidsForVertices")

@attr.s(auto_attribs=True)
class PathGetCurveUuidsForVertices:
	""" The response from the `PathGetCurveUuidsForVertices` command. """ # noqa: E501
	curve_ids: Union[Unset, List[str]] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		curve_ids: Union[Unset, List[str]] = UNSET
		if not isinstance(self.curve_ids, Unset):
			curve_ids = self.curve_ids

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if curve_ids is not UNSET:
			field_dict['curve_ids'] = curve_ids

		return field_dict

	@classmethod
	def from_dict(cls: Type[FS], src_dict: Dict[str, Any]) -> FS:
		d = src_dict.copy()
		curve_ids = cast(List[str], d.pop("curve_ids", UNSET))


		path_get_curve_uuids_for_vertices = cls(
			curve_ids= curve_ids,
		)

		path_get_curve_uuids_for_vertices.additional_properties = d
		return path_get_curve_uuids_for_vertices

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
