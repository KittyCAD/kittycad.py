from typing import Any, Dict, List, Optional, Type, TypeVar, Union
from uuid import UUID

import attr
from pydantic import BaseModel, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema

from ..models.annotation_options import AnnotationOptions
from ..models.annotation_type import AnnotationType
from ..models.camera_drag_interaction_type import CameraDragInteractionType
from ..models.color import Color
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

    type: str = "start_path"


class move_path_pen(BaseModel):
    """Move the path's "pen"."""

    path: ModelingCmdId

    to: Point3d

    type: str = "move_path_pen"


class extend_path(BaseModel):
    """Extend a path by adding a new segment which starts at the path's "pen". If no "pen" location has been set before (via `MovePen`), then the pen is at the origin."""

    path: ModelingCmdId

    segment: PathSegment

    type: str = "extend_path"


class extrude(BaseModel):
    """Extrude a 2D solid."""

    cap: bool

    distance: float

    target: ModelingCmdId

    type: str = "extrude"


class close_path(BaseModel):
    """Closes a path, converting it to a 2D solid."""

    path_id: UUID

    type: str = "close_path"


class camera_drag_start(BaseModel):
    """Camera drag started."""

    interaction: CameraDragInteractionType

    type: str = "camera_drag_start"

    window: Point2d


class camera_drag_move(BaseModel):
    """Camera drag continued."""

    interaction: CameraDragInteractionType

    sequence: Optional[int] = None

    type: str = "camera_drag_move"

    window: Point2d


class camera_drag_end(BaseModel):
    """Camera drag ended."""

    interaction: CameraDragInteractionType

    type: str = "camera_drag_end"

    window: Point2d


class default_camera_look_at(BaseModel):
    """Change what the default camera is looking at."""

    center: Point3d

    type: str = "default_camera_look_at"

    up: Point3d

    vantage: Point3d


class default_camera_zoom(BaseModel):
    """Adjust zoom of the default camera."""

    magnitude: float

    type: str = "default_camera_zoom"


class default_camera_enable_sketch_mode(BaseModel):
    """Enable sketch mode, where users can sketch 2D geometry. Users choose a plane to sketch on."""

    animated: bool

    distance_to_plane: float

    origin: Point3d

    ortho: bool

    type: str = "default_camera_enable_sketch_mode"

    x_axis: Point3d

    y_axis: Point3d


class default_camera_disable_sketch_mode(BaseModel):
    """Disable sketch mode, from the default camera."""

    type: str = "default_camera_disable_sketch_mode"


class default_camera_focus_on(BaseModel):
    """Focus default camera on object."""

    type: str = "default_camera_focus_on"

    uuid: UUID


class export(BaseModel):
    """Export the scene to a file."""

    entity_ids: List[UUID]

    format: OutputFormat

    source_unit: UnitLength

    type: str = "export"


class entity_get_parent_id(BaseModel):
    """What is this entity's parent?"""

    entity_id: UUID

    type: str = "entity_get_parent_id"


class entity_get_num_children(BaseModel):
    """How many children does the entity have?"""

    entity_id: UUID

    type: str = "entity_get_num_children"


class entity_get_child_uuid(BaseModel):
    """What is the UUID of this entity's n-th child?"""

    child_index: int

    entity_id: UUID

    type: str = "entity_get_child_uuid"


class entity_get_all_child_uuids(BaseModel):
    """What are all UUIDs of this entity's children?"""

    entity_id: UUID

    type: str = "entity_get_all_child_uuids"


class edit_mode_enter(BaseModel):
    """Enter edit mode"""

    target: UUID

    type: str = "edit_mode_enter"


class edit_mode_exit(BaseModel):
    """Exit edit mode"""

    type: str = "edit_mode_exit"


class select_with_point(BaseModel):
    """Modifies the selection by simulating a "mouse click" at the given x,y window coordinate Returns ID of whatever was selected."""

    selected_at_window: Point2d

    selection_type: SceneSelectionType

    type: str = "select_with_point"


class select_clear(BaseModel):
    """Clear the selection"""

    type: str = "select_clear"


class select_add(BaseModel):
    """Adds one or more entities (by UUID) to the selection."""

    entities: List[UUID]

    type: str = "select_add"


class select_remove(BaseModel):
    """Removes one or more entities (by UUID) from the selection."""

    entities: List[UUID]

    type: str = "select_remove"


class select_replace(BaseModel):
    """Replaces the current selection with these new entities (by UUID). Equivalent to doing SelectClear then SelectAdd."""

    entities: List[UUID]

    type: str = "select_replace"


class select_get(BaseModel):
    """Find all IDs of selected entities"""

    type: str = "select_get"


class highlight_set_entity(BaseModel):
    """Changes the current highlighted entity to whichever one is at the given window coordinate. If there's no entity at this location, clears the highlight."""

    selected_at_window: Point2d

    sequence: Optional[int] = None

    type: str = "highlight_set_entity"


class highlight_set_entities(BaseModel):
    """Changes the current highlighted entity to these entities."""

    entities: List[UUID]

    type: str = "highlight_set_entities"


class new_annotation(BaseModel):
    """Create a new annotation"""

    annotation_type: AnnotationType

    clobber: bool

    options: AnnotationOptions

    type: str = "new_annotation"


class update_annotation(BaseModel):
    """Update an annotation"""

    annotation_id: UUID

    options: AnnotationOptions

    type: str = "update_annotation"


class object_visible(BaseModel):
    """Hide or show an object"""

    hidden: bool

    object_id: UUID

    type: str = "object_visible"


class object_bring_to_front(BaseModel):
    """Bring an object to the front of the scene"""

    object_id: UUID

    type: str = "object_bring_to_front"


class get_entity_type(BaseModel):
    """What type of entity is this?"""

    entity_id: UUID

    type: str = "get_entity_type"


class solid2d_add_hole(BaseModel):
    """Add a hole to a Solid2d object before extruding it."""

    hole_id: UUID

    object_id: UUID

    type: str = "solid2d_add_hole"


class solid3d_get_all_edge_faces(BaseModel):
    """Gets all faces which use the given edge."""

    edge_id: UUID

    object_id: UUID

    type: str = "solid3d_get_all_edge_faces"


class solid3d_get_all_opposite_edges(BaseModel):
    """Gets all edges which are opposite the given edge, across all possible faces."""

    along_vector: Optional[Point3d] = None

    edge_id: UUID

    object_id: UUID

    type: str = "solid3d_get_all_opposite_edges"


class solid3d_get_opposite_edge(BaseModel):
    """Gets the edge opposite the given edge, along the given face."""

    edge_id: UUID

    face_id: UUID

    object_id: UUID

    type: str = "solid3d_get_opposite_edge"


class solid3d_get_next_adjacent_edge(BaseModel):
    """Gets the next adjacent edge for the given edge, along the given face."""

    edge_id: UUID

    face_id: UUID

    object_id: UUID

    type: str = "solid3d_get_next_adjacent_edge"


class solid3d_get_prev_adjacent_edge(BaseModel):
    """Gets the previous adjacent edge for the given edge, along the given face."""

    edge_id: UUID

    face_id: UUID

    object_id: UUID

    type: str = "solid3d_get_prev_adjacent_edge"


class send_object(BaseModel):
    """Sends object to front or back."""

    front: bool

    object_id: UUID

    type: str = "send_object"


class entity_set_opacity(BaseModel):
    """Set opacity of the entity."""

    entity_id: UUID

    opacity: float

    type: str = "entity_set_opacity"


class entity_fade(BaseModel):
    """Fade the entity in or out."""

    duration_seconds: Optional[float] = None

    entity_id: UUID

    fade_in: bool

    type: str = "entity_fade"


class make_plane(BaseModel):
    """Make a plane."""

    clobber: bool

    hide: Optional[bool] = None

    origin: Point3d

    size: float

    type: str = "make_plane"

    x_axis: Point3d

    y_axis: Point3d


class plane_set_color(BaseModel):
    """Set the plane's color."""

    color: Color

    plane_id: UUID

    type: str = "plane_set_color"


class set_tool(BaseModel):
    """Set the active tool."""

    tool: SceneToolType

    type: str = "set_tool"


class mouse_move(BaseModel):
    """Send a mouse move event."""

    sequence: Optional[int] = None

    type: str = "mouse_move"

    window: Point2d


class mouse_click(BaseModel):
    """Send a mouse click event. Updates modified/selected entities."""

    type: str = "mouse_click"

    window: Point2d


class sketch_mode_enable(BaseModel):
    """Enable sketch mode on the given plane."""

    animated: bool

    disable_camera_with_plane: Optional[Point3d] = None

    ortho: bool

    plane_id: UUID

    type: str = "sketch_mode_enable"


class sketch_mode_disable(BaseModel):
    """Disable sketch mode."""

    type: str = "sketch_mode_disable"


class curve_get_type(BaseModel):
    """Get type of a given curve."""

    curve_id: UUID

    type: str = "curve_get_type"


class curve_get_control_points(BaseModel):
    """Get control points of a given curve."""

    curve_id: UUID

    type: str = "curve_get_control_points"


class take_snapshot(BaseModel):
    """Take a snapshot."""

    format: ImageFormat

    type: str = "take_snapshot"


class make_axes_gizmo(BaseModel):
    """Add a gizmo showing the axes."""

    clobber: bool

    gizmo_mode: bool

    type: str = "make_axes_gizmo"


class path_get_info(BaseModel):
    """Query the given path"""

    path_id: UUID

    type: str = "path_get_info"


class path_get_curve_uuids_for_vertices(BaseModel):
    """Get curves for vertices within a path"""

    path_id: UUID

    type: str = "path_get_curve_uuids_for_vertices"

    vertex_ids: List[UUID]


class path_get_vertex_uuids(BaseModel):
    """Get vertices within a path"""

    path_id: UUID

    type: str = "path_get_vertex_uuids"


class handle_mouse_drag_start(BaseModel):
    """Start dragging mouse."""

    type: str = "handle_mouse_drag_start"

    window: Point2d


class handle_mouse_drag_move(BaseModel):
    """Continue dragging mouse."""

    sequence: Optional[int] = None

    type: str = "handle_mouse_drag_move"

    window: Point2d


class handle_mouse_drag_end(BaseModel):
    """Stop dragging mouse."""

    type: str = "handle_mouse_drag_end"

    window: Point2d


class remove_scene_objects(BaseModel):
    """Remove scene objects."""

    object_ids: List[UUID]

    type: str = "remove_scene_objects"


class plane_intersect_and_project(BaseModel):
    """Utility method. Performs both a ray cast and projection to plane-local coordinates. Returns the plane coordinates for the given window coordinates."""

    plane_id: UUID

    type: str = "plane_intersect_and_project"

    window: Point2d


class curve_get_end_points(BaseModel):
    """Find the start and end of a curve."""

    curve_id: UUID

    type: str = "curve_get_end_points"


class reconfigure_stream(BaseModel):
    """Reconfigure the stream."""

    fps: int

    height: int

    type: str = "reconfigure_stream"

    width: int


class import_files(BaseModel):
    """Import files to the current model."""

    files: List[ImportFile]

    format: InputFormat

    type: str = "import_files"


class mass(BaseModel):
    """Get the mass of entities in the scene or the default scene."""

    entity_ids: List[UUID]

    material_density: float

    material_density_unit: UnitDensity

    output_unit: UnitMass

    source_unit: UnitLength

    type: str = "mass"


class density(BaseModel):
    """Get the density of entities in the scene or the default scene."""

    entity_ids: List[UUID]

    material_mass: float

    material_mass_unit: UnitMass

    output_unit: UnitDensity

    source_unit: UnitLength

    type: str = "density"


class volume(BaseModel):
    """Get the volume of entities in the scene or the default scene."""

    entity_ids: List[UUID]

    output_unit: UnitVolume

    source_unit: UnitLength

    type: str = "volume"


class center_of_mass(BaseModel):
    """Get the center of mass of entities in the scene or the default scene."""

    entity_ids: List[UUID]

    output_unit: UnitLength

    source_unit: UnitLength

    type: str = "center_of_mass"


class surface_area(BaseModel):
    """Get the surface area of entities in the scene or the default scene."""

    entity_ids: List[UUID]

    output_unit: UnitArea

    source_unit: UnitLength

    type: str = "surface_area"


class get_sketch_mode_plane(BaseModel):
    """Get the plane of the sketch mode. This is useful for getting the normal of the plane after a user selects a plane."""

    type: str = "get_sketch_mode_plane"


class curve_set_constraint(BaseModel):
    """Constrain a curve."""

    constraint_bound: PathComponentConstraintBound

    constraint_type: PathComponentConstraintType

    object_id: UUID

    type: str = "curve_set_constraint"


GY = TypeVar("GY", bound="ModelingCmd")


@attr.s(auto_attribs=True)
class ModelingCmd:

    """Commands that the KittyCAD engine can execute."""

    type: Union[
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
    ]

    def __init__(
        self,
        type: Union[
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
        ],
    ):
        self.type = type

    def model_dump(self) -> Dict[str, Any]:
        if isinstance(self.type, start_path):
            ON: start_path = self.type
            return ON.model_dump()
        elif isinstance(self.type, move_path_pen):
            US: move_path_pen = self.type
            return US.model_dump()
        elif isinstance(self.type, extend_path):
            FH: extend_path = self.type
            return FH.model_dump()
        elif isinstance(self.type, extrude):
            BB: extrude = self.type
            return BB.model_dump()
        elif isinstance(self.type, close_path):
            TV: close_path = self.type
            return TV.model_dump()
        elif isinstance(self.type, camera_drag_start):
            CE: camera_drag_start = self.type
            return CE.model_dump()
        elif isinstance(self.type, camera_drag_move):
            LT: camera_drag_move = self.type
            return LT.model_dump()
        elif isinstance(self.type, camera_drag_end):
            YY: camera_drag_end = self.type
            return YY.model_dump()
        elif isinstance(self.type, default_camera_look_at):
            FZ: default_camera_look_at = self.type
            return FZ.model_dump()
        elif isinstance(self.type, default_camera_zoom):
            NN: default_camera_zoom = self.type
            return NN.model_dump()
        elif isinstance(self.type, default_camera_enable_sketch_mode):
            VI: default_camera_enable_sketch_mode = self.type
            return VI.model_dump()
        elif isinstance(self.type, default_camera_disable_sketch_mode):
            QF: default_camera_disable_sketch_mode = self.type
            return QF.model_dump()
        elif isinstance(self.type, default_camera_focus_on):
            OJ: default_camera_focus_on = self.type
            return OJ.model_dump()
        elif isinstance(self.type, export):
            YF: export = self.type
            return YF.model_dump()
        elif isinstance(self.type, entity_get_parent_id):
            LK: entity_get_parent_id = self.type
            return LK.model_dump()
        elif isinstance(self.type, entity_get_num_children):
            WB: entity_get_num_children = self.type
            return WB.model_dump()
        elif isinstance(self.type, entity_get_child_uuid):
            HC: entity_get_child_uuid = self.type
            return HC.model_dump()
        elif isinstance(self.type, entity_get_all_child_uuids):
            PV: entity_get_all_child_uuids = self.type
            return PV.model_dump()
        elif isinstance(self.type, edit_mode_enter):
            TP: edit_mode_enter = self.type
            return TP.model_dump()
        elif isinstance(self.type, edit_mode_exit):
            OM: edit_mode_exit = self.type
            return OM.model_dump()
        elif isinstance(self.type, select_with_point):
            RS: select_with_point = self.type
            return RS.model_dump()
        elif isinstance(self.type, select_clear):
            MP: select_clear = self.type
            return MP.model_dump()
        elif isinstance(self.type, select_add):
            RO: select_add = self.type
            return RO.model_dump()
        elif isinstance(self.type, select_remove):
            BA: select_remove = self.type
            return BA.model_dump()
        elif isinstance(self.type, select_replace):
            CB: select_replace = self.type
            return CB.model_dump()
        elif isinstance(self.type, select_get):
            TO: select_get = self.type
            return TO.model_dump()
        elif isinstance(self.type, highlight_set_entity):
            EO: highlight_set_entity = self.type
            return EO.model_dump()
        elif isinstance(self.type, highlight_set_entities):
            QO: highlight_set_entities = self.type
            return QO.model_dump()
        elif isinstance(self.type, new_annotation):
            IZ: new_annotation = self.type
            return IZ.model_dump()
        elif isinstance(self.type, update_annotation):
            NK: update_annotation = self.type
            return NK.model_dump()
        elif isinstance(self.type, object_visible):
            QE: object_visible = self.type
            return QE.model_dump()
        elif isinstance(self.type, object_bring_to_front):
            KT: object_bring_to_front = self.type
            return KT.model_dump()
        elif isinstance(self.type, get_entity_type):
            GU: get_entity_type = self.type
            return GU.model_dump()
        elif isinstance(self.type, solid2d_add_hole):
            UP: solid2d_add_hole = self.type
            return UP.model_dump()
        elif isinstance(self.type, solid3d_get_all_edge_faces):
            DJ: solid3d_get_all_edge_faces = self.type
            return DJ.model_dump()
        elif isinstance(self.type, solid3d_get_all_opposite_edges):
            TR: solid3d_get_all_opposite_edges = self.type
            return TR.model_dump()
        elif isinstance(self.type, solid3d_get_opposite_edge):
            JF: solid3d_get_opposite_edge = self.type
            return JF.model_dump()
        elif isinstance(self.type, solid3d_get_next_adjacent_edge):
            EL: solid3d_get_next_adjacent_edge = self.type
            return EL.model_dump()
        elif isinstance(self.type, solid3d_get_prev_adjacent_edge):
            LF: solid3d_get_prev_adjacent_edge = self.type
            return LF.model_dump()
        elif isinstance(self.type, send_object):
            GN: send_object = self.type
            return GN.model_dump()
        elif isinstance(self.type, entity_set_opacity):
            VJ: entity_set_opacity = self.type
            return VJ.model_dump()
        elif isinstance(self.type, entity_fade):
            YW: entity_fade = self.type
            return YW.model_dump()
        elif isinstance(self.type, make_plane):
            NO: make_plane = self.type
            return NO.model_dump()
        elif isinstance(self.type, plane_set_color):
            RG: plane_set_color = self.type
            return RG.model_dump()
        elif isinstance(self.type, set_tool):
            LD: set_tool = self.type
            return LD.model_dump()
        elif isinstance(self.type, mouse_move):
            TN: mouse_move = self.type
            return TN.model_dump()
        elif isinstance(self.type, mouse_click):
            UG: mouse_click = self.type
            return UG.model_dump()
        elif isinstance(self.type, sketch_mode_enable):
            NZ: sketch_mode_enable = self.type
            return NZ.model_dump()
        elif isinstance(self.type, sketch_mode_disable):
            LO: sketch_mode_disable = self.type
            return LO.model_dump()
        elif isinstance(self.type, curve_get_type):
            OW: curve_get_type = self.type
            return OW.model_dump()
        elif isinstance(self.type, curve_get_control_points):
            PQ: curve_get_control_points = self.type
            return PQ.model_dump()
        elif isinstance(self.type, take_snapshot):
            OU: take_snapshot = self.type
            return OU.model_dump()
        elif isinstance(self.type, make_axes_gizmo):
            XI: make_axes_gizmo = self.type
            return XI.model_dump()
        elif isinstance(self.type, path_get_info):
            PS: path_get_info = self.type
            return PS.model_dump()
        elif isinstance(self.type, path_get_curve_uuids_for_vertices):
            XL: path_get_curve_uuids_for_vertices = self.type
            return XL.model_dump()
        elif isinstance(self.type, path_get_vertex_uuids):
            FT: path_get_vertex_uuids = self.type
            return FT.model_dump()
        elif isinstance(self.type, handle_mouse_drag_start):
            SC: handle_mouse_drag_start = self.type
            return SC.model_dump()
        elif isinstance(self.type, handle_mouse_drag_move):
            JA: handle_mouse_drag_move = self.type
            return JA.model_dump()
        elif isinstance(self.type, handle_mouse_drag_end):
            UK: handle_mouse_drag_end = self.type
            return UK.model_dump()
        elif isinstance(self.type, remove_scene_objects):
            MT: remove_scene_objects = self.type
            return MT.model_dump()
        elif isinstance(self.type, plane_intersect_and_project):
            TF: plane_intersect_and_project = self.type
            return TF.model_dump()
        elif isinstance(self.type, curve_get_end_points):
            JD: curve_get_end_points = self.type
            return JD.model_dump()
        elif isinstance(self.type, reconfigure_stream):
            BH: reconfigure_stream = self.type
            return BH.model_dump()
        elif isinstance(self.type, import_files):
            CN: import_files = self.type
            return CN.model_dump()
        elif isinstance(self.type, mass):
            SO: mass = self.type
            return SO.model_dump()
        elif isinstance(self.type, density):
            AM: density = self.type
            return AM.model_dump()
        elif isinstance(self.type, volume):
            SG: volume = self.type
            return SG.model_dump()
        elif isinstance(self.type, center_of_mass):
            SY: center_of_mass = self.type
            return SY.model_dump()
        elif isinstance(self.type, surface_area):
            WS: surface_area = self.type
            return WS.model_dump()
        elif isinstance(self.type, get_sketch_mode_plane):
            MK: get_sketch_mode_plane = self.type
            return MK.model_dump()
        elif isinstance(self.type, curve_set_constraint):
            FY: curve_set_constraint = self.type
            return FY.model_dump()

        raise Exception("Unknown type")

    @classmethod
    def from_dict(cls: Type[GY], d: Dict[str, Any]) -> GY:
        if d.get("type") == "start_path":
            PC: start_path = start_path(**d)
            return cls(type=PC)
        elif d.get("type") == "move_path_pen":
            KQ: move_path_pen = move_path_pen(**d)
            return cls(type=KQ)
        elif d.get("type") == "extend_path":
            NH: extend_path = extend_path(**d)
            return cls(type=NH)
        elif d.get("type") == "extrude":
            PJ: extrude = extrude(**d)
            return cls(type=PJ)
        elif d.get("type") == "close_path":
            CR: close_path = close_path(**d)
            return cls(type=CR)
        elif d.get("type") == "camera_drag_start":
            MS: camera_drag_start = camera_drag_start(**d)
            return cls(type=MS)
        elif d.get("type") == "camera_drag_move":
            ED: camera_drag_move = camera_drag_move(**d)
            return cls(type=ED)
        elif d.get("type") == "camera_drag_end":
            DO: camera_drag_end = camera_drag_end(**d)
            return cls(type=DO)
        elif d.get("type") == "default_camera_look_at":
            GL: default_camera_look_at = default_camera_look_at(**d)
            return cls(type=GL)
        elif d.get("type") == "default_camera_zoom":
            OH: default_camera_zoom = default_camera_zoom(**d)
            return cls(type=OH)
        elif d.get("type") == "default_camera_enable_sketch_mode":
            ET: default_camera_enable_sketch_mode = default_camera_enable_sketch_mode(
                **d
            )
            return cls(type=ET)
        elif d.get("type") == "default_camera_disable_sketch_mode":
            DI: default_camera_disable_sketch_mode = default_camera_disable_sketch_mode(
                **d
            )
            return cls(type=DI)
        elif d.get("type") == "default_camera_focus_on":
            UF: default_camera_focus_on = default_camera_focus_on(**d)
            return cls(type=UF)
        elif d.get("type") == "export":
            PY: export = export(**d)
            return cls(type=PY)
        elif d.get("type") == "entity_get_parent_id":
            AR: entity_get_parent_id = entity_get_parent_id(**d)
            return cls(type=AR)
        elif d.get("type") == "entity_get_num_children":
            KK: entity_get_num_children = entity_get_num_children(**d)
            return cls(type=KK)
        elif d.get("type") == "entity_get_child_uuid":
            FM: entity_get_child_uuid = entity_get_child_uuid(**d)
            return cls(type=FM)
        elif d.get("type") == "entity_get_all_child_uuids":
            QI: entity_get_all_child_uuids = entity_get_all_child_uuids(**d)
            return cls(type=QI)
        elif d.get("type") == "edit_mode_enter":
            CF: edit_mode_enter = edit_mode_enter(**d)
            return cls(type=CF)
        elif d.get("type") == "edit_mode_exit":
            EN: edit_mode_exit = edit_mode_exit(**d)
            return cls(type=EN)
        elif d.get("type") == "select_with_point":
            LR: select_with_point = select_with_point(**d)
            return cls(type=LR)
        elif d.get("type") == "select_clear":
            WF: select_clear = select_clear(**d)
            return cls(type=WF)
        elif d.get("type") == "select_add":
            DN: select_add = select_add(**d)
            return cls(type=DN)
        elif d.get("type") == "select_remove":
            OR: select_remove = select_remove(**d)
            return cls(type=OR)
        elif d.get("type") == "select_replace":
            LC: select_replace = select_replace(**d)
            return cls(type=LC)
        elif d.get("type") == "select_get":
            ZP: select_get = select_get(**d)
            return cls(type=ZP)
        elif d.get("type") == "highlight_set_entity":
            NY: highlight_set_entity = highlight_set_entity(**d)
            return cls(type=NY)
        elif d.get("type") == "highlight_set_entities":
            KX: highlight_set_entities = highlight_set_entities(**d)
            return cls(type=KX)
        elif d.get("type") == "new_annotation":
            WO: new_annotation = new_annotation(**d)
            return cls(type=WO)
        elif d.get("type") == "update_annotation":
            UQ: update_annotation = update_annotation(**d)
            return cls(type=UQ)
        elif d.get("type") == "object_visible":
            XH: object_visible = object_visible(**d)
            return cls(type=XH)
        elif d.get("type") == "object_bring_to_front":
            BV: object_bring_to_front = object_bring_to_front(**d)
            return cls(type=BV)
        elif d.get("type") == "get_entity_type":
            SS: get_entity_type = get_entity_type(**d)
            return cls(type=SS)
        elif d.get("type") == "solid2d_add_hole":
            AZ: solid2d_add_hole = solid2d_add_hole(**d)
            return cls(type=AZ)
        elif d.get("type") == "solid3d_get_all_edge_faces":
            WJ: solid3d_get_all_edge_faces = solid3d_get_all_edge_faces(**d)
            return cls(type=WJ)
        elif d.get("type") == "solid3d_get_all_opposite_edges":
            YD: solid3d_get_all_opposite_edges = solid3d_get_all_opposite_edges(**d)
            return cls(type=YD)
        elif d.get("type") == "solid3d_get_opposite_edge":
            VP: solid3d_get_opposite_edge = solid3d_get_opposite_edge(**d)
            return cls(type=VP)
        elif d.get("type") == "solid3d_get_next_adjacent_edge":
            ZG: solid3d_get_next_adjacent_edge = solid3d_get_next_adjacent_edge(**d)
            return cls(type=ZG)
        elif d.get("type") == "solid3d_get_prev_adjacent_edge":
            CS: solid3d_get_prev_adjacent_edge = solid3d_get_prev_adjacent_edge(**d)
            return cls(type=CS)
        elif d.get("type") == "send_object":
            GD: send_object = send_object(**d)
            return cls(type=GD)
        elif d.get("type") == "entity_set_opacity":
            OX: entity_set_opacity = entity_set_opacity(**d)
            return cls(type=OX)
        elif d.get("type") == "entity_fade":
            QX: entity_fade = entity_fade(**d)
            return cls(type=QX)
        elif d.get("type") == "make_plane":
            VX: make_plane = make_plane(**d)
            return cls(type=VX)
        elif d.get("type") == "plane_set_color":
            IT: plane_set_color = plane_set_color(**d)
            return cls(type=IT)
        elif d.get("type") == "set_tool":
            UA: set_tool = set_tool(**d)
            return cls(type=UA)
        elif d.get("type") == "mouse_move":
            MZ: mouse_move = mouse_move(**d)
            return cls(type=MZ)
        elif d.get("type") == "mouse_click":
            CY: mouse_click = mouse_click(**d)
            return cls(type=CY)
        elif d.get("type") == "sketch_mode_enable":
            LI: sketch_mode_enable = sketch_mode_enable(**d)
            return cls(type=LI)
        elif d.get("type") == "sketch_mode_disable":
            XJ: sketch_mode_disable = sketch_mode_disable(**d)
            return cls(type=XJ)
        elif d.get("type") == "curve_get_type":
            JQ: curve_get_type = curve_get_type(**d)
            return cls(type=JQ)
        elif d.get("type") == "curve_get_control_points":
            IM: curve_get_control_points = curve_get_control_points(**d)
            return cls(type=IM)
        elif d.get("type") == "take_snapshot":
            KL: take_snapshot = take_snapshot(**d)
            return cls(type=KL)
        elif d.get("type") == "make_axes_gizmo":
            PO: make_axes_gizmo = make_axes_gizmo(**d)
            return cls(type=PO)
        elif d.get("type") == "path_get_info":
            WR: path_get_info = path_get_info(**d)
            return cls(type=WR)
        elif d.get("type") == "path_get_curve_uuids_for_vertices":
            ZX: path_get_curve_uuids_for_vertices = path_get_curve_uuids_for_vertices(
                **d
            )
            return cls(type=ZX)
        elif d.get("type") == "path_get_vertex_uuids":
            NX: path_get_vertex_uuids = path_get_vertex_uuids(**d)
            return cls(type=NX)
        elif d.get("type") == "handle_mouse_drag_start":
            TX: handle_mouse_drag_start = handle_mouse_drag_start(**d)
            return cls(type=TX)
        elif d.get("type") == "handle_mouse_drag_move":
            SK: handle_mouse_drag_move = handle_mouse_drag_move(**d)
            return cls(type=SK)
        elif d.get("type") == "handle_mouse_drag_end":
            CX: handle_mouse_drag_end = handle_mouse_drag_end(**d)
            return cls(type=CX)
        elif d.get("type") == "remove_scene_objects":
            LJ: remove_scene_objects = remove_scene_objects(**d)
            return cls(type=LJ)
        elif d.get("type") == "plane_intersect_and_project":
            HF: plane_intersect_and_project = plane_intersect_and_project(**d)
            return cls(type=HF)
        elif d.get("type") == "curve_get_end_points":
            RZ: curve_get_end_points = curve_get_end_points(**d)
            return cls(type=RZ)
        elif d.get("type") == "reconfigure_stream":
            SX: reconfigure_stream = reconfigure_stream(**d)
            return cls(type=SX)
        elif d.get("type") == "import_files":
            GS: import_files = import_files(**d)
            return cls(type=GS)
        elif d.get("type") == "mass":
            ZS: mass = mass(**d)
            return cls(type=ZS)
        elif d.get("type") == "density":
            GK: density = density(**d)
            return cls(type=GK)
        elif d.get("type") == "volume":
            QZ: volume = volume(**d)
            return cls(type=QZ)
        elif d.get("type") == "center_of_mass":
            YK: center_of_mass = center_of_mass(**d)
            return cls(type=YK)
        elif d.get("type") == "surface_area":
            SL: surface_area = surface_area(**d)
            return cls(type=SL)
        elif d.get("type") == "get_sketch_mode_plane":
            TU: get_sketch_mode_plane = get_sketch_mode_plane(**d)
            return cls(type=TU)
        elif d.get("type") == "curve_set_constraint":
            FD: curve_set_constraint = curve_set_constraint(**d)
            return cls(type=FD)

        raise Exception("Unknown type")

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls,
            handler(
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
                ]
            ),
        )
