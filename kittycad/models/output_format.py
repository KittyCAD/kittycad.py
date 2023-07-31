from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.storage import Storage
from ..models.system import System
from ..types import UNSET, Unset

F = TypeVar("F", bound="Gltf")


@attr.s(auto_attribs=True)
class Gltf:
    """glTF 2.0. We refer to this as glTF since that is how our customers refer to it, although by default it will be in binary format and thus technically (glb). If you prefer ascii output, you can set that option for the export."""  # noqa: E501

    storage: Union[Unset, Storage] = UNSET
    type: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.storage, Unset):
            storage = self.storage
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if storage is not UNSET:
            field_dict["storage"] = storage
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[F], src_dict: Dict[str, Any]) -> F:
        d = src_dict.copy()
        _storage = d.pop("storage", UNSET)
        storage: Union[Unset, Storage]
        if isinstance(_storage, Unset):
            storage = UNSET
        else:
            storage = _storage  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        gltf = cls(
            storage=storage,
            type=type,
        )

        gltf.additional_properties = d
        return gltf

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


Z = TypeVar("Z", bound="Obj")


@attr.s(auto_attribs=True)
class Obj:
    """Wavefront OBJ format."""  # noqa: E501

    coords: Union[Unset, System] = UNSET
    type: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.coords, Unset):
            coords = self.coords
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if coords is not UNSET:
            field_dict["coords"] = coords
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[Z], src_dict: Dict[str, Any]) -> Z:
        d = src_dict.copy()
        _coords = d.pop("coords", UNSET)
        coords: Union[Unset, System]
        if isinstance(_coords, Unset):
            coords = UNSET
        else:
            coords = System(_coords)

        type = d.pop("type", UNSET)

        obj = cls(
            coords=coords,
            type=type,
        )

        obj.additional_properties = d
        return obj

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


G = TypeVar("G", bound="Ply")


@attr.s(auto_attribs=True)
class Ply:
    """The PLY Polygon File Format."""  # noqa: E501

    coords: Union[Unset, System] = UNSET
    storage: Union[Unset, Storage] = UNSET
    type: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.coords, Unset):
            coords = self.coords
        if not isinstance(self.storage, Unset):
            storage = self.storage
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if coords is not UNSET:
            field_dict["coords"] = coords
        if storage is not UNSET:
            field_dict["storage"] = storage
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[G], src_dict: Dict[str, Any]) -> G:
        d = src_dict.copy()
        _coords = d.pop("coords", UNSET)
        coords: Union[Unset, System]
        if isinstance(_coords, Unset):
            coords = UNSET
        else:
            coords = System(_coords)

        _storage = d.pop("storage", UNSET)
        storage: Union[Unset, Storage]
        if isinstance(_storage, Unset):
            storage = UNSET
        else:
            storage = _storage  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        ply = cls(
            coords=coords,
            storage=storage,
            type=type,
        )

        ply.additional_properties = d
        return ply

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


L = TypeVar("L", bound="Step")


@attr.s(auto_attribs=True)
class Step:
    """ISO 10303-21 (STEP) format."""  # noqa: E501

    coords: Union[Unset, System] = UNSET
    type: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.coords, Unset):
            coords = self.coords
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if coords is not UNSET:
            field_dict["coords"] = coords
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[L], src_dict: Dict[str, Any]) -> L:
        d = src_dict.copy()
        _coords = d.pop("coords", UNSET)
        coords: Union[Unset, System]
        if isinstance(_coords, Unset):
            coords = UNSET
        else:
            coords = System(_coords)

        type = d.pop("type", UNSET)

        step = cls(
            coords=coords,
            type=type,
        )

        step.additional_properties = d
        return step

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


N = TypeVar("N", bound="Stl")


@attr.s(auto_attribs=True)
class Stl:
    """*ST**ereo**L**ithography format."""  # noqa: E501

    coords: Union[Unset, System] = UNSET
    storage: Union[Unset, Storage] = UNSET
    type: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.coords, Unset):
            coords = self.coords
        if not isinstance(self.storage, Unset):
            storage = self.storage
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if coords is not UNSET:
            field_dict["coords"] = coords
        if storage is not UNSET:
            field_dict["storage"] = storage
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[N], src_dict: Dict[str, Any]) -> N:
        d = src_dict.copy()
        _coords = d.pop("coords", UNSET)
        coords: Union[Unset, System]
        if isinstance(_coords, Unset):
            coords = UNSET
        else:
            coords = System(_coords)

        _storage = d.pop("storage", UNSET)
        storage: Union[Unset, Storage]
        if isinstance(_storage, Unset):
            storage = UNSET
        else:
            storage = _storage  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        stl = cls(
            coords=coords,
            storage=storage,
            type=type,
        )

        stl.additional_properties = d
        return stl

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


OutputFormat = Union[Gltf, Obj, Ply, Step, Stl]
