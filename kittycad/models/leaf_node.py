from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

N = TypeVar("N", bound="LeafNode")


@attr.s(auto_attribs=True)
class LeafNode:
    """Leaf node information."""  # noqa: E501

    auth_timeout: Union[Unset, int] = UNSET
    host: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    tls_timeout: Union[Unset, int] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auth_timeout = self.auth_timeout
        host = self.host
        port = self.port
        tls_timeout = self.tls_timeout

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_timeout is not UNSET:
            field_dict["auth_timeout"] = auth_timeout
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if tls_timeout is not UNSET:
            field_dict["tls_timeout"] = tls_timeout

        return field_dict

    @classmethod
    def from_dict(cls: Type[N], src_dict: Dict[str, Any]) -> N:
        d = src_dict.copy()
        auth_timeout = d.pop("auth_timeout", UNSET)

        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        tls_timeout = d.pop("tls_timeout", UNSET)

        leaf_node = cls(
            auth_timeout=auth_timeout,
            host=host,
            port=port,
            tls_timeout=tls_timeout,
        )

        leaf_node.additional_properties = d
        return leaf_node

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
