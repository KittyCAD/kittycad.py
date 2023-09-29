from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

GL = TypeVar("GL", bound="EntityGetChildUuid")

@attr.s(auto_attribs=True)
class EntityGetChildUuid:
	""" The response from the `EntityGetChildUuid` command. """ # noqa: E501
	entity_id: Union[Unset, str] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		entity_id = self.entity_id

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if entity_id is not UNSET:
			field_dict['entity_id'] = entity_id

		return field_dict

	@classmethod
	def from_dict(cls: Type[GL], src_dict: Dict[str, Any]) -> GL:
		d = src_dict.copy()
		entity_id = d.pop("entity_id", UNSET)


		entity_get_child_uuid = cls(
			entity_id= entity_id,
		)

		entity_get_child_uuid.additional_properties = d
		return entity_get_child_uuid

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
