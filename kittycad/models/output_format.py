from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.storage import Storage
from ..models.system import System
from ..types import UNSET, Unset

IM = TypeVar("IM", bound="gltf")


@attr.s(auto_attribs=True)
class gltf:
    """glTF 2.0. We refer to this as glTF since that is how our customers refer to it, although by default it will be in binary format and thus technically (glb). If you prefer ascii output, you can set that option for the export."""  # noqa: E501

    storage: Union[Unset, Storage] = UNSET
    type: str = "gltf"

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
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[IM], src_dict: Dict[str, Any]) -> IM:
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


OU = TypeVar("OU", bound="obj")


@attr.s(auto_attribs=True)
class obj:
    """Wavefront OBJ format."""  # noqa: E501

    coords: Union[Unset, System] = UNSET
    type: str = "obj"

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
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[OU], src_dict: Dict[str, Any]) -> OU:
        d = src_dict.copy()
        _coords = d.pop("coords", UNSET)
        coords: Union[Unset, System]
        if isinstance(_coords, Unset):
            coords = UNSET
        else:
            coords = _coords  # type: ignore[arg-type]

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


KL = TypeVar("KL", bound="ply")


@attr.s(auto_attribs=True)
class ply:
    """The PLY Polygon File Format."""  # noqa: E501

    coords: Union[Unset, System] = UNSET
    storage: Union[Unset, Storage] = UNSET
    type: str = "ply"

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
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[KL], src_dict: Dict[str, Any]) -> KL:
        d = src_dict.copy()
        _coords = d.pop("coords", UNSET)
        coords: Union[Unset, System]
        if isinstance(_coords, Unset):
            coords = UNSET
        else:
            coords = _coords  # type: ignore[arg-type]

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


XI = TypeVar("XI", bound="step")


@attr.s(auto_attribs=True)
class step:
    """ISO 10303-21 (STEP) format."""  # noqa: E501

    coords: Union[Unset, System] = UNSET
    type: str = "step"

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
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[XI], src_dict: Dict[str, Any]) -> XI:
        d = src_dict.copy()
        _coords = d.pop("coords", UNSET)
        coords: Union[Unset, System]
        if isinstance(_coords, Unset):
            coords = UNSET
        else:
            coords = _coords  # type: ignore[arg-type]

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


PO = TypeVar("PO", bound="stl")


@attr.s(auto_attribs=True)
class stl:
    """*ST**ereo**L**ithography format."""  # noqa: E501

    coords: Union[Unset, System] = UNSET
    storage: Union[Unset, Storage] = UNSET
    type: str = "stl"

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
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[PO], src_dict: Dict[str, Any]) -> PO:
        d = src_dict.copy()
        _coords = d.pop("coords", UNSET)
        coords: Union[Unset, System]
        if isinstance(_coords, Unset):
            coords = UNSET
        else:
            coords = _coords  # type: ignore[arg-type]

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


OutputFormat = Union[gltf, obj, ply, step, stl]
