from enum import Enum
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.camera_drag_interaction_type import CameraDragInteractionType
from ..models.modeling_cmd_id import ModelingCmdId
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


B = TypeVar("B", bound="ExtendPath")


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
    def from_dict(cls: Type[B], src_dict: Dict[str, Any]) -> B:
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


P = TypeVar("P", bound="ClosePath")


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
    def from_dict(cls: Type[P], src_dict: Dict[str, Any]) -> P:
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


J = TypeVar("J", bound="CameraDragStart")


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
    def from_dict(cls: Type[J], src_dict: Dict[str, Any]) -> J:
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


T = TypeVar("T", bound="CameraDragMove")


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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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


V = TypeVar("V", bound="CameraDragEnd")


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
    def from_dict(cls: Type[V], src_dict: Dict[str, Any]) -> V:
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


ModelingCmd = Union[
    StartPath,
    MovePathPen,
    ExtendPath,
    Extrude,
    ClosePath,
    CameraDragStart,
    CameraDragMove,
    CameraDragEnd,
]
