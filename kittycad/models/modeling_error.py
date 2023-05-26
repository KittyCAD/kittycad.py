from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

H = TypeVar("H", bound="ModelingError")


@attr.s(auto_attribs=True)
class ModelingError:
    """Why a command submitted to the Modeling API failed."""  # noqa: E501

    error_code: Union[Unset, str] = UNSET
    external_message: Union[Unset, str] = UNSET
    internal_message: Union[Unset, str] = UNSET
    status_code: Union[Unset, int] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_code = self.error_code
        external_message = self.external_message
        internal_message = self.internal_message
        status_code = self.status_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if external_message is not UNSET:
            field_dict["external_message"] = external_message
        if internal_message is not UNSET:
            field_dict["internal_message"] = internal_message
        if status_code is not UNSET:
            field_dict["status_code"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[H], src_dict: Dict[str, Any]) -> H:
        d = src_dict.copy()
        error_code = d.pop("error_code", UNSET)

        external_message = d.pop("external_message", UNSET)

        internal_message = d.pop("internal_message", UNSET)

        status_code = d.pop("status_code", UNSET)

        modeling_error = cls(
            error_code=error_code,
            external_message=external_message,
            internal_message=internal_message,
            status_code=status_code,
        )

        modeling_error.additional_properties = d
        return modeling_error

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
