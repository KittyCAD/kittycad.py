from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

N = TypeVar("N", bound="Cluster")


@attr.s(auto_attribs=True)
class Cluster:
    """Cluster information."""  # noqa: E501

    addr: Union[Unset, str] = UNSET
    auth_timeout: Union[Unset, int] = UNSET
    cluster_port: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    tls_timeout: Union[Unset, int] = UNSET
    urls: Union[Unset, List[str]] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        addr = self.addr
        auth_timeout = self.auth_timeout
        cluster_port = self.cluster_port
        name = self.name
        tls_timeout = self.tls_timeout
        urls: Union[Unset, List[str]] = UNSET
        if not isinstance(self.urls, Unset):
            urls = self.urls

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addr is not UNSET:
            field_dict["addr"] = addr
        if auth_timeout is not UNSET:
            field_dict["auth_timeout"] = auth_timeout
        if cluster_port is not UNSET:
            field_dict["cluster_port"] = cluster_port
        if name is not UNSET:
            field_dict["name"] = name
        if tls_timeout is not UNSET:
            field_dict["tls_timeout"] = tls_timeout
        if urls is not UNSET:
            field_dict["urls"] = urls

        return field_dict

    @classmethod
    def from_dict(cls: Type[N], src_dict: Dict[str, Any]) -> N:
        d = src_dict.copy()
        addr = d.pop("addr", UNSET)

        auth_timeout = d.pop("auth_timeout", UNSET)

        cluster_port = d.pop("cluster_port", UNSET)

        name = d.pop("name", UNSET)

        tls_timeout = d.pop("tls_timeout", UNSET)

        urls = cast(List[str], d.pop("urls", UNSET))

        cluster = cls(
            addr=addr,
            auth_timeout=auth_timeout,
            cluster_port=cluster_port,
            name=name,
            tls_timeout=tls_timeout,
            urls=urls,
        )

        cluster.additional_properties = d
        return cluster

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
