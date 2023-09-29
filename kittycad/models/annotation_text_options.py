from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.annotation_text_alignment_x import AnnotationTextAlignmentX
from ..models.annotation_text_alignment_y import AnnotationTextAlignmentY
from ..types import UNSET, Unset

FB = TypeVar("FB", bound="AnnotationTextOptions")

@attr.s(auto_attribs=True)
class AnnotationTextOptions:
	""" Options for annotation text """ # noqa: E501
	point_size:  Union[Unset, int] = UNSET
	text: Union[Unset, str] = UNSET
	x: Union[Unset, AnnotationTextAlignmentX] = UNSET
	y: Union[Unset, AnnotationTextAlignmentY] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		point_size = self.point_size
		text = self.text
		if not isinstance(self.x, Unset):
			x = self.x
		if not isinstance(self.y, Unset):
			y = self.y

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if point_size is not UNSET:
			field_dict['point_size'] = point_size
		if text is not UNSET:
			field_dict['text'] = text
		if x is not UNSET:
			field_dict['x'] = x
		if y is not UNSET:
			field_dict['y'] = y

		return field_dict

	@classmethod
	def from_dict(cls: Type[FB], src_dict: Dict[str, Any]) -> FB:
		d = src_dict.copy()
		point_size = d.pop("point_size", UNSET)

		text = d.pop("text", UNSET)

		_x = d.pop("x", UNSET)
		x: Union[Unset, AnnotationTextAlignmentX]
		if isinstance(_x, Unset):
			x = UNSET
		else:
			x = _x # type: ignore[arg-type]

		_y = d.pop("y", UNSET)
		y: Union[Unset, AnnotationTextAlignmentY]
		if isinstance(_y, Unset):
			y = UNSET
		else:
			y = _y # type: ignore[arg-type]


		annotation_text_options = cls(
			point_size= point_size,
			text= text,
			x= x,
			y= y,
		)

		annotation_text_options.additional_properties = d
		return annotation_text_options

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
