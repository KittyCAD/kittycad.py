from typing import Literal, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.add_hole_from_offset import AddHoleFromOffset
from ..models.adjacency_info import AdjacencyInfo
from ..models.boolean_intersection import BooleanIntersection
from ..models.boolean_subtract import BooleanSubtract
from ..models.boolean_union import BooleanUnion
from ..models.camera_drag_end import CameraDragEnd
from ..models.camera_drag_move import CameraDragMove
from ..models.camera_drag_start import CameraDragStart
from ..models.center_of_mass import CenterOfMass
from ..models.close_path import ClosePath
from ..models.complementary_edges import ComplementaryEdges
from ..models.curve_get_control_points import CurveGetControlPoints
from ..models.curve_get_end_points import CurveGetEndPoints
from ..models.curve_get_type import CurveGetType
from ..models.curve_set_constraint import CurveSetConstraint
from ..models.default_camera_center_to_scene import DefaultCameraCenterToScene
from ..models.default_camera_center_to_selection import DefaultCameraCenterToSelection
from ..models.default_camera_focus_on import DefaultCameraFocusOn
from ..models.default_camera_get_settings import DefaultCameraGetSettings
from ..models.default_camera_get_view import DefaultCameraGetView
from ..models.default_camera_look_at import DefaultCameraLookAt
from ..models.default_camera_perspective_settings import (
    DefaultCameraPerspectiveSettings,
)
from ..models.default_camera_set_orthographic import DefaultCameraSetOrthographic
from ..models.default_camera_set_perspective import DefaultCameraSetPerspective
from ..models.default_camera_set_view import DefaultCameraSetView
from ..models.default_camera_zoom import DefaultCameraZoom
from ..models.density import Density
from ..models.disable_dry_run import DisableDryRun
from ..models.edge_info import EdgeInfo
from ..models.edge_lines_visible import EdgeLinesVisible
from ..models.enable_dry_run import EnableDryRun
from ..models.enable_sketch_mode import EnableSketchMode
from ..models.engine_util_evaluate_path import EngineUtilEvaluatePath
from ..models.entity_circular_pattern import EntityCircularPattern
from ..models.entity_clone import EntityClone
from ..models.entity_fade import EntityFade
from ..models.entity_get_all_child_uuids import EntityGetAllChildUuids
from ..models.entity_get_child_uuid import EntityGetChildUuid
from ..models.entity_get_distance import EntityGetDistance
from ..models.entity_get_num_children import EntityGetNumChildren
from ..models.entity_get_parent_id import EntityGetParentId
from ..models.entity_get_sketch_paths import EntityGetSketchPaths
from ..models.entity_linear_pattern import EntityLinearPattern
from ..models.entity_linear_pattern_transform import EntityLinearPatternTransform
from ..models.entity_make_helix import EntityMakeHelix
from ..models.entity_make_helix_from_edge import EntityMakeHelixFromEdge
from ..models.entity_make_helix_from_params import EntityMakeHelixFromParams
from ..models.entity_mirror import EntityMirror
from ..models.entity_mirror_across_edge import EntityMirrorAcrossEdge
from ..models.entity_set_opacity import EntitySetOpacity
from ..models.export import Export
from ..models.export2d import Export2d
from ..models.export3d import Export3d
from ..models.extend_path import ExtendPath
from ..models.extrude import Extrude
from ..models.extrude_to_reference import ExtrudeToReference
from ..models.extrusion_face_info import ExtrusionFaceInfo
from ..models.face_edge_info import FaceEdgeInfo
from ..models.face_get_center import FaceGetCenter
from ..models.face_get_gradient import FaceGetGradient
from ..models.face_get_position import FaceGetPosition
from ..models.face_is_planar import FaceIsPlanar
from ..models.get_entity_type import GetEntityType
from ..models.get_num_objects import GetNumObjects
from ..models.get_sketch_mode_plane import GetSketchModePlane
from ..models.handle_mouse_drag_end import HandleMouseDragEnd
from ..models.handle_mouse_drag_move import HandleMouseDragMove
from ..models.handle_mouse_drag_start import HandleMouseDragStart
from ..models.highlight_set_entities import HighlightSetEntities
from ..models.highlight_set_entity import HighlightSetEntity
from ..models.import_files import ImportFiles
from ..models.imported_geometry import ImportedGeometry
from ..models.loft import Loft
from ..models.make_axes_gizmo import MakeAxesGizmo
from ..models.make_offset_path import MakeOffsetPath
from ..models.make_plane import MakePlane
from ..models.mass import Mass
from ..models.mouse_click import MouseClick
from ..models.mouse_move import MouseMove
from ..models.move_path_pen import MovePathPen
from ..models.new_annotation import NewAnnotation
from ..models.object_bring_to_front import ObjectBringToFront
from ..models.object_set_material_params_pbr import ObjectSetMaterialParamsPbr
from ..models.object_visible import ObjectVisible
from ..models.orient_to_face import OrientToFace
from ..models.path_get_curve_uuid import PathGetCurveUuid
from ..models.path_get_curve_uuids_for_vertices import PathGetCurveUuidsForVertices
from ..models.path_get_info import PathGetInfo
from ..models.path_get_sketch_target_uuid import PathGetSketchTargetUuid
from ..models.path_get_vertex_uuids import PathGetVertexUuids
from ..models.path_segment_info import PathSegmentInfo
from ..models.plane_intersect_and_project import PlaneIntersectAndProject
from ..models.plane_set_color import PlaneSetColor
from ..models.project_entity_to_plane import ProjectEntityToPlane
from ..models.project_points_to_plane import ProjectPointsToPlane
from ..models.reconfigure_stream import ReconfigureStream
from ..models.remove_scene_objects import RemoveSceneObjects
from ..models.revolve import Revolve
from ..models.revolve_about_edge import RevolveAboutEdge
from ..models.scene_clear_all import SceneClearAll
from ..models.scene_get_entity_ids import SceneGetEntityIds
from ..models.select_add import SelectAdd
from ..models.select_clear import SelectClear
from ..models.select_get import SelectGet
from ..models.select_remove import SelectRemove
from ..models.select_replace import SelectReplace
from ..models.select_with_point import SelectWithPoint
from ..models.send_object import SendObject
from ..models.set_background_color import SetBackgroundColor
from ..models.set_current_tool_properties import SetCurrentToolProperties
from ..models.set_default_system_properties import SetDefaultSystemProperties
from ..models.set_grid_auto_scale import SetGridAutoScale
from ..models.set_grid_reference_plane import SetGridReferencePlane
from ..models.set_grid_scale import SetGridScale
from ..models.set_object_transform import SetObjectTransform
from ..models.set_order_independent_transparency import SetOrderIndependentTransparency
from ..models.set_scene_units import SetSceneUnits
from ..models.set_selection_filter import SetSelectionFilter
from ..models.set_selection_type import SetSelectionType
from ..models.set_tool import SetTool
from ..models.sketch_mode_disable import SketchModeDisable
from ..models.solid2d_add_hole import Solid2dAddHole
from ..models.solid3d_cut_edges import Solid3dCutEdges
from ..models.solid3d_fillet_edge import Solid3dFilletEdge
from ..models.solid3d_get_adjacency_info import Solid3dGetAdjacencyInfo
from ..models.solid3d_get_all_edge_faces import Solid3dGetAllEdgeFaces
from ..models.solid3d_get_all_opposite_edges import Solid3dGetAllOppositeEdges
from ..models.solid3d_get_common_edge import Solid3dGetCommonEdge
from ..models.solid3d_get_extrusion_face_info import Solid3dGetExtrusionFaceInfo
from ..models.solid3d_get_next_adjacent_edge import Solid3dGetNextAdjacentEdge
from ..models.solid3d_get_opposite_edge import Solid3dGetOppositeEdge
from ..models.solid3d_get_prev_adjacent_edge import Solid3dGetPrevAdjacentEdge
from ..models.solid3d_shell_face import Solid3dShellFace
from ..models.start_path import StartPath
from ..models.surface_area import SurfaceArea
from ..models.sweep import Sweep
from ..models.take_snapshot import TakeSnapshot
from ..models.twist_extrude import TwistExtrude
from ..models.update_annotation import UpdateAnnotation
from ..models.view_isometric import ViewIsometric
from ..models.volume import Volume
from ..models.zoom_to_fit import ZoomToFit
from .base import KittyCadBaseModel


class OptionEmpty(KittyCadBaseModel):
    """An empty response, used for any command that does not explicitly have a response defined here."""

    type: Literal["empty"] = "empty"


class OptionEngineUtilEvaluatePath(KittyCadBaseModel):
    """"""

    data: EngineUtilEvaluatePath

    type: Literal["engine_util_evaluate_path"] = "engine_util_evaluate_path"


class OptionStartPath(KittyCadBaseModel):
    """"""

    data: StartPath

    type: Literal["start_path"] = "start_path"


class OptionMovePathPen(KittyCadBaseModel):
    """"""

    data: MovePathPen

    type: Literal["move_path_pen"] = "move_path_pen"


class OptionExtendPath(KittyCadBaseModel):
    """"""

    data: ExtendPath

    type: Literal["extend_path"] = "extend_path"


class OptionExtrude(KittyCadBaseModel):
    """"""

    data: Extrude

    type: Literal["extrude"] = "extrude"


class OptionExtrudeToReference(KittyCadBaseModel):
    """"""

    data: ExtrudeToReference

    type: Literal["extrude_to_reference"] = "extrude_to_reference"


class OptionTwistExtrude(KittyCadBaseModel):
    """"""

    data: TwistExtrude

    type: Literal["twist_extrude"] = "twist_extrude"


class OptionSweep(KittyCadBaseModel):
    """"""

    data: Sweep

    type: Literal["sweep"] = "sweep"


class OptionRevolve(KittyCadBaseModel):
    """"""

    data: Revolve

    type: Literal["revolve"] = "revolve"


class OptionSolid3dShellFace(KittyCadBaseModel):
    """"""

    data: Solid3dShellFace

    type: Literal["solid3d_shell_face"] = "solid3d_shell_face"


class OptionRevolveAboutEdge(KittyCadBaseModel):
    """"""

    data: RevolveAboutEdge

    type: Literal["revolve_about_edge"] = "revolve_about_edge"


class OptionCameraDragStart(KittyCadBaseModel):
    """"""

    data: CameraDragStart

    type: Literal["camera_drag_start"] = "camera_drag_start"


class OptionDefaultCameraLookAt(KittyCadBaseModel):
    """"""

    data: DefaultCameraLookAt

    type: Literal["default_camera_look_at"] = "default_camera_look_at"


class OptionDefaultCameraPerspectiveSettings(KittyCadBaseModel):
    """"""

    data: DefaultCameraPerspectiveSettings

    type: Literal["default_camera_perspective_settings"] = (
        "default_camera_perspective_settings"
    )


class OptionSelectAdd(KittyCadBaseModel):
    """"""

    data: SelectAdd

    type: Literal["select_add"] = "select_add"


class OptionSelectRemove(KittyCadBaseModel):
    """"""

    data: SelectRemove

    type: Literal["select_remove"] = "select_remove"


class OptionSceneClearAll(KittyCadBaseModel):
    """"""

    data: SceneClearAll

    type: Literal["scene_clear_all"] = "scene_clear_all"


class OptionSelectReplace(KittyCadBaseModel):
    """"""

    data: SelectReplace

    type: Literal["select_replace"] = "select_replace"


class OptionHighlightSetEntities(KittyCadBaseModel):
    """"""

    data: HighlightSetEntities

    type: Literal["highlight_set_entities"] = "highlight_set_entities"


class OptionNewAnnotation(KittyCadBaseModel):
    """"""

    data: NewAnnotation

    type: Literal["new_annotation"] = "new_annotation"


class OptionUpdateAnnotation(KittyCadBaseModel):
    """"""

    data: UpdateAnnotation

    type: Literal["update_annotation"] = "update_annotation"


class OptionEdgeLinesVisible(KittyCadBaseModel):
    """"""

    data: EdgeLinesVisible

    type: Literal["edge_lines_visible"] = "edge_lines_visible"


class OptionObjectVisible(KittyCadBaseModel):
    """"""

    data: ObjectVisible

    type: Literal["object_visible"] = "object_visible"


class OptionObjectBringToFront(KittyCadBaseModel):
    """"""

    data: ObjectBringToFront

    type: Literal["object_bring_to_front"] = "object_bring_to_front"


class OptionObjectSetMaterialParamsPbr(KittyCadBaseModel):
    """"""

    data: ObjectSetMaterialParamsPbr

    type: Literal["object_set_material_params_pbr"] = "object_set_material_params_pbr"


class OptionSolid2dAddHole(KittyCadBaseModel):
    """"""

    data: Solid2dAddHole

    type: Literal["solid2d_add_hole"] = "solid2d_add_hole"


class OptionSolid3dFilletEdge(KittyCadBaseModel):
    """"""

    data: Solid3dFilletEdge

    type: Literal["solid3d_fillet_edge"] = "solid3d_fillet_edge"


class OptionSolid3dCutEdges(KittyCadBaseModel):
    """"""

    data: Solid3dCutEdges

    type: Literal["solid3d_cut_edges"] = "solid3d_cut_edges"


class OptionSendObject(KittyCadBaseModel):
    """"""

    data: SendObject

    type: Literal["send_object"] = "send_object"


class OptionEntitySetOpacity(KittyCadBaseModel):
    """"""

    data: EntitySetOpacity

    type: Literal["entity_set_opacity"] = "entity_set_opacity"


class OptionEntityFade(KittyCadBaseModel):
    """"""

    data: EntityFade

    type: Literal["entity_fade"] = "entity_fade"


class OptionMakePlane(KittyCadBaseModel):
    """"""

    data: MakePlane

    type: Literal["make_plane"] = "make_plane"


class OptionPlaneSetColor(KittyCadBaseModel):
    """"""

    data: PlaneSetColor

    type: Literal["plane_set_color"] = "plane_set_color"


class OptionSetTool(KittyCadBaseModel):
    """"""

    data: SetTool

    type: Literal["set_tool"] = "set_tool"


class OptionMouseMove(KittyCadBaseModel):
    """"""

    data: MouseMove

    type: Literal["mouse_move"] = "mouse_move"


class OptionSketchModeDisable(KittyCadBaseModel):
    """"""

    data: SketchModeDisable

    type: Literal["sketch_mode_disable"] = "sketch_mode_disable"


class OptionEnableDryRun(KittyCadBaseModel):
    """"""

    data: EnableDryRun

    type: Literal["enable_dry_run"] = "enable_dry_run"


class OptionDisableDryRun(KittyCadBaseModel):
    """"""

    data: DisableDryRun

    type: Literal["disable_dry_run"] = "disable_dry_run"


class OptionCurveSetConstraint(KittyCadBaseModel):
    """"""

    data: CurveSetConstraint

    type: Literal["curve_set_constraint"] = "curve_set_constraint"


class OptionEnableSketchMode(KittyCadBaseModel):
    """"""

    data: EnableSketchMode

    type: Literal["enable_sketch_mode"] = "enable_sketch_mode"


class OptionSetBackgroundColor(KittyCadBaseModel):
    """"""

    data: SetBackgroundColor

    type: Literal["set_background_color"] = "set_background_color"


class OptionSetCurrentToolProperties(KittyCadBaseModel):
    """"""

    data: SetCurrentToolProperties

    type: Literal["set_current_tool_properties"] = "set_current_tool_properties"


class OptionSetDefaultSystemProperties(KittyCadBaseModel):
    """"""

    data: SetDefaultSystemProperties

    type: Literal["set_default_system_properties"] = "set_default_system_properties"


class OptionMakeAxesGizmo(KittyCadBaseModel):
    """"""

    data: MakeAxesGizmo

    type: Literal["make_axes_gizmo"] = "make_axes_gizmo"


class OptionHandleMouseDragStart(KittyCadBaseModel):
    """"""

    data: HandleMouseDragStart

    type: Literal["handle_mouse_drag_start"] = "handle_mouse_drag_start"


class OptionHandleMouseDragMove(KittyCadBaseModel):
    """"""

    data: HandleMouseDragMove

    type: Literal["handle_mouse_drag_move"] = "handle_mouse_drag_move"


class OptionHandleMouseDragEnd(KittyCadBaseModel):
    """"""

    data: HandleMouseDragEnd

    type: Literal["handle_mouse_drag_end"] = "handle_mouse_drag_end"


class OptionRemoveSceneObjects(KittyCadBaseModel):
    """"""

    data: RemoveSceneObjects

    type: Literal["remove_scene_objects"] = "remove_scene_objects"


class OptionReconfigureStream(KittyCadBaseModel):
    """"""

    data: ReconfigureStream

    type: Literal["reconfigure_stream"] = "reconfigure_stream"


class OptionSetSceneUnits(KittyCadBaseModel):
    """"""

    data: SetSceneUnits

    type: Literal["set_scene_units"] = "set_scene_units"


class OptionSetSelectionType(KittyCadBaseModel):
    """"""

    data: SetSelectionType

    type: Literal["set_selection_type"] = "set_selection_type"


class OptionSetSelectionFilter(KittyCadBaseModel):
    """"""

    data: SetSelectionFilter

    type: Literal["set_selection_filter"] = "set_selection_filter"


class OptionDefaultCameraSetOrthographic(KittyCadBaseModel):
    """"""

    data: DefaultCameraSetOrthographic

    type: Literal["default_camera_set_orthographic"] = "default_camera_set_orthographic"


class OptionDefaultCameraSetPerspective(KittyCadBaseModel):
    """"""

    data: DefaultCameraSetPerspective

    type: Literal["default_camera_set_perspective"] = "default_camera_set_perspective"


class OptionDefaultCameraCenterToSelection(KittyCadBaseModel):
    """"""

    data: DefaultCameraCenterToSelection

    type: Literal["default_camera_center_to_selection"] = (
        "default_camera_center_to_selection"
    )


class OptionDefaultCameraCenterToScene(KittyCadBaseModel):
    """"""

    data: DefaultCameraCenterToScene

    type: Literal["default_camera_center_to_scene"] = "default_camera_center_to_scene"


class OptionSelectClear(KittyCadBaseModel):
    """"""

    data: SelectClear

    type: Literal["select_clear"] = "select_clear"


class OptionExport2d(KittyCadBaseModel):
    """"""

    data: Export2d

    type: Literal["export2d"] = "export2d"


class OptionExport3d(KittyCadBaseModel):
    """"""

    data: Export3d

    type: Literal["export3d"] = "export3d"


class OptionExport(KittyCadBaseModel):
    """"""

    data: Export

    type: Literal["export"] = "export"


class OptionSelectWithPoint(KittyCadBaseModel):
    """"""

    data: SelectWithPoint

    type: Literal["select_with_point"] = "select_with_point"


class OptionHighlightSetEntity(KittyCadBaseModel):
    """"""

    data: HighlightSetEntity

    type: Literal["highlight_set_entity"] = "highlight_set_entity"


class OptionEntityGetChildUuid(KittyCadBaseModel):
    """"""

    data: EntityGetChildUuid

    type: Literal["entity_get_child_uuid"] = "entity_get_child_uuid"


class OptionEntityGetNumChildren(KittyCadBaseModel):
    """"""

    data: EntityGetNumChildren

    type: Literal["entity_get_num_children"] = "entity_get_num_children"


class OptionEntityGetParentId(KittyCadBaseModel):
    """"""

    data: EntityGetParentId

    type: Literal["entity_get_parent_id"] = "entity_get_parent_id"


class OptionEntityGetAllChildUuids(KittyCadBaseModel):
    """"""

    data: EntityGetAllChildUuids

    type: Literal["entity_get_all_child_uuids"] = "entity_get_all_child_uuids"


class OptionEntityGetSketchPaths(KittyCadBaseModel):
    """"""

    data: EntityGetSketchPaths

    type: Literal["entity_get_sketch_paths"] = "entity_get_sketch_paths"


class OptionLoft(KittyCadBaseModel):
    """"""

    data: Loft

    type: Literal["loft"] = "loft"


class OptionClosePath(KittyCadBaseModel):
    """"""

    data: ClosePath

    type: Literal["close_path"] = "close_path"


class OptionCameraDragMove(KittyCadBaseModel):
    """"""

    data: CameraDragMove

    type: Literal["camera_drag_move"] = "camera_drag_move"


class OptionCameraDragEnd(KittyCadBaseModel):
    """"""

    data: CameraDragEnd

    type: Literal["camera_drag_end"] = "camera_drag_end"


class OptionDefaultCameraGetSettings(KittyCadBaseModel):
    """"""

    data: DefaultCameraGetSettings

    type: Literal["default_camera_get_settings"] = "default_camera_get_settings"


class OptionDefaultCameraGetView(KittyCadBaseModel):
    """"""

    data: DefaultCameraGetView

    type: Literal["default_camera_get_view"] = "default_camera_get_view"


class OptionDefaultCameraSetView(KittyCadBaseModel):
    """"""

    data: DefaultCameraSetView

    type: Literal["default_camera_set_view"] = "default_camera_set_view"


class OptionDefaultCameraZoom(KittyCadBaseModel):
    """"""

    data: DefaultCameraZoom

    type: Literal["default_camera_zoom"] = "default_camera_zoom"


class OptionZoomToFit(KittyCadBaseModel):
    """"""

    data: ZoomToFit

    type: Literal["zoom_to_fit"] = "zoom_to_fit"


class OptionOrientToFace(KittyCadBaseModel):
    """"""

    data: OrientToFace

    type: Literal["orient_to_face"] = "orient_to_face"


class OptionViewIsometric(KittyCadBaseModel):
    """"""

    data: ViewIsometric

    type: Literal["view_isometric"] = "view_isometric"


class OptionGetNumObjects(KittyCadBaseModel):
    """"""

    data: GetNumObjects

    type: Literal["get_num_objects"] = "get_num_objects"


class OptionMakeOffsetPath(KittyCadBaseModel):
    """"""

    data: MakeOffsetPath

    type: Literal["make_offset_path"] = "make_offset_path"


class OptionSetObjectTransform(KittyCadBaseModel):
    """"""

    data: SetObjectTransform

    type: Literal["set_object_transform"] = "set_object_transform"


class OptionAddHoleFromOffset(KittyCadBaseModel):
    """"""

    data: AddHoleFromOffset

    type: Literal["add_hole_from_offset"] = "add_hole_from_offset"


class OptionDefaultCameraFocusOn(KittyCadBaseModel):
    """"""

    data: DefaultCameraFocusOn

    type: Literal["default_camera_focus_on"] = "default_camera_focus_on"


class OptionSelectGet(KittyCadBaseModel):
    """"""

    data: SelectGet

    type: Literal["select_get"] = "select_get"


class OptionSolid3dGetAdjacencyInfo(KittyCadBaseModel):
    """"""

    data: Solid3dGetAdjacencyInfo

    type: Literal["solid3d_get_adjacency_info"] = "solid3d_get_adjacency_info"


class OptionSolid3dGetAllEdgeFaces(KittyCadBaseModel):
    """"""

    data: Solid3dGetAllEdgeFaces

    type: Literal["solid3d_get_all_edge_faces"] = "solid3d_get_all_edge_faces"


class OptionSolid3dGetAllOppositeEdges(KittyCadBaseModel):
    """"""

    data: Solid3dGetAllOppositeEdges

    type: Literal["solid3d_get_all_opposite_edges"] = "solid3d_get_all_opposite_edges"


class OptionSolid3dGetOppositeEdge(KittyCadBaseModel):
    """"""

    data: Solid3dGetOppositeEdge

    type: Literal["solid3d_get_opposite_edge"] = "solid3d_get_opposite_edge"


class OptionSolid3dGetNextAdjacentEdge(KittyCadBaseModel):
    """"""

    data: Solid3dGetNextAdjacentEdge

    type: Literal["solid3d_get_next_adjacent_edge"] = "solid3d_get_next_adjacent_edge"


class OptionSolid3dGetPrevAdjacentEdge(KittyCadBaseModel):
    """"""

    data: Solid3dGetPrevAdjacentEdge

    type: Literal["solid3d_get_prev_adjacent_edge"] = "solid3d_get_prev_adjacent_edge"


class OptionSolid3dGetCommonEdge(KittyCadBaseModel):
    """"""

    data: Solid3dGetCommonEdge

    type: Literal["solid3d_get_common_edge"] = "solid3d_get_common_edge"


class OptionGetEntityType(KittyCadBaseModel):
    """"""

    data: GetEntityType

    type: Literal["get_entity_type"] = "get_entity_type"


class OptionSceneGetEntityIds(KittyCadBaseModel):
    """"""

    data: SceneGetEntityIds

    type: Literal["scene_get_entity_ids"] = "scene_get_entity_ids"


class OptionCurveGetControlPoints(KittyCadBaseModel):
    """"""

    data: CurveGetControlPoints

    type: Literal["curve_get_control_points"] = "curve_get_control_points"


class OptionProjectEntityToPlane(KittyCadBaseModel):
    """"""

    data: ProjectEntityToPlane

    type: Literal["project_entity_to_plane"] = "project_entity_to_plane"


class OptionProjectPointsToPlane(KittyCadBaseModel):
    """"""

    data: ProjectPointsToPlane

    type: Literal["project_points_to_plane"] = "project_points_to_plane"


class OptionCurveGetType(KittyCadBaseModel):
    """"""

    data: CurveGetType

    type: Literal["curve_get_type"] = "curve_get_type"


class OptionMouseClick(KittyCadBaseModel):
    """"""

    data: MouseClick

    type: Literal["mouse_click"] = "mouse_click"


class OptionTakeSnapshot(KittyCadBaseModel):
    """"""

    data: TakeSnapshot

    type: Literal["take_snapshot"] = "take_snapshot"


class OptionPathGetInfo(KittyCadBaseModel):
    """"""

    data: PathGetInfo

    type: Literal["path_get_info"] = "path_get_info"


class OptionPathSegmentInfo(KittyCadBaseModel):
    """"""

    data: PathSegmentInfo

    type: Literal["path_segment_info"] = "path_segment_info"


class OptionPathGetCurveUuidsForVertices(KittyCadBaseModel):
    """"""

    data: PathGetCurveUuidsForVertices

    type: Literal["path_get_curve_uuids_for_vertices"] = (
        "path_get_curve_uuids_for_vertices"
    )


class OptionPathGetCurveUuid(KittyCadBaseModel):
    """"""

    data: PathGetCurveUuid

    type: Literal["path_get_curve_uuid"] = "path_get_curve_uuid"


class OptionPathGetVertexUuids(KittyCadBaseModel):
    """"""

    data: PathGetVertexUuids

    type: Literal["path_get_vertex_uuids"] = "path_get_vertex_uuids"


class OptionPathGetSketchTargetUuid(KittyCadBaseModel):
    """"""

    data: PathGetSketchTargetUuid

    type: Literal["path_get_sketch_target_uuid"] = "path_get_sketch_target_uuid"


class OptionCurveGetEndPoints(KittyCadBaseModel):
    """"""

    data: CurveGetEndPoints

    type: Literal["curve_get_end_points"] = "curve_get_end_points"


class OptionFaceIsPlanar(KittyCadBaseModel):
    """"""

    data: FaceIsPlanar

    type: Literal["face_is_planar"] = "face_is_planar"


class OptionFaceGetPosition(KittyCadBaseModel):
    """"""

    data: FaceGetPosition

    type: Literal["face_get_position"] = "face_get_position"


class OptionFaceGetCenter(KittyCadBaseModel):
    """"""

    data: FaceGetCenter

    type: Literal["face_get_center"] = "face_get_center"


class OptionFaceGetGradient(KittyCadBaseModel):
    """"""

    data: FaceGetGradient

    type: Literal["face_get_gradient"] = "face_get_gradient"


class OptionPlaneIntersectAndProject(KittyCadBaseModel):
    """"""

    data: PlaneIntersectAndProject

    type: Literal["plane_intersect_and_project"] = "plane_intersect_and_project"


class OptionImportFiles(KittyCadBaseModel):
    """"""

    data: ImportFiles

    type: Literal["import_files"] = "import_files"


class OptionImportedGeometry(KittyCadBaseModel):
    """"""

    data: ImportedGeometry

    type: Literal["imported_geometry"] = "imported_geometry"


class OptionMass(KittyCadBaseModel):
    """"""

    data: Mass

    type: Literal["mass"] = "mass"


class OptionVolume(KittyCadBaseModel):
    """"""

    data: Volume

    type: Literal["volume"] = "volume"


class OptionDensity(KittyCadBaseModel):
    """"""

    data: Density

    type: Literal["density"] = "density"


class OptionSurfaceArea(KittyCadBaseModel):
    """"""

    data: SurfaceArea

    type: Literal["surface_area"] = "surface_area"


class OptionCenterOfMass(KittyCadBaseModel):
    """"""

    data: CenterOfMass

    type: Literal["center_of_mass"] = "center_of_mass"


class OptionGetSketchModePlane(KittyCadBaseModel):
    """"""

    data: GetSketchModePlane

    type: Literal["get_sketch_mode_plane"] = "get_sketch_mode_plane"


class OptionEntityGetDistance(KittyCadBaseModel):
    """"""

    data: EntityGetDistance

    type: Literal["entity_get_distance"] = "entity_get_distance"


class OptionFaceEdgeInfo(KittyCadBaseModel):
    """"""

    data: FaceEdgeInfo

    type: Literal["face_edge_info"] = "face_edge_info"


class OptionEdgeInfo(KittyCadBaseModel):
    """"""

    data: EdgeInfo

    type: Literal["edge_info"] = "edge_info"


class OptionEntityClone(KittyCadBaseModel):
    """"""

    data: EntityClone

    type: Literal["entity_clone"] = "entity_clone"


class OptionEntityLinearPatternTransform(KittyCadBaseModel):
    """"""

    data: EntityLinearPatternTransform

    type: Literal["entity_linear_pattern_transform"] = "entity_linear_pattern_transform"


class OptionEntityLinearPattern(KittyCadBaseModel):
    """"""

    data: EntityLinearPattern

    type: Literal["entity_linear_pattern"] = "entity_linear_pattern"


class OptionEntityCircularPattern(KittyCadBaseModel):
    """"""

    data: EntityCircularPattern

    type: Literal["entity_circular_pattern"] = "entity_circular_pattern"


class OptionEntityMirror(KittyCadBaseModel):
    """"""

    data: EntityMirror

    type: Literal["entity_mirror"] = "entity_mirror"


class OptionEntityMirrorAcrossEdge(KittyCadBaseModel):
    """"""

    data: EntityMirrorAcrossEdge

    type: Literal["entity_mirror_across_edge"] = "entity_mirror_across_edge"


class OptionEntityMakeHelix(KittyCadBaseModel):
    """"""

    data: EntityMakeHelix

    type: Literal["entity_make_helix"] = "entity_make_helix"


class OptionEntityMakeHelixFromParams(KittyCadBaseModel):
    """"""

    data: EntityMakeHelixFromParams

    type: Literal["entity_make_helix_from_params"] = "entity_make_helix_from_params"


class OptionEntityMakeHelixFromEdge(KittyCadBaseModel):
    """"""

    data: EntityMakeHelixFromEdge

    type: Literal["entity_make_helix_from_edge"] = "entity_make_helix_from_edge"


class OptionSolid3dGetExtrusionFaceInfo(KittyCadBaseModel):
    """"""

    data: Solid3dGetExtrusionFaceInfo

    type: Literal["solid3d_get_extrusion_face_info"] = "solid3d_get_extrusion_face_info"


class OptionExtrusionFaceInfo(KittyCadBaseModel):
    """"""

    data: ExtrusionFaceInfo

    type: Literal["extrusion_face_info"] = "extrusion_face_info"


class OptionComplementaryEdges(KittyCadBaseModel):
    """"""

    data: ComplementaryEdges

    type: Literal["complementary_edges"] = "complementary_edges"


class OptionAdjacencyInfo(KittyCadBaseModel):
    """"""

    data: AdjacencyInfo

    type: Literal["adjacency_info"] = "adjacency_info"


class OptionSetGridReferencePlane(KittyCadBaseModel):
    """"""

    data: SetGridReferencePlane

    type: Literal["set_grid_reference_plane"] = "set_grid_reference_plane"


class OptionBooleanUnion(KittyCadBaseModel):
    """"""

    data: BooleanUnion

    type: Literal["boolean_union"] = "boolean_union"


class OptionBooleanIntersection(KittyCadBaseModel):
    """"""

    data: BooleanIntersection

    type: Literal["boolean_intersection"] = "boolean_intersection"


class OptionBooleanSubtract(KittyCadBaseModel):
    """"""

    data: BooleanSubtract

    type: Literal["boolean_subtract"] = "boolean_subtract"


class OptionSetGridScale(KittyCadBaseModel):
    """"""

    data: SetGridScale

    type: Literal["set_grid_scale"] = "set_grid_scale"


class OptionSetGridAutoScale(KittyCadBaseModel):
    """"""

    data: SetGridAutoScale

    type: Literal["set_grid_auto_scale"] = "set_grid_auto_scale"


class OptionSetOrderIndependentTransparency(KittyCadBaseModel):
    """"""

    data: SetOrderIndependentTransparency

    type: Literal["set_order_independent_transparency"] = (
        "set_order_independent_transparency"
    )


OkModelingCmdResponse = RootModel[
    Annotated[
        Union[
            OptionEmpty,
            OptionEngineUtilEvaluatePath,
            OptionStartPath,
            OptionMovePathPen,
            OptionExtendPath,
            OptionExtrude,
            OptionExtrudeToReference,
            OptionTwistExtrude,
            OptionSweep,
            OptionRevolve,
            OptionSolid3dShellFace,
            OptionRevolveAboutEdge,
            OptionCameraDragStart,
            OptionDefaultCameraLookAt,
            OptionDefaultCameraPerspectiveSettings,
            OptionSelectAdd,
            OptionSelectRemove,
            OptionSceneClearAll,
            OptionSelectReplace,
            OptionHighlightSetEntities,
            OptionNewAnnotation,
            OptionUpdateAnnotation,
            OptionEdgeLinesVisible,
            OptionObjectVisible,
            OptionObjectBringToFront,
            OptionObjectSetMaterialParamsPbr,
            OptionSolid2dAddHole,
            OptionSolid3dFilletEdge,
            OptionSolid3dCutEdges,
            OptionSendObject,
            OptionEntitySetOpacity,
            OptionEntityFade,
            OptionMakePlane,
            OptionPlaneSetColor,
            OptionSetTool,
            OptionMouseMove,
            OptionSketchModeDisable,
            OptionEnableDryRun,
            OptionDisableDryRun,
            OptionCurveSetConstraint,
            OptionEnableSketchMode,
            OptionSetBackgroundColor,
            OptionSetCurrentToolProperties,
            OptionSetDefaultSystemProperties,
            OptionMakeAxesGizmo,
            OptionHandleMouseDragStart,
            OptionHandleMouseDragMove,
            OptionHandleMouseDragEnd,
            OptionRemoveSceneObjects,
            OptionReconfigureStream,
            OptionSetSceneUnits,
            OptionSetSelectionType,
            OptionSetSelectionFilter,
            OptionDefaultCameraSetOrthographic,
            OptionDefaultCameraSetPerspective,
            OptionDefaultCameraCenterToSelection,
            OptionDefaultCameraCenterToScene,
            OptionSelectClear,
            OptionExport2d,
            OptionExport3d,
            OptionExport,
            OptionSelectWithPoint,
            OptionHighlightSetEntity,
            OptionEntityGetChildUuid,
            OptionEntityGetNumChildren,
            OptionEntityGetParentId,
            OptionEntityGetAllChildUuids,
            OptionEntityGetSketchPaths,
            OptionLoft,
            OptionClosePath,
            OptionCameraDragMove,
            OptionCameraDragEnd,
            OptionDefaultCameraGetSettings,
            OptionDefaultCameraGetView,
            OptionDefaultCameraSetView,
            OptionDefaultCameraZoom,
            OptionZoomToFit,
            OptionOrientToFace,
            OptionViewIsometric,
            OptionGetNumObjects,
            OptionMakeOffsetPath,
            OptionSetObjectTransform,
            OptionAddHoleFromOffset,
            OptionDefaultCameraFocusOn,
            OptionSelectGet,
            OptionSolid3dGetAdjacencyInfo,
            OptionSolid3dGetAllEdgeFaces,
            OptionSolid3dGetAllOppositeEdges,
            OptionSolid3dGetOppositeEdge,
            OptionSolid3dGetNextAdjacentEdge,
            OptionSolid3dGetPrevAdjacentEdge,
            OptionSolid3dGetCommonEdge,
            OptionGetEntityType,
            OptionSceneGetEntityIds,
            OptionCurveGetControlPoints,
            OptionProjectEntityToPlane,
            OptionProjectPointsToPlane,
            OptionCurveGetType,
            OptionMouseClick,
            OptionTakeSnapshot,
            OptionPathGetInfo,
            OptionPathSegmentInfo,
            OptionPathGetCurveUuidsForVertices,
            OptionPathGetCurveUuid,
            OptionPathGetVertexUuids,
            OptionPathGetSketchTargetUuid,
            OptionCurveGetEndPoints,
            OptionFaceIsPlanar,
            OptionFaceGetPosition,
            OptionFaceGetCenter,
            OptionFaceGetGradient,
            OptionPlaneIntersectAndProject,
            OptionImportFiles,
            OptionImportedGeometry,
            OptionMass,
            OptionVolume,
            OptionDensity,
            OptionSurfaceArea,
            OptionCenterOfMass,
            OptionGetSketchModePlane,
            OptionEntityGetDistance,
            OptionFaceEdgeInfo,
            OptionEdgeInfo,
            OptionEntityClone,
            OptionEntityLinearPatternTransform,
            OptionEntityLinearPattern,
            OptionEntityCircularPattern,
            OptionEntityMirror,
            OptionEntityMirrorAcrossEdge,
            OptionEntityMakeHelix,
            OptionEntityMakeHelixFromParams,
            OptionEntityMakeHelixFromEdge,
            OptionSolid3dGetExtrusionFaceInfo,
            OptionExtrusionFaceInfo,
            OptionComplementaryEdges,
            OptionAdjacencyInfo,
            OptionSetGridReferencePlane,
            OptionBooleanUnion,
            OptionBooleanIntersection,
            OptionBooleanSubtract,
            OptionSetGridScale,
            OptionSetGridAutoScale,
            OptionSetOrderIndependentTransparency,
        ],
        Field(discriminator="type"),
    ]
]
