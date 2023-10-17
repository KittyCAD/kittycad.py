from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

BR = TypeVar("BR", bound="TextToCadCreateBody")

@attr.s(auto_attribs=True)
class TextToCadCreateBody:
	""" Body for generating models from text. """ # noqa: E501
	prompt: Union[Unset, str] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		prompt = self.prompt

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if prompt is not UNSET:
			field_dict['prompt'] = prompt

		return field_dict

	@classmethod
	def from_dict(cls: Type[BR], src_dict: Dict[str, Any]) -> BR:
		d = src_dict.copy()
		prompt = d.pop("prompt", UNSET)


		text_to_cad_create_body = cls(
			prompt= prompt,
		)

		text_to_cad_create_body.additional_properties = d
		return text_to_cad_create_body

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
