from enum import Enum
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.camera_drag_interaction_type import CameraDragInteractionType
from ..models.modeling_cmd_id import ModelingCmdId
from ..models.output_format import OutputFormat
from ..models.path_segment import PathSegment
from ..models.point2d import Point2d
from ..models.point3d import Point3d
from ..types import UNSET, Unset
from .extrude import Extrude


class StartPath(str, Enum):
    """Start a path."""  # noqa: E501

    START_PATH = "StartPath"

    def __str__(self) -> str:
        return str(self.value)


B = TypeVar("B", bound="MovePathPen")


@attr.s(auto_attribs=True)
class MovePathPen:
    path: Union[Unset, ModelingCmdId] = UNSET
    to: Union[Unset, Point3d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.path, Unset):
            path = self.path
        if not isinstance(self.to, Unset):
            to = self.to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: Type[B], src_dict: Dict[str, Any]) -> B:
        d = src_dict.copy()
        _path = d.pop("path", UNSET)
        path: Union[Unset, ModelingCmdId]
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = ModelingCmdId(_path)

        _to = d.pop("to", UNSET)
        to: Union[Unset, Point3d]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = Point3d(_to)

        move_path_pen = cls(
            path=path,
            to=to,
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


P = TypeVar("P", bound="ExtendPath")


@attr.s(auto_attribs=True)
class ExtendPath:
    path: Union[Unset, ModelingCmdId] = UNSET
    segment: Union[Unset, PathSegment] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.path, Unset):
            path = self.path
        if not isinstance(self.segment, Unset):
            segment = self.segment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if segment is not UNSET:
            field_dict["segment"] = segment

        return field_dict

    @classmethod
    def from_dict(cls: Type[P], src_dict: Dict[str, Any]) -> P:
        d = src_dict.copy()
        _path = d.pop("path", UNSET)
        path: Union[Unset, ModelingCmdId]
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = ModelingCmdId(_path)

        _segment = d.pop("segment", UNSET)
        segment: Union[Unset, PathSegment]
        if isinstance(_segment, Unset):
            segment = UNSET
        else:
            segment = _segment  # type: ignore[arg-type]

        extend_path = cls(
            path=path,
            segment=segment,
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


J = TypeVar("J", bound="ClosePath")


@attr.s(auto_attribs=True)
class ClosePath:
    path_id: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path_id = self.path_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path_id is not UNSET:
            field_dict["path_id"] = path_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[J], src_dict: Dict[str, Any]) -> J:
        d = src_dict.copy()
        path_id = d.pop("path_id", UNSET)

        close_path = cls(
            path_id=path_id,
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


T = TypeVar("T", bound="CameraDragStart")


@attr.s(auto_attribs=True)
class CameraDragStart:
    interaction: Union[Unset, CameraDragInteractionType] = UNSET
    window: Union[Unset, Point2d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.interaction, Unset):
            interaction = self.interaction
        if not isinstance(self.window, Unset):
            window = self.window

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interaction is not UNSET:
            field_dict["interaction"] = interaction
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _interaction = d.pop("interaction", UNSET)
        interaction: Union[Unset, CameraDragInteractionType]
        if isinstance(_interaction, Unset):
            interaction = UNSET
        else:
            interaction = _interaction  # type: ignore[arg-type]

        _window = d.pop("window", UNSET)
        window: Union[Unset, Point2d]
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = Point2d(_window)

        camera_drag_start = cls(
            interaction=interaction,
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


V = TypeVar("V", bound="CameraDragMove")


@attr.s(auto_attribs=True)
class CameraDragMove:
    interaction: Union[Unset, CameraDragInteractionType] = UNSET
    sequence: Union[Unset, int] = UNSET
    window: Union[Unset, Point2d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.interaction, Unset):
            interaction = self.interaction
        sequence = self.sequence
        if not isinstance(self.window, Unset):
            window = self.window

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interaction is not UNSET:
            field_dict["interaction"] = interaction
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: Type[V], src_dict: Dict[str, Any]) -> V:
        d = src_dict.copy()
        _interaction = d.pop("interaction", UNSET)
        interaction: Union[Unset, CameraDragInteractionType]
        if isinstance(_interaction, Unset):
            interaction = UNSET
        else:
            interaction = _interaction  # type: ignore[arg-type]

        sequence = d.pop("sequence", UNSET)

        _window = d.pop("window", UNSET)
        window: Union[Unset, Point2d]
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = Point2d(_window)

        camera_drag_move = cls(
            interaction=interaction,
            sequence=sequence,
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


C = TypeVar("C", bound="CameraDragEnd")


@attr.s(auto_attribs=True)
class CameraDragEnd:
    interaction: Union[Unset, CameraDragInteractionType] = UNSET
    window: Union[Unset, Point2d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.interaction, Unset):
            interaction = self.interaction
        if not isinstance(self.window, Unset):
            window = self.window

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interaction is not UNSET:
            field_dict["interaction"] = interaction
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: Type[C], src_dict: Dict[str, Any]) -> C:
        d = src_dict.copy()
        _interaction = d.pop("interaction", UNSET)
        interaction: Union[Unset, CameraDragInteractionType]
        if isinstance(_interaction, Unset):
            interaction = UNSET
        else:
            interaction = _interaction  # type: ignore[arg-type]

        _window = d.pop("window", UNSET)
        window: Union[Unset, Point2d]
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = Point2d(_window)

        camera_drag_end = cls(
            interaction=interaction,
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


R = TypeVar("R", bound="DefaultCameraLookAt")


@attr.s(auto_attribs=True)
class DefaultCameraLookAt:
    center: Union[Unset, Point3d] = UNSET
    up: Union[Unset, Point3d] = UNSET
    vantage: Union[Unset, Point3d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.center, Unset):
            center = self.center
        if not isinstance(self.up, Unset):
            up = self.up
        if not isinstance(self.vantage, Unset):
            vantage = self.vantage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if center is not UNSET:
            field_dict["center"] = center
        if up is not UNSET:
            field_dict["up"] = up
        if vantage is not UNSET:
            field_dict["vantage"] = vantage

        return field_dict

    @classmethod
    def from_dict(cls: Type[R], src_dict: Dict[str, Any]) -> R:
        d = src_dict.copy()
        _center = d.pop("center", UNSET)
        center: Union[Unset, Point3d]
        if isinstance(_center, Unset):
            center = UNSET
        else:
            center = Point3d(_center)

        _up = d.pop("up", UNSET)
        up: Union[Unset, Point3d]
        if isinstance(_up, Unset):
            up = UNSET
        else:
            up = Point3d(_up)

        _vantage = d.pop("vantage", UNSET)
        vantage: Union[Unset, Point3d]
        if isinstance(_vantage, Unset):
            vantage = UNSET
        else:
            vantage = Point3d(_vantage)

        default_camera_look_at = cls(
            center=center,
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


C = TypeVar("C", bound="DefaultCameraEnableSketchMode")


@attr.s(auto_attribs=True)
class DefaultCameraEnableSketchMode:
    distance_to_plane: Union[Unset, float] = UNSET
    origin: Union[Unset, Point3d] = UNSET
    ortho: Union[Unset, bool] = False
    x_axis: Union[Unset, Point3d] = UNSET
    y_axis: Union[Unset, Point3d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        distance_to_plane = self.distance_to_plane
        if not isinstance(self.origin, Unset):
            origin = self.origin
        ortho = self.ortho
        if not isinstance(self.x_axis, Unset):
            x_axis = self.x_axis
        if not isinstance(self.y_axis, Unset):
            y_axis = self.y_axis

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if distance_to_plane is not UNSET:
            field_dict["distance_to_plane"] = distance_to_plane
        if origin is not UNSET:
            field_dict["origin"] = origin
        if ortho is not UNSET:
            field_dict["ortho"] = ortho
        if x_axis is not UNSET:
            field_dict["x_axis"] = x_axis
        if y_axis is not UNSET:
            field_dict["y_axis"] = y_axis

        return field_dict

    @classmethod
    def from_dict(cls: Type[C], src_dict: Dict[str, Any]) -> C:
        d = src_dict.copy()
        distance_to_plane = d.pop("distance_to_plane", UNSET)

        _origin = d.pop("origin", UNSET)
        origin: Union[Unset, Point3d]
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = Point3d(_origin)

        ortho = d.pop("ortho", UNSET)

        _x_axis = d.pop("x_axis", UNSET)
        x_axis: Union[Unset, Point3d]
        if isinstance(_x_axis, Unset):
            x_axis = UNSET
        else:
            x_axis = Point3d(_x_axis)

        _y_axis = d.pop("y_axis", UNSET)
        y_axis: Union[Unset, Point3d]
        if isinstance(_y_axis, Unset):
            y_axis = UNSET
        else:
            y_axis = Point3d(_y_axis)

        default_camera_enable_sketch_mode = cls(
            distance_to_plane=distance_to_plane,
            origin=origin,
            ortho=ortho,
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


class DefaultCameraDisableSketchMode(str, Enum):
    """Disable sketch mode, from the default camera."""  # noqa: E501

    DEFAULT_CAMERA_DISABLE_SKETCH_MODE = "DefaultCameraDisableSketchMode"

    def __str__(self) -> str:
        return str(self.value)


E = TypeVar("E", bound="Export")


@attr.s(auto_attribs=True)
class Export:
    format: Union[Unset, OutputFormat] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.format, Unset):
            format = self.format

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if format is not UNSET:
            field_dict["format"] = format

        return field_dict

    @classmethod
    def from_dict(cls: Type[E], src_dict: Dict[str, Any]) -> E:
        d = src_dict.copy()
        _format = d.pop("format", UNSET)
        format: Union[Unset, OutputFormat]
        if isinstance(_format, Unset):
            format = UNSET
        else:
            format = OutputFormat(_format)

        export = cls(
            format=format,
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


ModelingCmd = Union[
    StartPath,
    MovePathPen,
    ExtendPath,
    Extrude,
    ClosePath,
    CameraDragStart,
    CameraDragMove,
    CameraDragEnd,
    DefaultCameraLookAt,
    DefaultCameraEnableSketchMode,
    DefaultCameraDisableSketchMode,
    Export,
]
