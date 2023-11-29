from typing import Literal, Union

from pydantic import BaseModel, Field, RootModel
from typing_extensions import Annotated

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


class empty(BaseModel):
    """An empty response, used for any command that does not explicitly have a response defined here."""

    type: Literal["empty"] = "empty"


class export(BaseModel):
    """The response from the `Export` command. When this is being performed over a websocket, this is sent as binary not JSON. The binary data can be deserialized as `bincode` into a `Vec<ExportFile>`."""

    data: Export

    type: Literal["export"] = "export"


class select_with_point(BaseModel):
    """The response from the `SelectWithPoint` command."""

    data: SelectWithPoint

    type: Literal["select_with_point"] = "select_with_point"


class highlight_set_entity(BaseModel):
    """The response from the `HighlightSetEntity` command."""

    data: HighlightSetEntity

    type: Literal["highlight_set_entity"] = "highlight_set_entity"


class entity_get_child_uuid(BaseModel):
    """The response from the `EntityGetChildUuid` command."""

    data: EntityGetChildUuid

    type: Literal["entity_get_child_uuid"] = "entity_get_child_uuid"


class entity_get_num_children(BaseModel):
    """The response from the `EntityGetNumChildren` command."""

    data: EntityGetNumChildren

    type: Literal["entity_get_num_children"] = "entity_get_num_children"


class entity_get_parent_id(BaseModel):
    """The response from the `EntityGetParentId` command."""

    data: EntityGetParentId

    type: Literal["entity_get_parent_id"] = "entity_get_parent_id"


class entity_get_all_child_uuids(BaseModel):
    """The response from the `EntityGetAllChildUuids` command."""

    data: EntityGetAllChildUuids

    type: Literal["entity_get_all_child_uuids"] = "entity_get_all_child_uuids"


class select_get(BaseModel):
    """The response from the `SelectGet` command."""

    data: SelectGet

    type: Literal["select_get"] = "select_get"


class get_entity_type(BaseModel):
    """The response from the `GetEntityType` command."""

    data: GetEntityType

    type: Literal["get_entity_type"] = "get_entity_type"


class solid3d_get_all_edge_faces(BaseModel):
    """The response from the `Solid3dGetAllEdgeFaces` command."""

    data: Solid3dGetAllEdgeFaces

    type: Literal["solid3d_get_all_edge_faces"] = "solid3d_get_all_edge_faces"


class solid3d_get_all_opposite_edges(BaseModel):
    """The response from the `Solid3dGetAllOppositeEdges` command."""

    data: Solid3dGetAllOppositeEdges

    type: Literal["solid3d_get_all_opposite_edges"] = "solid3d_get_all_opposite_edges"


class solid3d_get_opposite_edge(BaseModel):
    """The response from the `Solid3dGetOppositeEdge` command."""

    data: Solid3dGetOppositeEdge

    type: Literal["solid3d_get_opposite_edge"] = "solid3d_get_opposite_edge"


class solid3d_get_prev_adjacent_edge(BaseModel):
    """The response from the `Solid3dGetPrevAdjacentEdge` command."""

    data: Solid3dGetPrevAdjacentEdge

    type: Literal["solid3d_get_prev_adjacent_edge"] = "solid3d_get_prev_adjacent_edge"


class solid3d_get_next_adjacent_edge(BaseModel):
    """The response from the `Solid3dGetNextAdjacentEdge` command."""

    data: Solid3dGetNextAdjacentEdge

    type: Literal["solid3d_get_next_adjacent_edge"] = "solid3d_get_next_adjacent_edge"


class mouse_click(BaseModel):
    """The response from the `MouseClick` command."""

    data: MouseClick

    type: Literal["mouse_click"] = "mouse_click"


class curve_get_type(BaseModel):
    """The response from the `CurveGetType` command."""

    data: CurveGetType

    type: Literal["curve_get_type"] = "curve_get_type"


class curve_get_control_points(BaseModel):
    """The response from the `CurveGetControlPoints` command."""

    data: CurveGetControlPoints

    type: Literal["curve_get_control_points"] = "curve_get_control_points"


class take_snapshot(BaseModel):
    """The response from the `Take Snapshot` command."""

    data: TakeSnapshot

    type: Literal["take_snapshot"] = "take_snapshot"


class path_get_info(BaseModel):
    """The response from the `Path Get Info` command."""

    data: PathGetInfo

    type: Literal["path_get_info"] = "path_get_info"


class path_get_curve_uuids_for_vertices(BaseModel):
    """The response from the `Path Get Curve UUIDs for Vertices` command."""

    data: PathGetCurveUuidsForVertices

    type: Literal[
        "path_get_curve_uuids_for_vertices"
    ] = "path_get_curve_uuids_for_vertices"


class path_get_vertex_uuids(BaseModel):
    """The response from the `Path Get Vertex UUIDs` command."""

    data: PathGetVertexUuids

    type: Literal["path_get_vertex_uuids"] = "path_get_vertex_uuids"


class plane_intersect_and_project(BaseModel):
    """The response from the `PlaneIntersectAndProject` command."""

    data: PlaneIntersectAndProject

    type: Literal["plane_intersect_and_project"] = "plane_intersect_and_project"


class curve_get_end_points(BaseModel):
    """The response from the `CurveGetEndPoints` command."""

    data: CurveGetEndPoints

    type: Literal["curve_get_end_points"] = "curve_get_end_points"


class import_files(BaseModel):
    """The response from the `ImportFiles` command."""

    data: ImportFiles

    type: Literal["import_files"] = "import_files"


class mass(BaseModel):
    """The response from the `Mass` command."""

    data: Mass

    type: Literal["mass"] = "mass"


class volume(BaseModel):
    """The response from the `Volume` command."""

    data: Volume

    type: Literal["volume"] = "volume"


class density(BaseModel):
    """The response from the `Density` command."""

    data: Density

    type: Literal["density"] = "density"


class surface_area(BaseModel):
    """The response from the `SurfaceArea` command."""

    data: SurfaceArea

    type: Literal["surface_area"] = "surface_area"


class center_of_mass(BaseModel):
    """The response from the `CenterOfMass` command."""

    data: CenterOfMass

    type: Literal["center_of_mass"] = "center_of_mass"


class get_sketch_mode_plane(BaseModel):
    """The response from the `GetSketchModePlane` command."""

    data: GetSketchModePlane

    type: Literal["get_sketch_mode_plane"] = "get_sketch_mode_plane"


OkModelingCmdResponse = RootModel[
    Annotated[
        Union[
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
        Field(discriminator="type"),
    ]
]
