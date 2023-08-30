from typing import Any, Dict, Type, TypeVar

import attr

VI = TypeVar("VI", bound="Empty")


@attr.s(auto_attribs=True)
class Empty:
    def __str__(self) -> str:
        return ""

    @classmethod
    def from_dict(cls: Type[VI], src_dict: Dict[str, Any]) -> Any:
        return {}
