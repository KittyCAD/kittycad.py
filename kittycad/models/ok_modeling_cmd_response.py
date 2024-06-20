from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated

from ..models.camera_drag_end import CameraDragEnd
from ..models.camera_drag_move import CameraDragMove
from ..models.center_of_mass import CenterOfMass
from ..models.close_path import ClosePath
from ..models.curve_get_control_points import CurveGetControlPoints
from ..models.curve_get_end_points import CurveGetEndPoints
from ..models.curve_get_type import CurveGetType
from ..models.default_camera_focus_on import DefaultCameraFocusOn
from ..models.default_camera_get_settings import DefaultCameraGetSettings
from ..models.default_camera_zoom import DefaultCameraZoom
from ..models.density import Density
from ..models.entity_circular_pattern import EntityCircularPattern
from ..models.entity_get_all_child_uuids import EntityGetAllChildUuids
from ..models.entity_get_child_uuid import EntityGetChildUuid
from ..models.entity_get_distance import EntityGetDistance
from ..models.entity_get_num_children import EntityGetNumChildren
from ..models.entity_get_parent_id import EntityGetParentId
from ..models.entity_linear_pattern import EntityLinearPattern
from ..models.entity_linear_pattern_transform import EntityLinearPatternTransform
from ..models.export import Export
from ..models.extrusion_face_info import ExtrusionFaceInfo
from ..models.face_get_center import FaceGetCenter
from ..models.face_get_gradient import FaceGetGradient
from ..models.face_get_position import FaceGetPosition
from ..models.face_is_planar import FaceIsPlanar
from ..models.get_entity_type import GetEntityType
from ..models.get_num_objects import GetNumObjects
from ..models.get_sketch_mode_plane import GetSketchModePlane
from ..models.highlight_set_entity import HighlightSetEntity
from ..models.import_files import ImportFiles
from ..models.imported_geometry import ImportedGeometry
from ..models.mass import Mass
from ..models.mouse_click import MouseClick
from ..models.path_get_curve_uuids_for_vertices import PathGetCurveUuidsForVertices
from ..models.path_get_info import PathGetInfo
from ..models.path_get_vertex_uuids import PathGetVertexUuids
from ..models.path_segment_info import PathSegmentInfo
from ..models.plane_intersect_and_project import PlaneIntersectAndProject
from ..models.select_get import SelectGet
from ..models.select_with_point import SelectWithPoint
from ..models.solid3d_get_all_edge_faces import Solid3dGetAllEdgeFaces
from ..models.solid3d_get_all_opposite_edges import Solid3dGetAllOppositeEdges
from ..models.solid3d_get_extrusion_face_info import Solid3dGetExtrusionFaceInfo
from ..models.solid3d_get_next_adjacent_edge import Solid3dGetNextAdjacentEdge
from ..models.solid3d_get_opposite_edge import Solid3dGetOppositeEdge
from ..models.solid3d_get_prev_adjacent_edge import Solid3dGetPrevAdjacentEdge
from ..models.surface_area import SurfaceArea
from ..models.take_snapshot import TakeSnapshot
from ..models.view_isometric import ViewIsometric
from ..models.volume import Volume
from ..models.zoom_to_fit import ZoomToFit


class empty(BaseModel):
    """An empty response, used for any command that does not explicitly have a response defined here."""

    type: Literal["empty"] = "empty"

    model_config = ConfigDict(protected_namespaces=())


class export(BaseModel):
    """The response to the 'Export' endpoint"""

    data: Export

    type: Literal["export"] = "export"

    model_config = ConfigDict(protected_namespaces=())


class select_with_point(BaseModel):
    """The response to the 'SelectWithPoint' endpoint"""

    data: SelectWithPoint

    type: Literal["select_with_point"] = "select_with_point"

    model_config = ConfigDict(protected_namespaces=())


class highlight_set_entity(BaseModel):
    """The response to the 'HighlightSetEntity' endpoint"""

    data: HighlightSetEntity

    type: Literal["highlight_set_entity"] = "highlight_set_entity"

    model_config = ConfigDict(protected_namespaces=())


class entity_get_child_uuid(BaseModel):
    """The response to the 'EntityGetChildUuid' endpoint"""

    data: EntityGetChildUuid

    type: Literal["entity_get_child_uuid"] = "entity_get_child_uuid"

    model_config = ConfigDict(protected_namespaces=())


class entity_get_num_children(BaseModel):
    """The response to the 'EntityGetNumChildren' endpoint"""

    data: EntityGetNumChildren

    type: Literal["entity_get_num_children"] = "entity_get_num_children"

    model_config = ConfigDict(protected_namespaces=())


class entity_get_parent_id(BaseModel):
    """The response to the 'EntityGetParentId' endpoint"""

    data: EntityGetParentId

    type: Literal["entity_get_parent_id"] = "entity_get_parent_id"

    model_config = ConfigDict(protected_namespaces=())


class entity_get_all_child_uuids(BaseModel):
    """The response to the 'EntityGetAllChildUuids' endpoint"""

    data: EntityGetAllChildUuids

    type: Literal["entity_get_all_child_uuids"] = "entity_get_all_child_uuids"

    model_config = ConfigDict(protected_namespaces=())


class close_path(BaseModel):
    """The response to the 'ClosePath' endpoint"""

    data: ClosePath

    type: Literal["close_path"] = "close_path"

    model_config = ConfigDict(protected_namespaces=())


class camera_drag_move(BaseModel):
    """The response to the 'CameraDragMove' endpoint"""

    data: CameraDragMove

    type: Literal["camera_drag_move"] = "camera_drag_move"

    model_config = ConfigDict(protected_namespaces=())


class camera_drag_end(BaseModel):
    """The response to the 'CameraDragEnd' endpoint"""

    data: CameraDragEnd

    type: Literal["camera_drag_end"] = "camera_drag_end"

    model_config = ConfigDict(protected_namespaces=())


class default_camera_get_settings(BaseModel):
    """The response to the 'DefaultCameraGetSettings' endpoint"""

    data: DefaultCameraGetSettings

    type: Literal["default_camera_get_settings"] = "default_camera_get_settings"

    model_config = ConfigDict(protected_namespaces=())


class default_camera_zoom(BaseModel):
    """The response to the 'DefaultCameraZoom' endpoint"""

    data: DefaultCameraZoom

    type: Literal["default_camera_zoom"] = "default_camera_zoom"

    model_config = ConfigDict(protected_namespaces=())


class zoom_to_fit(BaseModel):
    """The response to the 'ZoomToFit' endpoint"""

    data: ZoomToFit

    type: Literal["zoom_to_fit"] = "zoom_to_fit"

    model_config = ConfigDict(protected_namespaces=())


class view_isometric(BaseModel):
    """The response to the 'ViewIsometric' endpoint"""

    data: ViewIsometric

    type: Literal["view_isometric"] = "view_isometric"

    model_config = ConfigDict(protected_namespaces=())


class get_num_objects(BaseModel):
    """The response to the 'GetNumObjects' endpoint"""

    data: GetNumObjects

    type: Literal["get_num_objects"] = "get_num_objects"

    model_config = ConfigDict(protected_namespaces=())


class default_camera_focus_on(BaseModel):
    """The response to the 'DefaultCameraFocusOn' endpoint"""

    data: DefaultCameraFocusOn

    type: Literal["default_camera_focus_on"] = "default_camera_focus_on"

    model_config = ConfigDict(protected_namespaces=())


class select_get(BaseModel):
    """The response to the 'SelectGet' endpoint"""

    data: SelectGet

    type: Literal["select_get"] = "select_get"

    model_config = ConfigDict(protected_namespaces=())


class solid3d_get_all_edge_faces(BaseModel):
    """The response to the 'Solid3dGetAllEdgeFaces' endpoint"""

    data: Solid3dGetAllEdgeFaces

    type: Literal["solid3d_get_all_edge_faces"] = "solid3d_get_all_edge_faces"

    model_config = ConfigDict(protected_namespaces=())


class solid3d_get_all_opposite_edges(BaseModel):
    """The response to the 'Solid3dGetAllOppositeEdges' endpoint"""

    data: Solid3dGetAllOppositeEdges

    type: Literal["solid3d_get_all_opposite_edges"] = "solid3d_get_all_opposite_edges"

    model_config = ConfigDict(protected_namespaces=())


class solid3d_get_opposite_edge(BaseModel):
    """The response to the 'Solid3dGetOppositeEdge' endpoint"""

    data: Solid3dGetOppositeEdge

    type: Literal["solid3d_get_opposite_edge"] = "solid3d_get_opposite_edge"

    model_config = ConfigDict(protected_namespaces=())


class solid3d_get_next_adjacent_edge(BaseModel):
    """The response to the 'Solid3dGetNextAdjacentEdge' endpoint"""

    data: Solid3dGetNextAdjacentEdge

    type: Literal["solid3d_get_next_adjacent_edge"] = "solid3d_get_next_adjacent_edge"

    model_config = ConfigDict(protected_namespaces=())


class solid3d_get_prev_adjacent_edge(BaseModel):
    """The response to the 'Solid3dGetPrevAdjacentEdge' endpoint"""

    data: Solid3dGetPrevAdjacentEdge

    type: Literal["solid3d_get_prev_adjacent_edge"] = "solid3d_get_prev_adjacent_edge"

    model_config = ConfigDict(protected_namespaces=())


class get_entity_type(BaseModel):
    """The response to the 'GetEntityType' endpoint"""

    data: GetEntityType

    type: Literal["get_entity_type"] = "get_entity_type"

    model_config = ConfigDict(protected_namespaces=())


class curve_get_control_points(BaseModel):
    """The response to the 'CurveGetControlPoints' endpoint"""

    data: CurveGetControlPoints

    type: Literal["curve_get_control_points"] = "curve_get_control_points"

    model_config = ConfigDict(protected_namespaces=())


class curve_get_type(BaseModel):
    """The response to the 'CurveGetType' endpoint"""

    data: CurveGetType

    type: Literal["curve_get_type"] = "curve_get_type"

    model_config = ConfigDict(protected_namespaces=())


class mouse_click(BaseModel):
    """The response to the 'MouseClick' endpoint"""

    data: MouseClick

    type: Literal["mouse_click"] = "mouse_click"

    model_config = ConfigDict(protected_namespaces=())


class take_snapshot(BaseModel):
    """The response to the 'TakeSnapshot' endpoint"""

    data: TakeSnapshot

    type: Literal["take_snapshot"] = "take_snapshot"

    model_config = ConfigDict(protected_namespaces=())


class path_get_info(BaseModel):
    """The response to the 'PathGetInfo' endpoint"""

    data: PathGetInfo

    type: Literal["path_get_info"] = "path_get_info"

    model_config = ConfigDict(protected_namespaces=())


class path_segment_info(BaseModel):
    """The response to the 'PathSegmentInfo' endpoint"""

    data: PathSegmentInfo

    type: Literal["path_segment_info"] = "path_segment_info"

    model_config = ConfigDict(protected_namespaces=())


class path_get_curve_uuids_for_vertices(BaseModel):
    """The response to the 'PathGetCurveUuidsForVertices' endpoint"""

    data: PathGetCurveUuidsForVertices

    type: Literal["path_get_curve_uuids_for_vertices"] = (
        "path_get_curve_uuids_for_vertices"
    )

    model_config = ConfigDict(protected_namespaces=())


class path_get_vertex_uuids(BaseModel):
    """The response to the 'PathGetVertexUuids' endpoint"""

    data: PathGetVertexUuids

    type: Literal["path_get_vertex_uuids"] = "path_get_vertex_uuids"

    model_config = ConfigDict(protected_namespaces=())


class curve_get_end_points(BaseModel):
    """The response to the 'CurveGetEndPoints' endpoint"""

    data: CurveGetEndPoints

    type: Literal["curve_get_end_points"] = "curve_get_end_points"

    model_config = ConfigDict(protected_namespaces=())


class face_is_planar(BaseModel):
    """The response to the 'FaceIsPlanar' endpoint"""

    data: FaceIsPlanar

    type: Literal["face_is_planar"] = "face_is_planar"

    model_config = ConfigDict(protected_namespaces=())


class face_get_position(BaseModel):
    """The response to the 'FaceGetPosition' endpoint"""

    data: FaceGetPosition

    type: Literal["face_get_position"] = "face_get_position"

    model_config = ConfigDict(protected_namespaces=())


class face_get_center(BaseModel):
    """The response to the 'FaceGetCenter' endpoint"""

    data: FaceGetCenter

    type: Literal["face_get_center"] = "face_get_center"

    model_config = ConfigDict(protected_namespaces=())


class face_get_gradient(BaseModel):
    """The response to the 'FaceGetGradient' endpoint"""

    data: FaceGetGradient

    type: Literal["face_get_gradient"] = "face_get_gradient"

    model_config = ConfigDict(protected_namespaces=())


class plane_intersect_and_project(BaseModel):
    """The response to the 'PlaneIntersectAndProject' endpoint"""

    data: PlaneIntersectAndProject

    type: Literal["plane_intersect_and_project"] = "plane_intersect_and_project"

    model_config = ConfigDict(protected_namespaces=())


class import_files(BaseModel):
    """The response to the 'ImportFiles' endpoint"""

    data: ImportFiles

    type: Literal["import_files"] = "import_files"

    model_config = ConfigDict(protected_namespaces=())


class imported_geometry(BaseModel):
    """The response to the 'ImportedGeometry' endpoint"""

    data: ImportedGeometry

    type: Literal["imported_geometry"] = "imported_geometry"

    model_config = ConfigDict(protected_namespaces=())


class mass(BaseModel):
    """The response to the 'Mass' endpoint"""

    data: Mass

    type: Literal["mass"] = "mass"

    model_config = ConfigDict(protected_namespaces=())


class volume(BaseModel):
    """The response to the 'Volume' endpoint"""

    data: Volume

    type: Literal["volume"] = "volume"

    model_config = ConfigDict(protected_namespaces=())


class density(BaseModel):
    """The response to the 'Density' endpoint"""

    data: Density

    type: Literal["density"] = "density"

    model_config = ConfigDict(protected_namespaces=())


class surface_area(BaseModel):
    """The response to the 'SurfaceArea' endpoint"""

    data: SurfaceArea

    type: Literal["surface_area"] = "surface_area"

    model_config = ConfigDict(protected_namespaces=())


class center_of_mass(BaseModel):
    """The response to the 'CenterOfMass' endpoint"""

    data: CenterOfMass

    type: Literal["center_of_mass"] = "center_of_mass"

    model_config = ConfigDict(protected_namespaces=())


class get_sketch_mode_plane(BaseModel):
    """The response to the 'GetSketchModePlane' endpoint"""

    data: GetSketchModePlane

    type: Literal["get_sketch_mode_plane"] = "get_sketch_mode_plane"

    model_config = ConfigDict(protected_namespaces=())


class entity_get_distance(BaseModel):
    """The response to the 'EntityGetDistance' endpoint"""

    data: EntityGetDistance

    type: Literal["entity_get_distance"] = "entity_get_distance"

    model_config = ConfigDict(protected_namespaces=())


class entity_linear_pattern_transform(BaseModel):
    """The response to the 'EntityLinearPatternTransform' endpoint"""

    data: EntityLinearPatternTransform

    type: Literal["entity_linear_pattern_transform"] = "entity_linear_pattern_transform"

    model_config = ConfigDict(protected_namespaces=())


class entity_linear_pattern(BaseModel):
    """The response to the 'EntityLinearPattern' endpoint"""

    data: EntityLinearPattern

    type: Literal["entity_linear_pattern"] = "entity_linear_pattern"

    model_config = ConfigDict(protected_namespaces=())


class entity_circular_pattern(BaseModel):
    """The response to the 'EntityCircularPattern' endpoint"""

    data: EntityCircularPattern

    type: Literal["entity_circular_pattern"] = "entity_circular_pattern"

    model_config = ConfigDict(protected_namespaces=())


class solid3d_get_extrusion_face_info(BaseModel):
    """The response to the 'Solid3dGetExtrusionFaceInfo' endpoint"""

    data: Solid3dGetExtrusionFaceInfo

    type: Literal["solid3d_get_extrusion_face_info"] = "solid3d_get_extrusion_face_info"

    model_config = ConfigDict(protected_namespaces=())


class extrusion_face_info(BaseModel):
    """The response to the 'ExtrusionFaceInfo' endpoint"""

    data: ExtrusionFaceInfo

    type: Literal["extrusion_face_info"] = "extrusion_face_info"

    model_config = ConfigDict(protected_namespaces=())


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
            close_path,
            camera_drag_move,
            camera_drag_end,
            default_camera_get_settings,
            default_camera_zoom,
            zoom_to_fit,
            view_isometric,
            get_num_objects,
            default_camera_focus_on,
            select_get,
            solid3d_get_all_edge_faces,
            solid3d_get_all_opposite_edges,
            solid3d_get_opposite_edge,
            solid3d_get_next_adjacent_edge,
            solid3d_get_prev_adjacent_edge,
            get_entity_type,
            curve_get_control_points,
            curve_get_type,
            mouse_click,
            take_snapshot,
            path_get_info,
            path_segment_info,
            path_get_curve_uuids_for_vertices,
            path_get_vertex_uuids,
            curve_get_end_points,
            face_is_planar,
            face_get_position,
            face_get_center,
            face_get_gradient,
            plane_intersect_and_project,
            import_files,
            imported_geometry,
            mass,
            volume,
            density,
            surface_area,
            center_of_mass,
            get_sketch_mode_plane,
            entity_get_distance,
            entity_linear_pattern_transform,
            entity_linear_pattern,
            entity_circular_pattern,
            solid3d_get_extrusion_face_info,
            extrusion_face_info,
        ],
        Field(discriminator="type"),
    ]
]
