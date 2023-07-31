from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.system import System
from ..models.unit_length import UnitLength
from ..types import UNSET, Unset

ET = TypeVar("ET", bound="Gltf")


@attr.s(auto_attribs=True)
class Gltf:
    """Binary glTF 2.0. We refer to this as glTF since that is how our customers refer to it, but this can also import binary glTF (glb)."""  # noqa: E501

    type: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[ET], src_dict: Dict[str, Any]) -> ET:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        gltf = cls(
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


QF = TypeVar("QF", bound="Step")


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
    def from_dict(cls: Type[QF], src_dict: Dict[str, Any]) -> QF:
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


DI = TypeVar("DI", bound="Obj")


@attr.s(auto_attribs=True)
class Obj:
    """Wavefront OBJ format."""  # noqa: E501

    coords: Union[Unset, System] = UNSET
    type: Union[Unset, str] = UNSET
    units: Union[Unset, UnitLength] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.coords, Unset):
            coords = self.coords
        type = self.type
        if not isinstance(self.units, Unset):
            units = self.units

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if coords is not UNSET:
            field_dict["coords"] = coords
        if type is not UNSET:
            field_dict["type"] = type
        if units is not UNSET:
            field_dict["units"] = units

        return field_dict

    @classmethod
    def from_dict(cls: Type[DI], src_dict: Dict[str, Any]) -> DI:
        d = src_dict.copy()
        _coords = d.pop("coords", UNSET)
        coords: Union[Unset, System]
        if isinstance(_coords, Unset):
            coords = UNSET
        else:
            coords = _coords  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        _units = d.pop("units", UNSET)
        units: Union[Unset, UnitLength]
        if isinstance(_units, Unset):
            units = UNSET
        else:
            units = _units  # type: ignore[arg-type]

        obj = cls(
            coords=coords,
            type=type,
            units=units,
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


OJ = TypeVar("OJ", bound="Ply")


@attr.s(auto_attribs=True)
class Ply:
    """The PLY Polygon File Format."""  # noqa: E501

    coords: Union[Unset, System] = UNSET
    type: Union[Unset, str] = UNSET
    units: Union[Unset, UnitLength] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.coords, Unset):
            coords = self.coords
        type = self.type
        if not isinstance(self.units, Unset):
            units = self.units

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if coords is not UNSET:
            field_dict["coords"] = coords
        if type is not UNSET:
            field_dict["type"] = type
        if units is not UNSET:
            field_dict["units"] = units

        return field_dict

    @classmethod
    def from_dict(cls: Type[OJ], src_dict: Dict[str, Any]) -> OJ:
        d = src_dict.copy()
        _coords = d.pop("coords", UNSET)
        coords: Union[Unset, System]
        if isinstance(_coords, Unset):
            coords = UNSET
        else:
            coords = _coords  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        _units = d.pop("units", UNSET)
        units: Union[Unset, UnitLength]
        if isinstance(_units, Unset):
            units = UNSET
        else:
            units = _units  # type: ignore[arg-type]

        ply = cls(
            coords=coords,
            type=type,
            units=units,
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


UF = TypeVar("UF", bound="Stl")


@attr.s(auto_attribs=True)
class Stl:
    """*ST**ereo**L**ithography format."""  # noqa: E501

    coords: Union[Unset, System] = UNSET
    type: Union[Unset, str] = UNSET
    units: Union[Unset, UnitLength] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.coords, Unset):
            coords = self.coords
        type = self.type
        if not isinstance(self.units, Unset):
            units = self.units

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if coords is not UNSET:
            field_dict["coords"] = coords
        if type is not UNSET:
            field_dict["type"] = type
        if units is not UNSET:
            field_dict["units"] = units

        return field_dict

    @classmethod
    def from_dict(cls: Type[UF], src_dict: Dict[str, Any]) -> UF:
        d = src_dict.copy()
        _coords = d.pop("coords", UNSET)
        coords: Union[Unset, System]
        if isinstance(_coords, Unset):
            coords = UNSET
        else:
            coords = _coords  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        _units = d.pop("units", UNSET)
        units: Union[Unset, UnitLength]
        if isinstance(_units, Unset):
            units = UNSET
        else:
            units = _units  # type: ignore[arg-type]

        stl = cls(
            coords=coords,
            type=type,
            units=units,
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


InputFormat = Union[Gltf, Step, Obj, Ply, Stl]
