from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Runtime")


@attr.s(auto_attribs=True)
class Runtime:
    """ """
    path: Union[Unset, str] = UNSET
    runtime_args: Union[Unset, List[str]] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        runtime_args: Union[Unset, List[str]] = UNSET
        if not isinstance(self.runtime_args, Unset):
            runtime_args = self.runtime_args

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict['path'] = path
        if runtime_args is not UNSET:
            field_dict['runtime_args'] = runtime_args

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path", UNSET)

        runtime_args = cast(List[str], d.pop("runtime_args", UNSET))

        runtime = cls(
            path=path,
            runtime_args=runtime_args,
        )

        runtime.additional_properties = d
        return runtime

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
