from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.entity_type import EntityType
from ..types import UNSET, Unset

PV = TypeVar("PV", bound="GetEntityType")

@attr.s(auto_attribs=True)
class GetEntityType:
	""" The response from the `GetEntityType` command. """ # noqa: E501
	entity_type: Union[Unset, EntityType] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.entity_type, Unset):
			entity_type = self.entity_type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if entity_type is not UNSET:
			field_dict['entity_type'] = entity_type

		return field_dict

	@classmethod
	def from_dict(cls: Type[PV], src_dict: Dict[str, Any]) -> PV:
		d = src_dict.copy()
		_entity_type = d.pop("entity_type", UNSET)
		entity_type: Union[Unset, EntityType]
		if isinstance(_entity_type, Unset):
			entity_type = UNSET
		else:
			entity_type = _entity_type # type: ignore[arg-type]


		get_entity_type = cls(
			entity_type= entity_type,
		)

		get_entity_type.additional_properties = d
		return get_entity_type

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
