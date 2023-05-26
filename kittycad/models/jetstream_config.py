from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

V = TypeVar("V", bound="JetstreamConfig")


@attr.s(auto_attribs=True)
class JetstreamConfig:
    """Jetstream configuration."""  # noqa: E501

    domain: Union[Unset, str] = UNSET
    max_memory: Union[Unset, int] = UNSET
    max_storage: Union[Unset, int] = UNSET
    store_dir: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        domain = self.domain
        max_memory = self.max_memory
        max_storage = self.max_storage
        store_dir = self.store_dir

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain is not UNSET:
            field_dict["domain"] = domain
        if max_memory is not UNSET:
            field_dict["max_memory"] = max_memory
        if max_storage is not UNSET:
            field_dict["max_storage"] = max_storage
        if store_dir is not UNSET:
            field_dict["store_dir"] = store_dir

        return field_dict

    @classmethod
    def from_dict(cls: Type[V], src_dict: Dict[str, Any]) -> V:
        d = src_dict.copy()
        domain = d.pop("domain", UNSET)

        max_memory = d.pop("max_memory", UNSET)

        max_storage = d.pop("max_storage", UNSET)

        store_dir = d.pop("store_dir", UNSET)

        jetstream_config = cls(
            domain=domain,
            max_memory=max_memory,
            max_storage=max_storage,
            store_dir=store_dir,
        )

        jetstream_config.additional_properties = d
        return jetstream_config

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
