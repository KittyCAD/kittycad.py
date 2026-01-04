from typing import List, Literal, Optional, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.angle import Angle
from ..models.annotation_options import AnnotationOptions
from ..models.annotation_type import AnnotationType
from ..models.camera_drag_interaction_type import CameraDragInteractionType
from ..models.camera_movement import CameraMovement
from ..models.camera_view_state import CameraViewState
from ..models.color import Color
from ..models.component_transform import ComponentTransform
from ..models.cut_strategy import CutStrategy
from ..models.cut_type import CutType
from ..models.cut_type_v2 import CutTypeV2
from ..models.distance_type import DistanceType
from ..models.entity_type import EntityType
from ..models.extrude_method import ExtrudeMethod
from ..models.extrude_reference import ExtrudeReference
from ..models.extruded_face_info import ExtrudedFaceInfo
from ..models.image_format import ImageFormat
from ..models.import_file import ImportFile
from ..models.input_format3d import InputFormat3d
from ..models.length_unit import LengthUnit
from ..models.modeling_cmd_id import ModelingCmdId
from ..models.opposite_for_angle import OppositeForAngle
from ..models.opposite_for_length_unit import OppositeForLengthUnit
from ..models.output_format2d import OutputFormat2d
from ..models.output_format3d import OutputFormat3d
from ..models.path_component_constraint_bound import PathComponentConstraintBound
from ..models.path_component_constraint_type import PathComponentConstraintType
from ..models.path_segment import PathSegment
from ..models.perspective_camera_parameters import PerspectiveCameraParameters
from ..models.point2d import Point2d
from ..models.point3d import Point3d
from ..models.relative_to import RelativeTo
from ..models.scene_selection_type import SceneSelectionType
from ..models.scene_tool_type import SceneToolType
from ..models.transform import Transform
from ..models.unit_area import UnitArea
from ..models.unit_density import UnitDensity
from ..models.unit_length import UnitLength
from ..models.unit_mass import UnitMass
from ..models.unit_volume import UnitVolume
from .base import KittyCadBaseModel


class OptionEngineUtilEvaluatePath(KittyCadBaseModel):
    """Evaluates the position of a path in one shot (engine utility for kcl executor)"""

    path_json: str

    t: float

    type: Literal["engine_util_evaluate_path"] = "engine_util_evaluate_path"


class OptionStartPath(KittyCadBaseModel):
    """Start a new path."""

    type: Literal["start_path"] = "start_path"


class OptionMovePathPen(KittyCadBaseModel):
    """Move the path's \"pen\". If you're in sketch mode, these coordinates are in the local coordinate system, not the world's coordinate system. For example, say you're sketching on the plane {x: (1,0,0), y: (0,1,0), origin: (0, 0, 50)}. In other words, the plane 50 units above the default XY plane. Then, moving the pen to (1, 1, 0) with this command uses local coordinates. So, it would move the pen to (1, 1, 50) in global coordinates."""

    path: ModelingCmdId

    to: Point3d

    type: Literal["move_path_pen"] = "move_path_pen"


class OptionExtendPath(KittyCadBaseModel):
    """Extend a path by adding a new segment which starts at the path's \"pen\". If no \"pen\" location has been set before (via `MovePen`), then the pen is at the origin."""

    label: Optional[str] = None

    path: ModelingCmdId

    segment: PathSegment

    type: Literal["extend_path"] = "extend_path"


class OptionExtrude(KittyCadBaseModel):
    """Command for extruding a solid 2d."""

    distance: LengthUnit

    extrude_method: ExtrudeMethod = "merge"  # type: ignore[assignment]

    faces: Optional[ExtrudedFaceInfo] = None

    opposite: OppositeForLengthUnit = "None"  # type: ignore[assignment]

    target: ModelingCmdId

    type: Literal["extrude"] = "extrude"


class OptionExtrudeToReference(KittyCadBaseModel):
    """Command for extruding a solid 2d to a reference geometry."""

    extrude_method: ExtrudeMethod = "merge"  # type: ignore[assignment]

    faces: Optional[ExtrudedFaceInfo] = None

    reference: ExtrudeReference

    target: ModelingCmdId

    type: Literal["extrude_to_reference"] = "extrude_to_reference"


class OptionTwistExtrude(KittyCadBaseModel):
    """Command for twist extruding a solid 2d."""

    angle_step_size: Angle = {"unit": "degrees", "value": 15.0}  # type: ignore[assignment]

    center_2d: Point2d = {"x": 0.0, "y": 0.0}  # type: ignore[assignment]

    distance: LengthUnit

    faces: Optional[ExtrudedFaceInfo] = None

    target: ModelingCmdId

    tolerance: LengthUnit

    total_rotation_angle: Angle

    type: Literal["twist_extrude"] = "twist_extrude"


class OptionSweep(KittyCadBaseModel):
    """Extrude the object along a path."""

    relative_to: RelativeTo = "sketch_plane"  # type: ignore[assignment]

    sectional: bool

    target: ModelingCmdId

    tolerance: LengthUnit

    trajectory: ModelingCmdId

    type: Literal["sweep"] = "sweep"


class OptionRevolve(KittyCadBaseModel):
    """Command for revolving a solid 2d."""

    angle: Angle

    axis: Point3d

    axis_is_2d: bool

    opposite: OppositeForAngle = "None"  # type: ignore[assignment]

    origin: Point3d

    target: ModelingCmdId

    tolerance: LengthUnit

    type: Literal["revolve"] = "revolve"


class OptionSolid3dShellFace(KittyCadBaseModel):
    """Command for shelling a solid3d face"""

    face_ids: List[str]

    hollow: bool = False

    object_id: str

    shell_thickness: LengthUnit

    type: Literal["solid3d_shell_face"] = "solid3d_shell_face"


class OptionRevolveAboutEdge(KittyCadBaseModel):
    """Command for revolving a solid 2d about a brep edge"""

    angle: Angle

    edge_id: str

    opposite: OppositeForAngle = "None"  # type: ignore[assignment]

    target: ModelingCmdId

    tolerance: LengthUnit

    type: Literal["revolve_about_edge"] = "revolve_about_edge"


class OptionLoft(KittyCadBaseModel):
    """Command for lofting sections to create a solid"""

    base_curve_index: Optional[int] = None

    bez_approximate_rational: bool

    section_ids: List[str]

    tolerance: LengthUnit

    type: Literal["loft"] = "loft"

    v_degree: int


class OptionClosePath(KittyCadBaseModel):
    """Closes a path, converting it to a 2D solid."""

    path_id: str

    type: Literal["close_path"] = "close_path"


class OptionCameraDragStart(KittyCadBaseModel):
    """Camera drag started."""

    interaction: CameraDragInteractionType

    type: Literal["camera_drag_start"] = "camera_drag_start"

    window: Point2d


class OptionCameraDragMove(KittyCadBaseModel):
    """Camera drag continued."""

    interaction: CameraDragInteractionType

    sequence: Optional[int] = None

    type: Literal["camera_drag_move"] = "camera_drag_move"

    window: Point2d


class OptionCameraDragEnd(KittyCadBaseModel):
    """Camera drag ended"""

    interaction: CameraDragInteractionType

    type: Literal["camera_drag_end"] = "camera_drag_end"

    window: Point2d


class OptionDefaultCameraGetSettings(KittyCadBaseModel):
    """Gets the default camera's camera settings"""

    type: Literal["default_camera_get_settings"] = "default_camera_get_settings"


class OptionDefaultCameraGetView(KittyCadBaseModel):
    """Gets the default camera's view state"""

    type: Literal["default_camera_get_view"] = "default_camera_get_view"


class OptionDefaultCameraSetView(KittyCadBaseModel):
    """Sets the default camera's view state"""

    type: Literal["default_camera_set_view"] = "default_camera_set_view"

    view: CameraViewState


class OptionDefaultCameraLookAt(KittyCadBaseModel):
    """Change what the default camera is looking at."""

    center: Point3d

    sequence: Optional[int] = None

    type: Literal["default_camera_look_at"] = "default_camera_look_at"

    up: Point3d

    vantage: Point3d


class OptionDefaultCameraPerspectiveSettings(KittyCadBaseModel):
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


class OptionDefaultCameraZoom(KittyCadBaseModel):
    """Adjust zoom of the default camera."""

    magnitude: float

    type: Literal["default_camera_zoom"] = "default_camera_zoom"


class OptionExport2d(KittyCadBaseModel):
    """Export a sketch to a file."""

    entity_ids: List[str]

    format: OutputFormat2d

    type: Literal["export2d"] = "export2d"


class OptionExport3d(KittyCadBaseModel):
    """Export the scene to a file."""

    entity_ids: List[str]

    format: OutputFormat3d

    type: Literal["export3d"] = "export3d"


class OptionExport(KittyCadBaseModel):
    """Export the scene to a file."""

    entity_ids: List[str]

    format: OutputFormat3d

    type: Literal["export"] = "export"


class OptionEntityGetParentId(KittyCadBaseModel):
    """What is this entity's parent?"""

    entity_id: str

    type: Literal["entity_get_parent_id"] = "entity_get_parent_id"


class OptionEntityGetNumChildren(KittyCadBaseModel):
    """How many children does the entity have?"""

    entity_id: str

    type: Literal["entity_get_num_children"] = "entity_get_num_children"


class OptionEntityGetChildUuid(KittyCadBaseModel):
    """What is the UUID of this entity's n-th child?"""

    child_index: int

    entity_id: str

    type: Literal["entity_get_child_uuid"] = "entity_get_child_uuid"


class OptionEntityGetAllChildUuids(KittyCadBaseModel):
    """What are all UUIDs of this entity's children?"""

    entity_id: str

    type: Literal["entity_get_all_child_uuids"] = "entity_get_all_child_uuids"


class OptionEntityGetSketchPaths(KittyCadBaseModel):
    """What are all UUIDs of all the paths sketched on top of this entity?"""

    entity_id: str

    type: Literal["entity_get_sketch_paths"] = "entity_get_sketch_paths"


class OptionEntityGetDistance(KittyCadBaseModel):
    """What is the distance between these two entities?"""

    distance_type: DistanceType

    entity_id1: str

    entity_id2: str

    type: Literal["entity_get_distance"] = "entity_get_distance"


class OptionEntityClone(KittyCadBaseModel):
    """Create a pattern using this entity by specifying the transform for each desired repetition. Transformations are performed in the following order (first applied to last applied): scale, rotate, translate."""

    entity_id: str

    type: Literal["entity_clone"] = "entity_clone"


class OptionEntityLinearPatternTransform(KittyCadBaseModel):
    """Create a pattern using this entity by specifying the transform for each desired repetition. Transformations are performed in the following order (first applied to last applied): scale, rotate, translate."""

    entity_id: str

    transform: List[Transform] = []

    transforms: List[List[Transform]] = []

    type: Literal["entity_linear_pattern_transform"] = "entity_linear_pattern_transform"


class OptionEntityLinearPattern(KittyCadBaseModel):
    """Create a linear pattern using this entity."""

    axis: Point3d

    entity_id: str

    num_repetitions: int

    spacing: LengthUnit

    type: Literal["entity_linear_pattern"] = "entity_linear_pattern"


class OptionEntityCircularPattern(KittyCadBaseModel):
    """Create a circular pattern using this entity."""

    arc_degrees: float

    axis: Point3d

    center: Point3d

    entity_id: str

    num_repetitions: int

    rotate_duplicates: bool

    type: Literal["entity_circular_pattern"] = "entity_circular_pattern"


class OptionEntityMakeHelix(KittyCadBaseModel):
    """Create a helix using the input cylinder and other specified parameters."""

    cylinder_id: str

    is_clockwise: bool

    length: Optional[LengthUnit] = None

    revolutions: float

    start_angle: Angle = {"unit": "degrees", "value": 0.0}  # type: ignore[assignment]

    type: Literal["entity_make_helix"] = "entity_make_helix"


class OptionEntityMakeHelixFromParams(KittyCadBaseModel):
    """Create a helix using the specified parameters."""

    axis: Point3d

    center: Point3d

    is_clockwise: bool

    length: LengthUnit

    radius: LengthUnit

    revolutions: float

    start_angle: Angle = {"unit": "degrees", "value": 0.0}  # type: ignore[assignment]

    type: Literal["entity_make_helix_from_params"] = "entity_make_helix_from_params"


class OptionEntityMakeHelixFromEdge(KittyCadBaseModel):
    """Create a helix using the specified parameters."""

    edge_id: str

    is_clockwise: bool

    length: Optional[LengthUnit] = None

    radius: LengthUnit

    revolutions: float

    start_angle: Angle = {"unit": "degrees", "value": 0.0}  # type: ignore[assignment]

    type: Literal["entity_make_helix_from_edge"] = "entity_make_helix_from_edge"


class OptionEntityMirror(KittyCadBaseModel):
    """Mirror the input entities over the specified axis. (Currently only supports sketches)"""

    axis: Point3d

    ids: List[str]

    point: Point3d

    type: Literal["entity_mirror"] = "entity_mirror"


class OptionEntityMirrorAcrossEdge(KittyCadBaseModel):
    """Mirror the input entities over the specified edge. (Currently only supports sketches)"""

    edge_id: str

    ids: List[str]

    type: Literal["entity_mirror_across_edge"] = "entity_mirror_across_edge"


class OptionSelectWithPoint(KittyCadBaseModel):
    """Modifies the selection by simulating a \"mouse click\" at the given x,y window coordinate Returns ID of whatever was selected."""

    selected_at_window: Point2d

    selection_type: SceneSelectionType

    type: Literal["select_with_point"] = "select_with_point"


class OptionSelectAdd(KittyCadBaseModel):
    """Adds one or more entities (by UUID) to the selection."""

    entities: List[str]

    type: Literal["select_add"] = "select_add"


class OptionSelectRemove(KittyCadBaseModel):
    """Removes one or more entities (by UUID) from the selection."""

    entities: List[str]

    type: Literal["select_remove"] = "select_remove"


class OptionSceneClearAll(KittyCadBaseModel):
    """Removes all of the Objects in the scene"""

    type: Literal["scene_clear_all"] = "scene_clear_all"


class OptionSelectReplace(KittyCadBaseModel):
    """Replaces current selection with these entities (by UUID)."""

    entities: List[str]

    type: Literal["select_replace"] = "select_replace"


class OptionHighlightSetEntity(KittyCadBaseModel):
    """Changes the current highlighted entity to whichever one is at the given window coordinate. If there's no entity at this location, clears the highlight."""

    selected_at_window: Point2d

    sequence: Optional[int] = None

    type: Literal["highlight_set_entity"] = "highlight_set_entity"


class OptionHighlightSetEntities(KittyCadBaseModel):
    """Changes the current highlighted entity to these entities."""

    entities: List[str]

    type: Literal["highlight_set_entities"] = "highlight_set_entities"


class OptionNewAnnotation(KittyCadBaseModel):
    """Create a new annotation"""

    annotation_type: AnnotationType

    clobber: bool

    options: AnnotationOptions

    type: Literal["new_annotation"] = "new_annotation"


class OptionUpdateAnnotation(KittyCadBaseModel):
    """Update an annotation"""

    annotation_id: str

    options: AnnotationOptions

    type: Literal["update_annotation"] = "update_annotation"


class OptionEdgeLinesVisible(KittyCadBaseModel):
    """Changes visibility of scene-wide edge lines on brep solids"""

    hidden: bool

    type: Literal["edge_lines_visible"] = "edge_lines_visible"


class OptionObjectVisible(KittyCadBaseModel):
    """Hide or show an object"""

    hidden: bool

    object_id: str

    type: Literal["object_visible"] = "object_visible"


class OptionObjectBringToFront(KittyCadBaseModel):
    """Bring an object to the front of the scene"""

    object_id: str

    type: Literal["object_bring_to_front"] = "object_bring_to_front"


class OptionObjectSetMaterialParamsPbr(KittyCadBaseModel):
    """Set the material properties of an object"""

    ambient_occlusion: float

    backface_color: Optional[Color] = None

    color: Color

    metalness: float

    object_id: str

    roughness: float

    type: Literal["object_set_material_params_pbr"] = "object_set_material_params_pbr"


class OptionGetEntityType(KittyCadBaseModel):
    """What type of entity is this?"""

    entity_id: str

    type: Literal["get_entity_type"] = "get_entity_type"


class OptionSolid3dGetAllEdgeFaces(KittyCadBaseModel):
    """Gets all faces which use the given edge."""

    edge_id: str

    object_id: str

    type: Literal["solid3d_get_all_edge_faces"] = "solid3d_get_all_edge_faces"


class OptionSolid2dAddHole(KittyCadBaseModel):
    """Add a hole to a Solid2d object before extruding it."""

    hole_id: str

    object_id: str

    type: Literal["solid2d_add_hole"] = "solid2d_add_hole"


class OptionSolid3dGetAllOppositeEdges(KittyCadBaseModel):
    """Gets all edges which are opposite the given edge, across all possible faces."""

    along_vector: Optional[Point3d] = None

    edge_id: str

    object_id: str

    type: Literal["solid3d_get_all_opposite_edges"] = "solid3d_get_all_opposite_edges"


class OptionSolid3dGetOppositeEdge(KittyCadBaseModel):
    """Gets the edge opposite the given edge, along the given face."""

    edge_id: str

    face_id: str

    object_id: str

    type: Literal["solid3d_get_opposite_edge"] = "solid3d_get_opposite_edge"


class OptionSolid3dGetNextAdjacentEdge(KittyCadBaseModel):
    """Gets the next adjacent edge for the given edge, along the given face."""

    edge_id: str

    face_id: str

    object_id: str

    type: Literal["solid3d_get_next_adjacent_edge"] = "solid3d_get_next_adjacent_edge"


class OptionSolid3dGetPrevAdjacentEdge(KittyCadBaseModel):
    """Gets the previous adjacent edge for the given edge, along the given face."""

    edge_id: str

    face_id: str

    object_id: str

    type: Literal["solid3d_get_prev_adjacent_edge"] = "solid3d_get_prev_adjacent_edge"


class OptionSolid3dGetCommonEdge(KittyCadBaseModel):
    """Gets the shared edge between these two faces if it exists"""

    face_ids: List[str]

    object_id: str

    type: Literal["solid3d_get_common_edge"] = "solid3d_get_common_edge"


class OptionSolid3dFilletEdge(KittyCadBaseModel):
    """Fillets the given edge with the specified radius."""

    cut_type: CutType = "fillet"  # type: ignore[assignment]

    edge_id: Optional[str] = None

    edge_ids: List[str] = []

    extra_face_ids: List[str] = []

    object_id: str

    radius: LengthUnit

    strategy: CutStrategy = "automatic"  # type: ignore[assignment]

    tolerance: LengthUnit

    type: Literal["solid3d_fillet_edge"] = "solid3d_fillet_edge"


class OptionSolid3dCutEdges(KittyCadBaseModel):
    """Cut the list of given edges with the given cut parameters."""

    cut_type: CutTypeV2

    edge_ids: List[str] = []

    extra_face_ids: List[str] = []

    object_id: str

    strategy: CutStrategy = "automatic"  # type: ignore[assignment]

    tolerance: LengthUnit

    type: Literal["solid3d_cut_edges"] = "solid3d_cut_edges"


class OptionFaceIsPlanar(KittyCadBaseModel):
    """Determines whether a brep face is planar and returns its surface-local planar axes if so"""

    object_id: str

    type: Literal["face_is_planar"] = "face_is_planar"


class OptionFaceGetPosition(KittyCadBaseModel):
    """Determines a position on a brep face evaluated by parameters u,v"""

    object_id: str

    type: Literal["face_get_position"] = "face_get_position"

    uv: Point2d


class OptionFaceGetCenter(KittyCadBaseModel):
    """Obtains the surface \"center of mass\" """

    object_id: str

    type: Literal["face_get_center"] = "face_get_center"


class OptionFaceGetGradient(KittyCadBaseModel):
    """Determines the gradient (dFdu, dFdv) + normal vector on a brep face evaluated by parameters u,v"""

    object_id: str

    type: Literal["face_get_gradient"] = "face_get_gradient"

    uv: Point2d


class OptionSendObject(KittyCadBaseModel):
    """Send object to front or back."""

    front: bool

    object_id: str

    type: Literal["send_object"] = "send_object"


class OptionEntitySetOpacity(KittyCadBaseModel):
    """Set opacity of the entity."""

    entity_id: str

    opacity: float

    type: Literal["entity_set_opacity"] = "entity_set_opacity"


class OptionEntityFade(KittyCadBaseModel):
    """Fade entity in or out."""

    duration_seconds: float = 0.4

    entity_id: str

    fade_in: bool

    type: Literal["entity_fade"] = "entity_fade"


class OptionMakePlane(KittyCadBaseModel):
    """Make a new plane"""

    clobber: bool

    hide: Optional[bool] = None

    origin: Point3d

    size: LengthUnit

    type: Literal["make_plane"] = "make_plane"

    x_axis: Point3d

    y_axis: Point3d


class OptionPlaneSetColor(KittyCadBaseModel):
    """Set the color of a plane."""

    color: Color

    plane_id: str

    type: Literal["plane_set_color"] = "plane_set_color"


class OptionSetTool(KittyCadBaseModel):
    """Set the current tool."""

    tool: SceneToolType

    type: Literal["set_tool"] = "set_tool"


class OptionMouseMove(KittyCadBaseModel):
    """Send a mouse move event"""

    sequence: Optional[int] = None

    type: Literal["mouse_move"] = "mouse_move"

    window: Point2d


class OptionMouseClick(KittyCadBaseModel):
    """Send a mouse click event Updates modified/selected entities."""

    type: Literal["mouse_click"] = "mouse_click"

    window: Point2d


class OptionSketchModeDisable(KittyCadBaseModel):
    """Disable sketch mode. If you are sketching on a face, be sure to not disable sketch mode until you have extruded. Otherwise, your object will not be fused with the face."""

    type: Literal["sketch_mode_disable"] = "sketch_mode_disable"


class OptionGetSketchModePlane(KittyCadBaseModel):
    """Get the plane for sketch mode."""

    type: Literal["get_sketch_mode_plane"] = "get_sketch_mode_plane"


class OptionCurveSetConstraint(KittyCadBaseModel):
    """Get the plane for sketch mode."""

    constraint_bound: PathComponentConstraintBound

    constraint_type: PathComponentConstraintType

    object_id: str

    type: Literal["curve_set_constraint"] = "curve_set_constraint"


class OptionEnableSketchMode(KittyCadBaseModel):
    """Sketch on some entity (e.g. a plane, a face)."""

    adjust_camera: bool

    animated: bool

    entity_id: str

    ortho: bool

    planar_normal: Optional[Point3d] = None

    type: Literal["enable_sketch_mode"] = "enable_sketch_mode"


class OptionEnableDryRun(KittyCadBaseModel):
    """Sets whether or not changes to the scene or its objects will be done as a \"dry run\" In a dry run, successful commands won't actually change the model. This is useful for catching errors before actually making the change."""

    type: Literal["enable_dry_run"] = "enable_dry_run"


class OptionDisableDryRun(KittyCadBaseModel):
    """Sets whether or not changes to the scene or its objects will be done as a \"dry run\" In a dry run, successful commands won't actually change the model. This is useful for catching errors before actually making the change."""

    type: Literal["disable_dry_run"] = "disable_dry_run"


class OptionSetBackgroundColor(KittyCadBaseModel):
    """Set the background color of the scene."""

    color: Color

    type: Literal["set_background_color"] = "set_background_color"


class OptionSetCurrentToolProperties(KittyCadBaseModel):
    """Set the properties of the tool lines for the scene."""

    color: Optional[Color] = None

    type: Literal["set_current_tool_properties"] = "set_current_tool_properties"


class OptionSetDefaultSystemProperties(KittyCadBaseModel):
    """Set the default system properties used when a specific property isn't set."""

    color: Optional[Color] = None

    type: Literal["set_default_system_properties"] = "set_default_system_properties"


class OptionCurveGetType(KittyCadBaseModel):
    """Get type of the given curve."""

    curve_id: str

    type: Literal["curve_get_type"] = "curve_get_type"


class OptionCurveGetControlPoints(KittyCadBaseModel):
    """Get control points of the given curve."""

    curve_id: str

    type: Literal["curve_get_control_points"] = "curve_get_control_points"


class OptionProjectEntityToPlane(KittyCadBaseModel):
    """Project an entity on to a plane."""

    entity_id: str

    plane_id: str

    type: Literal["project_entity_to_plane"] = "project_entity_to_plane"

    use_plane_coords: bool


class OptionProjectPointsToPlane(KittyCadBaseModel):
    """Project a list of points on to a plane."""

    plane_id: str

    points: List[Point3d]

    type: Literal["project_points_to_plane"] = "project_points_to_plane"

    use_plane_coords: bool


class OptionTakeSnapshot(KittyCadBaseModel):
    """Take a snapshot of the current view."""

    format: ImageFormat

    type: Literal["take_snapshot"] = "take_snapshot"


class OptionMakeAxesGizmo(KittyCadBaseModel):
    """Add a gizmo showing the axes."""

    clobber: bool

    gizmo_mode: bool

    type: Literal["make_axes_gizmo"] = "make_axes_gizmo"


class OptionPathGetInfo(KittyCadBaseModel):
    """Query the given path."""

    path_id: str

    type: Literal["path_get_info"] = "path_get_info"


class OptionPathGetCurveUuidsForVertices(KittyCadBaseModel):
    """Obtain curve ids for vertex ids"""

    path_id: str

    type: Literal["path_get_curve_uuids_for_vertices"] = (
        "path_get_curve_uuids_for_vertices"
    )

    vertex_ids: List[str]


class OptionPathGetCurveUuid(KittyCadBaseModel):
    """Obtain curve id by index"""

    index: int

    path_id: str

    type: Literal["path_get_curve_uuid"] = "path_get_curve_uuid"


class OptionPathGetVertexUuids(KittyCadBaseModel):
    """Obtain vertex ids for a path"""

    path_id: str

    type: Literal["path_get_vertex_uuids"] = "path_get_vertex_uuids"


class OptionPathGetSketchTargetUuid(KittyCadBaseModel):
    """Obtain the sketch target id (if the path was drawn in sketchmode) for a path"""

    path_id: str

    type: Literal["path_get_sketch_target_uuid"] = "path_get_sketch_target_uuid"


class OptionHandleMouseDragStart(KittyCadBaseModel):
    """Start dragging the mouse."""

    type: Literal["handle_mouse_drag_start"] = "handle_mouse_drag_start"

    window: Point2d


class OptionHandleMouseDragMove(KittyCadBaseModel):
    """Continue dragging the mouse."""

    sequence: Optional[int] = None

    type: Literal["handle_mouse_drag_move"] = "handle_mouse_drag_move"

    window: Point2d


class OptionHandleMouseDragEnd(KittyCadBaseModel):
    """Stop dragging the mouse."""

    type: Literal["handle_mouse_drag_end"] = "handle_mouse_drag_end"

    window: Point2d


class OptionRemoveSceneObjects(KittyCadBaseModel):
    """Remove scene objects."""

    object_ids: List[str]

    type: Literal["remove_scene_objects"] = "remove_scene_objects"


class OptionPlaneIntersectAndProject(KittyCadBaseModel):
    """Utility method. Performs both a ray cast and projection to plane-local coordinates. Returns the plane coordinates for the given window coordinates."""

    plane_id: str

    type: Literal["plane_intersect_and_project"] = "plane_intersect_and_project"

    window: Point2d


class OptionCurveGetEndPoints(KittyCadBaseModel):
    """Find the start and end of a curve."""

    curve_id: str

    type: Literal["curve_get_end_points"] = "curve_get_end_points"


class OptionReconfigureStream(KittyCadBaseModel):
    """Reconfigure the stream."""

    bitrate: Optional[int] = None

    fps: int

    height: int

    type: Literal["reconfigure_stream"] = "reconfigure_stream"

    width: int


class OptionImportFiles(KittyCadBaseModel):
    """Import files to the current model."""

    files: List[ImportFile]

    format: InputFormat3d

    type: Literal["import_files"] = "import_files"


class OptionSetSceneUnits(KittyCadBaseModel):
    """Set the units of the scene. For all following commands, the units will be interpreted as the given units. Any previously executed commands will not be affected or have their units changed. They will remain in the units they were originally executed in."""

    type: Literal["set_scene_units"] = "set_scene_units"

    unit: UnitLength


class OptionMass(KittyCadBaseModel):
    """Get the mass of entities in the scene or the default scene."""

    entity_ids: List[str]

    material_density: float

    material_density_unit: UnitDensity

    output_unit: UnitMass

    type: Literal["mass"] = "mass"


class OptionDensity(KittyCadBaseModel):
    """Get the density of entities in the scene or the default scene."""

    entity_ids: List[str]

    material_mass: float

    material_mass_unit: UnitMass

    output_unit: UnitDensity

    type: Literal["density"] = "density"


class OptionVolume(KittyCadBaseModel):
    """Get the volume of entities in the scene or the default scene."""

    entity_ids: List[str]

    output_unit: UnitVolume

    type: Literal["volume"] = "volume"


class OptionCenterOfMass(KittyCadBaseModel):
    """Get the center of mass of entities in the scene or the default scene."""

    entity_ids: List[str]

    output_unit: UnitLength

    type: Literal["center_of_mass"] = "center_of_mass"


class OptionSurfaceArea(KittyCadBaseModel):
    """Get the surface area of entities in the scene or the default scene."""

    entity_ids: List[str]

    output_unit: UnitArea

    type: Literal["surface_area"] = "surface_area"


class OptionDefaultCameraFocusOn(KittyCadBaseModel):
    """Focus the default camera upon an object in the scene."""

    type: Literal["default_camera_focus_on"] = "default_camera_focus_on"

    uuid: str


class OptionSetSelectionType(KittyCadBaseModel):
    """When you select some entity with the current tool, what should happen to the entity?"""

    selection_type: SceneSelectionType

    type: Literal["set_selection_type"] = "set_selection_type"


class OptionSetSelectionFilter(KittyCadBaseModel):
    """What kind of entities can be selected?"""

    filter: List[EntityType]

    type: Literal["set_selection_filter"] = "set_selection_filter"


class OptionSceneGetEntityIds(KittyCadBaseModel):
    """Get the ids of a given entity type."""

    filter: List[EntityType]

    skip: int

    take: int

    type: Literal["scene_get_entity_ids"] = "scene_get_entity_ids"


class OptionDefaultCameraSetOrthographic(KittyCadBaseModel):
    """Use orthographic projection."""

    type: Literal["default_camera_set_orthographic"] = "default_camera_set_orthographic"


class OptionDefaultCameraSetPerspective(KittyCadBaseModel):
    """Use perspective projection."""

    parameters: Optional[PerspectiveCameraParameters] = None

    type: Literal["default_camera_set_perspective"] = "default_camera_set_perspective"


class OptionDefaultCameraCenterToSelection(KittyCadBaseModel):
    """Updates the camera to center to the center of the current selection (or the origin if nothing is selected)"""

    camera_movement: CameraMovement = "vantage"  # type: ignore[assignment]

    type: Literal["default_camera_center_to_selection"] = (
        "default_camera_center_to_selection"
    )


class OptionDefaultCameraCenterToScene(KittyCadBaseModel):
    """Updates the camera to center to the center of the current scene's bounds"""

    camera_movement: CameraMovement = "vantage"  # type: ignore[assignment]

    type: Literal["default_camera_center_to_scene"] = "default_camera_center_to_scene"


class OptionZoomToFit(KittyCadBaseModel):
    """Fit the view to the specified object(s)."""

    animated: bool = False

    object_ids: List[str] = []

    padding: float = 0.0

    type: Literal["zoom_to_fit"] = "zoom_to_fit"


class OptionOrientToFace(KittyCadBaseModel):
    """Looks along the normal of the specified face (if it is planar!), and fits the view to it."""

    animated: bool = False

    face_id: str

    padding: float = 0.0

    type: Literal["orient_to_face"] = "orient_to_face"


class OptionViewIsometric(KittyCadBaseModel):
    """Fit the view to the scene with an isometric view."""

    padding: float = 0.0

    type: Literal["view_isometric"] = "view_isometric"


class OptionSolid3dGetExtrusionFaceInfo(KittyCadBaseModel):
    """Get a concise description of all of an extrusion's faces."""

    edge_id: str

    object_id: str

    type: Literal["solid3d_get_extrusion_face_info"] = "solid3d_get_extrusion_face_info"


class OptionSolid3dGetAdjacencyInfo(KittyCadBaseModel):
    """Get a concise description of all of solids edges."""

    edge_id: str

    object_id: str

    type: Literal["solid3d_get_adjacency_info"] = "solid3d_get_adjacency_info"


class OptionSelectClear(KittyCadBaseModel):
    """Clear the selection"""

    type: Literal["select_clear"] = "select_clear"


class OptionSelectGet(KittyCadBaseModel):
    """Find all IDs of selected entities"""

    type: Literal["select_get"] = "select_get"


class OptionGetNumObjects(KittyCadBaseModel):
    """Get the number of objects in the scene"""

    type: Literal["get_num_objects"] = "get_num_objects"


class OptionSetObjectTransform(KittyCadBaseModel):
    """Set the transform of an object."""

    object_id: str

    transforms: List[ComponentTransform]

    type: Literal["set_object_transform"] = "set_object_transform"


class OptionBooleanUnion(KittyCadBaseModel):
    """Create a new solid from combining other smaller solids. In other words, every part of the input solids will be included in the output solid."""

    solid_ids: List[str]

    tolerance: LengthUnit

    type: Literal["boolean_union"] = "boolean_union"


class OptionBooleanIntersection(KittyCadBaseModel):
    """Create a new solid from intersecting several other solids. In other words, the part of the input solids where they all overlap will be the output solid."""

    solid_ids: List[str]

    tolerance: LengthUnit

    type: Literal["boolean_intersection"] = "boolean_intersection"


class OptionBooleanSubtract(KittyCadBaseModel):
    """Create a new solid from subtracting several other solids. The 'target' is what will be cut from. The 'tool' is what will be cut out from 'target'."""

    target_ids: List[str]

    tolerance: LengthUnit

    tool_ids: List[str]

    type: Literal["boolean_subtract"] = "boolean_subtract"


class OptionMakeOffsetPath(KittyCadBaseModel):
    """Make a new path by offsetting an object by a given distance. The new path's ID will be the ID of this command."""

    face_id: Optional[str] = None

    object_id: str

    offset: LengthUnit

    type: Literal["make_offset_path"] = "make_offset_path"


class OptionAddHoleFromOffset(KittyCadBaseModel):
    """Add a hole to a closed path by offsetting it a uniform distance inward."""

    object_id: str

    offset: LengthUnit

    type: Literal["add_hole_from_offset"] = "add_hole_from_offset"


class OptionSetGridReferencePlane(KittyCadBaseModel):
    """Align the grid with a plane or a planar face."""

    grid_id: str

    reference_id: str

    type: Literal["set_grid_reference_plane"] = "set_grid_reference_plane"


class OptionSetGridScale(KittyCadBaseModel):
    """Set the scale of the grid lines in the video feed."""

    type: Literal["set_grid_scale"] = "set_grid_scale"

    units: UnitLength

    value: float


class OptionSetGridAutoScale(KittyCadBaseModel):
    """Set the grid lines to auto scale. The grid will get larger the further you zoom out, and smaller the more you zoom in."""

    type: Literal["set_grid_auto_scale"] = "set_grid_auto_scale"


class OptionSetOrderIndependentTransparency(KittyCadBaseModel):
    """Render transparent surfaces more accurately, but this might make rendering slower. Because it can interfere with runtime performance, it defaults to false."""

    enabled: Optional[bool] = None

    type: Literal["set_order_independent_transparency"] = (
        "set_order_independent_transparency"
    )


ModelingCmd = RootModel[
    Annotated[
        Union[
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
            OptionLoft,
            OptionClosePath,
            OptionCameraDragStart,
            OptionCameraDragMove,
            OptionCameraDragEnd,
            OptionDefaultCameraGetSettings,
            OptionDefaultCameraGetView,
            OptionDefaultCameraSetView,
            OptionDefaultCameraLookAt,
            OptionDefaultCameraPerspectiveSettings,
            OptionDefaultCameraZoom,
            OptionExport2d,
            OptionExport3d,
            OptionExport,
            OptionEntityGetParentId,
            OptionEntityGetNumChildren,
            OptionEntityGetChildUuid,
            OptionEntityGetAllChildUuids,
            OptionEntityGetSketchPaths,
            OptionEntityGetDistance,
            OptionEntityClone,
            OptionEntityLinearPatternTransform,
            OptionEntityLinearPattern,
            OptionEntityCircularPattern,
            OptionEntityMakeHelix,
            OptionEntityMakeHelixFromParams,
            OptionEntityMakeHelixFromEdge,
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
            OptionSolid3dGetAllEdgeFaces,
            OptionSolid2dAddHole,
            OptionSolid3dGetAllOppositeEdges,
            OptionSolid3dGetOppositeEdge,
            OptionSolid3dGetNextAdjacentEdge,
            OptionSolid3dGetPrevAdjacentEdge,
            OptionSolid3dGetCommonEdge,
            OptionSolid3dFilletEdge,
            OptionSolid3dCutEdges,
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
            OptionProjectEntityToPlane,
            OptionProjectPointsToPlane,
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
            OptionSceneGetEntityIds,
            OptionDefaultCameraSetOrthographic,
            OptionDefaultCameraSetPerspective,
            OptionDefaultCameraCenterToSelection,
            OptionDefaultCameraCenterToScene,
            OptionZoomToFit,
            OptionOrientToFace,
            OptionViewIsometric,
            OptionSolid3dGetExtrusionFaceInfo,
            OptionSolid3dGetAdjacencyInfo,
            OptionSelectClear,
            OptionSelectGet,
            OptionGetNumObjects,
            OptionSetObjectTransform,
            OptionBooleanUnion,
            OptionBooleanIntersection,
            OptionBooleanSubtract,
            OptionMakeOffsetPath,
            OptionAddHoleFromOffset,
            OptionSetGridReferencePlane,
            OptionSetGridScale,
            OptionSetGridAutoScale,
            OptionSetOrderIndependentTransparency,
        ],
        Field(discriminator="type"),
    ]
]
