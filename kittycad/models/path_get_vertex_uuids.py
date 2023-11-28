from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

VS = TypeVar("VS", bound="PathGetVertexUuids")


@attr.s(auto_attribs=True)
class PathGetVertexUuids:
    """The response from the `PathGetVertexUuids` command."""  # noqa: E501

    vertex_ids: Union[Unset, List[str]] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vertex_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.vertex_ids, Unset):
            vertex_ids = self.vertex_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vertex_ids is not UNSET:
            field_dict["vertex_ids"] = vertex_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[VS], src_dict: Dict[str, Any]) -> VS:
        d = src_dict.copy()
        vertex_ids = cast(List[str], d.pop("vertex_ids", UNSET))

        path_get_vertex_uuids = cls(
            vertex_ids=vertex_ids,
        )

        path_get_vertex_uuids.additional_properties = d
        return path_get_vertex_uuids

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
