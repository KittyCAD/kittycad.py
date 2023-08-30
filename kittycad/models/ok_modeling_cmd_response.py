from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.curve_get_control_points import CurveGetControlPoints
from ..models.curve_get_type import CurveGetType
from ..models.entity_get_all_child_uuids import EntityGetAllChildUuids
from ..models.entity_get_child_uuid import EntityGetChildUuid
from ..models.entity_get_num_children import EntityGetNumChildren
from ..models.entity_get_parent_id import EntityGetParentId
from ..models.export import Export
from ..models.get_entity_type import GetEntityType
from ..models.highlight_set_entity import HighlightSetEntity
from ..models.mouse_click import MouseClick
from ..models.path_get_info import PathGetInfo
from ..models.select_get import SelectGet
from ..models.select_with_point import SelectWithPoint
from ..models.solid3d_get_all_edge_faces import Solid3dGetAllEdgeFaces
from ..models.solid3d_get_all_opposite_edges import Solid3dGetAllOppositeEdges
from ..models.solid3d_get_next_adjacent_edge import Solid3dGetNextAdjacentEdge
from ..models.solid3d_get_opposite_edge import Solid3dGetOppositeEdge
from ..models.solid3d_get_prev_adjacent_edge import Solid3dGetPrevAdjacentEdge
from ..models.take_snapshot import TakeSnapshot
from ..types import UNSET, Unset

SK = TypeVar("SK", bound="empty")


@attr.s(auto_attribs=True)
class empty:
    """An empty response, used for any command that does not explicitly have a response defined here."""  # noqa: E501

    type: str = "empty"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[SK], src_dict: Dict[str, Any]) -> SK:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        empty = cls(
            type=type,
        )

        empty.additional_properties = d
        return empty

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


UK = TypeVar("UK", bound="export")


@attr.s(auto_attribs=True)
class export:
    """The response from the `Export` command. When this is being performed over a websocket, this is sent as binary not JSON. The binary data can be deserialized as `bincode` into a `Vec<ExportFile>`."""  # noqa: E501

    data: Union[Unset, Export] = UNSET
    type: str = "export"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[UK], src_dict: Dict[str, Any]) -> UK:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, Export]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = _data  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        export = cls(
            data=data,
            type=type,
        )

        export.additional_properties = d
        return export

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


CX = TypeVar("CX", bound="select_with_point")


@attr.s(auto_attribs=True)
class select_with_point:
    """The response from the `SelectWithPoint` command."""  # noqa: E501

    data: Union[Unset, SelectWithPoint] = UNSET
    type: str = "select_with_point"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[CX], src_dict: Dict[str, Any]) -> CX:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, SelectWithPoint]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = _data  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        select_with_point = cls(
            data=data,
            type=type,
        )

        select_with_point.additional_properties = d
        return select_with_point

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


MT = TypeVar("MT", bound="highlight_set_entity")


@attr.s(auto_attribs=True)
class highlight_set_entity:
    """The response from the `HighlightSetEntity` command."""  # noqa: E501

    data: Union[Unset, HighlightSetEntity] = UNSET
    type: str = "highlight_set_entity"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[MT], src_dict: Dict[str, Any]) -> MT:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, HighlightSetEntity]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = _data  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        highlight_set_entity = cls(
            data=data,
            type=type,
        )

        highlight_set_entity.additional_properties = d
        return highlight_set_entity

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


LJ = TypeVar("LJ", bound="entity_get_child_uuid")


@attr.s(auto_attribs=True)
class entity_get_child_uuid:
    """The response from the `EntityGetChildUuid` command."""  # noqa: E501

    data: Union[Unset, EntityGetChildUuid] = UNSET
    type: str = "entity_get_child_uuid"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[LJ], src_dict: Dict[str, Any]) -> LJ:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, EntityGetChildUuid]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = _data  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        entity_get_child_uuid = cls(
            data=data,
            type=type,
        )

        entity_get_child_uuid.additional_properties = d
        return entity_get_child_uuid

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


TF = TypeVar("TF", bound="entity_get_num_children")


@attr.s(auto_attribs=True)
class entity_get_num_children:
    """The response from the `EntityGetNumChildren` command."""  # noqa: E501

    data: Union[Unset, EntityGetNumChildren] = UNSET
    type: str = "entity_get_num_children"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[TF], src_dict: Dict[str, Any]) -> TF:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, EntityGetNumChildren]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = _data  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        entity_get_num_children = cls(
            data=data,
            type=type,
        )

        entity_get_num_children.additional_properties = d
        return entity_get_num_children

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


HF = TypeVar("HF", bound="entity_get_parent_id")


@attr.s(auto_attribs=True)
class entity_get_parent_id:
    """The response from the `EntityGetParentId` command."""  # noqa: E501

    data: Union[Unset, EntityGetParentId] = UNSET
    type: str = "entity_get_parent_id"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[HF], src_dict: Dict[str, Any]) -> HF:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, EntityGetParentId]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = _data  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        entity_get_parent_id = cls(
            data=data,
            type=type,
        )

        entity_get_parent_id.additional_properties = d
        return entity_get_parent_id

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


JD = TypeVar("JD", bound="entity_get_all_child_uuids")


@attr.s(auto_attribs=True)
class entity_get_all_child_uuids:
    """The response from the `EntityGetAllChildUuids` command."""  # noqa: E501

    data: Union[Unset, EntityGetAllChildUuids] = UNSET
    type: str = "entity_get_all_child_uuids"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[JD], src_dict: Dict[str, Any]) -> JD:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, EntityGetAllChildUuids]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = _data  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        entity_get_all_child_uuids = cls(
            data=data,
            type=type,
        )

        entity_get_all_child_uuids.additional_properties = d
        return entity_get_all_child_uuids

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


RZ = TypeVar("RZ", bound="select_get")


@attr.s(auto_attribs=True)
class select_get:
    """The response from the `SelectGet` command."""  # noqa: E501

    data: Union[Unset, SelectGet] = UNSET
    type: str = "select_get"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[RZ], src_dict: Dict[str, Any]) -> RZ:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, SelectGet]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = _data  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        select_get = cls(
            data=data,
            type=type,
        )

        select_get.additional_properties = d
        return select_get

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


BH = TypeVar("BH", bound="get_entity_type")


@attr.s(auto_attribs=True)
class get_entity_type:
    """The response from the `GetEntityType` command."""  # noqa: E501

    data: Union[Unset, GetEntityType] = UNSET
    type: str = "get_entity_type"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[BH], src_dict: Dict[str, Any]) -> BH:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, GetEntityType]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = _data  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        get_entity_type = cls(
            data=data,
            type=type,
        )

        get_entity_type.additional_properties = d
        return get_entity_type

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


SX = TypeVar("SX", bound="solid3d_get_all_edge_faces")


@attr.s(auto_attribs=True)
class solid3d_get_all_edge_faces:
    """The response from the `Solid3dGetAllEdgeFaces` command."""  # noqa: E501

    data: Union[Unset, Solid3dGetAllEdgeFaces] = UNSET
    type: str = "solid3d_get_all_edge_faces"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[SX], src_dict: Dict[str, Any]) -> SX:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, Solid3dGetAllEdgeFaces]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = _data  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        solid3d_get_all_edge_faces = cls(
            data=data,
            type=type,
        )

        solid3d_get_all_edge_faces.additional_properties = d
        return solid3d_get_all_edge_faces

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


CN = TypeVar("CN", bound="solid3d_get_all_opposite_edges")


@attr.s(auto_attribs=True)
class solid3d_get_all_opposite_edges:
    """The response from the `Solid3dGetAllOppositeEdges` command."""  # noqa: E501

    data: Union[Unset, Solid3dGetAllOppositeEdges] = UNSET
    type: str = "solid3d_get_all_opposite_edges"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[CN], src_dict: Dict[str, Any]) -> CN:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, Solid3dGetAllOppositeEdges]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = _data  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        solid3d_get_all_opposite_edges = cls(
            data=data,
            type=type,
        )

        solid3d_get_all_opposite_edges.additional_properties = d
        return solid3d_get_all_opposite_edges

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


GS = TypeVar("GS", bound="solid3d_get_opposite_edge")


@attr.s(auto_attribs=True)
class solid3d_get_opposite_edge:
    """The response from the `Solid3dGetOppositeEdge` command."""  # noqa: E501

    data: Union[Unset, Solid3dGetOppositeEdge] = UNSET
    type: str = "solid3d_get_opposite_edge"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[GS], src_dict: Dict[str, Any]) -> GS:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, Solid3dGetOppositeEdge]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = _data  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        solid3d_get_opposite_edge = cls(
            data=data,
            type=type,
        )

        solid3d_get_opposite_edge.additional_properties = d
        return solid3d_get_opposite_edge

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


SO = TypeVar("SO", bound="solid3d_get_prev_adjacent_edge")


@attr.s(auto_attribs=True)
class solid3d_get_prev_adjacent_edge:
    """The response from the `Solid3dGetPrevAdjacentEdge` command."""  # noqa: E501

    data: Union[Unset, Solid3dGetPrevAdjacentEdge] = UNSET
    type: str = "solid3d_get_prev_adjacent_edge"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[SO], src_dict: Dict[str, Any]) -> SO:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, Solid3dGetPrevAdjacentEdge]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = _data  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        solid3d_get_prev_adjacent_edge = cls(
            data=data,
            type=type,
        )

        solid3d_get_prev_adjacent_edge.additional_properties = d
        return solid3d_get_prev_adjacent_edge

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


ZS = TypeVar("ZS", bound="solid3d_get_next_adjacent_edge")


@attr.s(auto_attribs=True)
class solid3d_get_next_adjacent_edge:
    """The response from the `Solid3dGetNextAdjacentEdge` command."""  # noqa: E501

    data: Union[Unset, Solid3dGetNextAdjacentEdge] = UNSET
    type: str = "solid3d_get_next_adjacent_edge"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[ZS], src_dict: Dict[str, Any]) -> ZS:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, Solid3dGetNextAdjacentEdge]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = _data  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        solid3d_get_next_adjacent_edge = cls(
            data=data,
            type=type,
        )

        solid3d_get_next_adjacent_edge.additional_properties = d
        return solid3d_get_next_adjacent_edge

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


AM = TypeVar("AM", bound="mouse_click")


@attr.s(auto_attribs=True)
class mouse_click:
    """The response from the `MouseClick` command."""  # noqa: E501

    data: Union[Unset, MouseClick] = UNSET
    type: str = "mouse_click"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[AM], src_dict: Dict[str, Any]) -> AM:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, MouseClick]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = _data  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        mouse_click = cls(
            data=data,
            type=type,
        )

        mouse_click.additional_properties = d
        return mouse_click

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


GK = TypeVar("GK", bound="curve_get_type")


@attr.s(auto_attribs=True)
class curve_get_type:
    """The response from the `CurveGetType` command."""  # noqa: E501

    data: Union[Unset, CurveGetType] = UNSET
    type: str = "curve_get_type"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[GK], src_dict: Dict[str, Any]) -> GK:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, CurveGetType]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = _data  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        curve_get_type = cls(
            data=data,
            type=type,
        )

        curve_get_type.additional_properties = d
        return curve_get_type

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


SG = TypeVar("SG", bound="curve_get_control_points")


@attr.s(auto_attribs=True)
class curve_get_control_points:
    """The response from the `CurveGetControlPoints` command."""  # noqa: E501

    data: Union[Unset, CurveGetControlPoints] = UNSET
    type: str = "curve_get_control_points"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[SG], src_dict: Dict[str, Any]) -> SG:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, CurveGetControlPoints]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = _data  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        curve_get_control_points = cls(
            data=data,
            type=type,
        )

        curve_get_control_points.additional_properties = d
        return curve_get_control_points

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


QZ = TypeVar("QZ", bound="take_snapshot")


@attr.s(auto_attribs=True)
class take_snapshot:
    """The response from the `Take Snapshot` command."""  # noqa: E501

    data: Union[Unset, TakeSnapshot] = UNSET
    type: str = "take_snapshot"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[QZ], src_dict: Dict[str, Any]) -> QZ:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, TakeSnapshot]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = _data  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        take_snapshot = cls(
            data=data,
            type=type,
        )

        take_snapshot.additional_properties = d
        return take_snapshot

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


SY = TypeVar("SY", bound="path_get_info")


@attr.s(auto_attribs=True)
class path_get_info:
    """The response from the `Path Get Info` command."""  # noqa: E501

    data: Union[Unset, PathGetInfo] = UNSET
    type: str = "path_get_info"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[SY], src_dict: Dict[str, Any]) -> SY:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, PathGetInfo]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = _data  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        path_get_info = cls(
            data=data,
            type=type,
        )

        path_get_info.additional_properties = d
        return path_get_info

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


OkModelingCmdResponse = Union[
    empty,
    export,
    select_with_point,
    highlight_set_entity,
    entity_get_child_uuid,
    entity_get_num_children,
    entity_get_parent_id,
    entity_get_all_child_uuids,
    select_get,
    get_entity_type,
    solid3d_get_all_edge_faces,
    solid3d_get_all_opposite_edges,
    solid3d_get_opposite_edge,
    solid3d_get_prev_adjacent_edge,
    solid3d_get_next_adjacent_edge,
    mouse_click,
    curve_get_type,
    curve_get_control_points,
    take_snapshot,
    path_get_info,
]
