from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.fbx_storage import FbxStorage
from ..models.gltf_presentation import GltfPresentation
from ..models.gltf_storage import GltfStorage
from ..models.ply_storage import PlyStorage
from ..models.selection import Selection
from ..models.stl_storage import StlStorage
from ..models.system import System
from ..models.unit_length import UnitLength
from ..types import UNSET, Unset

DX = TypeVar("DX", bound="fbx")


@attr.s(auto_attribs=True)
class fbx:
    """Autodesk Filmbox (FBX) format."""  # noqa: E501

    storage: Union[Unset, FbxStorage] = UNSET
    type: str = "fbx"

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
    def from_dict(cls: Type[DX], src_dict: Dict[str, Any]) -> DX:
        d = src_dict.copy()
        _storage = d.pop("storage", UNSET)
        storage: Union[Unset, FbxStorage]
        if isinstance(_storage, Unset):
            storage = UNSET
        if _storage is None:
            storage = UNSET
        else:
            storage = _storage

        type = d.pop("type", UNSET)

        fbx = cls(
            storage=storage,
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


LH = TypeVar("LH", bound="gltf")


@attr.s(auto_attribs=True)
class gltf:
    """glTF 2.0. We refer to this as glTF since that is how our customers refer to it, although by default it will be in binary format and thus technically (glb). If you prefer ascii output, you can set that option for the export."""  # noqa: E501

    presentation: Union[Unset, GltfPresentation] = UNSET
    storage: Union[Unset, GltfStorage] = UNSET
    type: str = "gltf"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.presentation, Unset):
            presentation = self.presentation
        if not isinstance(self.storage, Unset):
            storage = self.storage
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if presentation is not UNSET:
            field_dict["presentation"] = presentation
        if storage is not UNSET:
            field_dict["storage"] = storage
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[LH], src_dict: Dict[str, Any]) -> LH:
        d = src_dict.copy()
        _presentation = d.pop("presentation", UNSET)
        presentation: Union[Unset, GltfPresentation]
        if isinstance(_presentation, Unset):
            presentation = UNSET
        if _presentation is None:
            presentation = UNSET
        else:
            presentation = _presentation

        _storage = d.pop("storage", UNSET)
        storage: Union[Unset, GltfStorage]
        if isinstance(_storage, Unset):
            storage = UNSET
        if _storage is None:
            storage = UNSET
        else:
            storage = _storage

        type = d.pop("type", UNSET)

        gltf = cls(
            presentation=presentation,
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


XA = TypeVar("XA", bound="obj")


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
    def from_dict(cls: Type[XA], src_dict: Dict[str, Any]) -> XA:
        d = src_dict.copy()
        _coords = d.pop("coords", UNSET)
        coords: Union[Unset, System]
        if isinstance(_coords, Unset):
            coords = UNSET
        if _coords is None:
            coords = UNSET
        else:
            coords = System.from_dict(_coords)

        type = d.pop("type", UNSET)

        _units = d.pop("units", UNSET)
        units: Union[Unset, UnitLength]
        if isinstance(_units, Unset):
            units = UNSET
        if _units is None:
            units = UNSET
        else:
            units = _units

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


QJ = TypeVar("QJ", bound="ply")


@attr.s(auto_attribs=True)
class ply:
    """The PLY Polygon File Format."""  # noqa: E501

    coords: Union[Unset, System] = UNSET
    selection: Union[Unset, Selection] = UNSET
    storage: Union[Unset, PlyStorage] = UNSET
    type: str = "ply"
    units: Union[Unset, UnitLength] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.coords, Unset):
            coords = self.coords
        if not isinstance(self.selection, Unset):
            selection = self.selection
        if not isinstance(self.storage, Unset):
            storage = self.storage
        type = self.type
        if not isinstance(self.units, Unset):
            units = self.units

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if coords is not UNSET:
            field_dict["coords"] = coords.to_dict()
        if selection is not UNSET:
            field_dict["selection"] = selection.to_dict()
        if storage is not UNSET:
            field_dict["storage"] = storage
        field_dict["type"] = type
        if units is not UNSET:
            field_dict["units"] = units

        return field_dict

    @classmethod
    def from_dict(cls: Type[QJ], src_dict: Dict[str, Any]) -> QJ:
        d = src_dict.copy()
        _coords = d.pop("coords", UNSET)
        coords: Union[Unset, System]
        if isinstance(_coords, Unset):
            coords = UNSET
        if _coords is None:
            coords = UNSET
        else:
            coords = System.from_dict(_coords)

        _selection = d.pop("selection", UNSET)
        selection: Union[Unset, Selection]
        if isinstance(_selection, Unset):
            selection = UNSET
        if _selection is None:
            selection = UNSET
        else:
            selection = Selection.from_dict(_selection)

        _storage = d.pop("storage", UNSET)
        storage: Union[Unset, PlyStorage]
        if isinstance(_storage, Unset):
            storage = UNSET
        if _storage is None:
            storage = UNSET
        else:
            storage = _storage

        type = d.pop("type", UNSET)

        _units = d.pop("units", UNSET)
        units: Union[Unset, UnitLength]
        if isinstance(_units, Unset):
            units = UNSET
        if _units is None:
            units = UNSET
        else:
            units = _units

        ply = cls(
            coords=coords,
            selection=selection,
            storage=storage,
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


ES = TypeVar("ES", bound="step")


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
            field_dict["coords"] = coords.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[ES], src_dict: Dict[str, Any]) -> ES:
        d = src_dict.copy()
        _coords = d.pop("coords", UNSET)
        coords: Union[Unset, System]
        if isinstance(_coords, Unset):
            coords = UNSET
        if _coords is None:
            coords = UNSET
        else:
            coords = System.from_dict(_coords)

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


AI = TypeVar("AI", bound="stl")


@attr.s(auto_attribs=True)
class stl:
    """*ST**ereo**L**ithography format."""  # noqa: E501

    coords: Union[Unset, System] = UNSET
    selection: Union[Unset, Selection] = UNSET
    storage: Union[Unset, StlStorage] = UNSET
    type: str = "stl"
    units: Union[Unset, UnitLength] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.coords, Unset):
            coords = self.coords
        if not isinstance(self.selection, Unset):
            selection = self.selection
        if not isinstance(self.storage, Unset):
            storage = self.storage
        type = self.type
        if not isinstance(self.units, Unset):
            units = self.units

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if coords is not UNSET:
            field_dict["coords"] = coords.to_dict()
        if selection is not UNSET:
            field_dict["selection"] = selection.to_dict()
        if storage is not UNSET:
            field_dict["storage"] = storage
        field_dict["type"] = type
        if units is not UNSET:
            field_dict["units"] = units

        return field_dict

    @classmethod
    def from_dict(cls: Type[AI], src_dict: Dict[str, Any]) -> AI:
        d = src_dict.copy()
        _coords = d.pop("coords", UNSET)
        coords: Union[Unset, System]
        if isinstance(_coords, Unset):
            coords = UNSET
        if _coords is None:
            coords = UNSET
        else:
            coords = System.from_dict(_coords)

        _selection = d.pop("selection", UNSET)
        selection: Union[Unset, Selection]
        if isinstance(_selection, Unset):
            selection = UNSET
        if _selection is None:
            selection = UNSET
        else:
            selection = Selection.from_dict(_selection)

        _storage = d.pop("storage", UNSET)
        storage: Union[Unset, StlStorage]
        if isinstance(_storage, Unset):
            storage = UNSET
        if _storage is None:
            storage = UNSET
        else:
            storage = _storage

        type = d.pop("type", UNSET)

        _units = d.pop("units", UNSET)
        units: Union[Unset, UnitLength]
        if isinstance(_units, Unset):
            units = UNSET
        if _units is None:
            units = UNSET
        else:
            units = _units

        stl = cls(
            coords=coords,
            selection=selection,
            storage=storage,
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


GY = TypeVar("GY", bound="OutputFormat")


@attr.s(auto_attribs=True)
class OutputFormat:

    """Output format specifier."""

    type: Union[
        fbx,
        gltf,
        obj,
        ply,
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
            step,
            stl,
        ],
    ):
        self.type = type

    def to_dict(self) -> Dict[str, Any]:
        if isinstance(self.type, fbx):
            MV: fbx = self.type
            return MV.to_dict()
        elif isinstance(self.type, gltf):
            NW: gltf = self.type
            return NW.to_dict()
        elif isinstance(self.type, obj):
            MR: obj = self.type
            return MR.to_dict()
        elif isinstance(self.type, ply):
            WG: ply = self.type
            return WG.to_dict()
        elif isinstance(self.type, step):
            DZ: step = self.type
            return DZ.to_dict()
        elif isinstance(self.type, stl):
            UC: stl = self.type
            return UC.to_dict()

        raise Exception("Unknown type")

    @classmethod
    def from_dict(cls: Type[GY], d: Dict[str, Any]) -> GY:
        if d.get("type") == "fbx":
            LU: fbx = fbx()
            LU.from_dict(d)
            return cls(type=LU)
        elif d.get("type") == "gltf":
            EH: gltf = gltf()
            EH.from_dict(d)
            return cls(type=EH)
        elif d.get("type") == "obj":
            MY: obj = obj()
            MY.from_dict(d)
            return cls(type=MY)
        elif d.get("type") == "ply":
            WC: ply = ply()
            WC.from_dict(d)
            return cls(type=WC)
        elif d.get("type") == "step":
            ZT: step = step()
            ZT.from_dict(d)
            return cls(type=ZT)
        elif d.get("type") == "stl":
            VZ: stl = stl()
            VZ.from_dict(d)
            return cls(type=VZ)

        raise Exception("Unknown type")
