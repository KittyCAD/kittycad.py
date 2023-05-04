from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.drawing_cmd_id import DrawingCmdId
from ..types import UNSET, Unset
from .drawing_error import DrawingError

Success = Any


Error = DrawingError


H = TypeVar("H", bound="Cancelled")


@attr.s(auto_attribs=True)
class Cancelled:
    what_failed: Union[Unset, DrawingCmdId] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.what_failed, Unset):
            what_failed = self.what_failed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if what_failed is not UNSET:
            field_dict["what_failed"] = what_failed

        return field_dict

    @classmethod
    def from_dict(cls: Type[H], src_dict: Dict[str, Any]) -> H:
        d = src_dict.copy()
        _what_failed = d.pop("what_failed", UNSET)
        what_failed: Union[Unset, DrawingCmdId]
        if isinstance(_what_failed, Unset):
            what_failed = UNSET
        else:
            what_failed = DrawingCmdId(_what_failed)

        cancelled = cls(
            what_failed=what_failed,
        )

        cancelled.additional_properties = d
        return cancelled

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


DrawingOutcome = Union[Success, Error, Cancelled]
