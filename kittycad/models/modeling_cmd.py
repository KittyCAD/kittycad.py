from typing import List, Literal, Optional, Union

from pydantic import BaseModel, Field, RootModel
from typing_extensions import Annotated

from ..models.annotation_options import AnnotationOptions
from ..models.annotation_type import AnnotationType
from ..models.camera_drag_interaction_type import CameraDragInteractionType
from ..models.color import Color
from ..models.distance_type import DistanceType
from ..models.image_format import ImageFormat
from ..models.import_file import ImportFile
from ..models.input_format import InputFormat
from ..models.modeling_cmd_id import ModelingCmdId
from ..models.output_format import OutputFormat
from ..models.path_component_constraint_bound import PathComponentConstraintBound
from ..models.path_component_constraint_type import PathComponentConstraintType
from ..models.path_segment import PathSegment
from ..models.point2d import Point2d
from ..models.point3d import Point3d
from ..models.scene_selection_type import SceneSelectionType
from ..models.scene_tool_type import SceneToolType
from ..models.unit_area import UnitArea
from ..models.unit_density import UnitDensity
from ..models.unit_length import UnitLength
from ..models.unit_mass import UnitMass
from ..models.unit_volume import UnitVolume


class start_path(BaseModel):
    """Start a path."""

    type: Literal["start_path"] = "start_path"


class move_path_pen(BaseModel):
    """Move the path's "pen"."""

    path: ModelingCmdId

    to: Point3d

    type: Literal["move_path_pen"] = "move_path_pen"


class extend_path(BaseModel):
    """Extend a path by adding a new segment which starts at the path's "pen". If no "pen" location has been set before (via `MovePen`), then the pen is at the origin."""

    path: ModelingCmdId

    segment: PathSegment

    type: Literal["extend_path"] = "extend_path"


class extrude(BaseModel):
    """Extrude a 2D solid."""

    cap: bool

    distance: float

    target: ModelingCmdId

    type: Literal["extrude"] = "extrude"


class close_path(BaseModel):
    """Closes a path, converting it to a 2D solid."""

    path_id: str

    type: Literal["close_path"] = "close_path"


class camera_drag_start(BaseModel):
    """Camera drag started."""

    interaction: CameraDragInteractionType

    type: Literal["camera_drag_start"] = "camera_drag_start"

    window: Point2d


class camera_drag_move(BaseModel):
    """Camera drag continued."""

    interaction: CameraDragInteractionType

    sequence: Optional[int] = None

    type: Literal["camera_drag_move"] = "camera_drag_move"

    window: Point2d


class camera_drag_end(BaseModel):
    """Camera drag ended."""

    interaction: CameraDragInteractionType

    type: Literal["camera_drag_end"] = "camera_drag_end"

    window: Point2d


class default_camera_look_at(BaseModel):
    """Change what the default camera is looking at."""

    center: Point3d

    type: Literal["default_camera_look_at"] = "default_camera_look_at"

    up: Point3d

    vantage: Point3d


class default_camera_zoom(BaseModel):
    """Adjust zoom of the default camera."""

    magnitude: float

    type: Literal["default_camera_zoom"] = "default_camera_zoom"


class default_camera_enable_sketch_mode(BaseModel):
    """Enable sketch mode, where users can sketch 2D geometry. Users choose a plane to sketch on."""

    animated: bool

    distance_to_plane: float

    origin: Point3d

    ortho: bool

    type: Literal[
        "default_camera_enable_sketch_mode"
    ] = "default_camera_enable_sketch_mode"

    x_axis: Point3d

    y_axis: Point3d


class default_camera_disable_sketch_mode(BaseModel):
    """Disable sketch mode, from the default camera."""

    type: Literal[
        "default_camera_disable_sketch_mode"
    ] = "default_camera_disable_sketch_mode"


class default_camera_focus_on(BaseModel):
    """Focus default camera on object."""

    type: Literal["default_camera_focus_on"] = "default_camera_focus_on"

    uuid: str


class export(BaseModel):
    """Export the scene to a file."""

    entity_ids: List[str]

    format: OutputFormat

    source_unit: UnitLength

    type: Literal["export"] = "export"


class entity_get_parent_id(BaseModel):
    """What is this entity's parent?"""

    entity_id: str

    type: Literal["entity_get_parent_id"] = "entity_get_parent_id"


class entity_get_num_children(BaseModel):
    """How many children does the entity have?"""

    entity_id: str

    type: Literal["entity_get_num_children"] = "entity_get_num_children"


class entity_get_child_uuid(BaseModel):
    """What is the UUID of this entity's n-th child?"""

    child_index: int

    entity_id: str

    type: Literal["entity_get_child_uuid"] = "entity_get_child_uuid"


class entity_get_all_child_uuids(BaseModel):
    """What are all UUIDs of this entity's children?"""

    entity_id: str

    type: Literal["entity_get_all_child_uuids"] = "entity_get_all_child_uuids"


class edit_mode_enter(BaseModel):
    """Enter edit mode"""

    target: str

    type: Literal["edit_mode_enter"] = "edit_mode_enter"


class edit_mode_exit(BaseModel):
    """Exit edit mode"""

    type: Literal["edit_mode_exit"] = "edit_mode_exit"


class select_with_point(BaseModel):
    """Modifies the selection by simulating a "mouse click" at the given x,y window coordinate Returns ID of whatever was selected."""

    selected_at_window: Point2d

    selection_type: SceneSelectionType

    type: Literal["select_with_point"] = "select_with_point"


class select_clear(BaseModel):
    """Clear the selection"""

    type: Literal["select_clear"] = "select_clear"


class select_add(BaseModel):
    """Adds one or more entities (by UUID) to the selection."""

    entities: List[str]

    type: Literal["select_add"] = "select_add"


class select_remove(BaseModel):
    """Removes one or more entities (by UUID) from the selection."""

    entities: List[str]

    type: Literal["select_remove"] = "select_remove"


class select_replace(BaseModel):
    """Replaces the current selection with these new entities (by UUID). Equivalent to doing SelectClear then SelectAdd."""

    entities: List[str]

    type: Literal["select_replace"] = "select_replace"


class select_get(BaseModel):
    """Find all IDs of selected entities"""

    type: Literal["select_get"] = "select_get"


class highlight_set_entity(BaseModel):
    """Changes the current highlighted entity to whichever one is at the given window coordinate. If there's no entity at this location, clears the highlight."""

    selected_at_window: Point2d

    sequence: Optional[int] = None

    type: Literal["highlight_set_entity"] = "highlight_set_entity"


class highlight_set_entities(BaseModel):
    """Changes the current highlighted entity to these entities."""

    entities: List[str]

    type: Literal["highlight_set_entities"] = "highlight_set_entities"


class new_annotation(BaseModel):
    """Create a new annotation"""

    annotation_type: AnnotationType

    clobber: bool

    options: AnnotationOptions

    type: Literal["new_annotation"] = "new_annotation"


class update_annotation(BaseModel):
    """Update an annotation"""

    annotation_id: str

    options: AnnotationOptions

    type: Literal["update_annotation"] = "update_annotation"


class object_visible(BaseModel):
    """Hide or show an object"""

    hidden: bool

    object_id: str

    type: Literal["object_visible"] = "object_visible"


class object_bring_to_front(BaseModel):
    """Bring an object to the front of the scene"""

    object_id: str

    type: Literal["object_bring_to_front"] = "object_bring_to_front"


class get_entity_type(BaseModel):
    """What type of entity is this?"""

    entity_id: str

    type: Literal["get_entity_type"] = "get_entity_type"


class solid2d_add_hole(BaseModel):
    """Add a hole to a Solid2d object before extruding it."""

    hole_id: str

    object_id: str

    type: Literal["solid2d_add_hole"] = "solid2d_add_hole"


class solid3d_get_all_edge_faces(BaseModel):
    """Gets all faces which use the given edge."""

    edge_id: str

    object_id: str

    type: Literal["solid3d_get_all_edge_faces"] = "solid3d_get_all_edge_faces"


class solid3d_get_all_opposite_edges(BaseModel):
    """Gets all edges which are opposite the given edge, across all possible faces."""

    along_vector: Optional[Point3d] = None

    edge_id: str

    object_id: str

    type: Literal["solid3d_get_all_opposite_edges"] = "solid3d_get_all_opposite_edges"


class solid3d_get_opposite_edge(BaseModel):
    """Gets the edge opposite the given edge, along the given face."""

    edge_id: str

    face_id: str

    object_id: str

    type: Literal["solid3d_get_opposite_edge"] = "solid3d_get_opposite_edge"


class solid3d_get_next_adjacent_edge(BaseModel):
    """Gets the next adjacent edge for the given edge, along the given face."""

    edge_id: str

    face_id: str

    object_id: str

    type: Literal["solid3d_get_next_adjacent_edge"] = "solid3d_get_next_adjacent_edge"


class solid3d_get_prev_adjacent_edge(BaseModel):
    """Gets the previous adjacent edge for the given edge, along the given face."""

    edge_id: str

    face_id: str

    object_id: str

    type: Literal["solid3d_get_prev_adjacent_edge"] = "solid3d_get_prev_adjacent_edge"


class send_object(BaseModel):
    """Sends object to front or back."""

    front: bool

    object_id: str

    type: Literal["send_object"] = "send_object"


class entity_set_opacity(BaseModel):
    """Set opacity of the entity."""

    entity_id: str

    opacity: float

    type: Literal["entity_set_opacity"] = "entity_set_opacity"


class entity_fade(BaseModel):
    """Fade the entity in or out."""

    duration_seconds: Optional[float] = None

    entity_id: str

    fade_in: bool

    type: Literal["entity_fade"] = "entity_fade"


class make_plane(BaseModel):
    """Make a plane."""

    clobber: bool

    hide: Optional[bool] = None

    origin: Point3d

    size: float

    type: Literal["make_plane"] = "make_plane"

    x_axis: Point3d

    y_axis: Point3d


class plane_set_color(BaseModel):
    """Set the plane's color."""

    color: Color

    plane_id: str

    type: Literal["plane_set_color"] = "plane_set_color"


class set_tool(BaseModel):
    """Set the active tool."""

    tool: SceneToolType

    type: Literal["set_tool"] = "set_tool"


class mouse_move(BaseModel):
    """Send a mouse move event."""

    sequence: Optional[int] = None

    type: Literal["mouse_move"] = "mouse_move"

    window: Point2d


class mouse_click(BaseModel):
    """Send a mouse click event. Updates modified/selected entities."""

    type: Literal["mouse_click"] = "mouse_click"

    window: Point2d


class sketch_mode_enable(BaseModel):
    """Enable sketch mode on the given plane."""

    animated: bool

    disable_camera_with_plane: Optional[Point3d] = None

    ortho: bool

    plane_id: str

    type: Literal["sketch_mode_enable"] = "sketch_mode_enable"


class sketch_mode_disable(BaseModel):
    """Disable sketch mode."""

    type: Literal["sketch_mode_disable"] = "sketch_mode_disable"


class curve_get_type(BaseModel):
    """Get type of a given curve."""

    curve_id: str

    type: Literal["curve_get_type"] = "curve_get_type"


class curve_get_control_points(BaseModel):
    """Get control points of a given curve."""

    curve_id: str

    type: Literal["curve_get_control_points"] = "curve_get_control_points"


class take_snapshot(BaseModel):
    """Take a snapshot."""

    format: ImageFormat

    type: Literal["take_snapshot"] = "take_snapshot"


class make_axes_gizmo(BaseModel):
    """Add a gizmo showing the axes."""

    clobber: bool

    gizmo_mode: bool

    type: Literal["make_axes_gizmo"] = "make_axes_gizmo"


class path_get_info(BaseModel):
    """Query the given path"""

    path_id: str

    type: Literal["path_get_info"] = "path_get_info"


class path_get_curve_uuids_for_vertices(BaseModel):
    """Get curves for vertices within a path"""

    path_id: str

    type: Literal[
        "path_get_curve_uuids_for_vertices"
    ] = "path_get_curve_uuids_for_vertices"

    vertex_ids: List[str]


class path_get_vertex_uuids(BaseModel):
    """Get vertices within a path"""

    path_id: str

    type: Literal["path_get_vertex_uuids"] = "path_get_vertex_uuids"


class handle_mouse_drag_start(BaseModel):
    """Start dragging mouse."""

    type: Literal["handle_mouse_drag_start"] = "handle_mouse_drag_start"

    window: Point2d


class handle_mouse_drag_move(BaseModel):
    """Continue dragging mouse."""

    sequence: Optional[int] = None

    type: Literal["handle_mouse_drag_move"] = "handle_mouse_drag_move"

    window: Point2d


class handle_mouse_drag_end(BaseModel):
    """Stop dragging mouse."""

    type: Literal["handle_mouse_drag_end"] = "handle_mouse_drag_end"

    window: Point2d


class remove_scene_objects(BaseModel):
    """Remove scene objects."""

    object_ids: List[str]

    type: Literal["remove_scene_objects"] = "remove_scene_objects"


class plane_intersect_and_project(BaseModel):
    """Utility method. Performs both a ray cast and projection to plane-local coordinates. Returns the plane coordinates for the given window coordinates."""

    plane_id: str

    type: Literal["plane_intersect_and_project"] = "plane_intersect_and_project"

    window: Point2d


class curve_get_end_points(BaseModel):
    """Find the start and end of a curve."""

    curve_id: str

    type: Literal["curve_get_end_points"] = "curve_get_end_points"


class reconfigure_stream(BaseModel):
    """Reconfigure the stream."""

    fps: int

    height: int

    type: Literal["reconfigure_stream"] = "reconfigure_stream"

    width: int


class import_files(BaseModel):
    """Import files to the current model."""

    files: List[ImportFile]

    format: InputFormat

    type: Literal["import_files"] = "import_files"


class mass(BaseModel):
    """Get the mass of entities in the scene or the default scene."""

    entity_ids: List[str]

    material_density: float

    material_density_unit: UnitDensity

    output_unit: UnitMass

    source_unit: UnitLength

    type: Literal["mass"] = "mass"


class density(BaseModel):
    """Get the density of entities in the scene or the default scene."""

    entity_ids: List[str]

    material_mass: float

    material_mass_unit: UnitMass

    output_unit: UnitDensity

    source_unit: UnitLength

    type: Literal["density"] = "density"


class volume(BaseModel):
    """Get the volume of entities in the scene or the default scene."""

    entity_ids: List[str]

    output_unit: UnitVolume

    source_unit: UnitLength

    type: Literal["volume"] = "volume"


class center_of_mass(BaseModel):
    """Get the center of mass of entities in the scene or the default scene."""

    entity_ids: List[str]

    output_unit: UnitLength

    source_unit: UnitLength

    type: Literal["center_of_mass"] = "center_of_mass"


class surface_area(BaseModel):
    """Get the surface area of entities in the scene or the default scene."""

    entity_ids: List[str]

    output_unit: UnitArea

    source_unit: UnitLength

    type: Literal["surface_area"] = "surface_area"


class get_sketch_mode_plane(BaseModel):
    """Get the plane of the sketch mode. This is useful for getting the normal of the plane after a user selects a plane."""

    type: Literal["get_sketch_mode_plane"] = "get_sketch_mode_plane"


class curve_set_constraint(BaseModel):
    """Constrain a curve."""

    constraint_bound: PathComponentConstraintBound

    constraint_type: PathComponentConstraintType

    object_id: str

    type: Literal["curve_set_constraint"] = "curve_set_constraint"


class enable_sketch_mode(BaseModel):
    """Sketch on some entity (e.g. a plane, a face)"""

    animated: bool

    entity_id: str

    ortho: bool

    type: Literal["enable_sketch_mode"] = "enable_sketch_mode"


class object_set_material_params_pbr(BaseModel):
    """Set the material properties of an object"""

    ambient_occlusion: float

    color: Color

    metalness: float

    object_id: str

    roughness: float

    type: Literal["object_set_material_params_pbr"] = "object_set_material_params_pbr"


class entity_get_distance(BaseModel):
    """What is the distance between these two entities?"""

    distance_type: DistanceType

    entity_id1: str

    entity_id2: str

    type: Literal["entity_get_distance"] = "entity_get_distance"


class entity_linear_pattern(BaseModel):
    """Duplicate the given entity, evenly spaced along the chosen axis."""

    axis: Point3d

    entity_id: str

    num_repetitions: int

    spacing: float

    type: Literal["entity_linear_pattern"] = "entity_linear_pattern"


ModelingCmd = RootModel[
    Annotated[
        Union[
            start_path,
            move_path_pen,
            extend_path,
            extrude,
            close_path,
            camera_drag_start,
            camera_drag_move,
            camera_drag_end,
            default_camera_look_at,
            default_camera_zoom,
            default_camera_enable_sketch_mode,
            default_camera_disable_sketch_mode,
            default_camera_focus_on,
            export,
            entity_get_parent_id,
            entity_get_num_children,
            entity_get_child_uuid,
            entity_get_all_child_uuids,
            edit_mode_enter,
            edit_mode_exit,
            select_with_point,
            select_clear,
            select_add,
            select_remove,
            select_replace,
            select_get,
            highlight_set_entity,
            highlight_set_entities,
            new_annotation,
            update_annotation,
            object_visible,
            object_bring_to_front,
            get_entity_type,
            solid2d_add_hole,
            solid3d_get_all_edge_faces,
            solid3d_get_all_opposite_edges,
            solid3d_get_opposite_edge,
            solid3d_get_next_adjacent_edge,
            solid3d_get_prev_adjacent_edge,
            send_object,
            entity_set_opacity,
            entity_fade,
            make_plane,
            plane_set_color,
            set_tool,
            mouse_move,
            mouse_click,
            sketch_mode_enable,
            sketch_mode_disable,
            curve_get_type,
            curve_get_control_points,
            take_snapshot,
            make_axes_gizmo,
            path_get_info,
            path_get_curve_uuids_for_vertices,
            path_get_vertex_uuids,
            handle_mouse_drag_start,
            handle_mouse_drag_move,
            handle_mouse_drag_end,
            remove_scene_objects,
            plane_intersect_and_project,
            curve_get_end_points,
            reconfigure_stream,
            import_files,
            mass,
            density,
            volume,
            center_of_mass,
            surface_area,
            get_sketch_mode_plane,
            curve_set_constraint,
            enable_sketch_mode,
            object_set_material_params_pbr,
            entity_get_distance,
            entity_linear_pattern,
        ],
        Field(discriminator="type"),
    ]
]
