from typing import List, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated

from ..models.angle import Angle
from ..models.annotation_options import AnnotationOptions
from ..models.annotation_type import AnnotationType
from ..models.camera_drag_interaction_type import CameraDragInteractionType
from ..models.camera_movement import CameraMovement
from ..models.color import Color
from ..models.cut_type import CutType
from ..models.distance_type import DistanceType
from ..models.entity_type import EntityType
from ..models.image_format import ImageFormat
from ..models.import_file import ImportFile
from ..models.input_format import InputFormat
from ..models.length_unit import LengthUnit
from ..models.modeling_cmd_id import ModelingCmdId
from ..models.output_format import OutputFormat
from ..models.path_component_constraint_bound import PathComponentConstraintBound
from ..models.path_component_constraint_type import PathComponentConstraintType
from ..models.path_segment import PathSegment
from ..models.perspective_camera_parameters import PerspectiveCameraParameters
from ..models.point2d import Point2d
from ..models.point3d import Point3d
from ..models.scene_selection_type import SceneSelectionType
from ..models.scene_tool_type import SceneToolType
from ..models.transform import Transform
from ..models.unit_area import UnitArea
from ..models.unit_density import UnitDensity
from ..models.unit_length import UnitLength
from ..models.unit_mass import UnitMass
from ..models.unit_volume import UnitVolume


class OptionEngineUtilEvaluatePath(BaseModel):
    """Evaluates the position of a path in one shot (engine utility for kcl executor)"""

    path_json: str

    t: float

    type: Literal["engine_util_evaluate_path"] = "engine_util_evaluate_path"

    model_config = ConfigDict(protected_namespaces=())


class OptionStartPath(BaseModel):
    """Start a new path."""

    type: Literal["start_path"] = "start_path"

    model_config = ConfigDict(protected_namespaces=())


class OptionMovePathPen(BaseModel):
    """Move the path's \"pen\". If you're in sketch mode, these coordinates are in the local coordinate system, not the world's coordinate system. For example, say you're sketching on the plane {x: (1,0,0), y: (0,1,0), origin: (0, 0, 50)}. In other words, the plane 50 units above the default XY plane. Then, moving the pen to (1, 1, 0) with this command uses local coordinates. So, it would move the pen to (1, 1, 50) in global coordinates."""

    path: ModelingCmdId

    to: Point3d

    type: Literal["move_path_pen"] = "move_path_pen"

    model_config = ConfigDict(protected_namespaces=())


class OptionExtendPath(BaseModel):
    """Extend a path by adding a new segment which starts at the path's \"pen\". If no \"pen\" location has been set before (via `MovePen`), then the pen is at the origin."""

    path: ModelingCmdId

    segment: PathSegment

    type: Literal["extend_path"] = "extend_path"

    model_config = ConfigDict(protected_namespaces=())


class OptionExtrude(BaseModel):
    """Command for extruding a solid 2d."""

    distance: LengthUnit

    target: ModelingCmdId

    type: Literal["extrude"] = "extrude"

    model_config = ConfigDict(protected_namespaces=())


class OptionRevolve(BaseModel):
    """Command for revolving a solid 2d."""

    angle: Angle

    axis: Point3d

    axis_is_2d: bool

    origin: Point3d

    target: ModelingCmdId

    tolerance: LengthUnit

    type: Literal["revolve"] = "revolve"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid3DShellFace(BaseModel):
    """Command for shelling a solid3d face"""

    face_ids: List[str]

    hollow: bool = False

    object_id: str

    shell_thickness: LengthUnit

    type: Literal["solid3d_shell_face"] = "solid3d_shell_face"

    model_config = ConfigDict(protected_namespaces=())


class OptionRevolveAboutEdge(BaseModel):
    """Command for revolving a solid 2d about a brep edge"""

    angle: Angle

    edge_id: str

    target: ModelingCmdId

    tolerance: LengthUnit

    type: Literal["revolve_about_edge"] = "revolve_about_edge"

    model_config = ConfigDict(protected_namespaces=())


class OptionLoft(BaseModel):
    """Command for lofting sections to create a solid"""

    base_curve_index: Optional[int] = None

    bez_approximate_rational: bool

    section_ids: List[str]

    tolerance: LengthUnit

    type: Literal["loft"] = "loft"

    v_degree: int

    model_config = ConfigDict(protected_namespaces=())


class OptionClosePath(BaseModel):
    """Closes a path, converting it to a 2D solid."""

    path_id: str

    type: Literal["close_path"] = "close_path"

    model_config = ConfigDict(protected_namespaces=())


class OptionCameraDragStart(BaseModel):
    """Camera drag started."""

    interaction: CameraDragInteractionType

    type: Literal["camera_drag_start"] = "camera_drag_start"

    window: Point2d

    model_config = ConfigDict(protected_namespaces=())


class OptionCameraDragMove(BaseModel):
    """Camera drag continued."""

    interaction: CameraDragInteractionType

    sequence: Optional[int] = None

    type: Literal["camera_drag_move"] = "camera_drag_move"

    window: Point2d

    model_config = ConfigDict(protected_namespaces=())


class OptionCameraDragEnd(BaseModel):
    """Camera drag ended"""

    interaction: CameraDragInteractionType

    type: Literal["camera_drag_end"] = "camera_drag_end"

    window: Point2d

    model_config = ConfigDict(protected_namespaces=())


class OptionDefaultCameraGetSettings(BaseModel):
    """Gets the default camera's camera settings"""

    type: Literal["default_camera_get_settings"] = "default_camera_get_settings"

    model_config = ConfigDict(protected_namespaces=())


class OptionDefaultCameraLookAt(BaseModel):
    """Change what the default camera is looking at."""

    center: Point3d

    sequence: Optional[int] = None

    type: Literal["default_camera_look_at"] = "default_camera_look_at"

    up: Point3d

    vantage: Point3d

    model_config = ConfigDict(protected_namespaces=())


class OptionDefaultCameraPerspectiveSettings(BaseModel):
    """Change what the default camera is looking at."""

    center: Point3d

    fov_y: Optional[float] = None

    sequence: Optional[int] = None

    type: Literal["default_camera_perspective_settings"] = (
        "default_camera_perspective_settings"
    )

    up: Point3d

    vantage: Point3d

    z_far: Optional[float] = None

    z_near: Optional[float] = None

    model_config = ConfigDict(protected_namespaces=())


class OptionDefaultCameraZoom(BaseModel):
    """Adjust zoom of the default camera."""

    magnitude: float

    type: Literal["default_camera_zoom"] = "default_camera_zoom"

    model_config = ConfigDict(protected_namespaces=())


class OptionExport(BaseModel):
    """Export the scene to a file."""

    entity_ids: List[str]

    format: OutputFormat

    type: Literal["export"] = "export"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityGetParentId(BaseModel):
    """What is this entity's parent?"""

    entity_id: str

    type: Literal["entity_get_parent_id"] = "entity_get_parent_id"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityGetNumChildren(BaseModel):
    """How many children does the entity have?"""

    entity_id: str

    type: Literal["entity_get_num_children"] = "entity_get_num_children"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityGetChildUuid(BaseModel):
    """What is the UUID of this entity's n-th child?"""

    child_index: int

    entity_id: str

    type: Literal["entity_get_child_uuid"] = "entity_get_child_uuid"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityGetAllChildUuids(BaseModel):
    """What are all UUIDs of this entity's children?"""

    entity_id: str

    type: Literal["entity_get_all_child_uuids"] = "entity_get_all_child_uuids"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityGetSketchPaths(BaseModel):
    """What are all UUIDs of all the paths sketched on top of this entity?"""

    entity_id: str

    type: Literal["entity_get_sketch_paths"] = "entity_get_sketch_paths"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityGetDistance(BaseModel):
    """What is the distance between these two entities?"""

    distance_type: DistanceType

    entity_id1: str

    entity_id2: str

    type: Literal["entity_get_distance"] = "entity_get_distance"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityLinearPatternTransform(BaseModel):
    """Create a pattern using this entity by specifying the transform for each desired repetition. Transformations are performed in the following order (first applied to last applied): scale, rotate, translate."""

    entity_id: str

    transform: List[Transform]

    type: Literal["entity_linear_pattern_transform"] = "entity_linear_pattern_transform"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityLinearPattern(BaseModel):
    """Create a linear pattern using this entity."""

    axis: Point3d

    entity_id: str

    num_repetitions: int

    spacing: LengthUnit

    type: Literal["entity_linear_pattern"] = "entity_linear_pattern"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityCircularPattern(BaseModel):
    """Create a circular pattern using this entity."""

    arc_degrees: float

    axis: Point3d

    center: Point3d

    entity_id: str

    num_repetitions: int

    rotate_duplicates: bool

    type: Literal["entity_circular_pattern"] = "entity_circular_pattern"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityMakeHelix(BaseModel):
    """Create a helix using the input cylinder and other specified parameters."""

    cylinder_id: str

    is_clockwise: bool

    length: LengthUnit

    revolutions: float

    start_angle: Angle

    type: Literal["entity_make_helix"] = "entity_make_helix"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityMirror(BaseModel):
    """Mirror the input entities over the specified axis. (Currently only supports sketches)"""

    axis: Point3d

    ids: List[str]

    point: Point3d

    type: Literal["entity_mirror"] = "entity_mirror"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityMirrorAcrossEdge(BaseModel):
    """Mirror the input entities over the specified edge. (Currently only supports sketches)"""

    edge_id: str

    ids: List[str]

    type: Literal["entity_mirror_across_edge"] = "entity_mirror_across_edge"

    model_config = ConfigDict(protected_namespaces=())


class OptionSelectWithPoint(BaseModel):
    """Modifies the selection by simulating a \"mouse click\" at the given x,y window coordinate Returns ID of whatever was selected."""

    selected_at_window: Point2d

    selection_type: SceneSelectionType

    type: Literal["select_with_point"] = "select_with_point"

    model_config = ConfigDict(protected_namespaces=())


class OptionSelectAdd(BaseModel):
    """Adds one or more entities (by UUID) to the selection."""

    entities: List[str]

    type: Literal["select_add"] = "select_add"

    model_config = ConfigDict(protected_namespaces=())


class OptionSelectRemove(BaseModel):
    """Removes one or more entities (by UUID) from the selection."""

    entities: List[str]

    type: Literal["select_remove"] = "select_remove"

    model_config = ConfigDict(protected_namespaces=())


class OptionSceneClearAll(BaseModel):
    """Removes all of the Objects in the scene"""

    type: Literal["scene_clear_all"] = "scene_clear_all"

    model_config = ConfigDict(protected_namespaces=())


class OptionSelectReplace(BaseModel):
    """Replaces current selection with these entities (by UUID)."""

    entities: List[str]

    type: Literal["select_replace"] = "select_replace"

    model_config = ConfigDict(protected_namespaces=())


class OptionHighlightSetEntity(BaseModel):
    """Changes the current highlighted entity to whichever one is at the given window coordinate. If there's no entity at this location, clears the highlight."""

    selected_at_window: Point2d

    sequence: Optional[int] = None

    type: Literal["highlight_set_entity"] = "highlight_set_entity"

    model_config = ConfigDict(protected_namespaces=())


class OptionHighlightSetEntities(BaseModel):
    """Changes the current highlighted entity to these entities."""

    entities: List[str]

    type: Literal["highlight_set_entities"] = "highlight_set_entities"

    model_config = ConfigDict(protected_namespaces=())


class OptionNewAnnotation(BaseModel):
    """Create a new annotation"""

    annotation_type: AnnotationType

    clobber: bool

    options: AnnotationOptions

    type: Literal["new_annotation"] = "new_annotation"

    model_config = ConfigDict(protected_namespaces=())


class OptionUpdateAnnotation(BaseModel):
    """Update an annotation"""

    annotation_id: str

    options: AnnotationOptions

    type: Literal["update_annotation"] = "update_annotation"

    model_config = ConfigDict(protected_namespaces=())


class OptionEdgeLinesVisible(BaseModel):
    """Changes visibility of scene-wide edge lines on brep solids"""

    hidden: bool

    type: Literal["edge_lines_visible"] = "edge_lines_visible"

    model_config = ConfigDict(protected_namespaces=())


class OptionObjectVisible(BaseModel):
    """Hide or show an object"""

    hidden: bool

    object_id: str

    type: Literal["object_visible"] = "object_visible"

    model_config = ConfigDict(protected_namespaces=())


class OptionObjectBringToFront(BaseModel):
    """Bring an object to the front of the scene"""

    object_id: str

    type: Literal["object_bring_to_front"] = "object_bring_to_front"

    model_config = ConfigDict(protected_namespaces=())


class OptionObjectSetMaterialParamsPbr(BaseModel):
    """Set the material properties of an object"""

    ambient_occlusion: float

    color: Color

    metalness: float

    object_id: str

    roughness: float

    type: Literal["object_set_material_params_pbr"] = "object_set_material_params_pbr"

    model_config = ConfigDict(protected_namespaces=())


class OptionGetEntityType(BaseModel):
    """What type of entity is this?"""

    entity_id: str

    type: Literal["get_entity_type"] = "get_entity_type"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid3DGetAllEdgeFaces(BaseModel):
    """Gets all faces which use the given edge."""

    edge_id: str

    object_id: str

    type: Literal["solid3d_get_all_edge_faces"] = "solid3d_get_all_edge_faces"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid2DAddHole(BaseModel):
    """Add a hole to a Solid2d object before extruding it."""

    hole_id: str

    object_id: str

    type: Literal["solid2d_add_hole"] = "solid2d_add_hole"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid3DGetAllOppositeEdges(BaseModel):
    """Gets all edges which are opposite the given edge, across all possible faces."""

    along_vector: Optional[Point3d] = None

    edge_id: str

    object_id: str

    type: Literal["solid3d_get_all_opposite_edges"] = "solid3d_get_all_opposite_edges"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid3DGetOppositeEdge(BaseModel):
    """Gets the edge opposite the given edge, along the given face."""

    edge_id: str

    face_id: str

    object_id: str

    type: Literal["solid3d_get_opposite_edge"] = "solid3d_get_opposite_edge"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid3DGetNextAdjacentEdge(BaseModel):
    """Gets the next adjacent edge for the given edge, along the given face."""

    edge_id: str

    face_id: str

    object_id: str

    type: Literal["solid3d_get_next_adjacent_edge"] = "solid3d_get_next_adjacent_edge"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid3DGetPrevAdjacentEdge(BaseModel):
    """Gets the previous adjacent edge for the given edge, along the given face."""

    edge_id: str

    face_id: str

    object_id: str

    type: Literal["solid3d_get_prev_adjacent_edge"] = "solid3d_get_prev_adjacent_edge"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid3DGetCommonEdge(BaseModel):
    """Gets the shared edge between these two faces if it exists"""

    face_ids: List[str]

    object_id: str

    type: Literal["solid3d_get_common_edge"] = "solid3d_get_common_edge"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid3DFilletEdge(BaseModel):
    """Fillets the given edge with the specified radius."""

    cut_type: CutType = "fillet"  # type: ignore

    edge_id: str

    face_id: Optional[str] = None

    object_id: str

    radius: LengthUnit

    tolerance: LengthUnit

    type: Literal["solid3d_fillet_edge"] = "solid3d_fillet_edge"

    model_config = ConfigDict(protected_namespaces=())


class OptionFaceIsPlanar(BaseModel):
    """Determines whether a brep face is planar and returns its surface-local planar axes if so"""

    object_id: str

    type: Literal["face_is_planar"] = "face_is_planar"

    model_config = ConfigDict(protected_namespaces=())


class OptionFaceGetPosition(BaseModel):
    """Determines a position on a brep face evaluated by parameters u,v"""

    object_id: str

    type: Literal["face_get_position"] = "face_get_position"

    uv: Point2d

    model_config = ConfigDict(protected_namespaces=())


class OptionFaceGetCenter(BaseModel):
    """Obtains the surface \"center of mass\" """

    object_id: str

    type: Literal["face_get_center"] = "face_get_center"

    model_config = ConfigDict(protected_namespaces=())


class OptionFaceGetGradient(BaseModel):
    """Determines the gradient (dFdu, dFdv) + normal vector on a brep face evaluated by parameters u,v"""

    object_id: str

    type: Literal["face_get_gradient"] = "face_get_gradient"

    uv: Point2d

    model_config = ConfigDict(protected_namespaces=())


class OptionSendObject(BaseModel):
    """Send object to front or back."""

    front: bool

    object_id: str

    type: Literal["send_object"] = "send_object"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntitySetOpacity(BaseModel):
    """Set opacity of the entity."""

    entity_id: str

    opacity: float

    type: Literal["entity_set_opacity"] = "entity_set_opacity"

    model_config = ConfigDict(protected_namespaces=())


class OptionEntityFade(BaseModel):
    """Fade entity in or out."""

    duration_seconds: float = 0.4000000059604645

    entity_id: str

    fade_in: bool

    type: Literal["entity_fade"] = "entity_fade"

    model_config = ConfigDict(protected_namespaces=())


class OptionMakePlane(BaseModel):
    """Make a new plane"""

    clobber: bool

    hide: Optional[bool] = None

    origin: Point3d

    size: LengthUnit

    type: Literal["make_plane"] = "make_plane"

    x_axis: Point3d

    y_axis: Point3d

    model_config = ConfigDict(protected_namespaces=())


class OptionPlaneSetColor(BaseModel):
    """Set the color of a plane."""

    color: Color

    plane_id: str

    type: Literal["plane_set_color"] = "plane_set_color"

    model_config = ConfigDict(protected_namespaces=())


class OptionSetTool(BaseModel):
    """Set the current tool."""

    tool: SceneToolType

    type: Literal["set_tool"] = "set_tool"

    model_config = ConfigDict(protected_namespaces=())


class OptionMouseMove(BaseModel):
    """Send a mouse move event"""

    sequence: Optional[int] = None

    type: Literal["mouse_move"] = "mouse_move"

    window: Point2d

    model_config = ConfigDict(protected_namespaces=())


class OptionMouseClick(BaseModel):
    """Send a mouse click event Updates modified/selected entities."""

    type: Literal["mouse_click"] = "mouse_click"

    window: Point2d

    model_config = ConfigDict(protected_namespaces=())


class OptionSketchModeDisable(BaseModel):
    """Disable sketch mode. If you are sketching on a face, be sure to not disable sketch mode until you have extruded. Otherwise, your object will not be fused with the face."""

    type: Literal["sketch_mode_disable"] = "sketch_mode_disable"

    model_config = ConfigDict(protected_namespaces=())


class OptionGetSketchModePlane(BaseModel):
    """Get the plane for sketch mode."""

    type: Literal["get_sketch_mode_plane"] = "get_sketch_mode_plane"

    model_config = ConfigDict(protected_namespaces=())


class OptionCurveSetConstraint(BaseModel):
    """Get the plane for sketch mode."""

    constraint_bound: PathComponentConstraintBound

    constraint_type: PathComponentConstraintType

    object_id: str

    type: Literal["curve_set_constraint"] = "curve_set_constraint"

    model_config = ConfigDict(protected_namespaces=())


class OptionEnableSketchMode(BaseModel):
    """Sketch on some entity (e.g. a plane, a face)."""

    adjust_camera: bool

    animated: bool

    entity_id: str

    ortho: bool

    planar_normal: Optional[Point3d] = None

    type: Literal["enable_sketch_mode"] = "enable_sketch_mode"

    model_config = ConfigDict(protected_namespaces=())


class OptionEnableDryRun(BaseModel):
    """Sets whether or not changes to the scene or its objects will be done as a \"dry run\" In a dry run, successful commands won't actually change the model. This is useful for catching errors before actually making the change."""

    type: Literal["enable_dry_run"] = "enable_dry_run"

    model_config = ConfigDict(protected_namespaces=())


class OptionDisableDryRun(BaseModel):
    """Sets whether or not changes to the scene or its objects will be done as a \"dry run\" In a dry run, successful commands won't actually change the model. This is useful for catching errors before actually making the change."""

    type: Literal["disable_dry_run"] = "disable_dry_run"

    model_config = ConfigDict(protected_namespaces=())


class OptionSetBackgroundColor(BaseModel):
    """Set the background color of the scene."""

    color: Color

    type: Literal["set_background_color"] = "set_background_color"

    model_config = ConfigDict(protected_namespaces=())


class OptionSetCurrentToolProperties(BaseModel):
    """Set the properties of the tool lines for the scene."""

    color: Optional[Color] = None

    type: Literal["set_current_tool_properties"] = "set_current_tool_properties"

    model_config = ConfigDict(protected_namespaces=())


class OptionSetDefaultSystemProperties(BaseModel):
    """Set the default system properties used when a specific property isn't set."""

    color: Optional[Color] = None

    type: Literal["set_default_system_properties"] = "set_default_system_properties"

    model_config = ConfigDict(protected_namespaces=())


class OptionCurveGetType(BaseModel):
    """Get type of the given curve."""

    curve_id: str

    type: Literal["curve_get_type"] = "curve_get_type"

    model_config = ConfigDict(protected_namespaces=())


class OptionCurveGetControlPoints(BaseModel):
    """Get control points of the given curve."""

    curve_id: str

    type: Literal["curve_get_control_points"] = "curve_get_control_points"

    model_config = ConfigDict(protected_namespaces=())


class OptionTakeSnapshot(BaseModel):
    """Take a snapshot of the current view."""

    format: ImageFormat

    type: Literal["take_snapshot"] = "take_snapshot"

    model_config = ConfigDict(protected_namespaces=())


class OptionMakeAxesGizmo(BaseModel):
    """Add a gizmo showing the axes."""

    clobber: bool

    gizmo_mode: bool

    type: Literal["make_axes_gizmo"] = "make_axes_gizmo"

    model_config = ConfigDict(protected_namespaces=())


class OptionPathGetInfo(BaseModel):
    """Query the given path."""

    path_id: str

    type: Literal["path_get_info"] = "path_get_info"

    model_config = ConfigDict(protected_namespaces=())


class OptionPathGetCurveUuidsForVertices(BaseModel):
    """Obtain curve ids for vertex ids"""

    path_id: str

    type: Literal["path_get_curve_uuids_for_vertices"] = (
        "path_get_curve_uuids_for_vertices"
    )

    vertex_ids: List[str]

    model_config = ConfigDict(protected_namespaces=())


class OptionPathGetCurveUuid(BaseModel):
    """Obtain curve id by index"""

    index: int

    path_id: str

    type: Literal["path_get_curve_uuid"] = "path_get_curve_uuid"

    model_config = ConfigDict(protected_namespaces=())


class OptionPathGetVertexUuids(BaseModel):
    """Obtain vertex ids for a path"""

    path_id: str

    type: Literal["path_get_vertex_uuids"] = "path_get_vertex_uuids"

    model_config = ConfigDict(protected_namespaces=())


class OptionPathGetSketchTargetUuid(BaseModel):
    """Obtain the sketch target id (if the path was drawn in sketchmode) for a path"""

    path_id: str

    type: Literal["path_get_sketch_target_uuid"] = "path_get_sketch_target_uuid"

    model_config = ConfigDict(protected_namespaces=())


class OptionHandleMouseDragStart(BaseModel):
    """Start dragging the mouse."""

    type: Literal["handle_mouse_drag_start"] = "handle_mouse_drag_start"

    window: Point2d

    model_config = ConfigDict(protected_namespaces=())


class OptionHandleMouseDragMove(BaseModel):
    """Continue dragging the mouse."""

    sequence: Optional[int] = None

    type: Literal["handle_mouse_drag_move"] = "handle_mouse_drag_move"

    window: Point2d

    model_config = ConfigDict(protected_namespaces=())


class OptionHandleMouseDragEnd(BaseModel):
    """Stop dragging the mouse."""

    type: Literal["handle_mouse_drag_end"] = "handle_mouse_drag_end"

    window: Point2d

    model_config = ConfigDict(protected_namespaces=())


class OptionRemoveSceneObjects(BaseModel):
    """Remove scene objects."""

    object_ids: List[str]

    type: Literal["remove_scene_objects"] = "remove_scene_objects"

    model_config = ConfigDict(protected_namespaces=())


class OptionPlaneIntersectAndProject(BaseModel):
    """Utility method. Performs both a ray cast and projection to plane-local coordinates. Returns the plane coordinates for the given window coordinates."""

    plane_id: str

    type: Literal["plane_intersect_and_project"] = "plane_intersect_and_project"

    window: Point2d

    model_config = ConfigDict(protected_namespaces=())


class OptionCurveGetEndPoints(BaseModel):
    """Find the start and end of a curve."""

    curve_id: str

    type: Literal["curve_get_end_points"] = "curve_get_end_points"

    model_config = ConfigDict(protected_namespaces=())


class OptionReconfigureStream(BaseModel):
    """Reconfigure the stream."""

    bitrate: Optional[int] = None

    fps: int

    height: int

    type: Literal["reconfigure_stream"] = "reconfigure_stream"

    width: int

    model_config = ConfigDict(protected_namespaces=())


class OptionImportFiles(BaseModel):
    """Import files to the current model."""

    files: List[ImportFile]

    format: InputFormat

    type: Literal["import_files"] = "import_files"

    model_config = ConfigDict(protected_namespaces=())


class OptionSetSceneUnits(BaseModel):
    """Set the units of the scene. For all following commands, the units will be interpreted as the given units."""

    type: Literal["set_scene_units"] = "set_scene_units"

    unit: UnitLength

    model_config = ConfigDict(protected_namespaces=())


class OptionMass(BaseModel):
    """Get the mass of entities in the scene or the default scene."""

    entity_ids: List[str]

    material_density: float

    material_density_unit: UnitDensity

    output_unit: UnitMass

    type: Literal["mass"] = "mass"

    model_config = ConfigDict(protected_namespaces=())


class OptionDensity(BaseModel):
    """Get the density of entities in the scene or the default scene."""

    entity_ids: List[str]

    material_mass: float

    material_mass_unit: UnitMass

    output_unit: UnitDensity

    type: Literal["density"] = "density"

    model_config = ConfigDict(protected_namespaces=())


class OptionVolume(BaseModel):
    """Get the volume of entities in the scene or the default scene."""

    entity_ids: List[str]

    output_unit: UnitVolume

    type: Literal["volume"] = "volume"

    model_config = ConfigDict(protected_namespaces=())


class OptionCenterOfMass(BaseModel):
    """Get the center of mass of entities in the scene or the default scene."""

    entity_ids: List[str]

    output_unit: UnitLength

    type: Literal["center_of_mass"] = "center_of_mass"

    model_config = ConfigDict(protected_namespaces=())


class OptionSurfaceArea(BaseModel):
    """Get the surface area of entities in the scene or the default scene."""

    entity_ids: List[str]

    output_unit: UnitArea

    type: Literal["surface_area"] = "surface_area"

    model_config = ConfigDict(protected_namespaces=())


class OptionDefaultCameraFocusOn(BaseModel):
    """Focus the default camera upon an object in the scene."""

    type: Literal["default_camera_focus_on"] = "default_camera_focus_on"

    uuid: str

    model_config = ConfigDict(protected_namespaces=())


class OptionSetSelectionType(BaseModel):
    """When you select some entity with the current tool, what should happen to the entity?"""

    selection_type: SceneSelectionType

    type: Literal["set_selection_type"] = "set_selection_type"

    model_config = ConfigDict(protected_namespaces=())


class OptionSetSelectionFilter(BaseModel):
    """What kind of entities can be selected?"""

    filter: List[EntityType]

    type: Literal["set_selection_filter"] = "set_selection_filter"

    model_config = ConfigDict(protected_namespaces=())


class OptionDefaultCameraSetOrthographic(BaseModel):
    """Use orthographic projection."""

    type: Literal["default_camera_set_orthographic"] = "default_camera_set_orthographic"

    model_config = ConfigDict(protected_namespaces=())


class OptionDefaultCameraSetPerspective(BaseModel):
    """Use perspective projection."""

    parameters: Optional[PerspectiveCameraParameters] = None

    type: Literal["default_camera_set_perspective"] = "default_camera_set_perspective"

    model_config = ConfigDict(protected_namespaces=())


class OptionDefaultCameraCenterToSelection(BaseModel):
    """Updates the camera to center to the center of the current selection (or the origin if nothing is selected)"""

    camera_movement: CameraMovement = "vantage"  # type: ignore

    type: Literal["default_camera_center_to_selection"] = (
        "default_camera_center_to_selection"
    )

    model_config = ConfigDict(protected_namespaces=())


class OptionDefaultCameraCenterToScene(BaseModel):
    """Updates the camera to center to the center of the current scene's bounds"""

    camera_movement: CameraMovement = "vantage"  # type: ignore

    type: Literal["default_camera_center_to_scene"] = "default_camera_center_to_scene"

    model_config = ConfigDict(protected_namespaces=())


class OptionZoomToFit(BaseModel):
    """Fit the view to the specified object(s)."""

    animated: bool = False

    object_ids: List[str] = []

    padding: float = 0.0

    type: Literal["zoom_to_fit"] = "zoom_to_fit"

    model_config = ConfigDict(protected_namespaces=())


class OptionViewIsometric(BaseModel):
    """Fit the view to the scene with an isometric view."""

    padding: float = 0.0

    type: Literal["view_isometric"] = "view_isometric"

    model_config = ConfigDict(protected_namespaces=())


class OptionSolid3DGetExtrusionFaceInfo(BaseModel):
    """Get a concise description of all of an extrusion's faces."""

    edge_id: str

    object_id: str

    type: Literal["solid3d_get_extrusion_face_info"] = "solid3d_get_extrusion_face_info"

    model_config = ConfigDict(protected_namespaces=())


class OptionSelectClear(BaseModel):
    """Clear the selection"""

    type: Literal["select_clear"] = "select_clear"

    model_config = ConfigDict(protected_namespaces=())


class OptionSelectGet(BaseModel):
    """Find all IDs of selected entities"""

    type: Literal["select_get"] = "select_get"

    model_config = ConfigDict(protected_namespaces=())


class OptionGetNumObjects(BaseModel):
    """Get the number of objects in the scene"""

    type: Literal["get_num_objects"] = "get_num_objects"

    model_config = ConfigDict(protected_namespaces=())


class OptionMakeOffsetPath(BaseModel):
    """Make a new path by offsetting an object by a given distance. The new path's ID will be the ID of this command."""

    face_id: Optional[str] = None

    object_id: str

    offset: LengthUnit

    type: Literal["make_offset_path"] = "make_offset_path"

    model_config = ConfigDict(protected_namespaces=())


ModelingCmd = RootModel[
    Annotated[
        Union[
            OptionEngineUtilEvaluatePath,
            OptionStartPath,
            OptionMovePathPen,
            OptionExtendPath,
            OptionExtrude,
            OptionRevolve,
            OptionSolid3DShellFace,
            OptionRevolveAboutEdge,
            OptionLoft,
            OptionClosePath,
            OptionCameraDragStart,
            OptionCameraDragMove,
            OptionCameraDragEnd,
            OptionDefaultCameraGetSettings,
            OptionDefaultCameraLookAt,
            OptionDefaultCameraPerspectiveSettings,
            OptionDefaultCameraZoom,
            OptionExport,
            OptionEntityGetParentId,
            OptionEntityGetNumChildren,
            OptionEntityGetChildUuid,
            OptionEntityGetAllChildUuids,
            OptionEntityGetSketchPaths,
            OptionEntityGetDistance,
            OptionEntityLinearPatternTransform,
            OptionEntityLinearPattern,
            OptionEntityCircularPattern,
            OptionEntityMakeHelix,
            OptionEntityMirror,
            OptionEntityMirrorAcrossEdge,
            OptionSelectWithPoint,
            OptionSelectAdd,
            OptionSelectRemove,
            OptionSceneClearAll,
            OptionSelectReplace,
            OptionHighlightSetEntity,
            OptionHighlightSetEntities,
            OptionNewAnnotation,
            OptionUpdateAnnotation,
            OptionEdgeLinesVisible,
            OptionObjectVisible,
            OptionObjectBringToFront,
            OptionObjectSetMaterialParamsPbr,
            OptionGetEntityType,
            OptionSolid3DGetAllEdgeFaces,
            OptionSolid2DAddHole,
            OptionSolid3DGetAllOppositeEdges,
            OptionSolid3DGetOppositeEdge,
            OptionSolid3DGetNextAdjacentEdge,
            OptionSolid3DGetPrevAdjacentEdge,
            OptionSolid3DGetCommonEdge,
            OptionSolid3DFilletEdge,
            OptionFaceIsPlanar,
            OptionFaceGetPosition,
            OptionFaceGetCenter,
            OptionFaceGetGradient,
            OptionSendObject,
            OptionEntitySetOpacity,
            OptionEntityFade,
            OptionMakePlane,
            OptionPlaneSetColor,
            OptionSetTool,
            OptionMouseMove,
            OptionMouseClick,
            OptionSketchModeDisable,
            OptionGetSketchModePlane,
            OptionCurveSetConstraint,
            OptionEnableSketchMode,
            OptionEnableDryRun,
            OptionDisableDryRun,
            OptionSetBackgroundColor,
            OptionSetCurrentToolProperties,
            OptionSetDefaultSystemProperties,
            OptionCurveGetType,
            OptionCurveGetControlPoints,
            OptionTakeSnapshot,
            OptionMakeAxesGizmo,
            OptionPathGetInfo,
            OptionPathGetCurveUuidsForVertices,
            OptionPathGetCurveUuid,
            OptionPathGetVertexUuids,
            OptionPathGetSketchTargetUuid,
            OptionHandleMouseDragStart,
            OptionHandleMouseDragMove,
            OptionHandleMouseDragEnd,
            OptionRemoveSceneObjects,
            OptionPlaneIntersectAndProject,
            OptionCurveGetEndPoints,
            OptionReconfigureStream,
            OptionImportFiles,
            OptionSetSceneUnits,
            OptionMass,
            OptionDensity,
            OptionVolume,
            OptionCenterOfMass,
            OptionSurfaceArea,
            OptionDefaultCameraFocusOn,
            OptionSetSelectionType,
            OptionSetSelectionFilter,
            OptionDefaultCameraSetOrthographic,
            OptionDefaultCameraSetPerspective,
            OptionDefaultCameraCenterToSelection,
            OptionDefaultCameraCenterToScene,
            OptionZoomToFit,
            OptionViewIsometric,
            OptionSolid3DGetExtrusionFaceInfo,
            OptionSelectClear,
            OptionSelectGet,
            OptionGetNumObjects,
            OptionMakeOffsetPath,
        ],
        Field(discriminator="type"),
    ]
]
