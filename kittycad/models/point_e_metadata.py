from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

S = TypeVar("S", bound="PointEMetadata")


@attr.s(auto_attribs=True)
class PointEMetadata:
    """Metadata about our point-e instance.

    This is mostly used for internal purposes and debugging."""  # noqa: E501

    ok: Union[Unset, bool] = False

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ok = self.ok

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ok is not UNSET:
            field_dict["ok"] = ok

        return field_dict

    @classmethod
    def from_dict(cls: Type[S], src_dict: Dict[str, Any]) -> S:
        d = src_dict.copy()
        ok = d.pop("ok", UNSET)

        point_e_metadata = cls(
            ok=ok,
        )

        point_e_metadata.additional_properties = d
        return point_e_metadata

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
