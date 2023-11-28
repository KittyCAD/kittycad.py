from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

AE = TypeVar("AE", bound="default_scene")


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
    def from_dict(cls: Type[AE], src_dict: Dict[str, Any]) -> AE:
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


AD = TypeVar("AD", bound="scene_by_index")


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
    def from_dict(cls: Type[AD], src_dict: Dict[str, Any]) -> AD:
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


AB = TypeVar("AB", bound="scene_by_name")


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
    def from_dict(cls: Type[AB], src_dict: Dict[str, Any]) -> AB:
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


VY = TypeVar("VY", bound="mesh_by_index")


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
    def from_dict(cls: Type[VY], src_dict: Dict[str, Any]) -> VY:
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


DW = TypeVar("DW", bound="mesh_by_name")


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
    def from_dict(cls: Type[DW], src_dict: Dict[str, Any]) -> DW:
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


Selection = Union[
    default_scene, scene_by_index, scene_by_name, mesh_by_index, mesh_by_name
]
