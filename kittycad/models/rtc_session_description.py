from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rtc_sdp_type import RtcSdpType
from ..types import UNSET, Unset

SM = TypeVar("SM", bound="RtcSessionDescription")

@attr.s(auto_attribs=True)
class RtcSessionDescription:
	""" SessionDescription is used to expose local and remote session descriptions. """ # noqa: E501
	sdp: Union[Unset, str] = UNSET
	type: Union[Unset, RtcSdpType] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		sdp = self.sdp
		if not isinstance(self.type, Unset):
			type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if sdp is not UNSET:
			field_dict['sdp'] = sdp
		if type is not UNSET:
			field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[SM], src_dict: Dict[str, Any]) -> SM:
		d = src_dict.copy()
		sdp = d.pop("sdp", UNSET)

		_type = d.pop("type", UNSET)
		type: Union[Unset, RtcSdpType]
		if isinstance(_type, Unset):
			type = UNSET
		else:
			type = _type # type: ignore[arg-type]


		rtc_session_description = cls(
			sdp= sdp,
			type= type,
		)

		rtc_session_description.additional_properties = d
		return rtc_session_description

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
