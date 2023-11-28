from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from typing_extensions import Self

from ..models.fbx_storage import FbxStorage
from ..models.gltf_presentation import GltfPresentation
from ..models.gltf_storage import GltfStorage
from ..models.ply_storage import PlyStorage
from ..models.selection import Selection
from ..models.stl_storage import StlStorage
from ..models.system import System
from ..models.unit_length import UnitLength
from ..types import UNSET, Unset

UJ = TypeVar("UJ", bound="fbx")


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
    def from_dict(cls: Type[UJ], src_dict: Dict[str, Any]) -> UJ:
        d = src_dict.copy()
        _storage = d.pop("storage", UNSET)
        storage: Union[Unset, FbxStorage]
        if isinstance(_storage, Unset):
            storage = UNSET
        else:
            storage = _storage  # type: ignore[arg-type]

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


RU = TypeVar("RU", bound="gltf")


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
    def from_dict(cls: Type[RU], src_dict: Dict[str, Any]) -> RU:
        d = src_dict.copy()
        _presentation = d.pop("presentation", UNSET)
        presentation: Union[Unset, GltfPresentation]
        if isinstance(_presentation, Unset):
            presentation = UNSET
        else:
            presentation = _presentation  # type: ignore[arg-type]

        _storage = d.pop("storage", UNSET)
        storage: Union[Unset, GltfStorage]
        if isinstance(_storage, Unset):
            storage = UNSET
        else:
            storage = _storage  # type: ignore[arg-type]

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


DL = TypeVar("DL", bound="obj")


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
    def from_dict(cls: Type[DL], src_dict: Dict[str, Any]) -> DL:
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


QT = TypeVar("QT", bound="ply")


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
    def from_dict(cls: Type[QT], src_dict: Dict[str, Any]) -> QT:
        d = src_dict.copy()
        _coords = d.pop("coords", UNSET)
        coords: Union[Unset, System]
        if isinstance(_coords, Unset):
            coords = UNSET
        else:
            coords = _coords  # type: ignore[arg-type]

        _selection = d.pop("selection", UNSET)
        selection: Union[Unset, Selection]
        if isinstance(_selection, Unset):
            selection = UNSET
        else:
            selection = _selection  # type: ignore[arg-type]

        _storage = d.pop("storage", UNSET)
        storage: Union[Unset, PlyStorage]
        if isinstance(_storage, Unset):
            storage = UNSET
        else:
            storage = _storage  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        _units = d.pop("units", UNSET)
        units: Union[Unset, UnitLength]
        if isinstance(_units, Unset):
            units = UNSET
        else:
            units = _units  # type: ignore[arg-type]

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


PT = TypeVar("PT", bound="step")


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
    def from_dict(cls: Type[PT], src_dict: Dict[str, Any]) -> PT:
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


HR = TypeVar("HR", bound="stl")


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
    def from_dict(cls: Type[HR], src_dict: Dict[str, Any]) -> HR:
        d = src_dict.copy()
        _coords = d.pop("coords", UNSET)
        coords: Union[Unset, System]
        if isinstance(_coords, Unset):
            coords = UNSET
        else:
            coords = _coords  # type: ignore[arg-type]

        _selection = d.pop("selection", UNSET)
        selection: Union[Unset, Selection]
        if isinstance(_selection, Unset):
            selection = UNSET
        else:
            selection = _selection  # type: ignore[arg-type]

        _storage = d.pop("storage", UNSET)
        storage: Union[Unset, StlStorage]
        if isinstance(_storage, Unset):
            storage = UNSET
        else:
            storage = _storage  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        _units = d.pop("units", UNSET)
        units: Union[Unset, UnitLength]
        if isinstance(_units, Unset):
            units = UNSET
        else:
            units = _units  # type: ignore[arg-type]

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


class OutputFormat:

    """Output format specifier."""

    type: Union[
        fbx,
        gltf,
        obj,
        ply,
        step,
        stl,
    ] = None

    def __init__(
        self,
        type: Union[
            type(fbx),
            type(gltf),
            type(obj),
            type(ply),
            type(step),
            type(stl),
        ],
    ):
        self.type = type

    def to_dict(self) -> Dict[str, Any]:
        if isinstance(self.type, fbx):
            n: fbx = self.type
            return n.to_dict()
        elif isinstance(self.type, gltf):
            n: gltf = self.type
            return n.to_dict()
        elif isinstance(self.type, obj):
            n: obj = self.type
            return n.to_dict()
        elif isinstance(self.type, ply):
            n: ply = self.type
            return n.to_dict()
        elif isinstance(self.type, step):
            n: step = self.type
            return n.to_dict()
        elif isinstance(self.type, stl):
            n: stl = self.type
            return n.to_dict()

        raise Exception("Unknown type")

    def from_dict(self, d) -> Self:
        if d.get("type") == "fbx":
            n: fbx = fbx()
            n.from_dict(d)
            self.type = n
            return Self
        elif d.get("type") == "gltf":
            n: gltf = gltf()
            n.from_dict(d)
            self.type = n
            return self
        elif d.get("type") == "obj":
            n: obj = obj()
            n.from_dict(d)
            self.type = n
            return self
        elif d.get("type") == "ply":
            n: ply = ply()
            n.from_dict(d)
            self.type = n
            return self
        elif d.get("type") == "step":
            n: step = step()
            n.from_dict(d)
            self.type = n
            return self
        elif d.get("type") == "stl":
            n: stl = stl()
            n.from_dict(d)
            self.type = n
            return self

        raise Exception("Unknown type")
