from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.annotation_line_end_options import AnnotationLineEndOptions
from ..models.annotation_text_options import AnnotationTextOptions
from ..models.color import Color
from ..models.point3d import Point3d
from ..types import UNSET, Unset

UZ = TypeVar("UZ", bound="AnnotationOptions")

@attr.s(auto_attribs=True)
class AnnotationOptions:
	""" Options for annotations """ # noqa: E501
	color: Union[Unset, Color] = UNSET
	line_ends: Union[Unset, AnnotationLineEndOptions] = UNSET
	line_width:  Union[Unset, float] = UNSET
	position: Union[Unset, Point3d] = UNSET
	text: Union[Unset, AnnotationTextOptions] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.color, Unset):
			color = self.color
		if not isinstance(self.line_ends, Unset):
			line_ends = self.line_ends
		line_width = self.line_width
		if not isinstance(self.position, Unset):
			position = self.position
		if not isinstance(self.text, Unset):
			text = self.text

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if color is not UNSET:
			field_dict['color'] = color
		if line_ends is not UNSET:
			field_dict['line_ends'] = line_ends
		if line_width is not UNSET:
			field_dict['line_width'] = line_width
		if position is not UNSET:
			field_dict['position'] = position
		if text is not UNSET:
			field_dict['text'] = text

		return field_dict

	@classmethod
	def from_dict(cls: Type[UZ], src_dict: Dict[str, Any]) -> UZ:
		d = src_dict.copy()
		_color = d.pop("color", UNSET)
		color: Union[Unset, Color]
		if isinstance(_color, Unset):
			color = UNSET
		else:
			color = _color # type: ignore[arg-type]

		_line_ends = d.pop("line_ends", UNSET)
		line_ends: Union[Unset, AnnotationLineEndOptions]
		if isinstance(_line_ends, Unset):
			line_ends = UNSET
		else:
			line_ends = _line_ends # type: ignore[arg-type]

		line_width = d.pop("line_width", UNSET)

		_position = d.pop("position", UNSET)
		position: Union[Unset, Point3d]
		if isinstance(_position, Unset):
			position = UNSET
		else:
			position = _position # type: ignore[arg-type]

		_text = d.pop("text", UNSET)
		text: Union[Unset, AnnotationTextOptions]
		if isinstance(_text, Unset):
			text = UNSET
		else:
			text = _text # type: ignore[arg-type]


		annotation_options = cls(
			color= color,
			line_ends= line_ends,
			line_width= line_width,
			position= position,
			text= text,
		)

		annotation_options.additional_properties = d
		return annotation_options

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
