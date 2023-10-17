from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

IU = TypeVar("IU", bound="UserResultsPage")

@attr.s(auto_attribs=True)
class UserResultsPage:
	""" A single page of results """ # noqa: E501
	from ..models.user import User
	items: Union[Unset, List[User]] = UNSET
	next_page: Union[Unset, str] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		from ..models.user import User
		items: Union[Unset, List[User]] = UNSET
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
	def from_dict(cls: Type[IU], src_dict: Dict[str, Any]) -> IU:
		d = src_dict.copy()
		from ..models.user import User
		items = cast(List[User], d.pop("items", UNSET))

		next_page = d.pop("next_page", UNSET)


		user_results_page = cls(
			items= items,
			next_page= next_page,
		)

		user_results_page.additional_properties = d
		return user_results_page

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
