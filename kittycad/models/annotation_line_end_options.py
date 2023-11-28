from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.annotation_line_end import AnnotationLineEnd
from ..types import UNSET, Unset

FB = TypeVar("FB", bound="AnnotationLineEndOptions")


@attr.s(auto_attribs=True)
class AnnotationLineEndOptions:
    """Options for annotation text"""  # noqa: E501

    end: Union[Unset, AnnotationLineEnd] = UNSET
    start: Union[Unset, AnnotationLineEnd] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.end, Unset):
            end = self.end
        if not isinstance(self.start, Unset):
            start = self.start

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end is not UNSET:
            field_dict["end"] = end
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: Type[FB], src_dict: Dict[str, Any]) -> FB:
        d = src_dict.copy()
        _end = d.pop("end", UNSET)
        end: Union[Unset, AnnotationLineEnd]
        if isinstance(_end, Unset):
            end = UNSET
        if _end is None:
            end = UNSET
        else:
            end = _end

        _start = d.pop("start", UNSET)
        start: Union[Unset, AnnotationLineEnd]
        if isinstance(_start, Unset):
            start = UNSET
        if _start is None:
            start = UNSET
        else:
            start = _start

        annotation_line_end_options = cls(
            end=end,
            start=start,
        )

        annotation_line_end_options.additional_properties = d
        return annotation_line_end_options

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
