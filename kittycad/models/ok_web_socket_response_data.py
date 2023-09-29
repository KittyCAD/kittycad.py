from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

BF = TypeVar("BF", bound="ice_server_info")

@attr.s(auto_attribs=True)
class ice_server_info:
	""" Information about the ICE servers. """ # noqa: E501
	data: Union[Unset, Any] = UNSET
	type: str = "ice_server_info"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		data = self.data
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if data is not UNSET:
			field_dict['data'] = data
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[BF], src_dict: Dict[str, Any]) -> BF:
		d = src_dict.copy()
		data = d.pop("data", UNSET)
		type = d.pop("type", UNSET)


		ice_server_info = cls(
			data= data,
			type= type,
		)

		ice_server_info.additional_properties = d
		return ice_server_info

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




UU = TypeVar("UU", bound="trickle_ice")

@attr.s(auto_attribs=True)
class trickle_ice:
	""" The trickle ICE candidate response. """ # noqa: E501
	data: Union[Unset, Any] = UNSET
	type: str = "trickle_ice"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		data = self.data
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if data is not UNSET:
			field_dict['data'] = data
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[UU], src_dict: Dict[str, Any]) -> UU:
		d = src_dict.copy()
		data = d.pop("data", UNSET)
		type = d.pop("type", UNSET)


		trickle_ice = cls(
			data= data,
			type= type,
		)

		trickle_ice.additional_properties = d
		return trickle_ice

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




MB = TypeVar("MB", bound="sdp_answer")

@attr.s(auto_attribs=True)
class sdp_answer:
	""" The SDP answer response. """ # noqa: E501
	data: Union[Unset, Any] = UNSET
	type: str = "sdp_answer"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		data = self.data
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if data is not UNSET:
			field_dict['data'] = data
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[MB], src_dict: Dict[str, Any]) -> MB:
		d = src_dict.copy()
		data = d.pop("data", UNSET)
		type = d.pop("type", UNSET)


		sdp_answer = cls(
			data= data,
			type= type,
		)

		sdp_answer.additional_properties = d
		return sdp_answer

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




TB = TypeVar("TB", bound="modeling")

@attr.s(auto_attribs=True)
class modeling:
	""" The modeling command response. """ # noqa: E501
	data: Union[Unset, Any] = UNSET
	type: str = "modeling"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		data = self.data
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if data is not UNSET:
			field_dict['data'] = data
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[TB], src_dict: Dict[str, Any]) -> TB:
		d = src_dict.copy()
		data = d.pop("data", UNSET)
		type = d.pop("type", UNSET)


		modeling = cls(
			data= data,
			type= type,
		)

		modeling.additional_properties = d
		return modeling

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




FJ = TypeVar("FJ", bound="export")

@attr.s(auto_attribs=True)
class export:
	""" The exported files. """ # noqa: E501
	data: Union[Unset, Any] = UNSET
	type: str = "export"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		data = self.data
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if data is not UNSET:
			field_dict['data'] = data
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[FJ], src_dict: Dict[str, Any]) -> FJ:
		d = src_dict.copy()
		data = d.pop("data", UNSET)
		type = d.pop("type", UNSET)


		export = cls(
			data= data,
			type= type,
		)

		export.additional_properties = d
		return export

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




HB = TypeVar("HB", bound="metrics_request")

@attr.s(auto_attribs=True)
class metrics_request:
	""" Request a collection of metrics, to include WebRTC. """ # noqa: E501
	data: Union[Unset, Any] = UNSET
	type: str = "metrics_request"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		data = self.data
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if data is not UNSET:
			field_dict['data'] = data
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[HB], src_dict: Dict[str, Any]) -> HB:
		d = src_dict.copy()
		data = d.pop("data", UNSET)
		type = d.pop("type", UNSET)


		metrics_request = cls(
			data= data,
			type= type,
		)

		metrics_request.additional_properties = d
		return metrics_request

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

OkWebSocketResponseData = Union[ice_server_info, trickle_ice, sdp_answer, modeling, export, metrics_request]
