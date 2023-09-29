from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

FH = TypeVar("FH", bound="Coupon")

@attr.s(auto_attribs=True)
class Coupon:
	""" The resource representing a Coupon. """ # noqa: E501
	amount_off:  Union[Unset, float] = UNSET
	deleted: Union[Unset, bool] = False
	id: Union[Unset, str] = UNSET
	percent_off:  Union[Unset, float] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		amount_off = self.amount_off
		deleted = self.deleted
		id = self.id
		percent_off = self.percent_off

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if amount_off is not UNSET:
			field_dict['amount_off'] = amount_off
		if deleted is not UNSET:
			field_dict['deleted'] = deleted
		if id is not UNSET:
			field_dict['id'] = id
		if percent_off is not UNSET:
			field_dict['percent_off'] = percent_off

		return field_dict

	@classmethod
	def from_dict(cls: Type[FH], src_dict: Dict[str, Any]) -> FH:
		d = src_dict.copy()
		amount_off = d.pop("amount_off", UNSET)

		deleted = d.pop("deleted", UNSET)

		id = d.pop("id", UNSET)

		percent_off = d.pop("percent_off", UNSET)


		coupon = cls(
			amount_off= amount_off,
			deleted= deleted,
			id= id,
			percent_off= percent_off,
		)

		coupon.additional_properties = d
		return coupon

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
