from typing import Any, Dict, Type, TypeVar, Union

import attr
from pydantic import BaseModel, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema

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

    type: str = "empty"


class export(BaseModel):
    """The response from the `Export` command. When this is being performed over a websocket, this is sent as binary not JSON. The binary data can be deserialized as `bincode` into a `Vec<ExportFile>`."""

    data: Export

    type: str = "export"


class select_with_point(BaseModel):
    """The response from the `SelectWithPoint` command."""

    data: SelectWithPoint

    type: str = "select_with_point"


class highlight_set_entity(BaseModel):
    """The response from the `HighlightSetEntity` command."""

    data: HighlightSetEntity

    type: str = "highlight_set_entity"


class entity_get_child_uuid(BaseModel):
    """The response from the `EntityGetChildUuid` command."""

    data: EntityGetChildUuid

    type: str = "entity_get_child_uuid"


class entity_get_num_children(BaseModel):
    """The response from the `EntityGetNumChildren` command."""

    data: EntityGetNumChildren

    type: str = "entity_get_num_children"


class entity_get_parent_id(BaseModel):
    """The response from the `EntityGetParentId` command."""

    data: EntityGetParentId

    type: str = "entity_get_parent_id"


class entity_get_all_child_uuids(BaseModel):
    """The response from the `EntityGetAllChildUuids` command."""

    data: EntityGetAllChildUuids

    type: str = "entity_get_all_child_uuids"


class select_get(BaseModel):
    """The response from the `SelectGet` command."""

    data: SelectGet

    type: str = "select_get"


class get_entity_type(BaseModel):
    """The response from the `GetEntityType` command."""

    data: GetEntityType

    type: str = "get_entity_type"


class solid3d_get_all_edge_faces(BaseModel):
    """The response from the `Solid3dGetAllEdgeFaces` command."""

    data: Solid3dGetAllEdgeFaces

    type: str = "solid3d_get_all_edge_faces"


class solid3d_get_all_opposite_edges(BaseModel):
    """The response from the `Solid3dGetAllOppositeEdges` command."""

    data: Solid3dGetAllOppositeEdges

    type: str = "solid3d_get_all_opposite_edges"


class solid3d_get_opposite_edge(BaseModel):
    """The response from the `Solid3dGetOppositeEdge` command."""

    data: Solid3dGetOppositeEdge

    type: str = "solid3d_get_opposite_edge"


class solid3d_get_prev_adjacent_edge(BaseModel):
    """The response from the `Solid3dGetPrevAdjacentEdge` command."""

    data: Solid3dGetPrevAdjacentEdge

    type: str = "solid3d_get_prev_adjacent_edge"


class solid3d_get_next_adjacent_edge(BaseModel):
    """The response from the `Solid3dGetNextAdjacentEdge` command."""

    data: Solid3dGetNextAdjacentEdge

    type: str = "solid3d_get_next_adjacent_edge"


class mouse_click(BaseModel):
    """The response from the `MouseClick` command."""

    data: MouseClick

    type: str = "mouse_click"


class curve_get_type(BaseModel):
    """The response from the `CurveGetType` command."""

    data: CurveGetType

    type: str = "curve_get_type"


class curve_get_control_points(BaseModel):
    """The response from the `CurveGetControlPoints` command."""

    data: CurveGetControlPoints

    type: str = "curve_get_control_points"


class take_snapshot(BaseModel):
    """The response from the `Take Snapshot` command."""

    data: TakeSnapshot

    type: str = "take_snapshot"


class path_get_info(BaseModel):
    """The response from the `Path Get Info` command."""

    data: PathGetInfo

    type: str = "path_get_info"


class path_get_curve_uuids_for_vertices(BaseModel):
    """The response from the `Path Get Curve UUIDs for Vertices` command."""

    data: PathGetCurveUuidsForVertices

    type: str = "path_get_curve_uuids_for_vertices"


class path_get_vertex_uuids(BaseModel):
    """The response from the `Path Get Vertex UUIDs` command."""

    data: PathGetVertexUuids

    type: str = "path_get_vertex_uuids"


class plane_intersect_and_project(BaseModel):
    """The response from the `PlaneIntersectAndProject` command."""

    data: PlaneIntersectAndProject

    type: str = "plane_intersect_and_project"


class curve_get_end_points(BaseModel):
    """The response from the `CurveGetEndPoints` command."""

    data: CurveGetEndPoints

    type: str = "curve_get_end_points"


class import_files(BaseModel):
    """The response from the `ImportFiles` command."""

    data: ImportFiles

    type: str = "import_files"


class mass(BaseModel):
    """The response from the `Mass` command."""

    data: Mass

    type: str = "mass"


class volume(BaseModel):
    """The response from the `Volume` command."""

    data: Volume

    type: str = "volume"


class density(BaseModel):
    """The response from the `Density` command."""

    data: Density

    type: str = "density"


class surface_area(BaseModel):
    """The response from the `SurfaceArea` command."""

    data: SurfaceArea

    type: str = "surface_area"


class center_of_mass(BaseModel):
    """The response from the `CenterOfMass` command."""

    data: CenterOfMass

    type: str = "center_of_mass"


class get_sketch_mode_plane(BaseModel):
    """The response from the `GetSketchModePlane` command."""

    data: GetSketchModePlane

    type: str = "get_sketch_mode_plane"


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

    def model_dump(self) -> Dict[str, Any]:
        if isinstance(self.type, empty):
            TZ: empty = self.type
            return TZ.model_dump()
        elif isinstance(self.type, export):
            RQ: export = self.type
            return RQ.model_dump()
        elif isinstance(self.type, select_with_point):
            CM: select_with_point = self.type
            return CM.model_dump()
        elif isinstance(self.type, highlight_set_entity):
            WP: highlight_set_entity = self.type
            return WP.model_dump()
        elif isinstance(self.type, entity_get_child_uuid):
            LN: entity_get_child_uuid = self.type
            return LN.model_dump()
        elif isinstance(self.type, entity_get_num_children):
            MG: entity_get_num_children = self.type
            return MG.model_dump()
        elif isinstance(self.type, entity_get_parent_id):
            BF: entity_get_parent_id = self.type
            return BF.model_dump()
        elif isinstance(self.type, entity_get_all_child_uuids):
            MB: entity_get_all_child_uuids = self.type
            return MB.model_dump()
        elif isinstance(self.type, select_get):
            FJ: select_get = self.type
            return FJ.model_dump()
        elif isinstance(self.type, get_entity_type):
            SF: get_entity_type = self.type
            return SF.model_dump()
        elif isinstance(self.type, solid3d_get_all_edge_faces):
            BM: solid3d_get_all_edge_faces = self.type
            return BM.model_dump()
        elif isinstance(self.type, solid3d_get_all_opposite_edges):
            NC: solid3d_get_all_opposite_edges = self.type
            return NC.model_dump()
        elif isinstance(self.type, solid3d_get_opposite_edge):
            FF: solid3d_get_opposite_edge = self.type
            return FF.model_dump()
        elif isinstance(self.type, solid3d_get_prev_adjacent_edge):
            FS: solid3d_get_prev_adjacent_edge = self.type
            return FS.model_dump()
        elif isinstance(self.type, solid3d_get_next_adjacent_edge):
            EQ: solid3d_get_next_adjacent_edge = self.type
            return EQ.model_dump()
        elif isinstance(self.type, mouse_click):
            MD: mouse_click = self.type
            return MD.model_dump()
        elif isinstance(self.type, curve_get_type):
            UJ: curve_get_type = self.type
            return UJ.model_dump()
        elif isinstance(self.type, curve_get_control_points):
            DL: curve_get_control_points = self.type
            return DL.model_dump()
        elif isinstance(self.type, take_snapshot):
            PT: take_snapshot = self.type
            return PT.model_dump()
        elif isinstance(self.type, path_get_info):
            VF: path_get_info = self.type
            return VF.model_dump()
        elif isinstance(self.type, path_get_curve_uuids_for_vertices):
            WH: path_get_curve_uuids_for_vertices = self.type
            return WH.model_dump()
        elif isinstance(self.type, path_get_vertex_uuids):
            UY: path_get_vertex_uuids = self.type
            return UY.model_dump()
        elif isinstance(self.type, plane_intersect_and_project):
            SM: plane_intersect_and_project = self.type
            return SM.model_dump()
        elif isinstance(self.type, curve_get_end_points):
            CG: curve_get_end_points = self.type
            return CG.model_dump()
        elif isinstance(self.type, import_files):
            ZB: import_files = self.type
            return ZB.model_dump()
        elif isinstance(self.type, mass):
            FX: mass = self.type
            return FX.model_dump()
        elif isinstance(self.type, volume):
            KU: volume = self.type
            return KU.model_dump()
        elif isinstance(self.type, density):
            FA: density = self.type
            return FA.model_dump()
        elif isinstance(self.type, surface_area):
            JG: surface_area = self.type
            return JG.model_dump()
        elif isinstance(self.type, center_of_mass):
            RY: center_of_mass = self.type
            return RY.model_dump()
        elif isinstance(self.type, get_sketch_mode_plane):
            AD: get_sketch_mode_plane = self.type
            return AD.model_dump()

        raise Exception("Unknown type")

    @classmethod
    def from_dict(cls: Type[GY], d: Dict[str, Any]) -> GY:
        if d.get("type") == "empty":
            AX: empty = empty(**d)
            return cls(type=AX)
        elif d.get("type") == "export":
            ZL: export = export(**d)
            return cls(type=ZL)
        elif d.get("type") == "select_with_point":
            OS: select_with_point = select_with_point(**d)
            return cls(type=OS)
        elif d.get("type") == "highlight_set_entity":
            XO: highlight_set_entity = highlight_set_entity(**d)
            return cls(type=XO)
        elif d.get("type") == "entity_get_child_uuid":
            KR: entity_get_child_uuid = entity_get_child_uuid(**d)
            return cls(type=KR)
        elif d.get("type") == "entity_get_num_children":
            UE: entity_get_num_children = entity_get_num_children(**d)
            return cls(type=UE)
        elif d.get("type") == "entity_get_parent_id":
            UU: entity_get_parent_id = entity_get_parent_id(**d)
            return cls(type=UU)
        elif d.get("type") == "entity_get_all_child_uuids":
            TB: entity_get_all_child_uuids = entity_get_all_child_uuids(**d)
            return cls(type=TB)
        elif d.get("type") == "select_get":
            HB: select_get = select_get(**d)
            return cls(type=HB)
        elif d.get("type") == "get_entity_type":
            DU: get_entity_type = get_entity_type(**d)
            return cls(type=DU)
        elif d.get("type") == "solid3d_get_all_edge_faces":
            TY: solid3d_get_all_edge_faces = solid3d_get_all_edge_faces(**d)
            return cls(type=TY)
        elif d.get("type") == "solid3d_get_all_opposite_edges":
            GP: solid3d_get_all_opposite_edges = solid3d_get_all_opposite_edges(**d)
            return cls(type=GP)
        elif d.get("type") == "solid3d_get_opposite_edge":
            YO: solid3d_get_opposite_edge = solid3d_get_opposite_edge(**d)
            return cls(type=YO)
        elif d.get("type") == "solid3d_get_prev_adjacent_edge":
            WN: solid3d_get_prev_adjacent_edge = solid3d_get_prev_adjacent_edge(**d)
            return cls(type=WN)
        elif d.get("type") == "solid3d_get_next_adjacent_edge":
            UW: solid3d_get_next_adjacent_edge = solid3d_get_next_adjacent_edge(**d)
            return cls(type=UW)
        elif d.get("type") == "mouse_click":
            HD: mouse_click = mouse_click(**d)
            return cls(type=HD)
        elif d.get("type") == "curve_get_type":
            RU: curve_get_type = curve_get_type(**d)
            return cls(type=RU)
        elif d.get("type") == "curve_get_control_points":
            QT: curve_get_control_points = curve_get_control_points(**d)
            return cls(type=QT)
        elif d.get("type") == "take_snapshot":
            HR: take_snapshot = take_snapshot(**d)
            return cls(type=HR)
        elif d.get("type") == "path_get_info":
            VM: path_get_info = path_get_info(**d)
            return cls(type=VM)
        elif d.get("type") == "path_get_curve_uuids_for_vertices":
            DQ: path_get_curve_uuids_for_vertices = path_get_curve_uuids_for_vertices(
                **d
            )
            return cls(type=DQ)
        elif d.get("type") == "path_get_vertex_uuids":
            PD: path_get_vertex_uuids = path_get_vertex_uuids(**d)
            return cls(type=PD)
        elif d.get("type") == "plane_intersect_and_project":
            JL: plane_intersect_and_project = plane_intersect_and_project(**d)
            return cls(type=JL)
        elif d.get("type") == "curve_get_end_points":
            QA: curve_get_end_points = curve_get_end_points(**d)
            return cls(type=QA)
        elif d.get("type") == "import_files":
            AU: import_files = import_files(**d)
            return cls(type=AU)
        elif d.get("type") == "mass":
            BL: mass = mass(**d)
            return cls(type=BL)
        elif d.get("type") == "volume":
            PZ: volume = volume(**d)
            return cls(type=PZ)
        elif d.get("type") == "density":
            GE: density = density(**d)
            return cls(type=GE)
        elif d.get("type") == "surface_area":
            HH: surface_area = surface_area(**d)
            return cls(type=HH)
        elif d.get("type") == "center_of_mass":
            AE: center_of_mass = center_of_mass(**d)
            return cls(type=AE)
        elif d.get("type") == "get_sketch_mode_plane":
            AB: get_sketch_mode_plane = get_sketch_mode_plane(**d)
            return cls(type=AB)

        raise Exception("Unknown type")

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls,
            handler(
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
                ]
            ),
        )
