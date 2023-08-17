from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.error_code import ErrorCode
from ..types import UNSET, Unset

MS = TypeVar("MS", bound="Error")


@attr.s(auto_attribs=True)
class Error:
    """An error."""  # noqa: E501

    code: Union[Unset, ErrorCode] = UNSET
    message: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.code, Unset):
            code = self.code
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[MS], src_dict: Dict[str, Any]) -> MS:
        d = src_dict.copy()
        _code = d.pop("code", UNSET)
        code: Union[Unset, ErrorCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = _code  # type: ignore[arg-type]

        message = d.pop("message", UNSET)

        error = cls(
            code=code,
            message=message,
        )

        error.additional_properties = d
        return error

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
