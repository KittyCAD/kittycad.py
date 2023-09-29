from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.client_metrics import ClientMetrics
from ..models.modeling_cmd import ModelingCmd
from ..models.modeling_cmd_id import ModelingCmdId
from ..models.rtc_ice_candidate_init import RtcIceCandidateInit
from ..models.rtc_session_description import RtcSessionDescription
from ..types import UNSET, Unset

OA = TypeVar("OA", bound="trickle_ice")

@attr.s(auto_attribs=True)
class trickle_ice:
	""" The trickle ICE candidate request. """ # noqa: E501
	candidate: Union[Unset, RtcIceCandidateInit] = UNSET
	type: str = "trickle_ice"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.candidate, Unset):
			candidate = self.candidate
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if candidate is not UNSET:
			field_dict['candidate'] = candidate
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[OA], src_dict: Dict[str, Any]) -> OA:
		d = src_dict.copy()
		_candidate = d.pop("candidate", UNSET)
		candidate: Union[Unset, RtcIceCandidateInit]
		if isinstance(_candidate, Unset):
			candidate = UNSET
		else:
			candidate = _candidate # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		trickle_ice = cls(
			candidate= candidate,
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




EI = TypeVar("EI", bound="sdp_offer")

@attr.s(auto_attribs=True)
class sdp_offer:
	""" The SDP offer request. """ # noqa: E501
	offer: Union[Unset, RtcSessionDescription] = UNSET
	type: str = "sdp_offer"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.offer, Unset):
			offer = self.offer
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if offer is not UNSET:
			field_dict['offer'] = offer
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[EI], src_dict: Dict[str, Any]) -> EI:
		d = src_dict.copy()
		_offer = d.pop("offer", UNSET)
		offer: Union[Unset, RtcSessionDescription]
		if isinstance(_offer, Unset):
			offer = UNSET
		else:
			offer = _offer # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		sdp_offer = cls(
			offer= offer,
			type= type,
		)

		sdp_offer.additional_properties = d
		return sdp_offer

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




CQ = TypeVar("CQ", bound="modeling_cmd_req")

@attr.s(auto_attribs=True)
class modeling_cmd_req:
	""" The modeling command request. """ # noqa: E501
	cmd: Union[Unset, ModelingCmd] = UNSET
	cmd_id: Union[Unset, ModelingCmdId] = UNSET
	type: str = "modeling_cmd_req"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.cmd, Unset):
			cmd = self.cmd
		if not isinstance(self.cmd_id, Unset):
			cmd_id = self.cmd_id
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if cmd is not UNSET:
			field_dict['cmd'] = cmd
		if cmd_id is not UNSET:
			field_dict['cmd_id'] = cmd_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[CQ], src_dict: Dict[str, Any]) -> CQ:
		d = src_dict.copy()
		_cmd = d.pop("cmd", UNSET)
		cmd: Union[Unset, ModelingCmd]
		if isinstance(_cmd, Unset):
			cmd = UNSET
		else:
			cmd = _cmd # type: ignore[arg-type]

		_cmd_id = d.pop("cmd_id", UNSET)
		cmd_id: Union[Unset, ModelingCmdId]
		if isinstance(_cmd_id, Unset):
			cmd_id = UNSET
		else:
			cmd_id = _cmd_id # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		modeling_cmd_req = cls(
			cmd= cmd,
			cmd_id= cmd_id,
			type= type,
		)

		modeling_cmd_req.additional_properties = d
		return modeling_cmd_req

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




JE = TypeVar("JE", bound="ping")

@attr.s(auto_attribs=True)
class ping:
	""" The client-to-server Ping to ensure the WebSocket stays alive. """ # noqa: E501
	type: str = "ping"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[JE], src_dict: Dict[str, Any]) -> JE:
		d = src_dict.copy()
		type = d.pop("type", UNSET)


		ping = cls(
			type= type,
		)

		ping.additional_properties = d
		return ping

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




RD = TypeVar("RD", bound="metrics_response")

@attr.s(auto_attribs=True)
class metrics_response:
	""" The response to a metrics collection request from the server. """ # noqa: E501
	metrics: Union[Unset, ClientMetrics] = UNSET
	type: str = "metrics_response"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.metrics, Unset):
			metrics = self.metrics
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if metrics is not UNSET:
			field_dict['metrics'] = metrics
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[RD], src_dict: Dict[str, Any]) -> RD:
		d = src_dict.copy()
		_metrics = d.pop("metrics", UNSET)
		metrics: Union[Unset, ClientMetrics]
		if isinstance(_metrics, Unset):
			metrics = UNSET
		else:
			metrics = _metrics # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		metrics_response = cls(
			metrics= metrics,
			type= type,
		)

		metrics_response.additional_properties = d
		return metrics_response

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

WebSocketRequest = Union[trickle_ice, sdp_offer, modeling_cmd_req, ping, metrics_response]
