from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.system import System
from ..models.unit_length import UnitLength
from ..types import UNSET, Unset

WO = TypeVar("WO", bound="fbx")


@attr.s(auto_attribs=True)
class fbx:
    """Autodesk Filmbox (FBX) format."""  # noqa: E501

    type: str = "fbx"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[WO], src_dict: Dict[str, Any]) -> WO:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        fbx = cls(
            type=type,
        )

        fbx.additional_properties = d
        return fbx

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


NK = TypeVar("NK", bound="gltf")


@attr.s(auto_attribs=True)
class gltf:
    """Binary glTF 2.0. We refer to this as glTF since that is how our customers refer to it, but this can also import binary glTF (glb)."""  # noqa: E501

    type: str = "gltf"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[NK], src_dict: Dict[str, Any]) -> NK:
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


UQ = TypeVar("UQ", bound="obj")


@attr.s(auto_attribs=True)
class obj:
    """Wavefront OBJ format."""  # noqa: E501

    coords: Union[Unset, System] = UNSET
    type: str = "obj"
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
            field_dict["coords"] = coords.to_dict()
        field_dict["type"] = type
        if units is not UNSET:
            field_dict["units"] = units

        return field_dict

    @classmethod
    def from_dict(cls: Type[UQ], src_dict: Dict[str, Any]) -> UQ:
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


QE = TypeVar("QE", bound="ply")


@attr.s(auto_attribs=True)
class ply:
    """The PLY Polygon File Format."""  # noqa: E501

    coords: Union[Unset, System] = UNSET
    type: str = "ply"
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
            field_dict["coords"] = coords.to_dict()
        field_dict["type"] = type
        if units is not UNSET:
            field_dict["units"] = units

        return field_dict

    @classmethod
    def from_dict(cls: Type[QE], src_dict: Dict[str, Any]) -> QE:
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


XH = TypeVar("XH", bound="sldprt")


@attr.s(auto_attribs=True)
class sldprt:
    """SolidWorks part (SLDPRT) format."""  # noqa: E501

    type: str = "sldprt"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[XH], src_dict: Dict[str, Any]) -> XH:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        sldprt = cls(
            type=type,
        )

        sldprt.additional_properties = d
        return sldprt

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


KT = TypeVar("KT", bound="step")


@attr.s(auto_attribs=True)
class step:
    """ISO 10303-21 (STEP) format."""  # noqa: E501

    type: str = "step"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[KT], src_dict: Dict[str, Any]) -> KT:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        step = cls(
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


BV = TypeVar("BV", bound="stl")


@attr.s(auto_attribs=True)
class stl:
    """*ST**ereo**L**ithography format."""  # noqa: E501

    coords: Union[Unset, System] = UNSET
    type: str = "stl"
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
            field_dict["coords"] = coords.to_dict()
        field_dict["type"] = type
        if units is not UNSET:
            field_dict["units"] = units

        return field_dict

    @classmethod
    def from_dict(cls: Type[BV], src_dict: Dict[str, Any]) -> BV:
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


GY = TypeVar("GY", bound="InputFormat")


@attr.s(auto_attribs=True)
class InputFormat:

    """Input format specifier."""

    type: Union[
        fbx,
        gltf,
        obj,
        ply,
        sldprt,
        step,
        stl,
    ]

    def __init__(
        self,
        type: Union[
            fbx,
            gltf,
            obj,
            ply,
            sldprt,
            step,
            stl,
        ],
    ):
        self.type = type

    def to_dict(self) -> Dict[str, Any]:
        if isinstance(self.type, fbx):
            GU: fbx = self.type
            return GU.to_dict()
        elif isinstance(self.type, gltf):
            UP: gltf = self.type
            return UP.to_dict()
        elif isinstance(self.type, obj):
            DJ: obj = self.type
            return DJ.to_dict()
        elif isinstance(self.type, ply):
            TR: ply = self.type
            return TR.to_dict()
        elif isinstance(self.type, sldprt):
            JF: sldprt = self.type
            return JF.to_dict()
        elif isinstance(self.type, step):
            EL: step = self.type
            return EL.to_dict()
        elif isinstance(self.type, stl):
            LF: stl = self.type
            return LF.to_dict()

        raise Exception("Unknown type")

    @classmethod
    def from_dict(cls: Type[GY], d: Dict[str, Any]) -> GY:
        if d.get("type") == "fbx":
            SS: fbx = fbx()
            SS.from_dict(d)
            return cls(type=SS)
        elif d.get("type") == "gltf":
            AZ: gltf = gltf()
            AZ.from_dict(d)
            return cls(type=AZ)
        elif d.get("type") == "obj":
            WJ: obj = obj()
            WJ.from_dict(d)
            return cls(type=WJ)
        elif d.get("type") == "ply":
            YD: ply = ply()
            YD.from_dict(d)
            return cls(type=YD)
        elif d.get("type") == "sldprt":
            VP: sldprt = sldprt()
            VP.from_dict(d)
            return cls(type=VP)
        elif d.get("type") == "step":
            ZG: step = step()
            ZG.from_dict(d)
            return cls(type=ZG)
        elif d.get("type") == "stl":
            CS: stl = stl()
            CS.from_dict(d)
            return cls(type=CS)

        raise Exception("Unknown type")
