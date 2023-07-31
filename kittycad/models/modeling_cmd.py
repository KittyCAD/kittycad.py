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


TP = TypeVar("TP", bound="MovePathPen")


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
    def from_dict(cls: Type[TP], src_dict: Dict[str, Any]) -> TP:
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


CF = TypeVar("CF", bound="ExtendPath")


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
    def from_dict(cls: Type[CF], src_dict: Dict[str, Any]) -> CF:
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


OM = TypeVar("OM", bound="ClosePath")


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
    def from_dict(cls: Type[OM], src_dict: Dict[str, Any]) -> OM:
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


EN = TypeVar("EN", bound="CameraDragStart")


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
    def from_dict(cls: Type[EN], src_dict: Dict[str, Any]) -> EN:
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
            window = _window  # type: ignore[arg-type]

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


RS = TypeVar("RS", bound="CameraDragMove")


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
    def from_dict(cls: Type[RS], src_dict: Dict[str, Any]) -> RS:
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
            window = _window  # type: ignore[arg-type]

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


LR = TypeVar("LR", bound="CameraDragEnd")


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
    def from_dict(cls: Type[LR], src_dict: Dict[str, Any]) -> LR:
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
            window = _window  # type: ignore[arg-type]

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


MP = TypeVar("MP", bound="DefaultCameraLookAt")


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
    def from_dict(cls: Type[MP], src_dict: Dict[str, Any]) -> MP:
        d = src_dict.copy()
        _center = d.pop("center", UNSET)
        center: Union[Unset, Point3d]
        if isinstance(_center, Unset):
            center = UNSET
        else:
            center = _center  # type: ignore[arg-type]

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


WF = TypeVar("WF", bound="DefaultCameraEnableSketchMode")


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
    def from_dict(cls: Type[WF], src_dict: Dict[str, Any]) -> WF:
        d = src_dict.copy()
        distance_to_plane = d.pop("distance_to_plane", UNSET)

        _origin = d.pop("origin", UNSET)
        origin: Union[Unset, Point3d]
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = _origin  # type: ignore[arg-type]

        ortho = d.pop("ortho", UNSET)

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


RO = TypeVar("RO", bound="Export")


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
    def from_dict(cls: Type[RO], src_dict: Dict[str, Any]) -> RO:
        d = src_dict.copy()
        _format = d.pop("format", UNSET)
        format: Union[Unset, OutputFormat]
        if isinstance(_format, Unset):
            format = UNSET
        else:
            format = _format  # type: ignore[arg-type]

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
