from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

U = TypeVar("U", bound="MetaClusterInfo")


@attr.s(auto_attribs=True)
class MetaClusterInfo:
    """Jetstream statistics."""  # noqa: E501

    cluster_size: Union[Unset, int] = UNSET
    leader: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cluster_size = self.cluster_size
        leader = self.leader
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster_size is not UNSET:
            field_dict["cluster_size"] = cluster_size
        if leader is not UNSET:
            field_dict["leader"] = leader
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[U], src_dict: Dict[str, Any]) -> U:
        d = src_dict.copy()
        cluster_size = d.pop("cluster_size", UNSET)

        leader = d.pop("leader", UNSET)

        name = d.pop("name", UNSET)

        meta_cluster_info = cls(
            cluster_size=cluster_size,
            leader=leader,
            name=name,
        )

        meta_cluster_info.additional_properties = d
        return meta_cluster_info

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
