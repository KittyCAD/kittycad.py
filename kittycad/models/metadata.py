from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.engine_metadata import EngineMetadata
from ..models.file_system_metadata import FileSystemMetadata
from ..models.nats_connection import NatsConnection
from ..types import UNSET, Unset

T = TypeVar("T", bound="Metadata")


@attr.s(auto_attribs=True)
class Metadata:
    """ """
    engine: Union[Unset, EngineMetadata] = UNSET
    fs: Union[Unset, FileSystemMetadata] = UNSET
    git_hash: Union[Unset, str] = UNSET
    nats: Union[Unset, NatsConnection] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        engine: Union[Unset, str] = UNSET
        if not isinstance(self.engine, Unset):
            engine = self.engine.value
        fs: Union[Unset, str] = UNSET
        if not isinstance(self.fs, Unset):
            fs = self.fs.value
        git_hash = self.git_hash
        nats: Union[Unset, str] = UNSET
        if not isinstance(self.nats, Unset):
            nats = self.nats.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if engine is not UNSET:
            field_dict['engine'] = engine
        if fs is not UNSET:
            field_dict['fs'] = fs
        if git_hash is not UNSET:
            field_dict['git_hash'] = git_hash
        if nats is not UNSET:
            field_dict['nats'] = nats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _engine = d.pop("engine", UNSET)
        engine: Union[Unset, EngineMetadata]
        if isinstance(_engine, Unset):
            engine = UNSET
        else:
            engine = EngineMetadata(_engine)

        _fs = d.pop("fs", UNSET)
        fs: Union[Unset, FileSystemMetadata]
        if isinstance(_fs, Unset):
            fs = UNSET
        else:
            fs = FileSystemMetadata(_fs)

        git_hash = d.pop("git_hash", UNSET)

        _nats = d.pop("nats", UNSET)
        nats: Union[Unset, NatsConnection]
        if isinstance(_nats, Unset):
            nats = UNSET
        else:
            nats = NatsConnection(_nats)

        metadata = cls(
            engine=engine,
            fs=fs,
            git_hash=git_hash,
            nats=nats,
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
