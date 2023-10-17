from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

PD = TypeVar("PD", bound="PaymentIntent")

@attr.s(auto_attribs=True)
class PaymentIntent:
	""" A payment intent response. """ # noqa: E501
	client_secret: Union[Unset, str] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		client_secret = self.client_secret

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if client_secret is not UNSET:
			field_dict['client_secret'] = client_secret

		return field_dict

	@classmethod
	def from_dict(cls: Type[PD], src_dict: Dict[str, Any]) -> PD:
		d = src_dict.copy()
		client_secret = d.pop("client_secret", UNSET)


		payment_intent = cls(
			client_secret= client_secret,
		)

		payment_intent.additional_properties = d
		return payment_intent

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
