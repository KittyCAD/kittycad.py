from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

UF = TypeVar("UF", bound="ExtendedUserResultsPage")

@attr.s(auto_attribs=True)
class ExtendedUserResultsPage:
	""" A single page of results """ # noqa: E501
	from ..models.extended_user import ExtendedUser
	items: Union[Unset, List[ExtendedUser]] = UNSET
	next_page: Union[Unset, str] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		from ..models.extended_user import ExtendedUser
		items: Union[Unset, List[ExtendedUser]] = UNSET
		if not isinstance(self.items, Unset):
			items = self.items
		next_page = self.next_page

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if items is not UNSET:
			field_dict['items'] = items
		if next_page is not UNSET:
			field_dict['next_page'] = next_page

		return field_dict

	@classmethod
	def from_dict(cls: Type[UF], src_dict: Dict[str, Any]) -> UF:
		d = src_dict.copy()
		from ..models.extended_user import ExtendedUser
		items = cast(List[ExtendedUser], d.pop("items", UNSET))

		next_page = d.pop("next_page", UNSET)


		extended_user_results_page = cls(
			items= items,
			next_page= next_page,
		)

		extended_user_results_page.additional_properties = d
		return extended_user_results_page

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
