from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

JD = TypeVar("JD", bound="MouseClick")

@attr.s(auto_attribs=True)
class MouseClick:
	""" The response from the `MouseClick` command. """ # noqa: E501
	entities_modified: Union[Unset, List[str]] = UNSET
	entities_selected: Union[Unset, List[str]] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		entities_modified: Union[Unset, List[str]] = UNSET
		if not isinstance(self.entities_modified, Unset):
			entities_modified = self.entities_modified
		entities_selected: Union[Unset, List[str]] = UNSET
		if not isinstance(self.entities_selected, Unset):
			entities_selected = self.entities_selected

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if entities_modified is not UNSET:
			field_dict['entities_modified'] = entities_modified
		if entities_selected is not UNSET:
			field_dict['entities_selected'] = entities_selected

		return field_dict

	@classmethod
	def from_dict(cls: Type[JD], src_dict: Dict[str, Any]) -> JD:
		d = src_dict.copy()
		entities_modified = cast(List[str], d.pop("entities_modified", UNSET))

		entities_selected = cast(List[str], d.pop("entities_selected", UNSET))


		mouse_click = cls(
			entities_modified= entities_modified,
			entities_selected= entities_selected,
		)

		mouse_click.additional_properties = d
		return mouse_click

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
