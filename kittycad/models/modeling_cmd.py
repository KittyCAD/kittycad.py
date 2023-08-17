from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.annotation_options import AnnotationOptions
from ..models.annotation_type import AnnotationType
from ..models.camera_drag_interaction_type import CameraDragInteractionType
from ..models.modeling_cmd_id import ModelingCmdId
from ..models.output_format import OutputFormat
from ..models.path_segment import PathSegment
from ..models.point2d import Point2d
from ..models.point3d import Point3d
from ..models.scene_selection_type import SceneSelectionType
from ..types import UNSET, Unset

MP = TypeVar("MP", bound="start_path")


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
    def from_dict(cls: Type[MP], src_dict: Dict[str, Any]) -> MP:
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


WF = TypeVar("WF", bound="move_path_pen")


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
            field_dict["to"] = to
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[WF], src_dict: Dict[str, Any]) -> WF:
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


RO = TypeVar("RO", bound="extend_path")


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
            field_dict["segment"] = segment
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[RO], src_dict: Dict[str, Any]) -> RO:
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


DN = TypeVar("DN", bound="extrude")


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
    def from_dict(cls: Type[DN], src_dict: Dict[str, Any]) -> DN:
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


BA = TypeVar("BA", bound="close_path")


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
    def from_dict(cls: Type[BA], src_dict: Dict[str, Any]) -> BA:
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


OR = TypeVar("OR", bound="camera_drag_start")


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
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: Type[OR], src_dict: Dict[str, Any]) -> OR:
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


CB = TypeVar("CB", bound="camera_drag_move")


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
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: Type[CB], src_dict: Dict[str, Any]) -> CB:
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


LC = TypeVar("LC", bound="camera_drag_end")


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
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: Type[LC], src_dict: Dict[str, Any]) -> LC:
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


TO = TypeVar("TO", bound="default_camera_look_at")


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
            field_dict["center"] = center
        field_dict["type"] = type
        if up is not UNSET:
            field_dict["up"] = up
        if vantage is not UNSET:
            field_dict["vantage"] = vantage

        return field_dict

    @classmethod
    def from_dict(cls: Type[TO], src_dict: Dict[str, Any]) -> TO:
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


ZP = TypeVar("ZP", bound="default_camera_enable_sketch_mode")


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
            field_dict["origin"] = origin
        if ortho is not UNSET:
            field_dict["ortho"] = ortho
        field_dict["type"] = type
        if x_axis is not UNSET:
            field_dict["x_axis"] = x_axis
        if y_axis is not UNSET:
            field_dict["y_axis"] = y_axis

        return field_dict

    @classmethod
    def from_dict(cls: Type[ZP], src_dict: Dict[str, Any]) -> ZP:
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


EO = TypeVar("EO", bound="default_camera_disable_sketch_mode")


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
    def from_dict(cls: Type[EO], src_dict: Dict[str, Any]) -> EO:
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


NY = TypeVar("NY", bound="export")


@attr.s(auto_attribs=True)
class export:
    """Export the scene to a file."""  # noqa: E501

    entity_ids: Union[Unset, List[str]] = UNSET
    format: Union[Unset, OutputFormat] = UNSET
    type: str = "export"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.entity_ids, Unset):
            entity_ids = self.entity_ids
        if not isinstance(self.format, Unset):
            format = self.format
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_ids is not UNSET:
            field_dict["entity_ids"] = entity_ids
        if format is not UNSET:
            field_dict["format"] = format
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[NY], src_dict: Dict[str, Any]) -> NY:
        d = src_dict.copy()
        entity_ids = cast(List[str], d.pop("entity_ids", UNSET))

        _format = d.pop("format", UNSET)
        format: Union[Unset, OutputFormat]
        if isinstance(_format, Unset):
            format = UNSET
        else:
            format = _format  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        export = cls(
            entity_ids=entity_ids,
            format=format,
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


QO = TypeVar("QO", bound="entity_get_parent_id")


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
    def from_dict(cls: Type[QO], src_dict: Dict[str, Any]) -> QO:
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


KX = TypeVar("KX", bound="entity_get_num_children")


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
    def from_dict(cls: Type[KX], src_dict: Dict[str, Any]) -> KX:
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


IZ = TypeVar("IZ", bound="entity_get_child_uuid")


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
    def from_dict(cls: Type[IZ], src_dict: Dict[str, Any]) -> IZ:
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


WO = TypeVar("WO", bound="entity_get_all_child_uuids")


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
    def from_dict(cls: Type[WO], src_dict: Dict[str, Any]) -> WO:
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


NK = TypeVar("NK", bound="edit_mode_enter")


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
    def from_dict(cls: Type[NK], src_dict: Dict[str, Any]) -> NK:
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


UQ = TypeVar("UQ", bound="edit_mode_exit")


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
    def from_dict(cls: Type[UQ], src_dict: Dict[str, Any]) -> UQ:
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


QE = TypeVar("QE", bound="select_with_point")


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
            field_dict["selected_at_window"] = selected_at_window
        if selection_type is not UNSET:
            field_dict["selection_type"] = selection_type
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[QE], src_dict: Dict[str, Any]) -> QE:
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


XH = TypeVar("XH", bound="select_clear")


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
    def from_dict(cls: Type[XH], src_dict: Dict[str, Any]) -> XH:
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


KT = TypeVar("KT", bound="select_add")


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
    def from_dict(cls: Type[KT], src_dict: Dict[str, Any]) -> KT:
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


BV = TypeVar("BV", bound="select_remove")


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
    def from_dict(cls: Type[BV], src_dict: Dict[str, Any]) -> BV:
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


GU = TypeVar("GU", bound="select_replace")


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
    def from_dict(cls: Type[GU], src_dict: Dict[str, Any]) -> GU:
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


SS = TypeVar("SS", bound="select_get")


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
    def from_dict(cls: Type[SS], src_dict: Dict[str, Any]) -> SS:
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


UP = TypeVar("UP", bound="highlight_set_entity")


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
            field_dict["selected_at_window"] = selected_at_window
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[UP], src_dict: Dict[str, Any]) -> UP:
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


AZ = TypeVar("AZ", bound="highlight_set_entities")


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
    def from_dict(cls: Type[AZ], src_dict: Dict[str, Any]) -> AZ:
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


DJ = TypeVar("DJ", bound="new_annotation")


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
            field_dict["options"] = options
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[DJ], src_dict: Dict[str, Any]) -> DJ:
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


WJ = TypeVar("WJ", bound="update_annotation")


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
            field_dict["options"] = options
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[WJ], src_dict: Dict[str, Any]) -> WJ:
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


TR = TypeVar("TR", bound="object_visible")


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
    def from_dict(cls: Type[TR], src_dict: Dict[str, Any]) -> TR:
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


YD = TypeVar("YD", bound="get_entity_type")


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
    def from_dict(cls: Type[YD], src_dict: Dict[str, Any]) -> YD:
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


JF = TypeVar("JF", bound="solid3d_get_all_edge_faces")


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
    def from_dict(cls: Type[JF], src_dict: Dict[str, Any]) -> JF:
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


VP = TypeVar("VP", bound="solid3d_get_all_opposite_edges")


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
            field_dict["along_vector"] = along_vector
        if edge_id is not UNSET:
            field_dict["edge_id"] = edge_id
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[VP], src_dict: Dict[str, Any]) -> VP:
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


EL = TypeVar("EL", bound="solid3d_get_opposite_edge")


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
    def from_dict(cls: Type[EL], src_dict: Dict[str, Any]) -> EL:
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


ZG = TypeVar("ZG", bound="solid3d_get_next_adjacent_edge")


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
    def from_dict(cls: Type[ZG], src_dict: Dict[str, Any]) -> ZG:
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


LF = TypeVar("LF", bound="solid3d_get_prev_adjacent_edge")


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
    def from_dict(cls: Type[LF], src_dict: Dict[str, Any]) -> LF:
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


ModelingCmd = Union[
    start_path,
    move_path_pen,
    extend_path,
    extrude,
    close_path,
    camera_drag_start,
    camera_drag_move,
    camera_drag_end,
    default_camera_look_at,
    default_camera_enable_sketch_mode,
    default_camera_disable_sketch_mode,
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
    get_entity_type,
    solid3d_get_all_edge_faces,
    solid3d_get_all_opposite_edges,
    solid3d_get_opposite_edge,
    solid3d_get_next_adjacent_edge,
    solid3d_get_prev_adjacent_edge,
]
