from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.center_of_mass import CenterOfMass
from ..models.curve_get_control_points import CurveGetControlPoints
from ..models.curve_get_end_points import CurveGetEndPoints
from ..models.curve_get_type import CurveGetType
from ..models.density import Density
from ..models.entity_get_all_child_uuids import EntityGetAllChildUuids
from ..models.entity_get_child_uuid import EntityGetChildUuid
from ..models.entity_get_num_children import EntityGetNumChildren
from ..models.entity_get_parent_id import EntityGetParentId
from ..models.export import Export
from ..models.get_entity_type import GetEntityType
from ..models.get_sketch_mode_plane import GetSketchModePlane
from ..models.highlight_set_entity import HighlightSetEntity
from ..models.import_files import ImportFiles
from ..models.mass import Mass
from ..models.mouse_click import MouseClick
from ..models.path_get_curve_uuids_for_vertices import PathGetCurveUuidsForVertices
from ..models.path_get_info import PathGetInfo
from ..models.path_get_vertex_uuids import PathGetVertexUuids
from ..models.plane_intersect_and_project import PlaneIntersectAndProject
from ..models.select_get import SelectGet
from ..models.select_with_point import SelectWithPoint
from ..models.solid3d_get_all_edge_faces import Solid3dGetAllEdgeFaces
from ..models.solid3d_get_all_opposite_edges import Solid3dGetAllOppositeEdges
from ..models.solid3d_get_next_adjacent_edge import Solid3dGetNextAdjacentEdge
from ..models.solid3d_get_opposite_edge import Solid3dGetOppositeEdge
from ..models.solid3d_get_prev_adjacent_edge import Solid3dGetPrevAdjacentEdge
from ..models.surface_area import SurfaceArea
from ..models.take_snapshot import TakeSnapshot
from ..models.volume import Volume
from ..types import UNSET, Unset

FO = TypeVar("FO", bound="empty")


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
    def from_dict(cls: Type[FO], src_dict: Dict[str, Any]) -> FO:
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


KB = TypeVar("KB", bound="export")


@attr.s(auto_attribs=True)
class export:
    """The response from the `Export` command. When this is being performed over a websocket, this is sent as binary not JSON. The binary data can be deserialized as `bincode` into a `Vec<ExportFile>`."""  # noqa: E501

    data: Union[Unset, Export] = UNSET
    type: str = "export"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Export] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: Export = cast(Export, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[KB], src_dict: Dict[str, Any]) -> KB:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, Export]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = Export.from_dict(_data)

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


QH = TypeVar("QH", bound="select_with_point")


@attr.s(auto_attribs=True)
class select_with_point:
    """The response from the `SelectWithPoint` command."""  # noqa: E501

    data: Union[Unset, SelectWithPoint] = UNSET
    type: str = "select_with_point"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, SelectWithPoint] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: SelectWithPoint = cast(SelectWithPoint, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[QH], src_dict: Dict[str, Any]) -> QH:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, SelectWithPoint]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = SelectWithPoint.from_dict(_data)

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


EV = TypeVar("EV", bound="highlight_set_entity")


@attr.s(auto_attribs=True)
class highlight_set_entity:
    """The response from the `HighlightSetEntity` command."""  # noqa: E501

    data: Union[Unset, HighlightSetEntity] = UNSET
    type: str = "highlight_set_entity"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, HighlightSetEntity] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: HighlightSetEntity = cast(HighlightSetEntity, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[EV], src_dict: Dict[str, Any]) -> EV:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, HighlightSetEntity]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = HighlightSetEntity.from_dict(_data)

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


YL = TypeVar("YL", bound="entity_get_child_uuid")


@attr.s(auto_attribs=True)
class entity_get_child_uuid:
    """The response from the `EntityGetChildUuid` command."""  # noqa: E501

    data: Union[Unset, EntityGetChildUuid] = UNSET
    type: str = "entity_get_child_uuid"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, EntityGetChildUuid] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: EntityGetChildUuid = cast(EntityGetChildUuid, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[YL], src_dict: Dict[str, Any]) -> YL:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, EntityGetChildUuid]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = EntityGetChildUuid.from_dict(_data)

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


AN = TypeVar("AN", bound="entity_get_num_children")


@attr.s(auto_attribs=True)
class entity_get_num_children:
    """The response from the `EntityGetNumChildren` command."""  # noqa: E501

    data: Union[Unset, EntityGetNumChildren] = UNSET
    type: str = "entity_get_num_children"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, EntityGetNumChildren] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: EntityGetNumChildren = cast(EntityGetNumChildren, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[AN], src_dict: Dict[str, Any]) -> AN:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, EntityGetNumChildren]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = EntityGetNumChildren.from_dict(_data)

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


UV = TypeVar("UV", bound="entity_get_parent_id")


@attr.s(auto_attribs=True)
class entity_get_parent_id:
    """The response from the `EntityGetParentId` command."""  # noqa: E501

    data: Union[Unset, EntityGetParentId] = UNSET
    type: str = "entity_get_parent_id"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, EntityGetParentId] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: EntityGetParentId = cast(EntityGetParentId, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[UV], src_dict: Dict[str, Any]) -> UV:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, EntityGetParentId]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = EntityGetParentId.from_dict(_data)

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


IB = TypeVar("IB", bound="entity_get_all_child_uuids")


@attr.s(auto_attribs=True)
class entity_get_all_child_uuids:
    """The response from the `EntityGetAllChildUuids` command."""  # noqa: E501

    data: Union[Unset, EntityGetAllChildUuids] = UNSET
    type: str = "entity_get_all_child_uuids"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, EntityGetAllChildUuids] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: EntityGetAllChildUuids = cast(EntityGetAllChildUuids, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[IB], src_dict: Dict[str, Any]) -> IB:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, EntityGetAllChildUuids]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = EntityGetAllChildUuids.from_dict(_data)

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


EU = TypeVar("EU", bound="select_get")


@attr.s(auto_attribs=True)
class select_get:
    """The response from the `SelectGet` command."""  # noqa: E501

    data: Union[Unset, SelectGet] = UNSET
    type: str = "select_get"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, SelectGet] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: SelectGet = cast(SelectGet, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[EU], src_dict: Dict[str, Any]) -> EU:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, SelectGet]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = SelectGet.from_dict(_data)

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


QW = TypeVar("QW", bound="get_entity_type")


@attr.s(auto_attribs=True)
class get_entity_type:
    """The response from the `GetEntityType` command."""  # noqa: E501

    data: Union[Unset, GetEntityType] = UNSET
    type: str = "get_entity_type"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, GetEntityType] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: GetEntityType = cast(GetEntityType, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[QW], src_dict: Dict[str, Any]) -> QW:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, GetEntityType]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = GetEntityType.from_dict(_data)

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


RN = TypeVar("RN", bound="solid3d_get_all_edge_faces")


@attr.s(auto_attribs=True)
class solid3d_get_all_edge_faces:
    """The response from the `Solid3dGetAllEdgeFaces` command."""  # noqa: E501

    data: Union[Unset, Solid3dGetAllEdgeFaces] = UNSET
    type: str = "solid3d_get_all_edge_faces"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Solid3dGetAllEdgeFaces] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: Solid3dGetAllEdgeFaces = cast(Solid3dGetAllEdgeFaces, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[RN], src_dict: Dict[str, Any]) -> RN:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, Solid3dGetAllEdgeFaces]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = Solid3dGetAllEdgeFaces.from_dict(_data)

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


JN = TypeVar("JN", bound="solid3d_get_all_opposite_edges")


@attr.s(auto_attribs=True)
class solid3d_get_all_opposite_edges:
    """The response from the `Solid3dGetAllOppositeEdges` command."""  # noqa: E501

    data: Union[Unset, Solid3dGetAllOppositeEdges] = UNSET
    type: str = "solid3d_get_all_opposite_edges"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Solid3dGetAllOppositeEdges] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: Solid3dGetAllOppositeEdges = cast(Solid3dGetAllOppositeEdges, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[JN], src_dict: Dict[str, Any]) -> JN:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, Solid3dGetAllOppositeEdges]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = Solid3dGetAllOppositeEdges.from_dict(_data)

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


BD = TypeVar("BD", bound="solid3d_get_opposite_edge")


@attr.s(auto_attribs=True)
class solid3d_get_opposite_edge:
    """The response from the `Solid3dGetOppositeEdge` command."""  # noqa: E501

    data: Union[Unset, Solid3dGetOppositeEdge] = UNSET
    type: str = "solid3d_get_opposite_edge"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Solid3dGetOppositeEdge] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: Solid3dGetOppositeEdge = cast(Solid3dGetOppositeEdge, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[BD], src_dict: Dict[str, Any]) -> BD:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, Solid3dGetOppositeEdge]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = Solid3dGetOppositeEdge.from_dict(_data)

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


XW = TypeVar("XW", bound="solid3d_get_prev_adjacent_edge")


@attr.s(auto_attribs=True)
class solid3d_get_prev_adjacent_edge:
    """The response from the `Solid3dGetPrevAdjacentEdge` command."""  # noqa: E501

    data: Union[Unset, Solid3dGetPrevAdjacentEdge] = UNSET
    type: str = "solid3d_get_prev_adjacent_edge"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Solid3dGetPrevAdjacentEdge] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: Solid3dGetPrevAdjacentEdge = cast(Solid3dGetPrevAdjacentEdge, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[XW], src_dict: Dict[str, Any]) -> XW:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, Solid3dGetPrevAdjacentEdge]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = Solid3dGetPrevAdjacentEdge.from_dict(_data)

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


LP = TypeVar("LP", bound="solid3d_get_next_adjacent_edge")


@attr.s(auto_attribs=True)
class solid3d_get_next_adjacent_edge:
    """The response from the `Solid3dGetNextAdjacentEdge` command."""  # noqa: E501

    data: Union[Unset, Solid3dGetNextAdjacentEdge] = UNSET
    type: str = "solid3d_get_next_adjacent_edge"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Solid3dGetNextAdjacentEdge] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: Solid3dGetNextAdjacentEdge = cast(Solid3dGetNextAdjacentEdge, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[LP], src_dict: Dict[str, Any]) -> LP:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, Solid3dGetNextAdjacentEdge]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = Solid3dGetNextAdjacentEdge.from_dict(_data)

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


XN = TypeVar("XN", bound="mouse_click")


@attr.s(auto_attribs=True)
class mouse_click:
    """The response from the `MouseClick` command."""  # noqa: E501

    data: Union[Unset, MouseClick] = UNSET
    type: str = "mouse_click"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, MouseClick] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: MouseClick = cast(MouseClick, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[XN], src_dict: Dict[str, Any]) -> XN:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, MouseClick]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = MouseClick.from_dict(_data)

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


PL = TypeVar("PL", bound="curve_get_type")


@attr.s(auto_attribs=True)
class curve_get_type:
    """The response from the `CurveGetType` command."""  # noqa: E501

    data: Union[Unset, CurveGetType] = UNSET
    type: str = "curve_get_type"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, CurveGetType] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: CurveGetType = cast(CurveGetType, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[PL], src_dict: Dict[str, Any]) -> PL:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, CurveGetType]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = CurveGetType.from_dict(_data)

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


XS = TypeVar("XS", bound="curve_get_control_points")


@attr.s(auto_attribs=True)
class curve_get_control_points:
    """The response from the `CurveGetControlPoints` command."""  # noqa: E501

    data: Union[Unset, CurveGetControlPoints] = UNSET
    type: str = "curve_get_control_points"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, CurveGetControlPoints] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: CurveGetControlPoints = cast(CurveGetControlPoints, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[XS], src_dict: Dict[str, Any]) -> XS:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, CurveGetControlPoints]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = CurveGetControlPoints.from_dict(_data)

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


YB = TypeVar("YB", bound="take_snapshot")


@attr.s(auto_attribs=True)
class take_snapshot:
    """The response from the `Take Snapshot` command."""  # noqa: E501

    data: Union[Unset, TakeSnapshot] = UNSET
    type: str = "take_snapshot"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, TakeSnapshot] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: TakeSnapshot = cast(TakeSnapshot, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[YB], src_dict: Dict[str, Any]) -> YB:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, TakeSnapshot]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = TakeSnapshot.from_dict(_data)

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


YX = TypeVar("YX", bound="path_get_info")


@attr.s(auto_attribs=True)
class path_get_info:
    """The response from the `Path Get Info` command."""  # noqa: E501

    data: Union[Unset, PathGetInfo] = UNSET
    type: str = "path_get_info"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, PathGetInfo] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: PathGetInfo = cast(PathGetInfo, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[YX], src_dict: Dict[str, Any]) -> YX:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, PathGetInfo]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = PathGetInfo.from_dict(_data)

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


LM = TypeVar("LM", bound="path_get_curve_uuids_for_vertices")


@attr.s(auto_attribs=True)
class path_get_curve_uuids_for_vertices:
    """The response from the `Path Get Curve UUIDs for Vertices` command."""  # noqa: E501

    data: Union[Unset, PathGetCurveUuidsForVertices] = UNSET
    type: str = "path_get_curve_uuids_for_vertices"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, PathGetCurveUuidsForVertices] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: PathGetCurveUuidsForVertices = cast(
                PathGetCurveUuidsForVertices, data
            )
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[LM], src_dict: Dict[str, Any]) -> LM:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, PathGetCurveUuidsForVertices]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = PathGetCurveUuidsForVertices.from_dict(_data)

        type = d.pop("type", UNSET)

        path_get_curve_uuids_for_vertices = cls(
            data=data,
            type=type,
        )

        path_get_curve_uuids_for_vertices.additional_properties = d
        return path_get_curve_uuids_for_vertices

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


DM = TypeVar("DM", bound="path_get_vertex_uuids")


@attr.s(auto_attribs=True)
class path_get_vertex_uuids:
    """The response from the `Path Get Vertex UUIDs` command."""  # noqa: E501

    data: Union[Unset, PathGetVertexUuids] = UNSET
    type: str = "path_get_vertex_uuids"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, PathGetVertexUuids] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: PathGetVertexUuids = cast(PathGetVertexUuids, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[DM], src_dict: Dict[str, Any]) -> DM:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, PathGetVertexUuids]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = PathGetVertexUuids.from_dict(_data)

        type = d.pop("type", UNSET)

        path_get_vertex_uuids = cls(
            data=data,
            type=type,
        )

        path_get_vertex_uuids.additional_properties = d
        return path_get_vertex_uuids

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


HZ = TypeVar("HZ", bound="plane_intersect_and_project")


@attr.s(auto_attribs=True)
class plane_intersect_and_project:
    """The response from the `PlaneIntersectAndProject` command."""  # noqa: E501

    data: Union[Unset, PlaneIntersectAndProject] = UNSET
    type: str = "plane_intersect_and_project"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, PlaneIntersectAndProject] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: PlaneIntersectAndProject = cast(PlaneIntersectAndProject, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[HZ], src_dict: Dict[str, Any]) -> HZ:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, PlaneIntersectAndProject]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = PlaneIntersectAndProject.from_dict(_data)

        type = d.pop("type", UNSET)

        plane_intersect_and_project = cls(
            data=data,
            type=type,
        )

        plane_intersect_and_project.additional_properties = d
        return plane_intersect_and_project

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


CP = TypeVar("CP", bound="curve_get_end_points")


@attr.s(auto_attribs=True)
class curve_get_end_points:
    """The response from the `CurveGetEndPoints` command."""  # noqa: E501

    data: Union[Unset, CurveGetEndPoints] = UNSET
    type: str = "curve_get_end_points"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, CurveGetEndPoints] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: CurveGetEndPoints = cast(CurveGetEndPoints, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[CP], src_dict: Dict[str, Any]) -> CP:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, CurveGetEndPoints]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = CurveGetEndPoints.from_dict(_data)

        type = d.pop("type", UNSET)

        curve_get_end_points = cls(
            data=data,
            type=type,
        )

        curve_get_end_points.additional_properties = d
        return curve_get_end_points

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


IP = TypeVar("IP", bound="import_files")


@attr.s(auto_attribs=True)
class import_files:
    """The response from the `ImportFiles` command."""  # noqa: E501

    data: Union[Unset, ImportFiles] = UNSET
    type: str = "import_files"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, ImportFiles] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: ImportFiles = cast(ImportFiles, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[IP], src_dict: Dict[str, Any]) -> IP:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, ImportFiles]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = ImportFiles.from_dict(_data)

        type = d.pop("type", UNSET)

        import_files = cls(
            data=data,
            type=type,
        )

        import_files.additional_properties = d
        return import_files

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


XV = TypeVar("XV", bound="mass")


@attr.s(auto_attribs=True)
class mass:
    """The response from the `Mass` command."""  # noqa: E501

    data: Union[Unset, Mass] = UNSET
    type: str = "mass"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Mass] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: Mass = cast(Mass, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[XV], src_dict: Dict[str, Any]) -> XV:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, Mass]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = Mass.from_dict(_data)

        type = d.pop("type", UNSET)

        mass = cls(
            data=data,
            type=type,
        )

        mass.additional_properties = d
        return mass

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


TW = TypeVar("TW", bound="volume")


@attr.s(auto_attribs=True)
class volume:
    """The response from the `Volume` command."""  # noqa: E501

    data: Union[Unset, Volume] = UNSET
    type: str = "volume"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Volume] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: Volume = cast(Volume, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[TW], src_dict: Dict[str, Any]) -> TW:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, Volume]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = Volume.from_dict(_data)

        type = d.pop("type", UNSET)

        volume = cls(
            data=data,
            type=type,
        )

        volume.additional_properties = d
        return volume

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


CH = TypeVar("CH", bound="density")


@attr.s(auto_attribs=True)
class density:
    """The response from the `Density` command."""  # noqa: E501

    data: Union[Unset, Density] = UNSET
    type: str = "density"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Density] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: Density = cast(Density, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[CH], src_dict: Dict[str, Any]) -> CH:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, Density]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = Density.from_dict(_data)

        type = d.pop("type", UNSET)

        density = cls(
            data=data,
            type=type,
        )

        density.additional_properties = d
        return density

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


MW = TypeVar("MW", bound="surface_area")


@attr.s(auto_attribs=True)
class surface_area:
    """The response from the `SurfaceArea` command."""  # noqa: E501

    data: Union[Unset, SurfaceArea] = UNSET
    type: str = "surface_area"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, SurfaceArea] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: SurfaceArea = cast(SurfaceArea, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[MW], src_dict: Dict[str, Any]) -> MW:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, SurfaceArea]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = SurfaceArea.from_dict(_data)

        type = d.pop("type", UNSET)

        surface_area = cls(
            data=data,
            type=type,
        )

        surface_area.additional_properties = d
        return surface_area

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


VN = TypeVar("VN", bound="center_of_mass")


@attr.s(auto_attribs=True)
class center_of_mass:
    """The response from the `CenterOfMass` command."""  # noqa: E501

    data: Union[Unset, CenterOfMass] = UNSET
    type: str = "center_of_mass"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, CenterOfMass] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: CenterOfMass = cast(CenterOfMass, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[VN], src_dict: Dict[str, Any]) -> VN:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, CenterOfMass]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = CenterOfMass.from_dict(_data)

        type = d.pop("type", UNSET)

        center_of_mass = cls(
            data=data,
            type=type,
        )

        center_of_mass.additional_properties = d
        return center_of_mass

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


WE = TypeVar("WE", bound="get_sketch_mode_plane")


@attr.s(auto_attribs=True)
class get_sketch_mode_plane:
    """The response from the `GetSketchModePlane` command."""  # noqa: E501

    data: Union[Unset, GetSketchModePlane] = UNSET
    type: str = "get_sketch_mode_plane"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, GetSketchModePlane] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            _data: GetSketchModePlane = cast(GetSketchModePlane, data)
            field_dict["data"] = _data.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[WE], src_dict: Dict[str, Any]) -> WE:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, GetSketchModePlane]
        if isinstance(_data, Unset):
            data = UNSET
        if _data is None:
            data = UNSET
        else:
            data = GetSketchModePlane.from_dict(_data)

        type = d.pop("type", UNSET)

        get_sketch_mode_plane = cls(
            data=data,
            type=type,
        )

        get_sketch_mode_plane.additional_properties = d
        return get_sketch_mode_plane

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


GY = TypeVar("GY", bound="OkModelingCmdResponse")


@attr.s(auto_attribs=True)
class OkModelingCmdResponse:

    """A successful response from a modeling command. This can be one of several types of responses, depending on the command."""

    type: Union[
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
        path_get_curve_uuids_for_vertices,
        path_get_vertex_uuids,
        plane_intersect_and_project,
        curve_get_end_points,
        import_files,
        mass,
        volume,
        density,
        surface_area,
        center_of_mass,
        get_sketch_mode_plane,
    ]

    def __init__(
        self,
        type: Union[
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
            path_get_curve_uuids_for_vertices,
            path_get_vertex_uuids,
            plane_intersect_and_project,
            curve_get_end_points,
            import_files,
            mass,
            volume,
            density,
            surface_area,
            center_of_mass,
            get_sketch_mode_plane,
        ],
    ):
        self.type = type

    def to_dict(self) -> Dict[str, Any]:
        if isinstance(self.type, empty):
            YZ: empty = self.type
            return YZ.to_dict()
        elif isinstance(self.type, export):
            SV: export = self.type
            return SV.to_dict()
        elif isinstance(self.type, select_with_point):
            ZF: select_with_point = self.type
            return ZF.to_dict()
        elif isinstance(self.type, highlight_set_entity):
            RA: highlight_set_entity = self.type
            return RA.to_dict()
        elif isinstance(self.type, entity_get_child_uuid):
            KP: entity_get_child_uuid = self.type
            return KP.to_dict()
        elif isinstance(self.type, entity_get_num_children):
            HM: entity_get_num_children = self.type
            return HM.to_dict()
        elif isinstance(self.type, entity_get_parent_id):
            NT: entity_get_parent_id = self.type
            return NT.to_dict()
        elif isinstance(self.type, entity_get_all_child_uuids):
            IH: entity_get_all_child_uuids = self.type
            return IH.to_dict()
        elif isinstance(self.type, select_get):
            WK: select_get = self.type
            return WK.to_dict()
        elif isinstance(self.type, get_entity_type):
            CA: get_entity_type = self.type
            return CA.to_dict()
        elif isinstance(self.type, solid3d_get_all_edge_faces):
            AF: solid3d_get_all_edge_faces = self.type
            return AF.to_dict()
        elif isinstance(self.type, solid3d_get_all_opposite_edges):
            IY: solid3d_get_all_opposite_edges = self.type
            return IY.to_dict()
        elif isinstance(self.type, solid3d_get_opposite_edge):
            QB: solid3d_get_opposite_edge = self.type
            return QB.to_dict()
        elif isinstance(self.type, solid3d_get_prev_adjacent_edge):
            QN: solid3d_get_prev_adjacent_edge = self.type
            return QN.to_dict()
        elif isinstance(self.type, solid3d_get_next_adjacent_edge):
            VL: solid3d_get_next_adjacent_edge = self.type
            return VL.to_dict()
        elif isinstance(self.type, mouse_click):
            IW: mouse_click = self.type
            return IW.to_dict()
        elif isinstance(self.type, curve_get_type):
            LW: curve_get_type = self.type
            return LW.to_dict()
        elif isinstance(self.type, curve_get_control_points):
            ID: curve_get_control_points = self.type
            return ID.to_dict()
        elif isinstance(self.type, take_snapshot):
            NI: take_snapshot = self.type
            return NI.to_dict()
        elif isinstance(self.type, path_get_info):
            BY: path_get_info = self.type
            return BY.to_dict()
        elif isinstance(self.type, path_get_curve_uuids_for_vertices):
            IC: path_get_curve_uuids_for_vertices = self.type
            return IC.to_dict()
        elif isinstance(self.type, path_get_vertex_uuids):
            SH: path_get_vertex_uuids = self.type
            return SH.to_dict()
        elif isinstance(self.type, plane_intersect_and_project):
            RV: plane_intersect_and_project = self.type
            return RV.to_dict()
        elif isinstance(self.type, curve_get_end_points):
            TI: curve_get_end_points = self.type
            return TI.to_dict()
        elif isinstance(self.type, import_files):
            KO: import_files = self.type
            return KO.to_dict()
        elif isinstance(self.type, mass):
            AL: mass = self.type
            return AL.to_dict()
        elif isinstance(self.type, volume):
            ZH: volume = self.type
            return ZH.to_dict()
        elif isinstance(self.type, density):
            KD: density = self.type
            return KD.to_dict()
        elif isinstance(self.type, surface_area):
            YA: surface_area = self.type
            return YA.to_dict()
        elif isinstance(self.type, center_of_mass):
            WD: center_of_mass = self.type
            return WD.to_dict()
        elif isinstance(self.type, get_sketch_mode_plane):
            RJ: get_sketch_mode_plane = self.type
            return RJ.to_dict()

        raise Exception("Unknown type")

    @classmethod
    def from_dict(cls: Type[GY], d: Dict[str, Any]) -> GY:
        if d.get("type") == "empty":
            GZ: empty = empty()
            GZ.from_dict(d)
            return cls(type=GZ)
        elif d.get("type") == "export":
            XB: export = export()
            XB.from_dict(d)
            return cls(type=XB)
        elif d.get("type") == "select_with_point":
            XM: select_with_point = select_with_point()
            XM.from_dict(d)
            return cls(type=XM)
        elif d.get("type") == "highlight_set_entity":
            TQ: highlight_set_entity = highlight_set_entity()
            TQ.from_dict(d)
            return cls(type=TQ)
        elif d.get("type") == "entity_get_child_uuid":
            SU: entity_get_child_uuid = entity_get_child_uuid()
            SU.from_dict(d)
            return cls(type=SU)
        elif d.get("type") == "entity_get_num_children":
            QD: entity_get_num_children = entity_get_num_children()
            QD.from_dict(d)
            return cls(type=QD)
        elif d.get("type") == "entity_get_parent_id":
            XC: entity_get_parent_id = entity_get_parent_id()
            XC.from_dict(d)
            return cls(type=XC)
        elif d.get("type") == "entity_get_all_child_uuids":
            IX: entity_get_all_child_uuids = entity_get_all_child_uuids()
            IX.from_dict(d)
            return cls(type=IX)
        elif d.get("type") == "select_get":
            YS: select_get = select_get()
            YS.from_dict(d)
            return cls(type=YS)
        elif d.get("type") == "get_entity_type":
            TT: get_entity_type = get_entity_type()
            TT.from_dict(d)
            return cls(type=TT)
        elif d.get("type") == "solid3d_get_all_edge_faces":
            CK: solid3d_get_all_edge_faces = solid3d_get_all_edge_faces()
            CK.from_dict(d)
            return cls(type=CK)
        elif d.get("type") == "solid3d_get_all_opposite_edges":
            BO: solid3d_get_all_opposite_edges = solid3d_get_all_opposite_edges()
            BO.from_dict(d)
            return cls(type=BO)
        elif d.get("type") == "solid3d_get_opposite_edge":
            VB: solid3d_get_opposite_edge = solid3d_get_opposite_edge()
            VB.from_dict(d)
            return cls(type=VB)
        elif d.get("type") == "solid3d_get_prev_adjacent_edge":
            RR: solid3d_get_prev_adjacent_edge = solid3d_get_prev_adjacent_edge()
            RR.from_dict(d)
            return cls(type=RR)
        elif d.get("type") == "solid3d_get_next_adjacent_edge":
            JS: solid3d_get_next_adjacent_edge = solid3d_get_next_adjacent_edge()
            JS.from_dict(d)
            return cls(type=JS)
        elif d.get("type") == "mouse_click":
            JU: mouse_click = mouse_click()
            JU.from_dict(d)
            return cls(type=JU)
        elif d.get("type") == "curve_get_type":
            MF: curve_get_type = curve_get_type()
            MF.from_dict(d)
            return cls(type=MF)
        elif d.get("type") == "curve_get_control_points":
            ER: curve_get_control_points = curve_get_control_points()
            ER.from_dict(d)
            return cls(type=ER)
        elif d.get("type") == "take_snapshot":
            GV: take_snapshot = take_snapshot()
            GV.from_dict(d)
            return cls(type=GV)
        elif d.get("type") == "path_get_info":
            SR: path_get_info = path_get_info()
            SR.from_dict(d)
            return cls(type=SR)
        elif d.get("type") == "path_get_curve_uuids_for_vertices":
            CU: path_get_curve_uuids_for_vertices = path_get_curve_uuids_for_vertices()
            CU.from_dict(d)
            return cls(type=CU)
        elif d.get("type") == "path_get_vertex_uuids":
            OZ: path_get_vertex_uuids = path_get_vertex_uuids()
            OZ.from_dict(d)
            return cls(type=OZ)
        elif d.get("type") == "plane_intersect_and_project":
            HS: plane_intersect_and_project = plane_intersect_and_project()
            HS.from_dict(d)
            return cls(type=HS)
        elif d.get("type") == "curve_get_end_points":
            JB: curve_get_end_points = curve_get_end_points()
            JB.from_dict(d)
            return cls(type=JB)
        elif d.get("type") == "import_files":
            RP: import_files = import_files()
            RP.from_dict(d)
            return cls(type=RP)
        elif d.get("type") == "mass":
            PF: mass = mass()
            PF.from_dict(d)
            return cls(type=PF)
        elif d.get("type") == "volume":
            KV: volume = volume()
            KV.from_dict(d)
            return cls(type=KV)
        elif d.get("type") == "density":
            IN: density = density()
            IN.from_dict(d)
            return cls(type=IN)
        elif d.get("type") == "surface_area":
            QR: surface_area = surface_area()
            QR.from_dict(d)
            return cls(type=QR)
        elif d.get("type") == "center_of_mass":
            PG: center_of_mass = center_of_mass()
            PG.from_dict(d)
            return cls(type=PG)
        elif d.get("type") == "get_sketch_mode_plane":
            QS: get_sketch_mode_plane = get_sketch_mode_plane()
            QS.from_dict(d)
            return cls(type=QS)

        raise Exception("Unknown type")
