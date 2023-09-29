from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

TP = TypeVar("TP", bound="IceServer")

@attr.s(auto_attribs=True)
class IceServer:
	""" Representation of an ICE server used for STUN/TURN Used to initiate WebRTC connections based on <https://developer.mozilla.org/en-US/docs/Web/API/RTCIceServer> """ # noqa: E501
	credential: Union[Unset, str] = UNSET
	urls: Union[Unset, List[str]] = UNSET
	username: Union[Unset, str] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		credential = self.credential
		urls: Union[Unset, List[str]] = UNSET
		if not isinstance(self.urls, Unset):
			urls = self.urls
		username = self.username

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if credential is not UNSET:
			field_dict['credential'] = credential
		if urls is not UNSET:
			field_dict['urls'] = urls
		if username is not UNSET:
			field_dict['username'] = username

		return field_dict

	@classmethod
	def from_dict(cls: Type[TP], src_dict: Dict[str, Any]) -> TP:
		d = src_dict.copy()
		credential = d.pop("credential", UNSET)

		urls = cast(List[str], d.pop("urls", UNSET))

		username = d.pop("username", UNSET)


		ice_server = cls(
			credential= credential,
			urls= urls,
			username= username,
		)

		ice_server.additional_properties = d
		return ice_server

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
