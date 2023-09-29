from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

WN = TypeVar("WN", bound="PathGetInfo")

@attr.s(auto_attribs=True)
class PathGetInfo:
	""" The response from the `PathGetInfo` command. """ # noqa: E501
	from ..models.path_segment_info import PathSegmentInfo
	segments: Union[Unset, List[PathSegmentInfo]] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		from ..models.path_segment_info import PathSegmentInfo
		segments: Union[Unset, List[PathSegmentInfo]] = UNSET
		if not isinstance(self.segments, Unset):
			segments = self.segments

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if segments is not UNSET:
			field_dict['segments'] = segments

		return field_dict

	@classmethod
	def from_dict(cls: Type[WN], src_dict: Dict[str, Any]) -> WN:
		d = src_dict.copy()
		from ..models.path_segment_info import PathSegmentInfo
		segments = cast(List[PathSegmentInfo], d.pop("segments", UNSET))


		path_get_info = cls(
			segments= segments,
		)

		path_get_info.additional_properties = d
		return path_get_info

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
