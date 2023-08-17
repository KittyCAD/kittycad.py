from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.entity_type import EntityType
from ..types import UNSET, Unset

NO = TypeVar("NO", bound="empty")


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
    def from_dict(cls: Type[NO], src_dict: Dict[str, Any]) -> NO:
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


VX = TypeVar("VX", bound="export")


@attr.s(auto_attribs=True)
class export:
    """The response from the `Export` command. When this is being performed over a websocket, this is sent as binary not JSON. The binary data can be deserialized as `bincode` into a `Vec<ExportFile>`."""  # noqa: E501

    from ..models.export_file import ExportFile

    files: Union[Unset, List[ExportFile]] = UNSET
    type: str = "export"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.export_file import ExportFile

        files: Union[Unset, List[ExportFile]] = UNSET
        if not isinstance(self.files, Unset):
            files = self.files
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[VX], src_dict: Dict[str, Any]) -> VX:
        d = src_dict.copy()
        from ..models.export_file import ExportFile

        files = cast(List[ExportFile], d.pop("files", UNSET))

        type = d.pop("type", UNSET)

        export = cls(
            files=files,
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


RG = TypeVar("RG", bound="select_with_point")


@attr.s(auto_attribs=True)
class select_with_point:
    """The response from the `SelectWithPoint` command."""  # noqa: E501

    entity_id: Union[Unset, str] = UNSET
    type: str = "select_with_point"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_id = self.entity_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[RG], src_dict: Dict[str, Any]) -> RG:
        d = src_dict.copy()
        entity_id = d.pop("entity_id", UNSET)

        type = d.pop("type", UNSET)

        select_with_point = cls(
            entity_id=entity_id,
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


IT = TypeVar("IT", bound="highlight_set_entity")


@attr.s(auto_attribs=True)
class highlight_set_entity:
    """The response from the `HighlightSetEntity` command."""  # noqa: E501

    entity_id: Union[Unset, str] = UNSET
    sequence: Union[Unset, int] = UNSET
    type: str = "highlight_set_entity"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_id = self.entity_id
        sequence = self.sequence
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[IT], src_dict: Dict[str, Any]) -> IT:
        d = src_dict.copy()
        entity_id = d.pop("entity_id", UNSET)

        sequence = d.pop("sequence", UNSET)

        type = d.pop("type", UNSET)

        highlight_set_entity = cls(
            entity_id=entity_id,
            sequence=sequence,
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


LD = TypeVar("LD", bound="entity_get_child_uuid")


@attr.s(auto_attribs=True)
class entity_get_child_uuid:
    """The response from the `EntityGetChildUuid` command."""  # noqa: E501

    entity_id: Union[Unset, str] = UNSET
    type: str = "entity_get_child_uuid"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_id = self.entity_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[LD], src_dict: Dict[str, Any]) -> LD:
        d = src_dict.copy()
        entity_id = d.pop("entity_id", UNSET)

        type = d.pop("type", UNSET)

        entity_get_child_uuid = cls(
            entity_id=entity_id,
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


UA = TypeVar("UA", bound="entity_get_num_children")


@attr.s(auto_attribs=True)
class entity_get_num_children:
    """The response from the `EntityGetNumChildren` command."""  # noqa: E501

    num: Union[Unset, int] = UNSET
    type: str = "entity_get_num_children"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        num = self.num
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num is not UNSET:
            field_dict["num"] = num
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[UA], src_dict: Dict[str, Any]) -> UA:
        d = src_dict.copy()
        num = d.pop("num", UNSET)

        type = d.pop("type", UNSET)

        entity_get_num_children = cls(
            num=num,
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


TN = TypeVar("TN", bound="entity_get_parent_id")


@attr.s(auto_attribs=True)
class entity_get_parent_id:
    """The response from the `EntityGetParentId` command."""  # noqa: E501

    entity_id: Union[Unset, str] = UNSET
    type: str = "entity_get_parent_id"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_id = self.entity_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[TN], src_dict: Dict[str, Any]) -> TN:
        d = src_dict.copy()
        entity_id = d.pop("entity_id", UNSET)

        type = d.pop("type", UNSET)

        entity_get_parent_id = cls(
            entity_id=entity_id,
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


MZ = TypeVar("MZ", bound="entity_get_all_child_uuids")


@attr.s(auto_attribs=True)
class entity_get_all_child_uuids:
    """The response from the `EntityGetAllChildUuids` command."""  # noqa: E501

    entity_ids: Union[Unset, List[str]] = UNSET
    type: str = "entity_get_all_child_uuids"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.entity_ids, Unset):
            entity_ids = self.entity_ids
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_ids is not UNSET:
            field_dict["entity_ids"] = entity_ids
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[MZ], src_dict: Dict[str, Any]) -> MZ:
        d = src_dict.copy()
        entity_ids = cast(List[str], d.pop("entity_ids", UNSET))

        type = d.pop("type", UNSET)

        entity_get_all_child_uuids = cls(
            entity_ids=entity_ids,
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


UG = TypeVar("UG", bound="select_get")


@attr.s(auto_attribs=True)
class select_get:
    """The response from the `SelectGet` command."""  # noqa: E501

    entity_ids: Union[Unset, List[str]] = UNSET
    type: str = "select_get"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.entity_ids, Unset):
            entity_ids = self.entity_ids
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_ids is not UNSET:
            field_dict["entity_ids"] = entity_ids
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[UG], src_dict: Dict[str, Any]) -> UG:
        d = src_dict.copy()
        entity_ids = cast(List[str], d.pop("entity_ids", UNSET))

        type = d.pop("type", UNSET)

        select_get = cls(
            entity_ids=entity_ids,
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


CY = TypeVar("CY", bound="get_entity_type")


@attr.s(auto_attribs=True)
class get_entity_type:
    """The response from the `GetEntityType` command."""  # noqa: E501

    entity_type: Union[Unset, EntityType] = UNSET
    type: str = "get_entity_type"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[CY], src_dict: Dict[str, Any]) -> CY:
        d = src_dict.copy()
        _entity_type = d.pop("entity_type", UNSET)
        entity_type: Union[Unset, EntityType]
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = _entity_type  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        get_entity_type = cls(
            entity_type=entity_type,
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


NZ = TypeVar("NZ", bound="solid3d_get_all_edge_faces")


@attr.s(auto_attribs=True)
class solid3d_get_all_edge_faces:
    """The response from the `Solid3dGetAllEdgeFaces` command."""  # noqa: E501

    faces: Union[Unset, List[str]] = UNSET
    type: str = "solid3d_get_all_edge_faces"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        faces: Union[Unset, List[str]] = UNSET
        if not isinstance(self.faces, Unset):
            faces = self.faces
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if faces is not UNSET:
            field_dict["faces"] = faces
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[NZ], src_dict: Dict[str, Any]) -> NZ:
        d = src_dict.copy()
        faces = cast(List[str], d.pop("faces", UNSET))

        type = d.pop("type", UNSET)

        solid3d_get_all_edge_faces = cls(
            faces=faces,
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


LI = TypeVar("LI", bound="solid3d_get_all_opposite_edges")


@attr.s(auto_attribs=True)
class solid3d_get_all_opposite_edges:
    """The response from the `Solid3dGetAllOppositeEdges` command."""  # noqa: E501

    edges: Union[Unset, List[str]] = UNSET
    type: str = "solid3d_get_all_opposite_edges"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        edges: Union[Unset, List[str]] = UNSET
        if not isinstance(self.edges, Unset):
            edges = self.edges
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edges is not UNSET:
            field_dict["edges"] = edges
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[LI], src_dict: Dict[str, Any]) -> LI:
        d = src_dict.copy()
        edges = cast(List[str], d.pop("edges", UNSET))

        type = d.pop("type", UNSET)

        solid3d_get_all_opposite_edges = cls(
            edges=edges,
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


LO = TypeVar("LO", bound="solid3d_get_opposite_edge")


@attr.s(auto_attribs=True)
class solid3d_get_opposite_edge:
    """The response from the `Solid3dGetOppositeEdge` command."""  # noqa: E501

    edge: Union[Unset, str] = UNSET
    type: str = "solid3d_get_opposite_edge"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        edge = self.edge
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edge is not UNSET:
            field_dict["edge"] = edge
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[LO], src_dict: Dict[str, Any]) -> LO:
        d = src_dict.copy()
        edge = d.pop("edge", UNSET)

        type = d.pop("type", UNSET)

        solid3d_get_opposite_edge = cls(
            edge=edge,
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


XJ = TypeVar("XJ", bound="solid3d_get_prev_adjacent_edge")


@attr.s(auto_attribs=True)
class solid3d_get_prev_adjacent_edge:
    """The response from the `Solid3dGetPrevAdjacentEdge` command."""  # noqa: E501

    edge: Union[Unset, str] = UNSET
    type: str = "solid3d_get_prev_adjacent_edge"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        edge = self.edge
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edge is not UNSET:
            field_dict["edge"] = edge
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[XJ], src_dict: Dict[str, Any]) -> XJ:
        d = src_dict.copy()
        edge = d.pop("edge", UNSET)

        type = d.pop("type", UNSET)

        solid3d_get_prev_adjacent_edge = cls(
            edge=edge,
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


OW = TypeVar("OW", bound="solid3d_get_next_adjacent_edge")


@attr.s(auto_attribs=True)
class solid3d_get_next_adjacent_edge:
    """The response from the `Solid3dGetNextAdjacentEdge` command."""  # noqa: E501

    edge: Union[Unset, str] = UNSET
    type: str = "solid3d_get_next_adjacent_edge"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        edge = self.edge
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edge is not UNSET:
            field_dict["edge"] = edge
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[OW], src_dict: Dict[str, Any]) -> OW:
        d = src_dict.copy()
        edge = d.pop("edge", UNSET)

        type = d.pop("type", UNSET)

        solid3d_get_next_adjacent_edge = cls(
            edge=edge,
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
]
