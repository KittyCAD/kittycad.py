from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

JL = TypeVar("JL", bound="SelectGet")

@attr.s(auto_attribs=True)
class SelectGet:
	""" The response from the `SelectGet` command. """ # noqa: E501
	entity_ids: Union[Unset, List[str]] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		entity_ids: Union[Unset, List[str]] = UNSET
		if not isinstance(self.entity_ids, Unset):
			entity_ids = self.entity_ids

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if entity_ids is not UNSET:
			field_dict['entity_ids'] = entity_ids

		return field_dict

	@classmethod
	def from_dict(cls: Type[JL], src_dict: Dict[str, Any]) -> JL:
		d = src_dict.copy()
		entity_ids = cast(List[str], d.pop("entity_ids", UNSET))


		select_get = cls(
			entity_ids= entity_ids,
		)

		select_get.additional_properties = d
		return select_get

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
