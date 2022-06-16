from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.cache_metadata import CacheMetadata
from ..models.environment import Environment
from ..models.file_system_metadata import FileSystemMetadata
from ..models.connection import Connection
from ..types import UNSET, Unset

T = TypeVar("T", bound="EngineMetadata")


@attr.s(auto_attribs=True)
class EngineMetadata:
    """ """
    async_jobs_running: Union[Unset, bool] = False
    cache: Union[Unset, CacheMetadata] = UNSET
    environment: Union[Unset, Environment] = UNSET
    fs: Union[Unset, FileSystemMetadata] = UNSET
    git_hash: Union[Unset, str] = UNSET
    pubsub: Union[Unset, Connection] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        async_jobs_running = self.async_jobs_running
        cache: Union[Unset, str] = UNSET
        if not isinstance(self.cache, Unset):
            cache = self.cache.value
        environment: Union[Unset, str] = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.value
        fs: Union[Unset, str] = UNSET
        if not isinstance(self.fs, Unset):
            fs = self.fs.value
        git_hash = self.git_hash
        pubsub: Union[Unset, str] = UNSET
        if not isinstance(self.pubsub, Unset):
            pubsub = self.pubsub.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if async_jobs_running is not UNSET:
            field_dict['async_jobs_running'] = async_jobs_running
        if cache is not UNSET:
            field_dict['cache'] = cache
        if environment is not UNSET:
            field_dict['environment'] = environment
        if fs is not UNSET:
            field_dict['fs'] = fs
        if git_hash is not UNSET:
            field_dict['git_hash'] = git_hash
        if pubsub is not UNSET:
            field_dict['pubsub'] = pubsub

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        async_jobs_running = d.pop("async_jobs_running", UNSET)

        _cache = d.pop("cache", UNSET)
        cache: Union[Unset, CacheMetadata]
        if isinstance(_cache, Unset):
            cache = UNSET
        else:
            cache = CacheMetadata(_cache)

        _environment = d.pop("environment", UNSET)
        environment: Union[Unset, Environment]
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = Environment(_environment)

        _fs = d.pop("fs", UNSET)
        fs: Union[Unset, FileSystemMetadata]
        if isinstance(_fs, Unset):
            fs = UNSET
        else:
            fs = FileSystemMetadata(_fs)

        git_hash = d.pop("git_hash", UNSET)

        _pubsub = d.pop("pubsub", UNSET)
        pubsub: Union[Unset, Connection]
        if isinstance(_pubsub, Unset):
            pubsub = UNSET
        else:
            pubsub = Connection(_pubsub)

        engine_metadata = cls(
            async_jobs_running=async_jobs_running,
            cache=cache,
            environment=environment,
            fs=fs,
            git_hash=git_hash,
            pubsub=pubsub,
        )

        engine_metadata.additional_properties = d
        return engine_metadata

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
