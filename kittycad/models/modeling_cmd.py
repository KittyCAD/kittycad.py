from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.annotation_options import AnnotationOptions
from ..models.annotation_type import AnnotationType
from ..models.camera_drag_interaction_type import CameraDragInteractionType
from ..models.color import Color
from ..models.image_format import ImageFormat
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
from ..types import UNSET, Unset

LD = TypeVar("LD", bound="start_path")


@attr.s(auto_attribs=True)
class start_path:
    """Start a path."""  # noqa: E501

    type: str = "start_path"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[LD], src_dict: Dict[str, Any]) -> LD:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        start_path = cls(
            type=type,
        )

        start_path.additional_properties = d
        return start_path

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


UA = TypeVar("UA", bound="move_path_pen")


@attr.s(auto_attribs=True)
class move_path_pen:
    """Move the path's "pen"."""  # noqa: E501

    path: Union[Unset, ModelingCmdId] = UNSET
    to: Union[Unset, Point3d] = UNSET
    type: str = "move_path_pen"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.path, Unset):
            path = self.path
        if not isinstance(self.to, Unset):
            to = self.to
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if to is not UNSET:
            field_dict["to"] = to.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[UA], src_dict: Dict[str, Any]) -> UA:
        d = src_dict.copy()
        _path = d.pop("path", UNSET)
        path: Union[Unset, ModelingCmdId]
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = _path  # type: ignore[arg-type]

        _to = d.pop("to", UNSET)
        to: Union[Unset, Point3d]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = _to  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        move_path_pen = cls(
            path=path,
            to=to,
            type=type,
        )

        move_path_pen.additional_properties = d
        return move_path_pen

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


TN = TypeVar("TN", bound="extend_path")


@attr.s(auto_attribs=True)
class extend_path:
    """Extend a path by adding a new segment which starts at the path's "pen". If no "pen" location has been set before (via `MovePen`), then the pen is at the origin."""  # noqa: E501

    path: Union[Unset, ModelingCmdId] = UNSET
    segment: Union[Unset, PathSegment] = UNSET
    type: str = "extend_path"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.path, Unset):
            path = self.path
        if not isinstance(self.segment, Unset):
            segment = self.segment
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if segment is not UNSET:
            field_dict["segment"] = segment.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[TN], src_dict: Dict[str, Any]) -> TN:
        d = src_dict.copy()
        _path = d.pop("path", UNSET)
        path: Union[Unset, ModelingCmdId]
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = _path  # type: ignore[arg-type]

        _segment = d.pop("segment", UNSET)
        segment: Union[Unset, PathSegment]
        if isinstance(_segment, Unset):
            segment = UNSET
        else:
            segment = _segment  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        extend_path = cls(
            path=path,
            segment=segment,
            type=type,
        )

        extend_path.additional_properties = d
        return extend_path

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


MZ = TypeVar("MZ", bound="extrude")


@attr.s(auto_attribs=True)
class extrude:
    """Extrude a 2D solid."""  # noqa: E501

    cap: Union[Unset, bool] = False
    distance: Union[Unset, float] = UNSET
    target: Union[Unset, ModelingCmdId] = UNSET
    type: str = "extrude"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cap = self.cap
        distance = self.distance
        if not isinstance(self.target, Unset):
            target = self.target
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cap is not UNSET:
            field_dict["cap"] = cap
        if distance is not UNSET:
            field_dict["distance"] = distance
        if target is not UNSET:
            field_dict["target"] = target
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[MZ], src_dict: Dict[str, Any]) -> MZ:
        d = src_dict.copy()
        cap = d.pop("cap", UNSET)

        distance = d.pop("distance", UNSET)

        _target = d.pop("target", UNSET)
        target: Union[Unset, ModelingCmdId]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = _target  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        extrude = cls(
            cap=cap,
            distance=distance,
            target=target,
            type=type,
        )

        extrude.additional_properties = d
        return extrude

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


UG = TypeVar("UG", bound="close_path")


@attr.s(auto_attribs=True)
class close_path:
    """Closes a path, converting it to a 2D solid."""  # noqa: E501

    path_id: Union[Unset, str] = UNSET
    type: str = "close_path"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path_id = self.path_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path_id is not UNSET:
            field_dict["path_id"] = path_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[UG], src_dict: Dict[str, Any]) -> UG:
        d = src_dict.copy()
        path_id = d.pop("path_id", UNSET)

        type = d.pop("type", UNSET)

        close_path = cls(
            path_id=path_id,
            type=type,
        )

        close_path.additional_properties = d
        return close_path

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


CY = TypeVar("CY", bound="camera_drag_start")


@attr.s(auto_attribs=True)
class camera_drag_start:
    """Camera drag started."""  # noqa: E501

    interaction: Union[Unset, CameraDragInteractionType] = UNSET
    type: str = "camera_drag_start"
    window: Union[Unset, Point2d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.interaction, Unset):
            interaction = self.interaction
        type = self.type
        if not isinstance(self.window, Unset):
            window = self.window

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interaction is not UNSET:
            field_dict["interaction"] = interaction
        field_dict["type"] = type
        if window is not UNSET:
            field_dict["window"] = window.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[CY], src_dict: Dict[str, Any]) -> CY:
        d = src_dict.copy()
        _interaction = d.pop("interaction", UNSET)
        interaction: Union[Unset, CameraDragInteractionType]
        if isinstance(_interaction, Unset):
            interaction = UNSET
        else:
            interaction = _interaction  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        _window = d.pop("window", UNSET)
        window: Union[Unset, Point2d]
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = _window  # type: ignore[arg-type]

        camera_drag_start = cls(
            interaction=interaction,
            type=type,
            window=window,
        )

        camera_drag_start.additional_properties = d
        return camera_drag_start

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


NZ = TypeVar("NZ", bound="camera_drag_move")


@attr.s(auto_attribs=True)
class camera_drag_move:
    """Camera drag continued."""  # noqa: E501

    interaction: Union[Unset, CameraDragInteractionType] = UNSET
    sequence: Union[Unset, int] = UNSET
    type: str = "camera_drag_move"
    window: Union[Unset, Point2d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.interaction, Unset):
            interaction = self.interaction
        sequence = self.sequence
        type = self.type
        if not isinstance(self.window, Unset):
            window = self.window

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interaction is not UNSET:
            field_dict["interaction"] = interaction
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        field_dict["type"] = type
        if window is not UNSET:
            field_dict["window"] = window.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[NZ], src_dict: Dict[str, Any]) -> NZ:
        d = src_dict.copy()
        _interaction = d.pop("interaction", UNSET)
        interaction: Union[Unset, CameraDragInteractionType]
        if isinstance(_interaction, Unset):
            interaction = UNSET
        else:
            interaction = _interaction  # type: ignore[arg-type]

        sequence = d.pop("sequence", UNSET)

        type = d.pop("type", UNSET)

        _window = d.pop("window", UNSET)
        window: Union[Unset, Point2d]
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = _window  # type: ignore[arg-type]

        camera_drag_move = cls(
            interaction=interaction,
            sequence=sequence,
            type=type,
            window=window,
        )

        camera_drag_move.additional_properties = d
        return camera_drag_move

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


LI = TypeVar("LI", bound="camera_drag_end")


@attr.s(auto_attribs=True)
class camera_drag_end:
    """Camera drag ended."""  # noqa: E501

    interaction: Union[Unset, CameraDragInteractionType] = UNSET
    type: str = "camera_drag_end"
    window: Union[Unset, Point2d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.interaction, Unset):
            interaction = self.interaction
        type = self.type
        if not isinstance(self.window, Unset):
            window = self.window

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interaction is not UNSET:
            field_dict["interaction"] = interaction
        field_dict["type"] = type
        if window is not UNSET:
            field_dict["window"] = window.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[LI], src_dict: Dict[str, Any]) -> LI:
        d = src_dict.copy()
        _interaction = d.pop("interaction", UNSET)
        interaction: Union[Unset, CameraDragInteractionType]
        if isinstance(_interaction, Unset):
            interaction = UNSET
        else:
            interaction = _interaction  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        _window = d.pop("window", UNSET)
        window: Union[Unset, Point2d]
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = _window  # type: ignore[arg-type]

        camera_drag_end = cls(
            interaction=interaction,
            type=type,
            window=window,
        )

        camera_drag_end.additional_properties = d
        return camera_drag_end

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


LO = TypeVar("LO", bound="default_camera_look_at")


@attr.s(auto_attribs=True)
class default_camera_look_at:
    """Change what the default camera is looking at."""  # noqa: E501

    center: Union[Unset, Point3d] = UNSET
    type: str = "default_camera_look_at"
    up: Union[Unset, Point3d] = UNSET
    vantage: Union[Unset, Point3d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.center, Unset):
            center = self.center
        type = self.type
        if not isinstance(self.up, Unset):
            up = self.up
        if not isinstance(self.vantage, Unset):
            vantage = self.vantage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if center is not UNSET:
            field_dict["center"] = center.to_dict()
        field_dict["type"] = type
        if up is not UNSET:
            field_dict["up"] = up.to_dict()
        if vantage is not UNSET:
            field_dict["vantage"] = vantage.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[LO], src_dict: Dict[str, Any]) -> LO:
        d = src_dict.copy()
        _center = d.pop("center", UNSET)
        center: Union[Unset, Point3d]
        if isinstance(_center, Unset):
            center = UNSET
        else:
            center = _center  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        _up = d.pop("up", UNSET)
        up: Union[Unset, Point3d]
        if isinstance(_up, Unset):
            up = UNSET
        else:
            up = _up  # type: ignore[arg-type]

        _vantage = d.pop("vantage", UNSET)
        vantage: Union[Unset, Point3d]
        if isinstance(_vantage, Unset):
            vantage = UNSET
        else:
            vantage = _vantage  # type: ignore[arg-type]

        default_camera_look_at = cls(
            center=center,
            type=type,
            up=up,
            vantage=vantage,
        )

        default_camera_look_at.additional_properties = d
        return default_camera_look_at

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


XJ = TypeVar("XJ", bound="default_camera_zoom")


@attr.s(auto_attribs=True)
class default_camera_zoom:
    """Adjust zoom of the default camera."""  # noqa: E501

    magnitude: Union[Unset, float] = UNSET
    type: str = "default_camera_zoom"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        magnitude = self.magnitude
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if magnitude is not UNSET:
            field_dict["magnitude"] = magnitude
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[XJ], src_dict: Dict[str, Any]) -> XJ:
        d = src_dict.copy()
        magnitude = d.pop("magnitude", UNSET)

        type = d.pop("type", UNSET)

        default_camera_zoom = cls(
            magnitude=magnitude,
            type=type,
        )

        default_camera_zoom.additional_properties = d
        return default_camera_zoom

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


OW = TypeVar("OW", bound="default_camera_enable_sketch_mode")


@attr.s(auto_attribs=True)
class default_camera_enable_sketch_mode:
    """Enable sketch mode, where users can sketch 2D geometry. Users choose a plane to sketch on."""  # noqa: E501

    animated: Union[Unset, bool] = False
    distance_to_plane: Union[Unset, float] = UNSET
    origin: Union[Unset, Point3d] = UNSET
    ortho: Union[Unset, bool] = False
    type: str = "default_camera_enable_sketch_mode"
    x_axis: Union[Unset, Point3d] = UNSET
    y_axis: Union[Unset, Point3d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        animated = self.animated
        distance_to_plane = self.distance_to_plane
        if not isinstance(self.origin, Unset):
            origin = self.origin
        ortho = self.ortho
        type = self.type
        if not isinstance(self.x_axis, Unset):
            x_axis = self.x_axis
        if not isinstance(self.y_axis, Unset):
            y_axis = self.y_axis

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if animated is not UNSET:
            field_dict["animated"] = animated
        if distance_to_plane is not UNSET:
            field_dict["distance_to_plane"] = distance_to_plane
        if origin is not UNSET:
            field_dict["origin"] = origin.to_dict()
        if ortho is not UNSET:
            field_dict["ortho"] = ortho
        field_dict["type"] = type
        if x_axis is not UNSET:
            field_dict["x_axis"] = x_axis.to_dict()
        if y_axis is not UNSET:
            field_dict["y_axis"] = y_axis.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[OW], src_dict: Dict[str, Any]) -> OW:
        d = src_dict.copy()
        animated = d.pop("animated", UNSET)

        distance_to_plane = d.pop("distance_to_plane", UNSET)

        _origin = d.pop("origin", UNSET)
        origin: Union[Unset, Point3d]
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = _origin  # type: ignore[arg-type]

        ortho = d.pop("ortho", UNSET)

        type = d.pop("type", UNSET)

        _x_axis = d.pop("x_axis", UNSET)
        x_axis: Union[Unset, Point3d]
        if isinstance(_x_axis, Unset):
            x_axis = UNSET
        else:
            x_axis = _x_axis  # type: ignore[arg-type]

        _y_axis = d.pop("y_axis", UNSET)
        y_axis: Union[Unset, Point3d]
        if isinstance(_y_axis, Unset):
            y_axis = UNSET
        else:
            y_axis = _y_axis  # type: ignore[arg-type]

        default_camera_enable_sketch_mode = cls(
            animated=animated,
            distance_to_plane=distance_to_plane,
            origin=origin,
            ortho=ortho,
            type=type,
            x_axis=x_axis,
            y_axis=y_axis,
        )

        default_camera_enable_sketch_mode.additional_properties = d
        return default_camera_enable_sketch_mode

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


JQ = TypeVar("JQ", bound="default_camera_disable_sketch_mode")


@attr.s(auto_attribs=True)
class default_camera_disable_sketch_mode:
    """Disable sketch mode, from the default camera."""  # noqa: E501

    type: str = "default_camera_disable_sketch_mode"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[JQ], src_dict: Dict[str, Any]) -> JQ:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        default_camera_disable_sketch_mode = cls(
            type=type,
        )

        default_camera_disable_sketch_mode.additional_properties = d
        return default_camera_disable_sketch_mode

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


PQ = TypeVar("PQ", bound="default_camera_focus_on")


@attr.s(auto_attribs=True)
class default_camera_focus_on:
    """Focus default camera on object."""  # noqa: E501

    type: str = "default_camera_focus_on"
    uuid: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        uuid = self.uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        field_dict["type"] = type
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[PQ], src_dict: Dict[str, Any]) -> PQ:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        uuid = d.pop("uuid", UNSET)

        default_camera_focus_on = cls(
            type=type,
            uuid=uuid,
        )

        default_camera_focus_on.additional_properties = d
        return default_camera_focus_on

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


IM = TypeVar("IM", bound="export")


@attr.s(auto_attribs=True)
class export:
    """Export the scene to a file."""  # noqa: E501

    entity_ids: Union[Unset, List[str]] = UNSET
    format: Union[Unset, OutputFormat] = UNSET
    source_unit: Union[Unset, UnitLength] = UNSET
    type: str = "export"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.entity_ids, Unset):
            entity_ids = self.entity_ids
        if not isinstance(self.format, Unset):
            format = self.format
        if not isinstance(self.source_unit, Unset):
            source_unit = self.source_unit
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_ids is not UNSET:
            field_dict["entity_ids"] = entity_ids
        if format is not UNSET:
            field_dict["format"] = format.to_dict()
        if source_unit is not UNSET:
            field_dict["source_unit"] = source_unit
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[IM], src_dict: Dict[str, Any]) -> IM:
        d = src_dict.copy()
        entity_ids = cast(List[str], d.pop("entity_ids", UNSET))

        _format = d.pop("format", UNSET)
        format: Union[Unset, OutputFormat]
        if isinstance(_format, Unset):
            format = UNSET
        else:
            format = _format  # type: ignore[arg-type]

        _source_unit = d.pop("source_unit", UNSET)
        source_unit: Union[Unset, UnitLength]
        if isinstance(_source_unit, Unset):
            source_unit = UNSET
        else:
            source_unit = _source_unit  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        export = cls(
            entity_ids=entity_ids,
            format=format,
            source_unit=source_unit,
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


OU = TypeVar("OU", bound="entity_get_parent_id")


@attr.s(auto_attribs=True)
class entity_get_parent_id:
    """What is this entity's parent?"""  # noqa: E501

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
    def from_dict(cls: Type[OU], src_dict: Dict[str, Any]) -> OU:
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


KL = TypeVar("KL", bound="entity_get_num_children")


@attr.s(auto_attribs=True)
class entity_get_num_children:
    """How many children does the entity have?"""  # noqa: E501

    entity_id: Union[Unset, str] = UNSET
    type: str = "entity_get_num_children"

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
    def from_dict(cls: Type[KL], src_dict: Dict[str, Any]) -> KL:
        d = src_dict.copy()
        entity_id = d.pop("entity_id", UNSET)

        type = d.pop("type", UNSET)

        entity_get_num_children = cls(
            entity_id=entity_id,
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


XI = TypeVar("XI", bound="entity_get_child_uuid")


@attr.s(auto_attribs=True)
class entity_get_child_uuid:
    """What is the UUID of this entity's n-th child?"""  # noqa: E501

    child_index: Union[Unset, int] = UNSET
    entity_id: Union[Unset, str] = UNSET
    type: str = "entity_get_child_uuid"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        child_index = self.child_index
        entity_id = self.entity_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if child_index is not UNSET:
            field_dict["child_index"] = child_index
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[XI], src_dict: Dict[str, Any]) -> XI:
        d = src_dict.copy()
        child_index = d.pop("child_index", UNSET)

        entity_id = d.pop("entity_id", UNSET)

        type = d.pop("type", UNSET)

        entity_get_child_uuid = cls(
            child_index=child_index,
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


PO = TypeVar("PO", bound="entity_get_all_child_uuids")


@attr.s(auto_attribs=True)
class entity_get_all_child_uuids:
    """What are all UUIDs of this entity's children?"""  # noqa: E501

    entity_id: Union[Unset, str] = UNSET
    type: str = "entity_get_all_child_uuids"

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
    def from_dict(cls: Type[PO], src_dict: Dict[str, Any]) -> PO:
        d = src_dict.copy()
        entity_id = d.pop("entity_id", UNSET)

        type = d.pop("type", UNSET)

        entity_get_all_child_uuids = cls(
            entity_id=entity_id,
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


PS = TypeVar("PS", bound="edit_mode_enter")


@attr.s(auto_attribs=True)
class edit_mode_enter:
    """Enter edit mode"""  # noqa: E501

    target: Union[Unset, str] = UNSET
    type: str = "edit_mode_enter"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        target = self.target
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target is not UNSET:
            field_dict["target"] = target
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[PS], src_dict: Dict[str, Any]) -> PS:
        d = src_dict.copy()
        target = d.pop("target", UNSET)

        type = d.pop("type", UNSET)

        edit_mode_enter = cls(
            target=target,
            type=type,
        )

        edit_mode_enter.additional_properties = d
        return edit_mode_enter

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


WR = TypeVar("WR", bound="edit_mode_exit")


@attr.s(auto_attribs=True)
class edit_mode_exit:
    """Exit edit mode"""  # noqa: E501

    type: str = "edit_mode_exit"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[WR], src_dict: Dict[str, Any]) -> WR:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        edit_mode_exit = cls(
            type=type,
        )

        edit_mode_exit.additional_properties = d
        return edit_mode_exit

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


XL = TypeVar("XL", bound="select_with_point")


@attr.s(auto_attribs=True)
class select_with_point:
    """Modifies the selection by simulating a "mouse click" at the given x,y window coordinate Returns ID of whatever was selected."""  # noqa: E501

    selected_at_window: Union[Unset, Point2d] = UNSET
    selection_type: Union[Unset, SceneSelectionType] = UNSET
    type: str = "select_with_point"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.selected_at_window, Unset):
            selected_at_window = self.selected_at_window
        if not isinstance(self.selection_type, Unset):
            selection_type = self.selection_type
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if selected_at_window is not UNSET:
            field_dict["selected_at_window"] = selected_at_window.to_dict()
        if selection_type is not UNSET:
            field_dict["selection_type"] = selection_type
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[XL], src_dict: Dict[str, Any]) -> XL:
        d = src_dict.copy()
        _selected_at_window = d.pop("selected_at_window", UNSET)
        selected_at_window: Union[Unset, Point2d]
        if isinstance(_selected_at_window, Unset):
            selected_at_window = UNSET
        else:
            selected_at_window = _selected_at_window  # type: ignore[arg-type]

        _selection_type = d.pop("selection_type", UNSET)
        selection_type: Union[Unset, SceneSelectionType]
        if isinstance(_selection_type, Unset):
            selection_type = UNSET
        else:
            selection_type = _selection_type  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        select_with_point = cls(
            selected_at_window=selected_at_window,
            selection_type=selection_type,
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


ZX = TypeVar("ZX", bound="select_clear")


@attr.s(auto_attribs=True)
class select_clear:
    """Clear the selection"""  # noqa: E501

    type: str = "select_clear"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[ZX], src_dict: Dict[str, Any]) -> ZX:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        select_clear = cls(
            type=type,
        )

        select_clear.additional_properties = d
        return select_clear

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


FT = TypeVar("FT", bound="select_add")


@attr.s(auto_attribs=True)
class select_add:
    """Adds one or more entities (by UUID) to the selection."""  # noqa: E501

    entities: Union[Unset, List[str]] = UNSET
    type: str = "select_add"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entities: Union[Unset, List[str]] = UNSET
        if not isinstance(self.entities, Unset):
            entities = self.entities
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entities is not UNSET:
            field_dict["entities"] = entities
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[FT], src_dict: Dict[str, Any]) -> FT:
        d = src_dict.copy()
        entities = cast(List[str], d.pop("entities", UNSET))

        type = d.pop("type", UNSET)

        select_add = cls(
            entities=entities,
            type=type,
        )

        select_add.additional_properties = d
        return select_add

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


NX = TypeVar("NX", bound="select_remove")


@attr.s(auto_attribs=True)
class select_remove:
    """Removes one or more entities (by UUID) from the selection."""  # noqa: E501

    entities: Union[Unset, List[str]] = UNSET
    type: str = "select_remove"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entities: Union[Unset, List[str]] = UNSET
        if not isinstance(self.entities, Unset):
            entities = self.entities
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entities is not UNSET:
            field_dict["entities"] = entities
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[NX], src_dict: Dict[str, Any]) -> NX:
        d = src_dict.copy()
        entities = cast(List[str], d.pop("entities", UNSET))

        type = d.pop("type", UNSET)

        select_remove = cls(
            entities=entities,
            type=type,
        )

        select_remove.additional_properties = d
        return select_remove

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


SC = TypeVar("SC", bound="select_replace")


@attr.s(auto_attribs=True)
class select_replace:
    """Replaces the current selection with these new entities (by UUID). Equivalent to doing SelectClear then SelectAdd."""  # noqa: E501

    entities: Union[Unset, List[str]] = UNSET
    type: str = "select_replace"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entities: Union[Unset, List[str]] = UNSET
        if not isinstance(self.entities, Unset):
            entities = self.entities
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entities is not UNSET:
            field_dict["entities"] = entities
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[SC], src_dict: Dict[str, Any]) -> SC:
        d = src_dict.copy()
        entities = cast(List[str], d.pop("entities", UNSET))

        type = d.pop("type", UNSET)

        select_replace = cls(
            entities=entities,
            type=type,
        )

        select_replace.additional_properties = d
        return select_replace

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


TX = TypeVar("TX", bound="select_get")


@attr.s(auto_attribs=True)
class select_get:
    """Find all IDs of selected entities"""  # noqa: E501

    type: str = "select_get"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[TX], src_dict: Dict[str, Any]) -> TX:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        select_get = cls(
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


JA = TypeVar("JA", bound="highlight_set_entity")


@attr.s(auto_attribs=True)
class highlight_set_entity:
    """Changes the current highlighted entity to whichever one is at the given window coordinate. If there's no entity at this location, clears the highlight."""  # noqa: E501

    selected_at_window: Union[Unset, Point2d] = UNSET
    sequence: Union[Unset, int] = UNSET
    type: str = "highlight_set_entity"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.selected_at_window, Unset):
            selected_at_window = self.selected_at_window
        sequence = self.sequence
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if selected_at_window is not UNSET:
            field_dict["selected_at_window"] = selected_at_window.to_dict()
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[JA], src_dict: Dict[str, Any]) -> JA:
        d = src_dict.copy()
        _selected_at_window = d.pop("selected_at_window", UNSET)
        selected_at_window: Union[Unset, Point2d]
        if isinstance(_selected_at_window, Unset):
            selected_at_window = UNSET
        else:
            selected_at_window = _selected_at_window  # type: ignore[arg-type]

        sequence = d.pop("sequence", UNSET)

        type = d.pop("type", UNSET)

        highlight_set_entity = cls(
            selected_at_window=selected_at_window,
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


SK = TypeVar("SK", bound="highlight_set_entities")


@attr.s(auto_attribs=True)
class highlight_set_entities:
    """Changes the current highlighted entity to these entities."""  # noqa: E501

    entities: Union[Unset, List[str]] = UNSET
    type: str = "highlight_set_entities"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entities: Union[Unset, List[str]] = UNSET
        if not isinstance(self.entities, Unset):
            entities = self.entities
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entities is not UNSET:
            field_dict["entities"] = entities
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[SK], src_dict: Dict[str, Any]) -> SK:
        d = src_dict.copy()
        entities = cast(List[str], d.pop("entities", UNSET))

        type = d.pop("type", UNSET)

        highlight_set_entities = cls(
            entities=entities,
            type=type,
        )

        highlight_set_entities.additional_properties = d
        return highlight_set_entities

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


UK = TypeVar("UK", bound="new_annotation")


@attr.s(auto_attribs=True)
class new_annotation:
    """Create a new annotation"""  # noqa: E501

    annotation_type: Union[Unset, AnnotationType] = UNSET
    clobber: Union[Unset, bool] = False
    options: Union[Unset, AnnotationOptions] = UNSET
    type: str = "new_annotation"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.annotation_type, Unset):
            annotation_type = self.annotation_type
        clobber = self.clobber
        if not isinstance(self.options, Unset):
            options = self.options
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotation_type is not UNSET:
            field_dict["annotation_type"] = annotation_type
        if clobber is not UNSET:
            field_dict["clobber"] = clobber
        if options is not UNSET:
            field_dict["options"] = options.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[UK], src_dict: Dict[str, Any]) -> UK:
        d = src_dict.copy()
        _annotation_type = d.pop("annotation_type", UNSET)
        annotation_type: Union[Unset, AnnotationType]
        if isinstance(_annotation_type, Unset):
            annotation_type = UNSET
        else:
            annotation_type = _annotation_type  # type: ignore[arg-type]

        clobber = d.pop("clobber", UNSET)

        _options = d.pop("options", UNSET)
        options: Union[Unset, AnnotationOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = _options  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        new_annotation = cls(
            annotation_type=annotation_type,
            clobber=clobber,
            options=options,
            type=type,
        )

        new_annotation.additional_properties = d
        return new_annotation

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


CX = TypeVar("CX", bound="update_annotation")


@attr.s(auto_attribs=True)
class update_annotation:
    """Update an annotation"""  # noqa: E501

    annotation_id: Union[Unset, str] = UNSET
    options: Union[Unset, AnnotationOptions] = UNSET
    type: str = "update_annotation"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        annotation_id = self.annotation_id
        if not isinstance(self.options, Unset):
            options = self.options
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotation_id is not UNSET:
            field_dict["annotation_id"] = annotation_id
        if options is not UNSET:
            field_dict["options"] = options.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[CX], src_dict: Dict[str, Any]) -> CX:
        d = src_dict.copy()
        annotation_id = d.pop("annotation_id", UNSET)

        _options = d.pop("options", UNSET)
        options: Union[Unset, AnnotationOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = _options  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        update_annotation = cls(
            annotation_id=annotation_id,
            options=options,
            type=type,
        )

        update_annotation.additional_properties = d
        return update_annotation

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


MT = TypeVar("MT", bound="object_visible")


@attr.s(auto_attribs=True)
class object_visible:
    """Hide or show an object"""  # noqa: E501

    hidden: Union[Unset, bool] = False
    object_id: Union[Unset, str] = UNSET
    type: str = "object_visible"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hidden = self.hidden
        object_id = self.object_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[MT], src_dict: Dict[str, Any]) -> MT:
        d = src_dict.copy()
        hidden = d.pop("hidden", UNSET)

        object_id = d.pop("object_id", UNSET)

        type = d.pop("type", UNSET)

        object_visible = cls(
            hidden=hidden,
            object_id=object_id,
            type=type,
        )

        object_visible.additional_properties = d
        return object_visible

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


LJ = TypeVar("LJ", bound="object_bring_to_front")


@attr.s(auto_attribs=True)
class object_bring_to_front:
    """Bring an object to the front of the scene"""  # noqa: E501

    object_id: Union[Unset, str] = UNSET
    type: str = "object_bring_to_front"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_id = self.object_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[LJ], src_dict: Dict[str, Any]) -> LJ:
        d = src_dict.copy()
        object_id = d.pop("object_id", UNSET)

        type = d.pop("type", UNSET)

        object_bring_to_front = cls(
            object_id=object_id,
            type=type,
        )

        object_bring_to_front.additional_properties = d
        return object_bring_to_front

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


TF = TypeVar("TF", bound="get_entity_type")


@attr.s(auto_attribs=True)
class get_entity_type:
    """What type of entity is this?"""  # noqa: E501

    entity_id: Union[Unset, str] = UNSET
    type: str = "get_entity_type"

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
    def from_dict(cls: Type[TF], src_dict: Dict[str, Any]) -> TF:
        d = src_dict.copy()
        entity_id = d.pop("entity_id", UNSET)

        type = d.pop("type", UNSET)

        get_entity_type = cls(
            entity_id=entity_id,
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


HF = TypeVar("HF", bound="solid2d_add_hole")


@attr.s(auto_attribs=True)
class solid2d_add_hole:
    """Add a hole to a Solid2d object before extruding it."""  # noqa: E501

    hole_id: Union[Unset, str] = UNSET
    object_id: Union[Unset, str] = UNSET
    type: str = "solid2d_add_hole"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hole_id = self.hole_id
        object_id = self.object_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hole_id is not UNSET:
            field_dict["hole_id"] = hole_id
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[HF], src_dict: Dict[str, Any]) -> HF:
        d = src_dict.copy()
        hole_id = d.pop("hole_id", UNSET)

        object_id = d.pop("object_id", UNSET)

        type = d.pop("type", UNSET)

        solid2d_add_hole = cls(
            hole_id=hole_id,
            object_id=object_id,
            type=type,
        )

        solid2d_add_hole.additional_properties = d
        return solid2d_add_hole

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


JD = TypeVar("JD", bound="solid3d_get_all_edge_faces")


@attr.s(auto_attribs=True)
class solid3d_get_all_edge_faces:
    """Gets all faces which use the given edge."""  # noqa: E501

    edge_id: Union[Unset, str] = UNSET
    object_id: Union[Unset, str] = UNSET
    type: str = "solid3d_get_all_edge_faces"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        edge_id = self.edge_id
        object_id = self.object_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edge_id is not UNSET:
            field_dict["edge_id"] = edge_id
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[JD], src_dict: Dict[str, Any]) -> JD:
        d = src_dict.copy()
        edge_id = d.pop("edge_id", UNSET)

        object_id = d.pop("object_id", UNSET)

        type = d.pop("type", UNSET)

        solid3d_get_all_edge_faces = cls(
            edge_id=edge_id,
            object_id=object_id,
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


RZ = TypeVar("RZ", bound="solid3d_get_all_opposite_edges")


@attr.s(auto_attribs=True)
class solid3d_get_all_opposite_edges:
    """Gets all edges which are opposite the given edge, across all possible faces."""  # noqa: E501

    along_vector: Union[Unset, Point3d] = UNSET
    edge_id: Union[Unset, str] = UNSET
    object_id: Union[Unset, str] = UNSET
    type: str = "solid3d_get_all_opposite_edges"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.along_vector, Unset):
            along_vector = self.along_vector
        edge_id = self.edge_id
        object_id = self.object_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if along_vector is not UNSET:
            field_dict["along_vector"] = along_vector.to_dict()
        if edge_id is not UNSET:
            field_dict["edge_id"] = edge_id
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[RZ], src_dict: Dict[str, Any]) -> RZ:
        d = src_dict.copy()
        _along_vector = d.pop("along_vector", UNSET)
        along_vector: Union[Unset, Point3d]
        if isinstance(_along_vector, Unset):
            along_vector = UNSET
        else:
            along_vector = _along_vector  # type: ignore[arg-type]

        edge_id = d.pop("edge_id", UNSET)

        object_id = d.pop("object_id", UNSET)

        type = d.pop("type", UNSET)

        solid3d_get_all_opposite_edges = cls(
            along_vector=along_vector,
            edge_id=edge_id,
            object_id=object_id,
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


BH = TypeVar("BH", bound="solid3d_get_opposite_edge")


@attr.s(auto_attribs=True)
class solid3d_get_opposite_edge:
    """Gets the edge opposite the given edge, along the given face."""  # noqa: E501

    edge_id: Union[Unset, str] = UNSET
    face_id: Union[Unset, str] = UNSET
    object_id: Union[Unset, str] = UNSET
    type: str = "solid3d_get_opposite_edge"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        edge_id = self.edge_id
        face_id = self.face_id
        object_id = self.object_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edge_id is not UNSET:
            field_dict["edge_id"] = edge_id
        if face_id is not UNSET:
            field_dict["face_id"] = face_id
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[BH], src_dict: Dict[str, Any]) -> BH:
        d = src_dict.copy()
        edge_id = d.pop("edge_id", UNSET)

        face_id = d.pop("face_id", UNSET)

        object_id = d.pop("object_id", UNSET)

        type = d.pop("type", UNSET)

        solid3d_get_opposite_edge = cls(
            edge_id=edge_id,
            face_id=face_id,
            object_id=object_id,
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


SX = TypeVar("SX", bound="solid3d_get_next_adjacent_edge")


@attr.s(auto_attribs=True)
class solid3d_get_next_adjacent_edge:
    """Gets the next adjacent edge for the given edge, along the given face."""  # noqa: E501

    edge_id: Union[Unset, str] = UNSET
    face_id: Union[Unset, str] = UNSET
    object_id: Union[Unset, str] = UNSET
    type: str = "solid3d_get_next_adjacent_edge"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        edge_id = self.edge_id
        face_id = self.face_id
        object_id = self.object_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edge_id is not UNSET:
            field_dict["edge_id"] = edge_id
        if face_id is not UNSET:
            field_dict["face_id"] = face_id
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[SX], src_dict: Dict[str, Any]) -> SX:
        d = src_dict.copy()
        edge_id = d.pop("edge_id", UNSET)

        face_id = d.pop("face_id", UNSET)

        object_id = d.pop("object_id", UNSET)

        type = d.pop("type", UNSET)

        solid3d_get_next_adjacent_edge = cls(
            edge_id=edge_id,
            face_id=face_id,
            object_id=object_id,
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


CN = TypeVar("CN", bound="solid3d_get_prev_adjacent_edge")


@attr.s(auto_attribs=True)
class solid3d_get_prev_adjacent_edge:
    """Gets the previous adjacent edge for the given edge, along the given face."""  # noqa: E501

    edge_id: Union[Unset, str] = UNSET
    face_id: Union[Unset, str] = UNSET
    object_id: Union[Unset, str] = UNSET
    type: str = "solid3d_get_prev_adjacent_edge"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        edge_id = self.edge_id
        face_id = self.face_id
        object_id = self.object_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edge_id is not UNSET:
            field_dict["edge_id"] = edge_id
        if face_id is not UNSET:
            field_dict["face_id"] = face_id
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[CN], src_dict: Dict[str, Any]) -> CN:
        d = src_dict.copy()
        edge_id = d.pop("edge_id", UNSET)

        face_id = d.pop("face_id", UNSET)

        object_id = d.pop("object_id", UNSET)

        type = d.pop("type", UNSET)

        solid3d_get_prev_adjacent_edge = cls(
            edge_id=edge_id,
            face_id=face_id,
            object_id=object_id,
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


GS = TypeVar("GS", bound="send_object")


@attr.s(auto_attribs=True)
class send_object:
    """Sends object to front or back."""  # noqa: E501

    front: Union[Unset, bool] = False
    object_id: Union[Unset, str] = UNSET
    type: str = "send_object"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        front = self.front
        object_id = self.object_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if front is not UNSET:
            field_dict["front"] = front
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[GS], src_dict: Dict[str, Any]) -> GS:
        d = src_dict.copy()
        front = d.pop("front", UNSET)

        object_id = d.pop("object_id", UNSET)

        type = d.pop("type", UNSET)

        send_object = cls(
            front=front,
            object_id=object_id,
            type=type,
        )

        send_object.additional_properties = d
        return send_object

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


SO = TypeVar("SO", bound="entity_set_opacity")


@attr.s(auto_attribs=True)
class entity_set_opacity:
    """Set opacity of the entity."""  # noqa: E501

    entity_id: Union[Unset, str] = UNSET
    opacity: Union[Unset, float] = UNSET
    type: str = "entity_set_opacity"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_id = self.entity_id
        opacity = self.opacity
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if opacity is not UNSET:
            field_dict["opacity"] = opacity
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[SO], src_dict: Dict[str, Any]) -> SO:
        d = src_dict.copy()
        entity_id = d.pop("entity_id", UNSET)

        opacity = d.pop("opacity", UNSET)

        type = d.pop("type", UNSET)

        entity_set_opacity = cls(
            entity_id=entity_id,
            opacity=opacity,
            type=type,
        )

        entity_set_opacity.additional_properties = d
        return entity_set_opacity

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


ZS = TypeVar("ZS", bound="entity_fade")


@attr.s(auto_attribs=True)
class entity_fade:
    """Fade the entity in or out."""  # noqa: E501

    duration_seconds: Union[Unset, float] = UNSET
    entity_id: Union[Unset, str] = UNSET
    fade_in: Union[Unset, bool] = False
    type: str = "entity_fade"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duration_seconds = self.duration_seconds
        entity_id = self.entity_id
        fade_in = self.fade_in
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duration_seconds is not UNSET:
            field_dict["duration_seconds"] = duration_seconds
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if fade_in is not UNSET:
            field_dict["fade_in"] = fade_in
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[ZS], src_dict: Dict[str, Any]) -> ZS:
        d = src_dict.copy()
        duration_seconds = d.pop("duration_seconds", UNSET)

        entity_id = d.pop("entity_id", UNSET)

        fade_in = d.pop("fade_in", UNSET)

        type = d.pop("type", UNSET)

        entity_fade = cls(
            duration_seconds=duration_seconds,
            entity_id=entity_id,
            fade_in=fade_in,
            type=type,
        )

        entity_fade.additional_properties = d
        return entity_fade

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


AM = TypeVar("AM", bound="make_plane")


@attr.s(auto_attribs=True)
class make_plane:
    """Make a plane."""  # noqa: E501

    clobber: Union[Unset, bool] = False
    hide: Union[Unset, bool] = False
    origin: Union[Unset, Point3d] = UNSET
    size: Union[Unset, float] = UNSET
    type: str = "make_plane"
    x_axis: Union[Unset, Point3d] = UNSET
    y_axis: Union[Unset, Point3d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        clobber = self.clobber
        hide = self.hide
        if not isinstance(self.origin, Unset):
            origin = self.origin
        size = self.size
        type = self.type
        if not isinstance(self.x_axis, Unset):
            x_axis = self.x_axis
        if not isinstance(self.y_axis, Unset):
            y_axis = self.y_axis

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clobber is not UNSET:
            field_dict["clobber"] = clobber
        if hide is not UNSET:
            field_dict["hide"] = hide
        if origin is not UNSET:
            field_dict["origin"] = origin.to_dict()
        if size is not UNSET:
            field_dict["size"] = size
        field_dict["type"] = type
        if x_axis is not UNSET:
            field_dict["x_axis"] = x_axis.to_dict()
        if y_axis is not UNSET:
            field_dict["y_axis"] = y_axis.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[AM], src_dict: Dict[str, Any]) -> AM:
        d = src_dict.copy()
        clobber = d.pop("clobber", UNSET)

        hide = d.pop("hide", UNSET)

        _origin = d.pop("origin", UNSET)
        origin: Union[Unset, Point3d]
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = _origin  # type: ignore[arg-type]

        size = d.pop("size", UNSET)

        type = d.pop("type", UNSET)

        _x_axis = d.pop("x_axis", UNSET)
        x_axis: Union[Unset, Point3d]
        if isinstance(_x_axis, Unset):
            x_axis = UNSET
        else:
            x_axis = _x_axis  # type: ignore[arg-type]

        _y_axis = d.pop("y_axis", UNSET)
        y_axis: Union[Unset, Point3d]
        if isinstance(_y_axis, Unset):
            y_axis = UNSET
        else:
            y_axis = _y_axis  # type: ignore[arg-type]

        make_plane = cls(
            clobber=clobber,
            hide=hide,
            origin=origin,
            size=size,
            type=type,
            x_axis=x_axis,
            y_axis=y_axis,
        )

        make_plane.additional_properties = d
        return make_plane

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


GK = TypeVar("GK", bound="plane_set_color")


@attr.s(auto_attribs=True)
class plane_set_color:
    """Set the plane's color."""  # noqa: E501

    color: Union[Unset, Color] = UNSET
    plane_id: Union[Unset, str] = UNSET
    type: str = "plane_set_color"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.color, Unset):
            color = self.color
        plane_id = self.plane_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color.to_dict()
        if plane_id is not UNSET:
            field_dict["plane_id"] = plane_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[GK], src_dict: Dict[str, Any]) -> GK:
        d = src_dict.copy()
        _color = d.pop("color", UNSET)
        color: Union[Unset, Color]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = _color  # type: ignore[arg-type]

        plane_id = d.pop("plane_id", UNSET)

        type = d.pop("type", UNSET)

        plane_set_color = cls(
            color=color,
            plane_id=plane_id,
            type=type,
        )

        plane_set_color.additional_properties = d
        return plane_set_color

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


SG = TypeVar("SG", bound="set_tool")


@attr.s(auto_attribs=True)
class set_tool:
    """Set the active tool."""  # noqa: E501

    tool: Union[Unset, SceneToolType] = UNSET
    type: str = "set_tool"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.tool, Unset):
            tool = self.tool
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tool is not UNSET:
            field_dict["tool"] = tool
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[SG], src_dict: Dict[str, Any]) -> SG:
        d = src_dict.copy()
        _tool = d.pop("tool", UNSET)
        tool: Union[Unset, SceneToolType]
        if isinstance(_tool, Unset):
            tool = UNSET
        else:
            tool = _tool  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        set_tool = cls(
            tool=tool,
            type=type,
        )

        set_tool.additional_properties = d
        return set_tool

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


QZ = TypeVar("QZ", bound="mouse_move")


@attr.s(auto_attribs=True)
class mouse_move:
    """Send a mouse move event."""  # noqa: E501

    sequence: Union[Unset, int] = UNSET
    type: str = "mouse_move"
    window: Union[Unset, Point2d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sequence = self.sequence
        type = self.type
        if not isinstance(self.window, Unset):
            window = self.window

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        field_dict["type"] = type
        if window is not UNSET:
            field_dict["window"] = window.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[QZ], src_dict: Dict[str, Any]) -> QZ:
        d = src_dict.copy()
        sequence = d.pop("sequence", UNSET)

        type = d.pop("type", UNSET)

        _window = d.pop("window", UNSET)
        window: Union[Unset, Point2d]
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = _window  # type: ignore[arg-type]

        mouse_move = cls(
            sequence=sequence,
            type=type,
            window=window,
        )

        mouse_move.additional_properties = d
        return mouse_move

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


SY = TypeVar("SY", bound="mouse_click")


@attr.s(auto_attribs=True)
class mouse_click:
    """Send a mouse click event. Updates modified/selected entities."""  # noqa: E501

    type: str = "mouse_click"
    window: Union[Unset, Point2d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        if not isinstance(self.window, Unset):
            window = self.window

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        field_dict["type"] = type
        if window is not UNSET:
            field_dict["window"] = window.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[SY], src_dict: Dict[str, Any]) -> SY:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        _window = d.pop("window", UNSET)
        window: Union[Unset, Point2d]
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = _window  # type: ignore[arg-type]

        mouse_click = cls(
            type=type,
            window=window,
        )

        mouse_click.additional_properties = d
        return mouse_click

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


YK = TypeVar("YK", bound="sketch_mode_enable")


@attr.s(auto_attribs=True)
class sketch_mode_enable:
    """Enable sketch mode on the given plane."""  # noqa: E501

    animated: Union[Unset, bool] = False
    disable_camera_with_plane: Union[Unset, Point3d] = UNSET
    ortho: Union[Unset, bool] = False
    plane_id: Union[Unset, str] = UNSET
    type: str = "sketch_mode_enable"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        animated = self.animated
        if not isinstance(self.disable_camera_with_plane, Unset):
            disable_camera_with_plane = self.disable_camera_with_plane
        ortho = self.ortho
        plane_id = self.plane_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if animated is not UNSET:
            field_dict["animated"] = animated
        if disable_camera_with_plane is not UNSET:
            field_dict[
                "disable_camera_with_plane"
            ] = disable_camera_with_plane.to_dict()
        if ortho is not UNSET:
            field_dict["ortho"] = ortho
        if plane_id is not UNSET:
            field_dict["plane_id"] = plane_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[YK], src_dict: Dict[str, Any]) -> YK:
        d = src_dict.copy()
        animated = d.pop("animated", UNSET)

        _disable_camera_with_plane = d.pop("disable_camera_with_plane", UNSET)
        disable_camera_with_plane: Union[Unset, Point3d]
        if isinstance(_disable_camera_with_plane, Unset):
            disable_camera_with_plane = UNSET
        else:
            disable_camera_with_plane = _disable_camera_with_plane  # type: ignore[arg-type]

        ortho = d.pop("ortho", UNSET)

        plane_id = d.pop("plane_id", UNSET)

        type = d.pop("type", UNSET)

        sketch_mode_enable = cls(
            animated=animated,
            disable_camera_with_plane=disable_camera_with_plane,
            ortho=ortho,
            plane_id=plane_id,
            type=type,
        )

        sketch_mode_enable.additional_properties = d
        return sketch_mode_enable

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


WS = TypeVar("WS", bound="sketch_mode_disable")


@attr.s(auto_attribs=True)
class sketch_mode_disable:
    """Disable sketch mode."""  # noqa: E501

    type: str = "sketch_mode_disable"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[WS], src_dict: Dict[str, Any]) -> WS:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        sketch_mode_disable = cls(
            type=type,
        )

        sketch_mode_disable.additional_properties = d
        return sketch_mode_disable

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


SL = TypeVar("SL", bound="curve_get_type")


@attr.s(auto_attribs=True)
class curve_get_type:
    """Get type of a given curve."""  # noqa: E501

    curve_id: Union[Unset, str] = UNSET
    type: str = "curve_get_type"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        curve_id = self.curve_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if curve_id is not UNSET:
            field_dict["curve_id"] = curve_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[SL], src_dict: Dict[str, Any]) -> SL:
        d = src_dict.copy()
        curve_id = d.pop("curve_id", UNSET)

        type = d.pop("type", UNSET)

        curve_get_type = cls(
            curve_id=curve_id,
            type=type,
        )

        curve_get_type.additional_properties = d
        return curve_get_type

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


MK = TypeVar("MK", bound="curve_get_control_points")


@attr.s(auto_attribs=True)
class curve_get_control_points:
    """Get control points of a given curve."""  # noqa: E501

    curve_id: Union[Unset, str] = UNSET
    type: str = "curve_get_control_points"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        curve_id = self.curve_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if curve_id is not UNSET:
            field_dict["curve_id"] = curve_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[MK], src_dict: Dict[str, Any]) -> MK:
        d = src_dict.copy()
        curve_id = d.pop("curve_id", UNSET)

        type = d.pop("type", UNSET)

        curve_get_control_points = cls(
            curve_id=curve_id,
            type=type,
        )

        curve_get_control_points.additional_properties = d
        return curve_get_control_points

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


TU = TypeVar("TU", bound="take_snapshot")


@attr.s(auto_attribs=True)
class take_snapshot:
    """Take a snapshot."""  # noqa: E501

    format: Union[Unset, ImageFormat] = UNSET
    type: str = "take_snapshot"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.format, Unset):
            format = self.format
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if format is not UNSET:
            field_dict["format"] = format
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[TU], src_dict: Dict[str, Any]) -> TU:
        d = src_dict.copy()
        _format = d.pop("format", UNSET)
        format: Union[Unset, ImageFormat]
        if isinstance(_format, Unset):
            format = UNSET
        else:
            format = _format  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        take_snapshot = cls(
            format=format,
            type=type,
        )

        take_snapshot.additional_properties = d
        return take_snapshot

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


FY = TypeVar("FY", bound="make_axes_gizmo")


@attr.s(auto_attribs=True)
class make_axes_gizmo:
    """Add a gizmo showing the axes."""  # noqa: E501

    clobber: Union[Unset, bool] = False
    gizmo_mode: Union[Unset, bool] = False
    type: str = "make_axes_gizmo"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        clobber = self.clobber
        gizmo_mode = self.gizmo_mode
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clobber is not UNSET:
            field_dict["clobber"] = clobber
        if gizmo_mode is not UNSET:
            field_dict["gizmo_mode"] = gizmo_mode
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[FY], src_dict: Dict[str, Any]) -> FY:
        d = src_dict.copy()
        clobber = d.pop("clobber", UNSET)

        gizmo_mode = d.pop("gizmo_mode", UNSET)

        type = d.pop("type", UNSET)

        make_axes_gizmo = cls(
            clobber=clobber,
            gizmo_mode=gizmo_mode,
            type=type,
        )

        make_axes_gizmo.additional_properties = d
        return make_axes_gizmo

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


FD = TypeVar("FD", bound="path_get_info")


@attr.s(auto_attribs=True)
class path_get_info:
    """Query the given path"""  # noqa: E501

    path_id: Union[Unset, str] = UNSET
    type: str = "path_get_info"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path_id = self.path_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path_id is not UNSET:
            field_dict["path_id"] = path_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[FD], src_dict: Dict[str, Any]) -> FD:
        d = src_dict.copy()
        path_id = d.pop("path_id", UNSET)

        type = d.pop("type", UNSET)

        path_get_info = cls(
            path_id=path_id,
            type=type,
        )

        path_get_info.additional_properties = d
        return path_get_info

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


TZ = TypeVar("TZ", bound="path_get_curve_uuids_for_vertices")


@attr.s(auto_attribs=True)
class path_get_curve_uuids_for_vertices:
    """Get curves for vertices within a path"""  # noqa: E501

    path_id: Union[Unset, str] = UNSET
    type: str = "path_get_curve_uuids_for_vertices"
    vertex_ids: Union[Unset, List[str]] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path_id = self.path_id
        type = self.type
        vertex_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.vertex_ids, Unset):
            vertex_ids = self.vertex_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path_id is not UNSET:
            field_dict["path_id"] = path_id
        field_dict["type"] = type
        if vertex_ids is not UNSET:
            field_dict["vertex_ids"] = vertex_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[TZ], src_dict: Dict[str, Any]) -> TZ:
        d = src_dict.copy()
        path_id = d.pop("path_id", UNSET)

        type = d.pop("type", UNSET)

        vertex_ids = cast(List[str], d.pop("vertex_ids", UNSET))

        path_get_curve_uuids_for_vertices = cls(
            path_id=path_id,
            type=type,
            vertex_ids=vertex_ids,
        )

        path_get_curve_uuids_for_vertices.additional_properties = d
        return path_get_curve_uuids_for_vertices

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


AX = TypeVar("AX", bound="path_get_vertex_uuids")


@attr.s(auto_attribs=True)
class path_get_vertex_uuids:
    """Get vertices within a path"""  # noqa: E501

    path_id: Union[Unset, str] = UNSET
    type: str = "path_get_vertex_uuids"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path_id = self.path_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path_id is not UNSET:
            field_dict["path_id"] = path_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[AX], src_dict: Dict[str, Any]) -> AX:
        d = src_dict.copy()
        path_id = d.pop("path_id", UNSET)

        type = d.pop("type", UNSET)

        path_get_vertex_uuids = cls(
            path_id=path_id,
            type=type,
        )

        path_get_vertex_uuids.additional_properties = d
        return path_get_vertex_uuids

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


RQ = TypeVar("RQ", bound="handle_mouse_drag_start")


@attr.s(auto_attribs=True)
class handle_mouse_drag_start:
    """Start dragging mouse."""  # noqa: E501

    type: str = "handle_mouse_drag_start"
    window: Union[Unset, Point2d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        if not isinstance(self.window, Unset):
            window = self.window

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        field_dict["type"] = type
        if window is not UNSET:
            field_dict["window"] = window.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[RQ], src_dict: Dict[str, Any]) -> RQ:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        _window = d.pop("window", UNSET)
        window: Union[Unset, Point2d]
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = _window  # type: ignore[arg-type]

        handle_mouse_drag_start = cls(
            type=type,
            window=window,
        )

        handle_mouse_drag_start.additional_properties = d
        return handle_mouse_drag_start

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


ZL = TypeVar("ZL", bound="handle_mouse_drag_move")


@attr.s(auto_attribs=True)
class handle_mouse_drag_move:
    """Continue dragging mouse."""  # noqa: E501

    sequence: Union[Unset, int] = UNSET
    type: str = "handle_mouse_drag_move"
    window: Union[Unset, Point2d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sequence = self.sequence
        type = self.type
        if not isinstance(self.window, Unset):
            window = self.window

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        field_dict["type"] = type
        if window is not UNSET:
            field_dict["window"] = window.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[ZL], src_dict: Dict[str, Any]) -> ZL:
        d = src_dict.copy()
        sequence = d.pop("sequence", UNSET)

        type = d.pop("type", UNSET)

        _window = d.pop("window", UNSET)
        window: Union[Unset, Point2d]
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = _window  # type: ignore[arg-type]

        handle_mouse_drag_move = cls(
            sequence=sequence,
            type=type,
            window=window,
        )

        handle_mouse_drag_move.additional_properties = d
        return handle_mouse_drag_move

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


CM = TypeVar("CM", bound="handle_mouse_drag_end")


@attr.s(auto_attribs=True)
class handle_mouse_drag_end:
    """Stop dragging mouse."""  # noqa: E501

    type: str = "handle_mouse_drag_end"
    window: Union[Unset, Point2d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        if not isinstance(self.window, Unset):
            window = self.window

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        field_dict["type"] = type
        if window is not UNSET:
            field_dict["window"] = window.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[CM], src_dict: Dict[str, Any]) -> CM:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        _window = d.pop("window", UNSET)
        window: Union[Unset, Point2d]
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = _window  # type: ignore[arg-type]

        handle_mouse_drag_end = cls(
            type=type,
            window=window,
        )

        handle_mouse_drag_end.additional_properties = d
        return handle_mouse_drag_end

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


OS = TypeVar("OS", bound="remove_scene_objects")


@attr.s(auto_attribs=True)
class remove_scene_objects:
    """Remove scene objects."""  # noqa: E501

    object_ids: Union[Unset, List[str]] = UNSET
    type: str = "remove_scene_objects"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.object_ids, Unset):
            object_ids = self.object_ids
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ids is not UNSET:
            field_dict["object_ids"] = object_ids
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[OS], src_dict: Dict[str, Any]) -> OS:
        d = src_dict.copy()
        object_ids = cast(List[str], d.pop("object_ids", UNSET))

        type = d.pop("type", UNSET)

        remove_scene_objects = cls(
            object_ids=object_ids,
            type=type,
        )

        remove_scene_objects.additional_properties = d
        return remove_scene_objects

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


WP = TypeVar("WP", bound="plane_intersect_and_project")


@attr.s(auto_attribs=True)
class plane_intersect_and_project:
    """Utility method. Performs both a ray cast and projection to plane-local coordinates. Returns the plane coordinates for the given window coordinates."""  # noqa: E501

    plane_id: Union[Unset, str] = UNSET
    type: str = "plane_intersect_and_project"
    window: Union[Unset, Point2d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        plane_id = self.plane_id
        type = self.type
        if not isinstance(self.window, Unset):
            window = self.window

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plane_id is not UNSET:
            field_dict["plane_id"] = plane_id
        field_dict["type"] = type
        if window is not UNSET:
            field_dict["window"] = window.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[WP], src_dict: Dict[str, Any]) -> WP:
        d = src_dict.copy()
        plane_id = d.pop("plane_id", UNSET)

        type = d.pop("type", UNSET)

        _window = d.pop("window", UNSET)
        window: Union[Unset, Point2d]
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = _window  # type: ignore[arg-type]

        plane_intersect_and_project = cls(
            plane_id=plane_id,
            type=type,
            window=window,
        )

        plane_intersect_and_project.additional_properties = d
        return plane_intersect_and_project

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


XO = TypeVar("XO", bound="curve_get_end_points")


@attr.s(auto_attribs=True)
class curve_get_end_points:
    """Find the start and end of a curve."""  # noqa: E501

    curve_id: Union[Unset, str] = UNSET
    type: str = "curve_get_end_points"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        curve_id = self.curve_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if curve_id is not UNSET:
            field_dict["curve_id"] = curve_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[XO], src_dict: Dict[str, Any]) -> XO:
        d = src_dict.copy()
        curve_id = d.pop("curve_id", UNSET)

        type = d.pop("type", UNSET)

        curve_get_end_points = cls(
            curve_id=curve_id,
            type=type,
        )

        curve_get_end_points.additional_properties = d
        return curve_get_end_points

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


LN = TypeVar("LN", bound="reconfigure_stream")


@attr.s(auto_attribs=True)
class reconfigure_stream:
    """Reconfigure the stream."""  # noqa: E501

    fps: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    type: str = "reconfigure_stream"
    width: Union[Unset, int] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fps = self.fps
        height = self.height
        type = self.type
        width = self.width

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fps is not UNSET:
            field_dict["fps"] = fps
        if height is not UNSET:
            field_dict["height"] = height
        field_dict["type"] = type
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: Type[LN], src_dict: Dict[str, Any]) -> LN:
        d = src_dict.copy()
        fps = d.pop("fps", UNSET)

        height = d.pop("height", UNSET)

        type = d.pop("type", UNSET)

        width = d.pop("width", UNSET)

        reconfigure_stream = cls(
            fps=fps,
            height=height,
            type=type,
            width=width,
        )

        reconfigure_stream.additional_properties = d
        return reconfigure_stream

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


KR = TypeVar("KR", bound="import_files")


@attr.s(auto_attribs=True)
class import_files:
    """Import files to the current model."""  # noqa: E501

    from ..models.import_file import ImportFile

    files: Union[Unset, List[ImportFile]] = UNSET
    format: Union[Unset, InputFormat] = UNSET
    type: str = "import_files"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.import_file import ImportFile

        files: Union[Unset, List[ImportFile]] = UNSET
        if not isinstance(self.files, Unset):
            files = self.files
        if not isinstance(self.format, Unset):
            format = self.format
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        if format is not UNSET:
            field_dict["format"] = format.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[KR], src_dict: Dict[str, Any]) -> KR:
        d = src_dict.copy()
        from ..models.import_file import ImportFile

        files = cast(List[ImportFile], d.pop("files", UNSET))

        _format = d.pop("format", UNSET)
        format: Union[Unset, InputFormat]
        if isinstance(_format, Unset):
            format = UNSET
        else:
            format = _format  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        import_files = cls(
            files=files,
            format=format,
            type=type,
        )

        import_files.additional_properties = d
        return import_files

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


MG = TypeVar("MG", bound="mass")


@attr.s(auto_attribs=True)
class mass:
    """Get the mass of entities in the scene or the default scene."""  # noqa: E501

    entity_ids: Union[Unset, List[str]] = UNSET
    material_density: Union[Unset, float] = UNSET
    material_density_unit: Union[Unset, UnitDensity] = UNSET
    output_unit: Union[Unset, UnitMass] = UNSET
    source_unit: Union[Unset, UnitLength] = UNSET
    type: str = "mass"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.entity_ids, Unset):
            entity_ids = self.entity_ids
        material_density = self.material_density
        if not isinstance(self.material_density_unit, Unset):
            material_density_unit = self.material_density_unit
        if not isinstance(self.output_unit, Unset):
            output_unit = self.output_unit
        if not isinstance(self.source_unit, Unset):
            source_unit = self.source_unit
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_ids is not UNSET:
            field_dict["entity_ids"] = entity_ids
        if material_density is not UNSET:
            field_dict["material_density"] = material_density
        if material_density_unit is not UNSET:
            field_dict["material_density_unit"] = material_density_unit
        if output_unit is not UNSET:
            field_dict["output_unit"] = output_unit
        if source_unit is not UNSET:
            field_dict["source_unit"] = source_unit
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[MG], src_dict: Dict[str, Any]) -> MG:
        d = src_dict.copy()
        entity_ids = cast(List[str], d.pop("entity_ids", UNSET))

        material_density = d.pop("material_density", UNSET)

        _material_density_unit = d.pop("material_density_unit", UNSET)
        material_density_unit: Union[Unset, UnitDensity]
        if isinstance(_material_density_unit, Unset):
            material_density_unit = UNSET
        else:
            material_density_unit = _material_density_unit  # type: ignore[arg-type]

        _output_unit = d.pop("output_unit", UNSET)
        output_unit: Union[Unset, UnitMass]
        if isinstance(_output_unit, Unset):
            output_unit = UNSET
        else:
            output_unit = _output_unit  # type: ignore[arg-type]

        _source_unit = d.pop("source_unit", UNSET)
        source_unit: Union[Unset, UnitLength]
        if isinstance(_source_unit, Unset):
            source_unit = UNSET
        else:
            source_unit = _source_unit  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        mass = cls(
            entity_ids=entity_ids,
            material_density=material_density,
            material_density_unit=material_density_unit,
            output_unit=output_unit,
            source_unit=source_unit,
            type=type,
        )

        mass.additional_properties = d
        return mass

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


UE = TypeVar("UE", bound="density")


@attr.s(auto_attribs=True)
class density:
    """Get the density of entities in the scene or the default scene."""  # noqa: E501

    entity_ids: Union[Unset, List[str]] = UNSET
    material_mass: Union[Unset, float] = UNSET
    material_mass_unit: Union[Unset, UnitMass] = UNSET
    output_unit: Union[Unset, UnitDensity] = UNSET
    source_unit: Union[Unset, UnitLength] = UNSET
    type: str = "density"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.entity_ids, Unset):
            entity_ids = self.entity_ids
        material_mass = self.material_mass
        if not isinstance(self.material_mass_unit, Unset):
            material_mass_unit = self.material_mass_unit
        if not isinstance(self.output_unit, Unset):
            output_unit = self.output_unit
        if not isinstance(self.source_unit, Unset):
            source_unit = self.source_unit
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_ids is not UNSET:
            field_dict["entity_ids"] = entity_ids
        if material_mass is not UNSET:
            field_dict["material_mass"] = material_mass
        if material_mass_unit is not UNSET:
            field_dict["material_mass_unit"] = material_mass_unit
        if output_unit is not UNSET:
            field_dict["output_unit"] = output_unit
        if source_unit is not UNSET:
            field_dict["source_unit"] = source_unit
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[UE], src_dict: Dict[str, Any]) -> UE:
        d = src_dict.copy()
        entity_ids = cast(List[str], d.pop("entity_ids", UNSET))

        material_mass = d.pop("material_mass", UNSET)

        _material_mass_unit = d.pop("material_mass_unit", UNSET)
        material_mass_unit: Union[Unset, UnitMass]
        if isinstance(_material_mass_unit, Unset):
            material_mass_unit = UNSET
        else:
            material_mass_unit = _material_mass_unit  # type: ignore[arg-type]

        _output_unit = d.pop("output_unit", UNSET)
        output_unit: Union[Unset, UnitDensity]
        if isinstance(_output_unit, Unset):
            output_unit = UNSET
        else:
            output_unit = _output_unit  # type: ignore[arg-type]

        _source_unit = d.pop("source_unit", UNSET)
        source_unit: Union[Unset, UnitLength]
        if isinstance(_source_unit, Unset):
            source_unit = UNSET
        else:
            source_unit = _source_unit  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        density = cls(
            entity_ids=entity_ids,
            material_mass=material_mass,
            material_mass_unit=material_mass_unit,
            output_unit=output_unit,
            source_unit=source_unit,
            type=type,
        )

        density.additional_properties = d
        return density

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


BF = TypeVar("BF", bound="volume")


@attr.s(auto_attribs=True)
class volume:
    """Get the volume of entities in the scene or the default scene."""  # noqa: E501

    entity_ids: Union[Unset, List[str]] = UNSET
    output_unit: Union[Unset, UnitVolume] = UNSET
    source_unit: Union[Unset, UnitLength] = UNSET
    type: str = "volume"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.entity_ids, Unset):
            entity_ids = self.entity_ids
        if not isinstance(self.output_unit, Unset):
            output_unit = self.output_unit
        if not isinstance(self.source_unit, Unset):
            source_unit = self.source_unit
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_ids is not UNSET:
            field_dict["entity_ids"] = entity_ids
        if output_unit is not UNSET:
            field_dict["output_unit"] = output_unit
        if source_unit is not UNSET:
            field_dict["source_unit"] = source_unit
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[BF], src_dict: Dict[str, Any]) -> BF:
        d = src_dict.copy()
        entity_ids = cast(List[str], d.pop("entity_ids", UNSET))

        _output_unit = d.pop("output_unit", UNSET)
        output_unit: Union[Unset, UnitVolume]
        if isinstance(_output_unit, Unset):
            output_unit = UNSET
        else:
            output_unit = _output_unit  # type: ignore[arg-type]

        _source_unit = d.pop("source_unit", UNSET)
        source_unit: Union[Unset, UnitLength]
        if isinstance(_source_unit, Unset):
            source_unit = UNSET
        else:
            source_unit = _source_unit  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        volume = cls(
            entity_ids=entity_ids,
            output_unit=output_unit,
            source_unit=source_unit,
            type=type,
        )

        volume.additional_properties = d
        return volume

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


UU = TypeVar("UU", bound="center_of_mass")


@attr.s(auto_attribs=True)
class center_of_mass:
    """Get the center of mass of entities in the scene or the default scene."""  # noqa: E501

    entity_ids: Union[Unset, List[str]] = UNSET
    output_unit: Union[Unset, UnitLength] = UNSET
    source_unit: Union[Unset, UnitLength] = UNSET
    type: str = "center_of_mass"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.entity_ids, Unset):
            entity_ids = self.entity_ids
        if not isinstance(self.output_unit, Unset):
            output_unit = self.output_unit
        if not isinstance(self.source_unit, Unset):
            source_unit = self.source_unit
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_ids is not UNSET:
            field_dict["entity_ids"] = entity_ids
        if output_unit is not UNSET:
            field_dict["output_unit"] = output_unit
        if source_unit is not UNSET:
            field_dict["source_unit"] = source_unit
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[UU], src_dict: Dict[str, Any]) -> UU:
        d = src_dict.copy()
        entity_ids = cast(List[str], d.pop("entity_ids", UNSET))

        _output_unit = d.pop("output_unit", UNSET)
        output_unit: Union[Unset, UnitLength]
        if isinstance(_output_unit, Unset):
            output_unit = UNSET
        else:
            output_unit = _output_unit  # type: ignore[arg-type]

        _source_unit = d.pop("source_unit", UNSET)
        source_unit: Union[Unset, UnitLength]
        if isinstance(_source_unit, Unset):
            source_unit = UNSET
        else:
            source_unit = _source_unit  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        center_of_mass = cls(
            entity_ids=entity_ids,
            output_unit=output_unit,
            source_unit=source_unit,
            type=type,
        )

        center_of_mass.additional_properties = d
        return center_of_mass

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


MB = TypeVar("MB", bound="surface_area")


@attr.s(auto_attribs=True)
class surface_area:
    """Get the surface area of entities in the scene or the default scene."""  # noqa: E501

    entity_ids: Union[Unset, List[str]] = UNSET
    output_unit: Union[Unset, UnitArea] = UNSET
    source_unit: Union[Unset, UnitLength] = UNSET
    type: str = "surface_area"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.entity_ids, Unset):
            entity_ids = self.entity_ids
        if not isinstance(self.output_unit, Unset):
            output_unit = self.output_unit
        if not isinstance(self.source_unit, Unset):
            source_unit = self.source_unit
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_ids is not UNSET:
            field_dict["entity_ids"] = entity_ids
        if output_unit is not UNSET:
            field_dict["output_unit"] = output_unit
        if source_unit is not UNSET:
            field_dict["source_unit"] = source_unit
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[MB], src_dict: Dict[str, Any]) -> MB:
        d = src_dict.copy()
        entity_ids = cast(List[str], d.pop("entity_ids", UNSET))

        _output_unit = d.pop("output_unit", UNSET)
        output_unit: Union[Unset, UnitArea]
        if isinstance(_output_unit, Unset):
            output_unit = UNSET
        else:
            output_unit = _output_unit  # type: ignore[arg-type]

        _source_unit = d.pop("source_unit", UNSET)
        source_unit: Union[Unset, UnitLength]
        if isinstance(_source_unit, Unset):
            source_unit = UNSET
        else:
            source_unit = _source_unit  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        surface_area = cls(
            entity_ids=entity_ids,
            output_unit=output_unit,
            source_unit=source_unit,
            type=type,
        )

        surface_area.additional_properties = d
        return surface_area

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


TB = TypeVar("TB", bound="get_sketch_mode_plane")


@attr.s(auto_attribs=True)
class get_sketch_mode_plane:
    """Get the plane of the sketch mode. This is useful for getting the normal of the plane after a user selects a plane."""  # noqa: E501

    type: str = "get_sketch_mode_plane"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[TB], src_dict: Dict[str, Any]) -> TB:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        get_sketch_mode_plane = cls(
            type=type,
        )

        get_sketch_mode_plane.additional_properties = d
        return get_sketch_mode_plane

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


FJ = TypeVar("FJ", bound="curve_set_constraint")


@attr.s(auto_attribs=True)
class curve_set_constraint:
    """Constrain a curve."""  # noqa: E501

    constraint_bound: Union[Unset, PathComponentConstraintBound] = UNSET
    constraint_type: Union[Unset, PathComponentConstraintType] = UNSET
    object_id: Union[Unset, str] = UNSET
    type: str = "curve_set_constraint"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.constraint_bound, Unset):
            constraint_bound = self.constraint_bound
        if not isinstance(self.constraint_type, Unset):
            constraint_type = self.constraint_type
        object_id = self.object_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if constraint_bound is not UNSET:
            field_dict["constraint_bound"] = constraint_bound
        if constraint_type is not UNSET:
            field_dict["constraint_type"] = constraint_type
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[FJ], src_dict: Dict[str, Any]) -> FJ:
        d = src_dict.copy()
        _constraint_bound = d.pop("constraint_bound", UNSET)
        constraint_bound: Union[Unset, PathComponentConstraintBound]
        if isinstance(_constraint_bound, Unset):
            constraint_bound = UNSET
        else:
            constraint_bound = _constraint_bound  # type: ignore[arg-type]

        _constraint_type = d.pop("constraint_type", UNSET)
        constraint_type: Union[Unset, PathComponentConstraintType]
        if isinstance(_constraint_type, Unset):
            constraint_type = UNSET
        else:
            constraint_type = _constraint_type  # type: ignore[arg-type]

        object_id = d.pop("object_id", UNSET)

        type = d.pop("type", UNSET)

        curve_set_constraint = cls(
            constraint_bound=constraint_bound,
            constraint_type=constraint_type,
            object_id=object_id,
            type=type,
        )

        curve_set_constraint.additional_properties = d
        return curve_set_constraint

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

    def to_dict(self) -> Dict[str, Any]:
        if isinstance(self.type, start_path):
            HB: start_path = self.type
            return HB.to_dict()
        elif isinstance(self.type, move_path_pen):
            DU: move_path_pen = self.type
            return DU.to_dict()
        elif isinstance(self.type, extend_path):
            TY: extend_path = self.type
            return TY.to_dict()
        elif isinstance(self.type, extrude):
            GP: extrude = self.type
            return GP.to_dict()
        elif isinstance(self.type, close_path):
            YO: close_path = self.type
            return YO.to_dict()
        elif isinstance(self.type, camera_drag_start):
            WN: camera_drag_start = self.type
            return WN.to_dict()
        elif isinstance(self.type, camera_drag_move):
            UW: camera_drag_move = self.type
            return UW.to_dict()
        elif isinstance(self.type, camera_drag_end):
            HD: camera_drag_end = self.type
            return HD.to_dict()
        elif isinstance(self.type, default_camera_look_at):
            RU: default_camera_look_at = self.type
            return RU.to_dict()
        elif isinstance(self.type, default_camera_zoom):
            QT: default_camera_zoom = self.type
            return QT.to_dict()
        elif isinstance(self.type, default_camera_enable_sketch_mode):
            HR: default_camera_enable_sketch_mode = self.type
            return HR.to_dict()
        elif isinstance(self.type, default_camera_disable_sketch_mode):
            VM: default_camera_disable_sketch_mode = self.type
            return VM.to_dict()
        elif isinstance(self.type, default_camera_focus_on):
            DQ: default_camera_focus_on = self.type
            return DQ.to_dict()
        elif isinstance(self.type, export):
            PD: export = self.type
            return PD.to_dict()
        elif isinstance(self.type, entity_get_parent_id):
            JL: entity_get_parent_id = self.type
            return JL.to_dict()
        elif isinstance(self.type, entity_get_num_children):
            QA: entity_get_num_children = self.type
            return QA.to_dict()
        elif isinstance(self.type, entity_get_child_uuid):
            AU: entity_get_child_uuid = self.type
            return AU.to_dict()
        elif isinstance(self.type, entity_get_all_child_uuids):
            BL: entity_get_all_child_uuids = self.type
            return BL.to_dict()
        elif isinstance(self.type, edit_mode_enter):
            PZ: edit_mode_enter = self.type
            return PZ.to_dict()
        elif isinstance(self.type, edit_mode_exit):
            GE: edit_mode_exit = self.type
            return GE.to_dict()
        elif isinstance(self.type, select_with_point):
            HH: select_with_point = self.type
            return HH.to_dict()
        elif isinstance(self.type, select_clear):
            AE: select_clear = self.type
            return AE.to_dict()
        elif isinstance(self.type, select_add):
            AB: select_add = self.type
            return AB.to_dict()
        elif isinstance(self.type, select_remove):
            DW: select_remove = self.type
            return DW.to_dict()
        elif isinstance(self.type, select_replace):
            AV: select_replace = self.type
            return AV.to_dict()
        elif isinstance(self.type, select_get):
            WM: select_get = self.type
            return WM.to_dict()
        elif isinstance(self.type, highlight_set_entity):
            MU: highlight_set_entity = self.type
            return MU.to_dict()
        elif isinstance(self.type, highlight_set_entities):
            WW: highlight_set_entities = self.type
            return WW.to_dict()
        elif isinstance(self.type, new_annotation):
            II: new_annotation = self.type
            return II.to_dict()
        elif isinstance(self.type, update_annotation):
            OA: update_annotation = self.type
            return OA.to_dict()
        elif isinstance(self.type, object_visible):
            CQ: object_visible = self.type
            return CQ.to_dict()
        elif isinstance(self.type, object_bring_to_front):
            RD: object_bring_to_front = self.type
            return RD.to_dict()
        elif isinstance(self.type, get_entity_type):
            KZ: get_entity_type = self.type
            return KZ.to_dict()
        elif isinstance(self.type, solid2d_add_hole):
            IU: solid2d_add_hole = self.type
            return IU.to_dict()
        elif isinstance(self.type, solid3d_get_all_edge_faces):
            NQ: solid3d_get_all_edge_faces = self.type
            return NQ.to_dict()
        elif isinstance(self.type, solid3d_get_all_opposite_edges):
            BU: solid3d_get_all_opposite_edges = self.type
            return BU.to_dict()
        elif isinstance(self.type, solid3d_get_opposite_edge):
            GR: solid3d_get_opposite_edge = self.type
            return GR.to_dict()
        elif isinstance(self.type, solid3d_get_next_adjacent_edge):
            EJ: solid3d_get_next_adjacent_edge = self.type
            return EJ.to_dict()
        elif isinstance(self.type, solid3d_get_prev_adjacent_edge):
            LQ: solid3d_get_prev_adjacent_edge = self.type
            return LQ.to_dict()
        elif isinstance(self.type, send_object):
            DP: send_object = self.type
            return DP.to_dict()
        elif isinstance(self.type, entity_set_opacity):
            OF: entity_set_opacity = self.type
            return OF.to_dict()
        elif isinstance(self.type, entity_fade):
            OV: entity_fade = self.type
            return OV.to_dict()
        elif isinstance(self.type, make_plane):
            FK: make_plane = self.type
            return FK.to_dict()
        elif isinstance(self.type, plane_set_color):
            PE: plane_set_color = self.type
            return PE.to_dict()
        elif isinstance(self.type, set_tool):
            FP: set_tool = self.type
            return FP.to_dict()
        elif isinstance(self.type, mouse_move):
            QL: mouse_move = self.type
            return QL.to_dict()
        elif isinstance(self.type, mouse_click):
            ME: mouse_click = self.type
            return ME.to_dict()
        elif isinstance(self.type, sketch_mode_enable):
            EB: sketch_mode_enable = self.type
            return EB.to_dict()
        elif isinstance(self.type, sketch_mode_disable):
            VK: sketch_mode_disable = self.type
            return VK.to_dict()
        elif isinstance(self.type, curve_get_type):
            ZC: curve_get_type = self.type
            return ZC.to_dict()
        elif isinstance(self.type, curve_get_control_points):
            BE: curve_get_control_points = self.type
            return BE.to_dict()
        elif isinstance(self.type, take_snapshot):
            CD: take_snapshot = self.type
            return CD.to_dict()
        elif isinstance(self.type, make_axes_gizmo):
            ZO: make_axes_gizmo = self.type
            return ZO.to_dict()
        elif isinstance(self.type, path_get_info):
            EY: path_get_info = self.type
            return EY.to_dict()
        elif isinstance(self.type, path_get_curve_uuids_for_vertices):
            RW: path_get_curve_uuids_for_vertices = self.type
            return RW.to_dict()
        elif isinstance(self.type, path_get_vertex_uuids):
            GQ: path_get_vertex_uuids = self.type
            return GQ.to_dict()
        elif isinstance(self.type, handle_mouse_drag_start):
            GC: handle_mouse_drag_start = self.type
            return GC.to_dict()
        elif isinstance(self.type, handle_mouse_drag_move):
            XE: handle_mouse_drag_move = self.type
            return XE.to_dict()
        elif isinstance(self.type, handle_mouse_drag_end):
            RE: handle_mouse_drag_end = self.type
            return RE.to_dict()
        elif isinstance(self.type, remove_scene_objects):
            MO: remove_scene_objects = self.type
            return MO.to_dict()
        elif isinstance(self.type, plane_intersect_and_project):
            FL: plane_intersect_and_project = self.type
            return FL.to_dict()
        elif isinstance(self.type, curve_get_end_points):
            KJ: curve_get_end_points = self.type
            return KJ.to_dict()
        elif isinstance(self.type, reconfigure_stream):
            PN: reconfigure_stream = self.type
            return PN.to_dict()
        elif isinstance(self.type, import_files):
            QY: import_files = self.type
            return QY.to_dict()
        elif isinstance(self.type, mass):
            RC: mass = self.type
            return RC.to_dict()
        elif isinstance(self.type, density):
            XR: density = self.type
            return XR.to_dict()
        elif isinstance(self.type, volume):
            ND: volume = self.type
            return ND.to_dict()
        elif isinstance(self.type, center_of_mass):
            PH: center_of_mass = self.type
            return PH.to_dict()
        elif isinstance(self.type, surface_area):
            OO: surface_area = self.type
            return OO.to_dict()
        elif isinstance(self.type, get_sketch_mode_plane):
            HP: get_sketch_mode_plane = self.type
            return HP.to_dict()
        elif isinstance(self.type, curve_set_constraint):
            RL: curve_set_constraint = self.type
            return RL.to_dict()

        raise Exception("Unknown type")

    @classmethod
    def from_dict(cls: Type[GY], d: Dict[str, Any]) -> GY:
        if d.get("type") == "start_path":
            SF: start_path = start_path()
            SF.from_dict(d)
            return cls(type=SF)
        elif d.get("type") == "move_path_pen":
            BM: move_path_pen = move_path_pen()
            BM.from_dict(d)
            return cls(type=BM)
        elif d.get("type") == "extend_path":
            NC: extend_path = extend_path()
            NC.from_dict(d)
            return cls(type=NC)
        elif d.get("type") == "extrude":
            FF: extrude = extrude()
            FF.from_dict(d)
            return cls(type=FF)
        elif d.get("type") == "close_path":
            FS: close_path = close_path()
            FS.from_dict(d)
            return cls(type=FS)
        elif d.get("type") == "camera_drag_start":
            EQ: camera_drag_start = camera_drag_start()
            EQ.from_dict(d)
            return cls(type=EQ)
        elif d.get("type") == "camera_drag_move":
            MD: camera_drag_move = camera_drag_move()
            MD.from_dict(d)
            return cls(type=MD)
        elif d.get("type") == "camera_drag_end":
            UJ: camera_drag_end = camera_drag_end()
            UJ.from_dict(d)
            return cls(type=UJ)
        elif d.get("type") == "default_camera_look_at":
            DL: default_camera_look_at = default_camera_look_at()
            DL.from_dict(d)
            return cls(type=DL)
        elif d.get("type") == "default_camera_zoom":
            PT: default_camera_zoom = default_camera_zoom()
            PT.from_dict(d)
            return cls(type=PT)
        elif d.get("type") == "default_camera_enable_sketch_mode":
            VF: default_camera_enable_sketch_mode = default_camera_enable_sketch_mode()
            VF.from_dict(d)
            return cls(type=VF)
        elif d.get("type") == "default_camera_disable_sketch_mode":
            WH: default_camera_disable_sketch_mode = (
                default_camera_disable_sketch_mode()
            )
            WH.from_dict(d)
            return cls(type=WH)
        elif d.get("type") == "default_camera_focus_on":
            UY: default_camera_focus_on = default_camera_focus_on()
            UY.from_dict(d)
            return cls(type=UY)
        elif d.get("type") == "export":
            SM: export = export()
            SM.from_dict(d)
            return cls(type=SM)
        elif d.get("type") == "entity_get_parent_id":
            CG: entity_get_parent_id = entity_get_parent_id()
            CG.from_dict(d)
            return cls(type=CG)
        elif d.get("type") == "entity_get_num_children":
            ZB: entity_get_num_children = entity_get_num_children()
            ZB.from_dict(d)
            return cls(type=ZB)
        elif d.get("type") == "entity_get_child_uuid":
            FX: entity_get_child_uuid = entity_get_child_uuid()
            FX.from_dict(d)
            return cls(type=FX)
        elif d.get("type") == "entity_get_all_child_uuids":
            KU: entity_get_all_child_uuids = entity_get_all_child_uuids()
            KU.from_dict(d)
            return cls(type=KU)
        elif d.get("type") == "edit_mode_enter":
            FA: edit_mode_enter = edit_mode_enter()
            FA.from_dict(d)
            return cls(type=FA)
        elif d.get("type") == "edit_mode_exit":
            JG: edit_mode_exit = edit_mode_exit()
            JG.from_dict(d)
            return cls(type=JG)
        elif d.get("type") == "select_with_point":
            RY: select_with_point = select_with_point()
            RY.from_dict(d)
            return cls(type=RY)
        elif d.get("type") == "select_clear":
            AD: select_clear = select_clear()
            AD.from_dict(d)
            return cls(type=AD)
        elif d.get("type") == "select_add":
            VY: select_add = select_add()
            VY.from_dict(d)
            return cls(type=VY)
        elif d.get("type") == "select_remove":
            MC: select_remove = select_remove()
            MC.from_dict(d)
            return cls(type=MC)
        elif d.get("type") == "select_replace":
            BR: select_replace = select_replace()
            BR.from_dict(d)
            return cls(type=BR)
        elif d.get("type") == "select_get":
            OK: select_get = select_get()
            OK.from_dict(d)
            return cls(type=OK)
        elif d.get("type") == "highlight_set_entity":
            OP: highlight_set_entity = highlight_set_entity()
            OP.from_dict(d)
            return cls(type=OP)
        elif d.get("type") == "highlight_set_entities":
            LV: highlight_set_entities = highlight_set_entities()
            LV.from_dict(d)
            return cls(type=LV)
        elif d.get("type") == "new_annotation":
            FC: new_annotation = new_annotation()
            FC.from_dict(d)
            return cls(type=FC)
        elif d.get("type") == "update_annotation":
            EI: update_annotation = update_annotation()
            EI.from_dict(d)
            return cls(type=EI)
        elif d.get("type") == "object_visible":
            JE: object_visible = object_visible()
            JE.from_dict(d)
            return cls(type=JE)
        elif d.get("type") == "object_bring_to_front":
            JW: object_bring_to_front = object_bring_to_front()
            JW.from_dict(d)
            return cls(type=JW)
        elif d.get("type") == "get_entity_type":
            AS: get_entity_type = get_entity_type()
            AS.from_dict(d)
            return cls(type=AS)
        elif d.get("type") == "solid2d_add_hole":
            YQ: solid2d_add_hole = solid2d_add_hole()
            YQ.from_dict(d)
            return cls(type=YQ)
        elif d.get("type") == "solid3d_get_all_edge_faces":
            EW: solid3d_get_all_edge_faces = solid3d_get_all_edge_faces()
            EW.from_dict(d)
            return cls(type=EW)
        elif d.get("type") == "solid3d_get_all_opposite_edges":
            BT: solid3d_get_all_opposite_edges = solid3d_get_all_opposite_edges()
            BT.from_dict(d)
            return cls(type=BT)
        elif d.get("type") == "solid3d_get_opposite_edge":
            AG: solid3d_get_opposite_edge = solid3d_get_opposite_edge()
            AG.from_dict(d)
            return cls(type=AG)
        elif d.get("type") == "solid3d_get_next_adjacent_edge":
            EA: solid3d_get_next_adjacent_edge = solid3d_get_next_adjacent_edge()
            EA.from_dict(d)
            return cls(type=EA)
        elif d.get("type") == "solid3d_get_prev_adjacent_edge":
            VW: solid3d_get_prev_adjacent_edge = solid3d_get_prev_adjacent_edge()
            VW.from_dict(d)
            return cls(type=VW)
        elif d.get("type") == "send_object":
            JO: send_object = send_object()
            JO.from_dict(d)
            return cls(type=JO)
        elif d.get("type") == "entity_set_opacity":
            TE: entity_set_opacity = entity_set_opacity()
            TE.from_dict(d)
            return cls(type=TE)
        elif d.get("type") == "entity_fade":
            WY: entity_fade = entity_fade()
            WY.from_dict(d)
            return cls(type=WY)
        elif d.get("type") == "make_plane":
            QV: make_plane = make_plane()
            QV.from_dict(d)
            return cls(type=QV)
        elif d.get("type") == "plane_set_color":
            BP: plane_set_color = plane_set_color()
            BP.from_dict(d)
            return cls(type=BP)
        elif d.get("type") == "set_tool":
            WI: set_tool = set_tool()
            WI.from_dict(d)
            return cls(type=WI)
        elif d.get("type") == "mouse_move":
            YR: mouse_move = mouse_move()
            YR.from_dict(d)
            return cls(type=YR)
        elif d.get("type") == "mouse_click":
            XK: mouse_click = mouse_click()
            XK.from_dict(d)
            return cls(type=XK)
        elif d.get("type") == "sketch_mode_enable":
            OB: sketch_mode_enable = sketch_mode_enable()
            OB.from_dict(d)
            return cls(type=OB)
        elif d.get("type") == "sketch_mode_disable":
            QQ: sketch_mode_disable = sketch_mode_disable()
            QQ.from_dict(d)
            return cls(type=QQ)
        elif d.get("type") == "curve_get_type":
            WX: curve_get_type = curve_get_type()
            WX.from_dict(d)
            return cls(type=WX)
        elif d.get("type") == "curve_get_control_points":
            HV: curve_get_control_points = curve_get_control_points()
            HV.from_dict(d)
            return cls(type=HV)
        elif d.get("type") == "take_snapshot":
            CL: take_snapshot = take_snapshot()
            CL.from_dict(d)
            return cls(type=CL)
        elif d.get("type") == "make_axes_gizmo":
            NJ: make_axes_gizmo = make_axes_gizmo()
            NJ.from_dict(d)
            return cls(type=NJ)
        elif d.get("type") == "path_get_info":
            UM: path_get_info = path_get_info()
            UM.from_dict(d)
            return cls(type=UM)
        elif d.get("type") == "path_get_curve_uuids_for_vertices":
            EM: path_get_curve_uuids_for_vertices = path_get_curve_uuids_for_vertices()
            EM.from_dict(d)
            return cls(type=EM)
        elif d.get("type") == "path_get_vertex_uuids":
            VV: path_get_vertex_uuids = path_get_vertex_uuids()
            VV.from_dict(d)
            return cls(type=VV)
        elif d.get("type") == "handle_mouse_drag_start":
            RX: handle_mouse_drag_start = handle_mouse_drag_start()
            RX.from_dict(d)
            return cls(type=RX)
        elif d.get("type") == "handle_mouse_drag_move":
            TS: handle_mouse_drag_move = handle_mouse_drag_move()
            TS.from_dict(d)
            return cls(type=TS)
        elif d.get("type") == "handle_mouse_drag_end":
            CV: handle_mouse_drag_end = handle_mouse_drag_end()
            CV.from_dict(d)
            return cls(type=CV)
        elif d.get("type") == "remove_scene_objects":
            AO: remove_scene_objects = remove_scene_objects()
            AO.from_dict(d)
            return cls(type=AO)
        elif d.get("type") == "plane_intersect_and_project":
            GH: plane_intersect_and_project = plane_intersect_and_project()
            GH.from_dict(d)
            return cls(type=GH)
        elif d.get("type") == "curve_get_end_points":
            SI: curve_get_end_points = curve_get_end_points()
            SI.from_dict(d)
            return cls(type=SI)
        elif d.get("type") == "reconfigure_stream":
            AK: reconfigure_stream = reconfigure_stream()
            AK.from_dict(d)
            return cls(type=AK)
        elif d.get("type") == "import_files":
            BN: import_files = import_files()
            BN.from_dict(d)
            return cls(type=BN)
        elif d.get("type") == "mass":
            AQ: mass = mass()
            AQ.from_dict(d)
            return cls(type=AQ)
        elif d.get("type") == "density":
            IS: density = density()
            IS.from_dict(d)
            return cls(type=IS)
        elif d.get("type") == "volume":
            YN: volume = volume()
            YN.from_dict(d)
            return cls(type=YN)
        elif d.get("type") == "center_of_mass":
            MA: center_of_mass = center_of_mass()
            MA.from_dict(d)
            return cls(type=MA)
        elif d.get("type") == "surface_area":
            VE: surface_area = surface_area()
            VE.from_dict(d)
            return cls(type=VE)
        elif d.get("type") == "get_sketch_mode_plane":
            JX: get_sketch_mode_plane = get_sketch_mode_plane()
            JX.from_dict(d)
            return cls(type=JX)
        elif d.get("type") == "curve_set_constraint":
            HL: curve_set_constraint = curve_set_constraint()
            HL.from_dict(d)
            return cls(type=HL)

        raise Exception("Unknown type")
