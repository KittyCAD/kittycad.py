from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

UF = TypeVar("UF", bound="FailureWebSocketResponse")

@attr.s(auto_attribs=True)
class FailureWebSocketResponse:
	""" Unsuccessful Websocket response. """ # noqa: E501
	from ..models.api_error import ApiError
	errors: Union[Unset, List[ApiError]] = UNSET
	request_id: Union[Unset, str] = UNSET
	success: Union[Unset, bool] = False

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		from ..models.api_error import ApiError
		errors: Union[Unset, List[ApiError]] = UNSET
		if not isinstance(self.errors, Unset):
			errors = self.errors
		request_id = self.request_id
		success = self.success

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if errors is not UNSET:
			field_dict['errors'] = errors
		if request_id is not UNSET:
			field_dict['request_id'] = request_id
		if success is not UNSET:
			field_dict['success'] = success

		return field_dict

	@classmethod
	def from_dict(cls: Type[UF], src_dict: Dict[str, Any]) -> UF:
		d = src_dict.copy()
		from ..models.api_error import ApiError
		errors = cast(List[ApiError], d.pop("errors", UNSET))

		request_id = d.pop("request_id", UNSET)

		success = d.pop("success", UNSET)


		failure_web_socket_response = cls(
			errors= errors,
			request_id= request_id,
			success= success,
		)

		failure_web_socket_response.additional_properties = d
		return failure_web_socket_response

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
