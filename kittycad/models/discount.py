from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.coupon import Coupon
from ..types import UNSET, Unset

YY = TypeVar("YY", bound="Discount")

@attr.s(auto_attribs=True)
class Discount:
	""" The resource representing a Discount. """ # noqa: E501
	coupon: Union[Unset, Coupon] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.coupon, Unset):
			coupon = self.coupon

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if coupon is not UNSET:
			field_dict['coupon'] = coupon

		return field_dict

	@classmethod
	def from_dict(cls: Type[YY], src_dict: Dict[str, Any]) -> YY:
		d = src_dict.copy()
		_coupon = d.pop("coupon", UNSET)
		coupon: Union[Unset, Coupon]
		if isinstance(_coupon, Unset):
			coupon = UNSET
		else:
			coupon = _coupon # type: ignore[arg-type]


		discount = cls(
			coupon= coupon,
		)

		discount.additional_properties = d
		return discount

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
