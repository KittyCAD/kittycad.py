from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

KW = TypeVar("KW", bound="default_scene")


@attr.s(auto_attribs=True)
class default_scene:
    """Visit the default scene."""  # noqa: E501

    type: str = "default_scene"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[KW], src_dict: Dict[str, Any]) -> KW:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        default_scene = cls(
            type=type,
        )

        default_scene.additional_properties = d
        return default_scene

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


HJ = TypeVar("HJ", bound="scene_by_index")


@attr.s(auto_attribs=True)
class scene_by_index:
    """Visit the indexed scene."""  # noqa: E501

    index: Union[Unset, int] = UNSET
    type: str = "scene_by_index"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        index = self.index
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[HJ], src_dict: Dict[str, Any]) -> HJ:
        d = src_dict.copy()
        index = d.pop("index", UNSET)

        type = d.pop("type", UNSET)

        scene_by_index = cls(
            index=index,
            type=type,
        )

        scene_by_index.additional_properties = d
        return scene_by_index

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


HA = TypeVar("HA", bound="scene_by_name")


@attr.s(auto_attribs=True)
class scene_by_name:
    """Visit the first scene with the given name."""  # noqa: E501

    name: Union[Unset, str] = UNSET
    type: str = "scene_by_name"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[HA], src_dict: Dict[str, Any]) -> HA:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        scene_by_name = cls(
            name=name,
            type=type,
        )

        scene_by_name.additional_properties = d
        return scene_by_name

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


ZM = TypeVar("ZM", bound="mesh_by_index")


@attr.s(auto_attribs=True)
class mesh_by_index:
    """Visit the indexed mesh."""  # noqa: E501

    index: Union[Unset, int] = UNSET
    type: str = "mesh_by_index"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        index = self.index
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[ZM], src_dict: Dict[str, Any]) -> ZM:
        d = src_dict.copy()
        index = d.pop("index", UNSET)

        type = d.pop("type", UNSET)

        mesh_by_index = cls(
            index=index,
            type=type,
        )

        mesh_by_index.additional_properties = d
        return mesh_by_index

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


BX = TypeVar("BX", bound="mesh_by_name")


@attr.s(auto_attribs=True)
class mesh_by_name:
    """Visit the first mesh with the given name."""  # noqa: E501

    name: Union[Unset, str] = UNSET
    type: str = "mesh_by_name"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[BX], src_dict: Dict[str, Any]) -> BX:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        mesh_by_name = cls(
            name=name,
            type=type,
        )

        mesh_by_name.additional_properties = d
        return mesh_by_name

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


GY = TypeVar("GY", bound="Selection")


@attr.s(auto_attribs=True)
class Selection:

    """Data item selection."""

    type: Union[
        default_scene,
        scene_by_index,
        scene_by_name,
        mesh_by_index,
        mesh_by_name,
    ]

    def __init__(
        self,
        type: Union[
            default_scene,
            scene_by_index,
            scene_by_name,
            mesh_by_index,
            mesh_by_name,
        ],
    ):
        self.type = type

    def to_dict(self) -> Dict[str, Any]:
        if isinstance(self.type, default_scene):
            TD: default_scene = self.type
            return TD.to_dict()
        elif isinstance(self.type, scene_by_index):
            SQ: scene_by_index = self.type
            return SQ.to_dict()
        elif isinstance(self.type, scene_by_name):
            IL: scene_by_name = self.type
            return IL.to_dict()
        elif isinstance(self.type, mesh_by_index):
            YG: mesh_by_index = self.type
            return YG.to_dict()
        elif isinstance(self.type, mesh_by_name):
            ZE: mesh_by_name = self.type
            return ZE.to_dict()

        raise Exception("Unknown type")

    @classmethod
    def from_dict(cls: Type[GY], d: Dict[str, Any]) -> GY:
        if d.get("type") == "default_scene":
            NR: default_scene = default_scene()
            NR.from_dict(d)
            return cls(type=NR)
        elif d.get("type") == "scene_by_index":
            WV: scene_by_index = scene_by_index()
            WV.from_dict(d)
            return cls(type=WV)
        elif d.get("type") == "scene_by_name":
            JT: scene_by_name = scene_by_name()
            JT.from_dict(d)
            return cls(type=JT)
        elif d.get("type") == "mesh_by_index":
            DD: mesh_by_index = mesh_by_index()
            DD.from_dict(d)
            return cls(type=DD)
        elif d.get("type") == "mesh_by_name":
            UI: mesh_by_name = mesh_by_name()
            UI.from_dict(d)
            return cls(type=UI)

        raise Exception("Unknown type")
