from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

VR = TypeVar("VR", bound="ClientMetrics")

@attr.s(auto_attribs=True)
class ClientMetrics:
	""" ClientMetrics contains information regarding the state of the peer. """ # noqa: E501
	rtc_frames_decoded:  Union[Unset, int] = UNSET
	rtc_frames_dropped:  Union[Unset, int] = UNSET
	rtc_frames_per_second:  Union[Unset, int] = UNSET
	rtc_frames_received:  Union[Unset, int] = UNSET
	rtc_freeze_count:  Union[Unset, int] = UNSET
	rtc_jitter_sec:  Union[Unset, float] = UNSET
	rtc_keyframes_decoded:  Union[Unset, int] = UNSET
	rtc_total_freezes_duration_sec:  Union[Unset, float] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		rtc_frames_decoded = self.rtc_frames_decoded
		rtc_frames_dropped = self.rtc_frames_dropped
		rtc_frames_per_second = self.rtc_frames_per_second
		rtc_frames_received = self.rtc_frames_received
		rtc_freeze_count = self.rtc_freeze_count
		rtc_jitter_sec = self.rtc_jitter_sec
		rtc_keyframes_decoded = self.rtc_keyframes_decoded
		rtc_total_freezes_duration_sec = self.rtc_total_freezes_duration_sec

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if rtc_frames_decoded is not UNSET:
			field_dict['rtc_frames_decoded'] = rtc_frames_decoded
		if rtc_frames_dropped is not UNSET:
			field_dict['rtc_frames_dropped'] = rtc_frames_dropped
		if rtc_frames_per_second is not UNSET:
			field_dict['rtc_frames_per_second'] = rtc_frames_per_second
		if rtc_frames_received is not UNSET:
			field_dict['rtc_frames_received'] = rtc_frames_received
		if rtc_freeze_count is not UNSET:
			field_dict['rtc_freeze_count'] = rtc_freeze_count
		if rtc_jitter_sec is not UNSET:
			field_dict['rtc_jitter_sec'] = rtc_jitter_sec
		if rtc_keyframes_decoded is not UNSET:
			field_dict['rtc_keyframes_decoded'] = rtc_keyframes_decoded
		if rtc_total_freezes_duration_sec is not UNSET:
			field_dict['rtc_total_freezes_duration_sec'] = rtc_total_freezes_duration_sec

		return field_dict

	@classmethod
	def from_dict(cls: Type[VR], src_dict: Dict[str, Any]) -> VR:
		d = src_dict.copy()
		rtc_frames_decoded = d.pop("rtc_frames_decoded", UNSET)

		rtc_frames_dropped = d.pop("rtc_frames_dropped", UNSET)

		rtc_frames_per_second = d.pop("rtc_frames_per_second", UNSET)

		rtc_frames_received = d.pop("rtc_frames_received", UNSET)

		rtc_freeze_count = d.pop("rtc_freeze_count", UNSET)

		rtc_jitter_sec = d.pop("rtc_jitter_sec", UNSET)

		rtc_keyframes_decoded = d.pop("rtc_keyframes_decoded", UNSET)

		rtc_total_freezes_duration_sec = d.pop("rtc_total_freezes_duration_sec", UNSET)


		client_metrics = cls(
			rtc_frames_decoded= rtc_frames_decoded,
			rtc_frames_dropped= rtc_frames_dropped,
			rtc_frames_per_second= rtc_frames_per_second,
			rtc_frames_received= rtc_frames_received,
			rtc_freeze_count= rtc_freeze_count,
			rtc_jitter_sec= rtc_jitter_sec,
			rtc_keyframes_decoded= rtc_keyframes_decoded,
			rtc_total_freezes_duration_sec= rtc_total_freezes_duration_sec,
		)

		client_metrics.additional_properties = d
		return client_metrics

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
