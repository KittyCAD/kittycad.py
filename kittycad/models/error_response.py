from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

LT = TypeVar("LT", bound="ErrorResponse")


@attr.s(auto_attribs=True)
class ErrorResponse:
    """The error response."""  # noqa: E501

    from ..models.error import Error

    errors: Union[Unset, List[Error]] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.error import Error

        errors: Union[Unset, List[Error]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[LT], src_dict: Dict[str, Any]) -> LT:
        d = src_dict.copy()
        from ..models.error import Error

        errors = cast(List[Error], d.pop("errors", UNSET))

        error_response = cls(
            errors=errors,
        )

        error_response.additional_properties = d
        return error_response

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
