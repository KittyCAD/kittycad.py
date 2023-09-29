from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

NN = TypeVar("NN", bound="EntityGetNumChildren")

@attr.s(auto_attribs=True)
class EntityGetNumChildren:
	""" The response from the `EntityGetNumChildren` command. """ # noqa: E501
	num:  Union[Unset, int] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		num = self.num

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if num is not UNSET:
			field_dict['num'] = num

		return field_dict

	@classmethod
	def from_dict(cls: Type[NN], src_dict: Dict[str, Any]) -> NN:
		d = src_dict.copy()
		num = d.pop("num", UNSET)


		entity_get_num_children = cls(
			num= num,
		)

		entity_get_num_children.additional_properties = d
		return entity_get_num_children

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
