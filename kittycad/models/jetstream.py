from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.jetstream_config import JetstreamConfig
from ..models.jetstream_stats import JetstreamStats
from ..models.meta_cluster_info import MetaClusterInfo
from ..types import UNSET, Unset

H = TypeVar("H", bound="Jetstream")


@attr.s(auto_attribs=True)
class Jetstream:
    """Jetstream information."""  # noqa: E501

    config: Union[Unset, JetstreamConfig] = UNSET
    meta: Union[Unset, MetaClusterInfo] = UNSET
    stats: Union[Unset, JetstreamStats] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.config, Unset):
            config = self.config
        if not isinstance(self.meta, Unset):
            meta = self.meta
        if not isinstance(self.stats, Unset):
            stats = self.stats

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if meta is not UNSET:
            field_dict["meta"] = meta
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: Type[H], src_dict: Dict[str, Any]) -> H:
        d = src_dict.copy()
        _config = d.pop("config", UNSET)
        config: Union[Unset, JetstreamConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = JetstreamConfig(_config)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, MetaClusterInfo]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = MetaClusterInfo(_meta)

        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, JetstreamStats]
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = JetstreamStats(_stats)

        jetstream = cls(
            config=config,
            meta=meta,
            stats=stats,
        )

        jetstream.additional_properties = d
        return jetstream

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
