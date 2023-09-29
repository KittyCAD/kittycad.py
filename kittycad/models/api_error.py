from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.error_code import ErrorCode
from ..types import UNSET, Unset

LB = TypeVar("LB", bound="ApiError")

@attr.s(auto_attribs=True)
class ApiError:
	""" An error. """ # noqa: E501
	error_code: Union[Unset, ErrorCode] = UNSET
	message: Union[Unset, str] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.error_code, Unset):
			error_code = self.error_code
		message = self.message

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if error_code is not UNSET:
			field_dict['error_code'] = error_code
		if message is not UNSET:
			field_dict['message'] = message

		return field_dict

	@classmethod
	def from_dict(cls: Type[LB], src_dict: Dict[str, Any]) -> LB:
		d = src_dict.copy()
		_error_code = d.pop("error_code", UNSET)
		error_code: Union[Unset, ErrorCode]
		if isinstance(_error_code, Unset):
			error_code = UNSET
		else:
			error_code = _error_code # type: ignore[arg-type]

		message = d.pop("message", UNSET)


		api_error = cls(
			error_code= error_code,
			message= message,
		)

		api_error.additional_properties = d
		return api_error

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
