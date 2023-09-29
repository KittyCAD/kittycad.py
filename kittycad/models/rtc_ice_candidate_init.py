from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

PD = TypeVar("PD", bound="RtcIceCandidateInit")

@attr.s(auto_attribs=True)
class RtcIceCandidateInit:
	""" ICECandidateInit is used to serialize ice candidates """ # noqa: E501
	candidate: Union[Unset, str] = UNSET
	sdp_m_line_index:  Union[Unset, int] = UNSET
	sdp_mid: Union[Unset, str] = UNSET
	username_fragment: Union[Unset, str] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		candidate = self.candidate
		sdp_m_line_index = self.sdp_m_line_index
		sdp_mid = self.sdp_mid
		username_fragment = self.username_fragment

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if candidate is not UNSET:
			field_dict['candidate'] = candidate
		if sdp_m_line_index is not UNSET:
			field_dict['sdpMLineIndex'] = sdp_m_line_index
		if sdp_mid is not UNSET:
			field_dict['sdpMid'] = sdp_mid
		if username_fragment is not UNSET:
			field_dict['usernameFragment'] = username_fragment

		return field_dict

	@classmethod
	def from_dict(cls: Type[PD], src_dict: Dict[str, Any]) -> PD:
		d = src_dict.copy()
		candidate = d.pop("candidate", UNSET)

		sdp_m_line_index = d.pop("sdpMLineIndex", UNSET)

		sdp_mid = d.pop("sdpMid", UNSET)

		username_fragment = d.pop("usernameFragment", UNSET)


		rtc_ice_candidate_init = cls(
			candidate= candidate,
			sdp_m_line_index= sdp_m_line_index,
			sdp_mid= sdp_mid,
			username_fragment= username_fragment,
		)

		rtc_ice_candidate_init.additional_properties = d
		return rtc_ice_candidate_init

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
