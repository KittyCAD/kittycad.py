from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cache_metadata import CacheMetadata
from ..models.connection import Connection
from ..models.engine_metadata import EngineMetadata
from ..models.environment import Environment
from ..models.executor_metadata import ExecutorMetadata
from ..models.file_system_metadata import FileSystemMetadata
from ..models.point_e_metadata import PointEMetadata
from ..types import UNSET, Unset

S = TypeVar("S", bound="Metadata")


@attr.s(auto_attribs=True)
class Metadata:
    """Metadata about our currently running server.

    This is mostly used for internal purposes and debugging."""  # noqa: E501

    cache: Union[Unset, CacheMetadata] = UNSET
    engine: Union[Unset, EngineMetadata] = UNSET
    environment: Union[Unset, Environment] = UNSET
    executor: Union[Unset, ExecutorMetadata] = UNSET
    fs: Union[Unset, FileSystemMetadata] = UNSET
    git_hash: Union[Unset, str] = UNSET
    point_e: Union[Unset, PointEMetadata] = UNSET
    pubsub: Union[Unset, Connection] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.cache, Unset):
            cache = self.cache
        if not isinstance(self.engine, Unset):
            engine = self.engine
        if not isinstance(self.environment, Unset):
            environment = self.environment
        if not isinstance(self.executor, Unset):
            executor = self.executor
        if not isinstance(self.fs, Unset):
            fs = self.fs
        git_hash = self.git_hash
        if not isinstance(self.point_e, Unset):
            point_e = self.point_e
        if not isinstance(self.pubsub, Unset):
            pubsub = self.pubsub

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cache is not UNSET:
            field_dict["cache"] = cache
        if engine is not UNSET:
            field_dict["engine"] = engine
        if environment is not UNSET:
            field_dict["environment"] = environment
        if executor is not UNSET:
            field_dict["executor"] = executor
        if fs is not UNSET:
            field_dict["fs"] = fs
        if git_hash is not UNSET:
            field_dict["git_hash"] = git_hash
        if point_e is not UNSET:
            field_dict["point_e"] = point_e
        if pubsub is not UNSET:
            field_dict["pubsub"] = pubsub

        return field_dict

    @classmethod
    def from_dict(cls: Type[S], src_dict: Dict[str, Any]) -> S:
        d = src_dict.copy()
        _cache = d.pop("cache", UNSET)
        cache: Union[Unset, CacheMetadata]
        if isinstance(_cache, Unset):
            cache = UNSET
        else:
            cache = CacheMetadata(_cache)

        _engine = d.pop("engine", UNSET)
        engine: Union[Unset, EngineMetadata]
        if isinstance(_engine, Unset):
            engine = UNSET
        else:
            engine = EngineMetadata(_engine)

        _environment = d.pop("environment", UNSET)
        environment: Union[Unset, Environment]
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = Environment(_environment)

        _executor = d.pop("executor", UNSET)
        executor: Union[Unset, ExecutorMetadata]
        if isinstance(_executor, Unset):
            executor = UNSET
        else:
            executor = ExecutorMetadata(_executor)

        _fs = d.pop("fs", UNSET)
        fs: Union[Unset, FileSystemMetadata]
        if isinstance(_fs, Unset):
            fs = UNSET
        else:
            fs = FileSystemMetadata(_fs)

        git_hash = d.pop("git_hash", UNSET)

        _point_e = d.pop("point_e", UNSET)
        point_e: Union[Unset, PointEMetadata]
        if isinstance(_point_e, Unset):
            point_e = UNSET
        else:
            point_e = PointEMetadata(_point_e)

        _pubsub = d.pop("pubsub", UNSET)
        pubsub: Union[Unset, Connection]
        if isinstance(_pubsub, Unset):
            pubsub = UNSET
        else:
            pubsub = Connection(_pubsub)

        metadata = cls(
            cache=cache,
            engine=engine,
            environment=environment,
            executor=executor,
            fs=fs,
            git_hash=git_hash,
            point_e=point_e,
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
