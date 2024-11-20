from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated

from ..models.camera_drag_end import CameraDragEnd
from ..models.camera_drag_move import CameraDragMove
from ..models.camera_drag_start import CameraDragStart
from ..models.center_of_mass import CenterOfMass
from ..models.close_path import ClosePath
from ..models.curve_get_control_points import CurveGetControlPoints
from ..models.curve_get_end_points import CurveGetEndPoints
from ..models.curve_get_type import CurveGetType
from ..models.curve_set_constraint import CurveSetConstraint
from ..models.default_camera_center_to_scene import DefaultCameraCenterToScene
from ..models.default_camera_center_to_selection import DefaultCameraCenterToSelection
from ..models.default_camera_focus_on import DefaultCameraFocusOn
from ..models.default_camera_get_settings import DefaultCameraGetSettings
from ..models.default_camera_look_at import DefaultCameraLookAt
from ..models.default_camera_perspective_settings import (
    DefaultCameraPerspectiveSettings,
)
from ..models.default_camera_set_orthographic import DefaultCameraSetOrthographic
from ..models.default_camera_set_perspective import DefaultCameraSetPerspective
from ..models.default_camera_zoom import DefaultCameraZoom
from ..models.density import Density
from ..models.disable_dry_run import DisableDryRun
from ..models.edge_lines_visible import EdgeLinesVisible
from ..models.enable_dry_run import EnableDryRun
from ..models.enable_sketch_mode import EnableSketchMode
from ..models.engine_util_evaluate_path import EngineUtilEvaluatePath
from ..models.entity_circular_pattern import EntityCircularPattern
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
from ..models.entity_mirror import EntityMirror
from ..models.entity_mirror_across_edge import EntityMirrorAcrossEdge
from ..models.entity_set_opacity import EntitySetOpacity
from ..models.export import Export
from ..models.extend_path import ExtendPath
from ..models.extrude import Extrude
from ..models.extrusion_face_info import ExtrusionFaceInfo
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
from ..models.path_get_curve_uuid import PathGetCurveUuid
from ..models.path_get_curve_uuids_for_vertices import PathGetCurveUuidsForVertices
from ..models.path_get_info import PathGetInfo
from ..models.path_get_sketch_target_uuid import PathGetSketchTargetUuid
from ..models.path_get_vertex_uuids import PathGetVertexUuids
from ..models.path_segment_info import PathSegmentInfo
from ..models.plane_intersect_and_project import PlaneIntersectAndProject
from ..models.plane_set_color import PlaneSetColor
from ..models.reconfigure_stream import ReconfigureStream
from ..models.remove_scene_objects import RemoveSceneObjects
from ..models.revolve import Revolve
from ..models.revolve_about_edge import RevolveAboutEdge
from ..models.scene_clear_all import SceneClearAll
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
from ..models.set_scene_units import SetSceneUnits
from ..models.set_selection_filter import SetSelectionFilter
from ..models.set_selection_type import SetSelectionType
from ..models.set_tool import SetTool
from ..models.sketch_mode_disable import SketchModeDisable
from ..models.solid2d_add_hole import Solid2dAddHole
from ..models.solid3d_fillet_edge import Solid3dFilletEdge
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
from ..models.take_snapshot import TakeSnapshot
from ..models.update_annotation import UpdateAnnotation
from ..models.view_isometric import ViewIsometric
from ..models.volume import Volume
from ..models.zoom_to_fit import ZoomToFit


class OptionEmpty(BaseModel):
    """An empty response, used for any command that does not explicitly have a response defined here."""

    type: Literal["empty"] = "empty"

    model_config = ConfigDict(protected_namespaces=())


class OptionEngineUtilEvaluatePath(BaseModel):
    """"""

    data: EngineUtilEvaluatePath

    type: Literal["engine_util_evaluate_path"] = "engine_util_evaluate_path"

    model_config = ConfigDict(protected_namespaces=())


class OptionStartPath(BaseModel):
    """"""

    data: StartPath

    type: Literal["start_path"] = "start_path"

    model_config = ConfigDict(protected_namespaces=())


class OptionMovePathPen(BaseModel):
    """"""

    data: MovePathPen

    type: Literal["move_path_pen"] = "move_path_pen"

    model_config = ConfigDict(protected_namespaces=())


class OptionExtendPath(BaseModel):
    """"""

    data: ExtendPath

    type: Literal["extend_path"] = "extend_path"

    model_config = ConfigDict(protected_namespaces=())


class OptionExtrude(BaseModel):
    """"""

    data: Extrude

    type: Literal["extrude"] = "extrude"

    model_config = ConfigDict(protected_namespaces=())


class OptionRevolve(BaseModel):
    """"""

    data: Revolve

    type: Literal["revolve"] = "revolve"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid3DShellFace(BaseModel):
    """"""

    data: Solid3dShellFace

    type: Literal["solid3d_shell_face"] = "solid3d_shell_face"

    model_config = ConfigDict(protected_namespaces=())


class OptionRevolveAboutEdge(BaseModel):
    """"""

    data: RevolveAboutEdge

    type: Literal["revolve_about_edge"] = "revolve_about_edge"

    model_config = ConfigDict(protected_namespaces=())


class OptionCameraDragStart(BaseModel):
    """"""

    data: CameraDragStart

    type: Literal["camera_drag_start"] = "camera_drag_start"

    model_config = ConfigDict(protected_namespaces=())


class OptionDefaultCameraLookAt(BaseModel):
    """"""

    data: DefaultCameraLookAt

    type: Literal["default_camera_look_at"] = "default_camera_look_at"

    model_config = ConfigDict(protected_namespaces=())


class OptionDefaultCameraPerspectiveSettings(BaseModel):
    """"""

    data: DefaultCameraPerspectiveSettings

    type: Literal["default_camera_perspective_settings"] = (
        "default_camera_perspective_settings"
    )

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityMakeHelix(BaseModel):
    """"""

    data: EntityMakeHelix

    type: Literal["entity_make_helix"] = "entity_make_helix"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityMirror(BaseModel):
    """"""

    data: EntityMirror

    type: Literal["entity_mirror"] = "entity_mirror"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityMirrorAcrossEdge(BaseModel):
    """"""

    data: EntityMirrorAcrossEdge

    type: Literal["entity_mirror_across_edge"] = "entity_mirror_across_edge"

    model_config = ConfigDict(protected_namespaces=())


class OptionSelectAdd(BaseModel):
    """"""

    data: SelectAdd

    type: Literal["select_add"] = "select_add"

    model_config = ConfigDict(protected_namespaces=())


class OptionSelectRemove(BaseModel):
    """"""

    data: SelectRemove

    type: Literal["select_remove"] = "select_remove"

    model_config = ConfigDict(protected_namespaces=())


class OptionSceneClearAll(BaseModel):
    """"""

    data: SceneClearAll

    type: Literal["scene_clear_all"] = "scene_clear_all"

    model_config = ConfigDict(protected_namespaces=())


class OptionSelectReplace(BaseModel):
    """"""

    data: SelectReplace

    type: Literal["select_replace"] = "select_replace"

    model_config = ConfigDict(protected_namespaces=())


class OptionHighlightSetEntities(BaseModel):
    """"""

    data: HighlightSetEntities

    type: Literal["highlight_set_entities"] = "highlight_set_entities"

    model_config = ConfigDict(protected_namespaces=())


class OptionNewAnnotation(BaseModel):
    """"""

    data: NewAnnotation

    type: Literal["new_annotation"] = "new_annotation"

    model_config = ConfigDict(protected_namespaces=())


class OptionUpdateAnnotation(BaseModel):
    """"""

    data: UpdateAnnotation

    type: Literal["update_annotation"] = "update_annotation"

    model_config = ConfigDict(protected_namespaces=())


class OptionEdgeLinesVisible(BaseModel):
    """"""

    data: EdgeLinesVisible

    type: Literal["edge_lines_visible"] = "edge_lines_visible"

    model_config = ConfigDict(protected_namespaces=())


class OptionObjectVisible(BaseModel):
    """"""

    data: ObjectVisible

    type: Literal["object_visible"] = "object_visible"

    model_config = ConfigDict(protected_namespaces=())


class OptionObjectBringToFront(BaseModel):
    """"""

    data: ObjectBringToFront

    type: Literal["object_bring_to_front"] = "object_bring_to_front"

    model_config = ConfigDict(protected_namespaces=())


class OptionObjectSetMaterialParamsPbr(BaseModel):
    """"""

    data: ObjectSetMaterialParamsPbr

    type: Literal["object_set_material_params_pbr"] = "object_set_material_params_pbr"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid2DAddHole(BaseModel):
    """"""

    data: Solid2dAddHole

    type: Literal["solid2d_add_hole"] = "solid2d_add_hole"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid3DFilletEdge(BaseModel):
    """"""

    data: Solid3dFilletEdge

    type: Literal["solid3d_fillet_edge"] = "solid3d_fillet_edge"

    model_config = ConfigDict(protected_namespaces=())


class OptionSendObject(BaseModel):
    """"""

    data: SendObject

    type: Literal["send_object"] = "send_object"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntitySetOpacity(BaseModel):
    """"""

    data: EntitySetOpacity

    type: Literal["entity_set_opacity"] = "entity_set_opacity"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityFade(BaseModel):
    """"""

    data: EntityFade

    type: Literal["entity_fade"] = "entity_fade"

    model_config = ConfigDict(protected_namespaces=())


class OptionMakePlane(BaseModel):
    """"""

    data: MakePlane

    type: Literal["make_plane"] = "make_plane"

    model_config = ConfigDict(protected_namespaces=())


class OptionPlaneSetColor(BaseModel):
    """"""

    data: PlaneSetColor

    type: Literal["plane_set_color"] = "plane_set_color"

    model_config = ConfigDict(protected_namespaces=())


class OptionSetTool(BaseModel):
    """"""

    data: SetTool

    type: Literal["set_tool"] = "set_tool"

    model_config = ConfigDict(protected_namespaces=())


class OptionMouseMove(BaseModel):
    """"""

    data: MouseMove

    type: Literal["mouse_move"] = "mouse_move"

    model_config = ConfigDict(protected_namespaces=())


class OptionSketchModeDisable(BaseModel):
    """"""

    data: SketchModeDisable

    type: Literal["sketch_mode_disable"] = "sketch_mode_disable"

    model_config = ConfigDict(protected_namespaces=())


class OptionEnableDryRun(BaseModel):
    """"""

    data: EnableDryRun

    type: Literal["enable_dry_run"] = "enable_dry_run"

    model_config = ConfigDict(protected_namespaces=())


class OptionDisableDryRun(BaseModel):
    """"""

    data: DisableDryRun

    type: Literal["disable_dry_run"] = "disable_dry_run"

    model_config = ConfigDict(protected_namespaces=())


class OptionCurveSetConstraint(BaseModel):
    """"""

    data: CurveSetConstraint

    type: Literal["curve_set_constraint"] = "curve_set_constraint"

    model_config = ConfigDict(protected_namespaces=())


class OptionEnableSketchMode(BaseModel):
    """"""

    data: EnableSketchMode

    type: Literal["enable_sketch_mode"] = "enable_sketch_mode"

    model_config = ConfigDict(protected_namespaces=())


class OptionSetBackgroundColor(BaseModel):
    """"""

    data: SetBackgroundColor

    type: Literal["set_background_color"] = "set_background_color"

    model_config = ConfigDict(protected_namespaces=())


class OptionSetCurrentToolProperties(BaseModel):
    """"""

    data: SetCurrentToolProperties

    type: Literal["set_current_tool_properties"] = "set_current_tool_properties"

    model_config = ConfigDict(protected_namespaces=())


class OptionSetDefaultSystemProperties(BaseModel):
    """"""

    data: SetDefaultSystemProperties

    type: Literal["set_default_system_properties"] = "set_default_system_properties"

    model_config = ConfigDict(protected_namespaces=())


class OptionMakeAxesGizmo(BaseModel):
    """"""

    data: MakeAxesGizmo

    type: Literal["make_axes_gizmo"] = "make_axes_gizmo"

    model_config = ConfigDict(protected_namespaces=())


class OptionHandleMouseDragStart(BaseModel):
    """"""

    data: HandleMouseDragStart

    type: Literal["handle_mouse_drag_start"] = "handle_mouse_drag_start"

    model_config = ConfigDict(protected_namespaces=())


class OptionHandleMouseDragMove(BaseModel):
    """"""

    data: HandleMouseDragMove

    type: Literal["handle_mouse_drag_move"] = "handle_mouse_drag_move"

    model_config = ConfigDict(protected_namespaces=())


class OptionHandleMouseDragEnd(BaseModel):
    """"""

    data: HandleMouseDragEnd

    type: Literal["handle_mouse_drag_end"] = "handle_mouse_drag_end"

    model_config = ConfigDict(protected_namespaces=())


class OptionRemoveSceneObjects(BaseModel):
    """"""

    data: RemoveSceneObjects

    type: Literal["remove_scene_objects"] = "remove_scene_objects"

    model_config = ConfigDict(protected_namespaces=())


class OptionReconfigureStream(BaseModel):
    """"""

    data: ReconfigureStream

    type: Literal["reconfigure_stream"] = "reconfigure_stream"

    model_config = ConfigDict(protected_namespaces=())


class OptionSetSceneUnits(BaseModel):
    """"""

    data: SetSceneUnits

    type: Literal["set_scene_units"] = "set_scene_units"

    model_config = ConfigDict(protected_namespaces=())


class OptionSetSelectionType(BaseModel):
    """"""

    data: SetSelectionType

    type: Literal["set_selection_type"] = "set_selection_type"

    model_config = ConfigDict(protected_namespaces=())


class OptionSetSelectionFilter(BaseModel):
    """"""

    data: SetSelectionFilter

    type: Literal["set_selection_filter"] = "set_selection_filter"

    model_config = ConfigDict(protected_namespaces=())


class OptionDefaultCameraSetOrthographic(BaseModel):
    """"""

    data: DefaultCameraSetOrthographic

    type: Literal["default_camera_set_orthographic"] = "default_camera_set_orthographic"

    model_config = ConfigDict(protected_namespaces=())


class OptionDefaultCameraSetPerspective(BaseModel):
    """"""

    data: DefaultCameraSetPerspective

    type: Literal["default_camera_set_perspective"] = "default_camera_set_perspective"

    model_config = ConfigDict(protected_namespaces=())


class OptionDefaultCameraCenterToSelection(BaseModel):
    """"""

    data: DefaultCameraCenterToSelection

    type: Literal["default_camera_center_to_selection"] = (
        "default_camera_center_to_selection"
    )

    model_config = ConfigDict(protected_namespaces=())


class OptionDefaultCameraCenterToScene(BaseModel):
    """"""

    data: DefaultCameraCenterToScene

    type: Literal["default_camera_center_to_scene"] = "default_camera_center_to_scene"

    model_config = ConfigDict(protected_namespaces=())


class OptionSelectClear(BaseModel):
    """"""

    data: SelectClear

    type: Literal["select_clear"] = "select_clear"

    model_config = ConfigDict(protected_namespaces=())


class OptionExport(BaseModel):
    """"""

    data: Export

    type: Literal["export"] = "export"

    model_config = ConfigDict(protected_namespaces=())


class OptionSelectWithPoint(BaseModel):
    """"""

    data: SelectWithPoint

    type: Literal["select_with_point"] = "select_with_point"

    model_config = ConfigDict(protected_namespaces=())


class OptionHighlightSetEntity(BaseModel):
    """"""

    data: HighlightSetEntity

    type: Literal["highlight_set_entity"] = "highlight_set_entity"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityGetChildUuid(BaseModel):
    """"""

    data: EntityGetChildUuid

    type: Literal["entity_get_child_uuid"] = "entity_get_child_uuid"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityGetNumChildren(BaseModel):
    """"""

    data: EntityGetNumChildren

    type: Literal["entity_get_num_children"] = "entity_get_num_children"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityGetParentId(BaseModel):
    """"""

    data: EntityGetParentId

    type: Literal["entity_get_parent_id"] = "entity_get_parent_id"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityGetAllChildUuids(BaseModel):
    """"""

    data: EntityGetAllChildUuids

    type: Literal["entity_get_all_child_uuids"] = "entity_get_all_child_uuids"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityGetSketchPaths(BaseModel):
    """"""

    data: EntityGetSketchPaths

    type: Literal["entity_get_sketch_paths"] = "entity_get_sketch_paths"

    model_config = ConfigDict(protected_namespaces=())


class OptionLoft(BaseModel):
    """"""

    data: Loft

    type: Literal["loft"] = "loft"

    model_config = ConfigDict(protected_namespaces=())


class OptionClosePath(BaseModel):
    """"""

    data: ClosePath

    type: Literal["close_path"] = "close_path"

    model_config = ConfigDict(protected_namespaces=())


class OptionCameraDragMove(BaseModel):
    """"""

    data: CameraDragMove

    type: Literal["camera_drag_move"] = "camera_drag_move"

    model_config = ConfigDict(protected_namespaces=())


class OptionCameraDragEnd(BaseModel):
    """"""

    data: CameraDragEnd

    type: Literal["camera_drag_end"] = "camera_drag_end"

    model_config = ConfigDict(protected_namespaces=())


class OptionDefaultCameraGetSettings(BaseModel):
    """"""

    data: DefaultCameraGetSettings

    type: Literal["default_camera_get_settings"] = "default_camera_get_settings"

    model_config = ConfigDict(protected_namespaces=())


class OptionDefaultCameraZoom(BaseModel):
    """"""

    data: DefaultCameraZoom

    type: Literal["default_camera_zoom"] = "default_camera_zoom"

    model_config = ConfigDict(protected_namespaces=())


class OptionZoomToFit(BaseModel):
    """"""

    data: ZoomToFit

    type: Literal["zoom_to_fit"] = "zoom_to_fit"

    model_config = ConfigDict(protected_namespaces=())


class OptionViewIsometric(BaseModel):
    """"""

    data: ViewIsometric

    type: Literal["view_isometric"] = "view_isometric"

    model_config = ConfigDict(protected_namespaces=())


class OptionGetNumObjects(BaseModel):
    """"""

    data: GetNumObjects

    type: Literal["get_num_objects"] = "get_num_objects"

    model_config = ConfigDict(protected_namespaces=())


class OptionMakeOffsetPath(BaseModel):
    """"""

    data: MakeOffsetPath

    type: Literal["make_offset_path"] = "make_offset_path"

    model_config = ConfigDict(protected_namespaces=())


class OptionDefaultCameraFocusOn(BaseModel):
    """"""

    data: DefaultCameraFocusOn

    type: Literal["default_camera_focus_on"] = "default_camera_focus_on"

    model_config = ConfigDict(protected_namespaces=())


class OptionSelectGet(BaseModel):
    """"""

    data: SelectGet

    type: Literal["select_get"] = "select_get"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid3DGetAllEdgeFaces(BaseModel):
    """"""

    data: Solid3dGetAllEdgeFaces

    type: Literal["solid3d_get_all_edge_faces"] = "solid3d_get_all_edge_faces"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid3DGetAllOppositeEdges(BaseModel):
    """"""

    data: Solid3dGetAllOppositeEdges

    type: Literal["solid3d_get_all_opposite_edges"] = "solid3d_get_all_opposite_edges"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid3DGetOppositeEdge(BaseModel):
    """"""

    data: Solid3dGetOppositeEdge

    type: Literal["solid3d_get_opposite_edge"] = "solid3d_get_opposite_edge"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid3DGetNextAdjacentEdge(BaseModel):
    """"""

    data: Solid3dGetNextAdjacentEdge

    type: Literal["solid3d_get_next_adjacent_edge"] = "solid3d_get_next_adjacent_edge"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid3DGetPrevAdjacentEdge(BaseModel):
    """"""

    data: Solid3dGetPrevAdjacentEdge

    type: Literal["solid3d_get_prev_adjacent_edge"] = "solid3d_get_prev_adjacent_edge"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid3DGetCommonEdge(BaseModel):
    """"""

    data: Solid3dGetCommonEdge

    type: Literal["solid3d_get_common_edge"] = "solid3d_get_common_edge"

    model_config = ConfigDict(protected_namespaces=())


class OptionGetEntityType(BaseModel):
    """"""

    data: GetEntityType

    type: Literal["get_entity_type"] = "get_entity_type"

    model_config = ConfigDict(protected_namespaces=())


class OptionCurveGetControlPoints(BaseModel):
    """"""

    data: CurveGetControlPoints

    type: Literal["curve_get_control_points"] = "curve_get_control_points"

    model_config = ConfigDict(protected_namespaces=())


class OptionCurveGetType(BaseModel):
    """"""

    data: CurveGetType

    type: Literal["curve_get_type"] = "curve_get_type"

    model_config = ConfigDict(protected_namespaces=())


class OptionMouseClick(BaseModel):
    """"""

    data: MouseClick

    type: Literal["mouse_click"] = "mouse_click"

    model_config = ConfigDict(protected_namespaces=())


class OptionTakeSnapshot(BaseModel):
    """"""

    data: TakeSnapshot

    type: Literal["take_snapshot"] = "take_snapshot"

    model_config = ConfigDict(protected_namespaces=())


class OptionPathGetInfo(BaseModel):
    """"""

    data: PathGetInfo

    type: Literal["path_get_info"] = "path_get_info"

    model_config = ConfigDict(protected_namespaces=())


class OptionPathSegmentInfo(BaseModel):
    """"""

    data: PathSegmentInfo

    type: Literal["path_segment_info"] = "path_segment_info"

    model_config = ConfigDict(protected_namespaces=())


class OptionPathGetCurveUuidsForVertices(BaseModel):
    """"""

    data: PathGetCurveUuidsForVertices

    type: Literal["path_get_curve_uuids_for_vertices"] = (
        "path_get_curve_uuids_for_vertices"
    )

    model_config = ConfigDict(protected_namespaces=())


class OptionPathGetCurveUuid(BaseModel):
    """"""

    data: PathGetCurveUuid

    type: Literal["path_get_curve_uuid"] = "path_get_curve_uuid"

    model_config = ConfigDict(protected_namespaces=())


class OptionPathGetVertexUuids(BaseModel):
    """"""

    data: PathGetVertexUuids

    type: Literal["path_get_vertex_uuids"] = "path_get_vertex_uuids"

    model_config = ConfigDict(protected_namespaces=())


class OptionPathGetSketchTargetUuid(BaseModel):
    """"""

    data: PathGetSketchTargetUuid

    type: Literal["path_get_sketch_target_uuid"] = "path_get_sketch_target_uuid"

    model_config = ConfigDict(protected_namespaces=())


class OptionCurveGetEndPoints(BaseModel):
    """"""

    data: CurveGetEndPoints

    type: Literal["curve_get_end_points"] = "curve_get_end_points"

    model_config = ConfigDict(protected_namespaces=())


class OptionFaceIsPlanar(BaseModel):
    """"""

    data: FaceIsPlanar

    type: Literal["face_is_planar"] = "face_is_planar"

    model_config = ConfigDict(protected_namespaces=())


class OptionFaceGetPosition(BaseModel):
    """"""

    data: FaceGetPosition

    type: Literal["face_get_position"] = "face_get_position"

    model_config = ConfigDict(protected_namespaces=())


class OptionFaceGetCenter(BaseModel):
    """"""

    data: FaceGetCenter

    type: Literal["face_get_center"] = "face_get_center"

    model_config = ConfigDict(protected_namespaces=())


class OptionFaceGetGradient(BaseModel):
    """"""

    data: FaceGetGradient

    type: Literal["face_get_gradient"] = "face_get_gradient"

    model_config = ConfigDict(protected_namespaces=())


class OptionPlaneIntersectAndProject(BaseModel):
    """"""

    data: PlaneIntersectAndProject

    type: Literal["plane_intersect_and_project"] = "plane_intersect_and_project"

    model_config = ConfigDict(protected_namespaces=())


class OptionImportFiles(BaseModel):
    """"""

    data: ImportFiles

    type: Literal["import_files"] = "import_files"

    model_config = ConfigDict(protected_namespaces=())


class OptionImportedGeometry(BaseModel):
    """"""

    data: ImportedGeometry

    type: Literal["imported_geometry"] = "imported_geometry"

    model_config = ConfigDict(protected_namespaces=())


class OptionMass(BaseModel):
    """"""

    data: Mass

    type: Literal["mass"] = "mass"

    model_config = ConfigDict(protected_namespaces=())


class OptionVolume(BaseModel):
    """"""

    data: Volume

    type: Literal["volume"] = "volume"

    model_config = ConfigDict(protected_namespaces=())


class OptionDensity(BaseModel):
    """"""

    data: Density

    type: Literal["density"] = "density"

    model_config = ConfigDict(protected_namespaces=())


class OptionSurfaceArea(BaseModel):
    """"""

    data: SurfaceArea

    type: Literal["surface_area"] = "surface_area"

    model_config = ConfigDict(protected_namespaces=())


class OptionCenterOfMass(BaseModel):
    """"""

    data: CenterOfMass

    type: Literal["center_of_mass"] = "center_of_mass"

    model_config = ConfigDict(protected_namespaces=())


class OptionGetSketchModePlane(BaseModel):
    """"""

    data: GetSketchModePlane

    type: Literal["get_sketch_mode_plane"] = "get_sketch_mode_plane"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityGetDistance(BaseModel):
    """"""

    data: EntityGetDistance

    type: Literal["entity_get_distance"] = "entity_get_distance"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityLinearPatternTransform(BaseModel):
    """"""

    data: EntityLinearPatternTransform

    type: Literal["entity_linear_pattern_transform"] = "entity_linear_pattern_transform"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityLinearPattern(BaseModel):
    """"""

    data: EntityLinearPattern

    type: Literal["entity_linear_pattern"] = "entity_linear_pattern"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityCircularPattern(BaseModel):
    """"""

    data: EntityCircularPattern

    type: Literal["entity_circular_pattern"] = "entity_circular_pattern"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid3DGetExtrusionFaceInfo(BaseModel):
    """"""

    data: Solid3dGetExtrusionFaceInfo

    type: Literal["solid3d_get_extrusion_face_info"] = "solid3d_get_extrusion_face_info"

    model_config = ConfigDict(protected_namespaces=())


class OptionExtrusionFaceInfo(BaseModel):
    """"""

    data: ExtrusionFaceInfo

    type: Literal["extrusion_face_info"] = "extrusion_face_info"

    model_config = ConfigDict(protected_namespaces=())


OkModelingCmdResponse = RootModel[
    Annotated[
        Union[
            OptionEmpty,
            OptionEngineUtilEvaluatePath,
            OptionStartPath,
            OptionMovePathPen,
            OptionExtendPath,
            OptionExtrude,
            OptionRevolve,
            OptionSolid3DShellFace,
            OptionRevolveAboutEdge,
            OptionCameraDragStart,
            OptionDefaultCameraLookAt,
            OptionDefaultCameraPerspectiveSettings,
            OptionEntityMakeHelix,
            OptionEntityMirror,
            OptionEntityMirrorAcrossEdge,
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
            OptionSolid2DAddHole,
            OptionSolid3DFilletEdge,
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
            OptionDefaultCameraZoom,
            OptionZoomToFit,
            OptionViewIsometric,
            OptionGetNumObjects,
            OptionMakeOffsetPath,
            OptionDefaultCameraFocusOn,
            OptionSelectGet,
            OptionSolid3DGetAllEdgeFaces,
            OptionSolid3DGetAllOppositeEdges,
            OptionSolid3DGetOppositeEdge,
            OptionSolid3DGetNextAdjacentEdge,
            OptionSolid3DGetPrevAdjacentEdge,
            OptionSolid3DGetCommonEdge,
            OptionGetEntityType,
            OptionCurveGetControlPoints,
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
            OptionEntityLinearPatternTransform,
            OptionEntityLinearPattern,
            OptionEntityCircularPattern,
            OptionSolid3DGetExtrusionFaceInfo,
            OptionExtrusionFaceInfo,
        ],
        Field(discriminator="type"),
    ]
]
