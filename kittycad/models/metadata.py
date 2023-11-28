from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cache_metadata import CacheMetadata
from ..models.connection import Connection
from ..models.environment import Environment
from ..models.file_system_metadata import FileSystemMetadata
from ..types import UNSET, Unset

IT = TypeVar("IT", bound="Metadata")


@attr.s(auto_attribs=True)
class Metadata:
    """Metadata about our currently running server.

    This is mostly used for internal purposes and debugging."""  # noqa: E501

    cache: Union[Unset, CacheMetadata] = UNSET
    environment: Union[Unset, Environment] = UNSET
    fs: Union[Unset, FileSystemMetadata] = UNSET
    git_hash: Union[Unset, str] = UNSET
    pubsub: Union[Unset, Connection] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.cache, Unset):
            cache = self.cache
        if not isinstance(self.environment, Unset):
            environment = self.environment
        if not isinstance(self.fs, Unset):
            fs = self.fs
        git_hash = self.git_hash
        if not isinstance(self.pubsub, Unset):
            pubsub = self.pubsub

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cache is not UNSET:
            field_dict["cache"] = cache.to_dict()
        if environment is not UNSET:
            field_dict["environment"] = environment
        if fs is not UNSET:
            field_dict["fs"] = fs.to_dict()
        if git_hash is not UNSET:
            field_dict["git_hash"] = git_hash
        if pubsub is not UNSET:
            field_dict["pubsub"] = pubsub.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[IT], src_dict: Dict[str, Any]) -> IT:
        d = src_dict.copy()
        _cache = d.pop("cache", UNSET)
        cache: Union[Unset, CacheMetadata]
        if isinstance(_cache, Unset):
            cache = UNSET
        if _cache is None:
            cache = UNSET
        else:
            cache = CacheMetadata.from_dict(_cache)

        _environment = d.pop("environment", UNSET)
        environment: Union[Unset, Environment]
        if isinstance(_environment, Unset):
            environment = UNSET
        if _environment is None:
            environment = UNSET
        else:
            environment = _environment

        _fs = d.pop("fs", UNSET)
        fs: Union[Unset, FileSystemMetadata]
        if isinstance(_fs, Unset):
            fs = UNSET
        if _fs is None:
            fs = UNSET
        else:
            fs = FileSystemMetadata.from_dict(_fs)

        git_hash = d.pop("git_hash", UNSET)

        _pubsub = d.pop("pubsub", UNSET)
        pubsub: Union[Unset, Connection]
        if isinstance(_pubsub, Unset):
            pubsub = UNSET
        if _pubsub is None:
            pubsub = UNSET
        else:
            pubsub = Connection.from_dict(_pubsub)

        metadata = cls(
            cache=cache,
            environment=environment,
            fs=fs,
            git_hash=git_hash,
            pubsub=pubsub,
        )

        metadata.additional_properties = d
        return metadata

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
