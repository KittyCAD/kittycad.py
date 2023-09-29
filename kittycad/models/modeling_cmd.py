from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.annotation_options import AnnotationOptions
from ..models.annotation_type import AnnotationType
from ..models.camera_drag_interaction_type import CameraDragInteractionType
from ..models.color import Color
from ..models.image_format import ImageFormat
from ..models.modeling_cmd_id import ModelingCmdId
from ..models.output_format import OutputFormat
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

WO = TypeVar("WO", bound="start_path")

@attr.s(auto_attribs=True)
class start_path:
	""" Start a path. """ # noqa: E501
	type: str = "start_path"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[WO], src_dict: Dict[str, Any]) -> WO:
		d = src_dict.copy()
		type = d.pop("type", UNSET)


		start_path = cls(
			type= type,
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




NK = TypeVar("NK", bound="move_path_pen")

@attr.s(auto_attribs=True)
class move_path_pen:
	""" Move the path's "pen". """ # noqa: E501
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
			field_dict['path'] = path
		if to is not UNSET:
			field_dict['to'] = to
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[NK], src_dict: Dict[str, Any]) -> NK:
		d = src_dict.copy()
		_path = d.pop("path", UNSET)
		path: Union[Unset, ModelingCmdId]
		if isinstance(_path, Unset):
			path = UNSET
		else:
			path = _path # type: ignore[arg-type]

		_to = d.pop("to", UNSET)
		to: Union[Unset, Point3d]
		if isinstance(_to, Unset):
			to = UNSET
		else:
			to = _to # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		move_path_pen = cls(
			path= path,
			to= to,
			type= type,
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




UQ = TypeVar("UQ", bound="extend_path")

@attr.s(auto_attribs=True)
class extend_path:
	""" Extend a path by adding a new segment which starts at the path's "pen". If no "pen" location has been set before (via `MovePen`), then the pen is at the origin. """ # noqa: E501
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
			field_dict['path'] = path
		if segment is not UNSET:
			field_dict['segment'] = segment
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[UQ], src_dict: Dict[str, Any]) -> UQ:
		d = src_dict.copy()
		_path = d.pop("path", UNSET)
		path: Union[Unset, ModelingCmdId]
		if isinstance(_path, Unset):
			path = UNSET
		else:
			path = _path # type: ignore[arg-type]

		_segment = d.pop("segment", UNSET)
		segment: Union[Unset, PathSegment]
		if isinstance(_segment, Unset):
			segment = UNSET
		else:
			segment = _segment # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		extend_path = cls(
			path= path,
			segment= segment,
			type= type,
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




QE = TypeVar("QE", bound="extrude")

@attr.s(auto_attribs=True)
class extrude:
	""" Extrude a 2D solid. """ # noqa: E501
	cap: Union[Unset, bool] = False
	distance:  Union[Unset, float] = UNSET
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
			field_dict['cap'] = cap
		if distance is not UNSET:
			field_dict['distance'] = distance
		if target is not UNSET:
			field_dict['target'] = target
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[QE], src_dict: Dict[str, Any]) -> QE:
		d = src_dict.copy()
		cap = d.pop("cap", UNSET)

		distance = d.pop("distance", UNSET)

		_target = d.pop("target", UNSET)
		target: Union[Unset, ModelingCmdId]
		if isinstance(_target, Unset):
			target = UNSET
		else:
			target = _target # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		extrude = cls(
			cap= cap,
			distance= distance,
			target= target,
			type= type,
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




XH = TypeVar("XH", bound="close_path")

@attr.s(auto_attribs=True)
class close_path:
	""" Closes a path, converting it to a 2D solid. """ # noqa: E501
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
			field_dict['path_id'] = path_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[XH], src_dict: Dict[str, Any]) -> XH:
		d = src_dict.copy()
		path_id = d.pop("path_id", UNSET)

		type = d.pop("type", UNSET)


		close_path = cls(
			path_id= path_id,
			type= type,
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




KT = TypeVar("KT", bound="camera_drag_start")

@attr.s(auto_attribs=True)
class camera_drag_start:
	""" Camera drag started. """ # noqa: E501
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
			field_dict['interaction'] = interaction
		field_dict['type'] = type
		if window is not UNSET:
			field_dict['window'] = window

		return field_dict

	@classmethod
	def from_dict(cls: Type[KT], src_dict: Dict[str, Any]) -> KT:
		d = src_dict.copy()
		_interaction = d.pop("interaction", UNSET)
		interaction: Union[Unset, CameraDragInteractionType]
		if isinstance(_interaction, Unset):
			interaction = UNSET
		else:
			interaction = _interaction # type: ignore[arg-type]

		type = d.pop("type", UNSET)

		_window = d.pop("window", UNSET)
		window: Union[Unset, Point2d]
		if isinstance(_window, Unset):
			window = UNSET
		else:
			window = _window # type: ignore[arg-type]


		camera_drag_start = cls(
			interaction= interaction,
			type= type,
			window= window,
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




BV = TypeVar("BV", bound="camera_drag_move")

@attr.s(auto_attribs=True)
class camera_drag_move:
	""" Camera drag continued. """ # noqa: E501
	interaction: Union[Unset, CameraDragInteractionType] = UNSET
	sequence:  Union[Unset, int] = UNSET
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
			field_dict['interaction'] = interaction
		if sequence is not UNSET:
			field_dict['sequence'] = sequence
		field_dict['type'] = type
		if window is not UNSET:
			field_dict['window'] = window

		return field_dict

	@classmethod
	def from_dict(cls: Type[BV], src_dict: Dict[str, Any]) -> BV:
		d = src_dict.copy()
		_interaction = d.pop("interaction", UNSET)
		interaction: Union[Unset, CameraDragInteractionType]
		if isinstance(_interaction, Unset):
			interaction = UNSET
		else:
			interaction = _interaction # type: ignore[arg-type]

		sequence = d.pop("sequence", UNSET)

		type = d.pop("type", UNSET)

		_window = d.pop("window", UNSET)
		window: Union[Unset, Point2d]
		if isinstance(_window, Unset):
			window = UNSET
		else:
			window = _window # type: ignore[arg-type]


		camera_drag_move = cls(
			interaction= interaction,
			sequence= sequence,
			type= type,
			window= window,
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




GU = TypeVar("GU", bound="camera_drag_end")

@attr.s(auto_attribs=True)
class camera_drag_end:
	""" Camera drag ended. """ # noqa: E501
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
			field_dict['interaction'] = interaction
		field_dict['type'] = type
		if window is not UNSET:
			field_dict['window'] = window

		return field_dict

	@classmethod
	def from_dict(cls: Type[GU], src_dict: Dict[str, Any]) -> GU:
		d = src_dict.copy()
		_interaction = d.pop("interaction", UNSET)
		interaction: Union[Unset, CameraDragInteractionType]
		if isinstance(_interaction, Unset):
			interaction = UNSET
		else:
			interaction = _interaction # type: ignore[arg-type]

		type = d.pop("type", UNSET)

		_window = d.pop("window", UNSET)
		window: Union[Unset, Point2d]
		if isinstance(_window, Unset):
			window = UNSET
		else:
			window = _window # type: ignore[arg-type]


		camera_drag_end = cls(
			interaction= interaction,
			type= type,
			window= window,
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




SS = TypeVar("SS", bound="default_camera_look_at")

@attr.s(auto_attribs=True)
class default_camera_look_at:
	""" Change what the default camera is looking at. """ # noqa: E501
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
			field_dict['center'] = center
		field_dict['type'] = type
		if up is not UNSET:
			field_dict['up'] = up
		if vantage is not UNSET:
			field_dict['vantage'] = vantage

		return field_dict

	@classmethod
	def from_dict(cls: Type[SS], src_dict: Dict[str, Any]) -> SS:
		d = src_dict.copy()
		_center = d.pop("center", UNSET)
		center: Union[Unset, Point3d]
		if isinstance(_center, Unset):
			center = UNSET
		else:
			center = _center # type: ignore[arg-type]

		type = d.pop("type", UNSET)

		_up = d.pop("up", UNSET)
		up: Union[Unset, Point3d]
		if isinstance(_up, Unset):
			up = UNSET
		else:
			up = _up # type: ignore[arg-type]

		_vantage = d.pop("vantage", UNSET)
		vantage: Union[Unset, Point3d]
		if isinstance(_vantage, Unset):
			vantage = UNSET
		else:
			vantage = _vantage # type: ignore[arg-type]


		default_camera_look_at = cls(
			center= center,
			type= type,
			up= up,
			vantage= vantage,
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




UP = TypeVar("UP", bound="default_camera_zoom")

@attr.s(auto_attribs=True)
class default_camera_zoom:
	""" Adjust zoom of the default camera. """ # noqa: E501
	magnitude:  Union[Unset, float] = UNSET
	type: str = "default_camera_zoom"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		magnitude = self.magnitude
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if magnitude is not UNSET:
			field_dict['magnitude'] = magnitude
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[UP], src_dict: Dict[str, Any]) -> UP:
		d = src_dict.copy()
		magnitude = d.pop("magnitude", UNSET)

		type = d.pop("type", UNSET)


		default_camera_zoom = cls(
			magnitude= magnitude,
			type= type,
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




AZ = TypeVar("AZ", bound="default_camera_enable_sketch_mode")

@attr.s(auto_attribs=True)
class default_camera_enable_sketch_mode:
	""" Enable sketch mode, where users can sketch 2D geometry. Users choose a plane to sketch on. """ # noqa: E501
	animated: Union[Unset, bool] = False
	distance_to_plane:  Union[Unset, float] = UNSET
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
			field_dict['animated'] = animated
		if distance_to_plane is not UNSET:
			field_dict['distance_to_plane'] = distance_to_plane
		if origin is not UNSET:
			field_dict['origin'] = origin
		if ortho is not UNSET:
			field_dict['ortho'] = ortho
		field_dict['type'] = type
		if x_axis is not UNSET:
			field_dict['x_axis'] = x_axis
		if y_axis is not UNSET:
			field_dict['y_axis'] = y_axis

		return field_dict

	@classmethod
	def from_dict(cls: Type[AZ], src_dict: Dict[str, Any]) -> AZ:
		d = src_dict.copy()
		animated = d.pop("animated", UNSET)

		distance_to_plane = d.pop("distance_to_plane", UNSET)

		_origin = d.pop("origin", UNSET)
		origin: Union[Unset, Point3d]
		if isinstance(_origin, Unset):
			origin = UNSET
		else:
			origin = _origin # type: ignore[arg-type]

		ortho = d.pop("ortho", UNSET)

		type = d.pop("type", UNSET)

		_x_axis = d.pop("x_axis", UNSET)
		x_axis: Union[Unset, Point3d]
		if isinstance(_x_axis, Unset):
			x_axis = UNSET
		else:
			x_axis = _x_axis # type: ignore[arg-type]

		_y_axis = d.pop("y_axis", UNSET)
		y_axis: Union[Unset, Point3d]
		if isinstance(_y_axis, Unset):
			y_axis = UNSET
		else:
			y_axis = _y_axis # type: ignore[arg-type]


		default_camera_enable_sketch_mode = cls(
			animated= animated,
			distance_to_plane= distance_to_plane,
			origin= origin,
			ortho= ortho,
			type= type,
			x_axis= x_axis,
			y_axis= y_axis,
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




DJ = TypeVar("DJ", bound="default_camera_disable_sketch_mode")

@attr.s(auto_attribs=True)
class default_camera_disable_sketch_mode:
	""" Disable sketch mode, from the default camera. """ # noqa: E501
	type: str = "default_camera_disable_sketch_mode"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[DJ], src_dict: Dict[str, Any]) -> DJ:
		d = src_dict.copy()
		type = d.pop("type", UNSET)


		default_camera_disable_sketch_mode = cls(
			type= type,
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




WJ = TypeVar("WJ", bound="export")

@attr.s(auto_attribs=True)
class export:
	""" Export the scene to a file. """ # noqa: E501
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
			field_dict['entity_ids'] = entity_ids
		if format is not UNSET:
			field_dict['format'] = format
		if source_unit is not UNSET:
			field_dict['source_unit'] = source_unit
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[WJ], src_dict: Dict[str, Any]) -> WJ:
		d = src_dict.copy()
		entity_ids = cast(List[str], d.pop("entity_ids", UNSET))

		_format = d.pop("format", UNSET)
		format: Union[Unset, OutputFormat]
		if isinstance(_format, Unset):
			format = UNSET
		else:
			format = _format # type: ignore[arg-type]

		_source_unit = d.pop("source_unit", UNSET)
		source_unit: Union[Unset, UnitLength]
		if isinstance(_source_unit, Unset):
			source_unit = UNSET
		else:
			source_unit = _source_unit # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		export = cls(
			entity_ids= entity_ids,
			format= format,
			source_unit= source_unit,
			type= type,
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




TR = TypeVar("TR", bound="entity_get_parent_id")

@attr.s(auto_attribs=True)
class entity_get_parent_id:
	""" What is this entity's parent? """ # noqa: E501
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
			field_dict['entity_id'] = entity_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[TR], src_dict: Dict[str, Any]) -> TR:
		d = src_dict.copy()
		entity_id = d.pop("entity_id", UNSET)

		type = d.pop("type", UNSET)


		entity_get_parent_id = cls(
			entity_id= entity_id,
			type= type,
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




YD = TypeVar("YD", bound="entity_get_num_children")

@attr.s(auto_attribs=True)
class entity_get_num_children:
	""" How many children does the entity have? """ # noqa: E501
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
			field_dict['entity_id'] = entity_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[YD], src_dict: Dict[str, Any]) -> YD:
		d = src_dict.copy()
		entity_id = d.pop("entity_id", UNSET)

		type = d.pop("type", UNSET)


		entity_get_num_children = cls(
			entity_id= entity_id,
			type= type,
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




JF = TypeVar("JF", bound="entity_get_child_uuid")

@attr.s(auto_attribs=True)
class entity_get_child_uuid:
	""" What is the UUID of this entity's n-th child? """ # noqa: E501
	child_index:  Union[Unset, int] = UNSET
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
			field_dict['child_index'] = child_index
		if entity_id is not UNSET:
			field_dict['entity_id'] = entity_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[JF], src_dict: Dict[str, Any]) -> JF:
		d = src_dict.copy()
		child_index = d.pop("child_index", UNSET)

		entity_id = d.pop("entity_id", UNSET)

		type = d.pop("type", UNSET)


		entity_get_child_uuid = cls(
			child_index= child_index,
			entity_id= entity_id,
			type= type,
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




VP = TypeVar("VP", bound="entity_get_all_child_uuids")

@attr.s(auto_attribs=True)
class entity_get_all_child_uuids:
	""" What are all UUIDs of this entity's children? """ # noqa: E501
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
			field_dict['entity_id'] = entity_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[VP], src_dict: Dict[str, Any]) -> VP:
		d = src_dict.copy()
		entity_id = d.pop("entity_id", UNSET)

		type = d.pop("type", UNSET)


		entity_get_all_child_uuids = cls(
			entity_id= entity_id,
			type= type,
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




EL = TypeVar("EL", bound="edit_mode_enter")

@attr.s(auto_attribs=True)
class edit_mode_enter:
	""" Enter edit mode """ # noqa: E501
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
			field_dict['target'] = target
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[EL], src_dict: Dict[str, Any]) -> EL:
		d = src_dict.copy()
		target = d.pop("target", UNSET)

		type = d.pop("type", UNSET)


		edit_mode_enter = cls(
			target= target,
			type= type,
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




ZG = TypeVar("ZG", bound="edit_mode_exit")

@attr.s(auto_attribs=True)
class edit_mode_exit:
	""" Exit edit mode """ # noqa: E501
	type: str = "edit_mode_exit"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[ZG], src_dict: Dict[str, Any]) -> ZG:
		d = src_dict.copy()
		type = d.pop("type", UNSET)


		edit_mode_exit = cls(
			type= type,
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




LF = TypeVar("LF", bound="select_with_point")

@attr.s(auto_attribs=True)
class select_with_point:
	""" Modifies the selection by simulating a "mouse click" at the given x,y window coordinate Returns ID of whatever was selected. """ # noqa: E501
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
			field_dict['selected_at_window'] = selected_at_window
		if selection_type is not UNSET:
			field_dict['selection_type'] = selection_type
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[LF], src_dict: Dict[str, Any]) -> LF:
		d = src_dict.copy()
		_selected_at_window = d.pop("selected_at_window", UNSET)
		selected_at_window: Union[Unset, Point2d]
		if isinstance(_selected_at_window, Unset):
			selected_at_window = UNSET
		else:
			selected_at_window = _selected_at_window # type: ignore[arg-type]

		_selection_type = d.pop("selection_type", UNSET)
		selection_type: Union[Unset, SceneSelectionType]
		if isinstance(_selection_type, Unset):
			selection_type = UNSET
		else:
			selection_type = _selection_type # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		select_with_point = cls(
			selected_at_window= selected_at_window,
			selection_type= selection_type,
			type= type,
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




CS = TypeVar("CS", bound="select_clear")

@attr.s(auto_attribs=True)
class select_clear:
	""" Clear the selection """ # noqa: E501
	type: str = "select_clear"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[CS], src_dict: Dict[str, Any]) -> CS:
		d = src_dict.copy()
		type = d.pop("type", UNSET)


		select_clear = cls(
			type= type,
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




GN = TypeVar("GN", bound="select_add")

@attr.s(auto_attribs=True)
class select_add:
	""" Adds one or more entities (by UUID) to the selection. """ # noqa: E501
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
			field_dict['entities'] = entities
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[GN], src_dict: Dict[str, Any]) -> GN:
		d = src_dict.copy()
		entities = cast(List[str], d.pop("entities", UNSET))

		type = d.pop("type", UNSET)


		select_add = cls(
			entities= entities,
			type= type,
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




GD = TypeVar("GD", bound="select_remove")

@attr.s(auto_attribs=True)
class select_remove:
	""" Removes one or more entities (by UUID) from the selection. """ # noqa: E501
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
			field_dict['entities'] = entities
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[GD], src_dict: Dict[str, Any]) -> GD:
		d = src_dict.copy()
		entities = cast(List[str], d.pop("entities", UNSET))

		type = d.pop("type", UNSET)


		select_remove = cls(
			entities= entities,
			type= type,
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




VJ = TypeVar("VJ", bound="select_replace")

@attr.s(auto_attribs=True)
class select_replace:
	""" Replaces the current selection with these new entities (by UUID). Equivalent to doing SelectClear then SelectAdd. """ # noqa: E501
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
			field_dict['entities'] = entities
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[VJ], src_dict: Dict[str, Any]) -> VJ:
		d = src_dict.copy()
		entities = cast(List[str], d.pop("entities", UNSET))

		type = d.pop("type", UNSET)


		select_replace = cls(
			entities= entities,
			type= type,
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




OX = TypeVar("OX", bound="select_get")

@attr.s(auto_attribs=True)
class select_get:
	""" Find all IDs of selected entities """ # noqa: E501
	type: str = "select_get"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[OX], src_dict: Dict[str, Any]) -> OX:
		d = src_dict.copy()
		type = d.pop("type", UNSET)


		select_get = cls(
			type= type,
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




YW = TypeVar("YW", bound="highlight_set_entity")

@attr.s(auto_attribs=True)
class highlight_set_entity:
	""" Changes the current highlighted entity to whichever one is at the given window coordinate. If there's no entity at this location, clears the highlight. """ # noqa: E501
	selected_at_window: Union[Unset, Point2d] = UNSET
	sequence:  Union[Unset, int] = UNSET
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
			field_dict['selected_at_window'] = selected_at_window
		if sequence is not UNSET:
			field_dict['sequence'] = sequence
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[YW], src_dict: Dict[str, Any]) -> YW:
		d = src_dict.copy()
		_selected_at_window = d.pop("selected_at_window", UNSET)
		selected_at_window: Union[Unset, Point2d]
		if isinstance(_selected_at_window, Unset):
			selected_at_window = UNSET
		else:
			selected_at_window = _selected_at_window # type: ignore[arg-type]

		sequence = d.pop("sequence", UNSET)

		type = d.pop("type", UNSET)


		highlight_set_entity = cls(
			selected_at_window= selected_at_window,
			sequence= sequence,
			type= type,
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




QX = TypeVar("QX", bound="highlight_set_entities")

@attr.s(auto_attribs=True)
class highlight_set_entities:
	""" Changes the current highlighted entity to these entities. """ # noqa: E501
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
			field_dict['entities'] = entities
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[QX], src_dict: Dict[str, Any]) -> QX:
		d = src_dict.copy()
		entities = cast(List[str], d.pop("entities", UNSET))

		type = d.pop("type", UNSET)


		highlight_set_entities = cls(
			entities= entities,
			type= type,
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




NO = TypeVar("NO", bound="new_annotation")

@attr.s(auto_attribs=True)
class new_annotation:
	""" Create a new annotation """ # noqa: E501
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
			field_dict['annotation_type'] = annotation_type
		if clobber is not UNSET:
			field_dict['clobber'] = clobber
		if options is not UNSET:
			field_dict['options'] = options
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[NO], src_dict: Dict[str, Any]) -> NO:
		d = src_dict.copy()
		_annotation_type = d.pop("annotation_type", UNSET)
		annotation_type: Union[Unset, AnnotationType]
		if isinstance(_annotation_type, Unset):
			annotation_type = UNSET
		else:
			annotation_type = _annotation_type # type: ignore[arg-type]

		clobber = d.pop("clobber", UNSET)

		_options = d.pop("options", UNSET)
		options: Union[Unset, AnnotationOptions]
		if isinstance(_options, Unset):
			options = UNSET
		else:
			options = _options # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		new_annotation = cls(
			annotation_type= annotation_type,
			clobber= clobber,
			options= options,
			type= type,
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




VX = TypeVar("VX", bound="update_annotation")

@attr.s(auto_attribs=True)
class update_annotation:
	""" Update an annotation """ # noqa: E501
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
			field_dict['annotation_id'] = annotation_id
		if options is not UNSET:
			field_dict['options'] = options
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[VX], src_dict: Dict[str, Any]) -> VX:
		d = src_dict.copy()
		annotation_id = d.pop("annotation_id", UNSET)

		_options = d.pop("options", UNSET)
		options: Union[Unset, AnnotationOptions]
		if isinstance(_options, Unset):
			options = UNSET
		else:
			options = _options # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		update_annotation = cls(
			annotation_id= annotation_id,
			options= options,
			type= type,
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




RG = TypeVar("RG", bound="object_visible")

@attr.s(auto_attribs=True)
class object_visible:
	""" Hide or show an object """ # noqa: E501
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
			field_dict['hidden'] = hidden
		if object_id is not UNSET:
			field_dict['object_id'] = object_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[RG], src_dict: Dict[str, Any]) -> RG:
		d = src_dict.copy()
		hidden = d.pop("hidden", UNSET)

		object_id = d.pop("object_id", UNSET)

		type = d.pop("type", UNSET)


		object_visible = cls(
			hidden= hidden,
			object_id= object_id,
			type= type,
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




IT = TypeVar("IT", bound="get_entity_type")

@attr.s(auto_attribs=True)
class get_entity_type:
	""" What type of entity is this? """ # noqa: E501
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
			field_dict['entity_id'] = entity_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[IT], src_dict: Dict[str, Any]) -> IT:
		d = src_dict.copy()
		entity_id = d.pop("entity_id", UNSET)

		type = d.pop("type", UNSET)


		get_entity_type = cls(
			entity_id= entity_id,
			type= type,
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




LD = TypeVar("LD", bound="solid3d_get_all_edge_faces")

@attr.s(auto_attribs=True)
class solid3d_get_all_edge_faces:
	""" Gets all faces which use the given edge. """ # noqa: E501
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
			field_dict['edge_id'] = edge_id
		if object_id is not UNSET:
			field_dict['object_id'] = object_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[LD], src_dict: Dict[str, Any]) -> LD:
		d = src_dict.copy()
		edge_id = d.pop("edge_id", UNSET)

		object_id = d.pop("object_id", UNSET)

		type = d.pop("type", UNSET)


		solid3d_get_all_edge_faces = cls(
			edge_id= edge_id,
			object_id= object_id,
			type= type,
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




UA = TypeVar("UA", bound="solid3d_get_all_opposite_edges")

@attr.s(auto_attribs=True)
class solid3d_get_all_opposite_edges:
	""" Gets all edges which are opposite the given edge, across all possible faces. """ # noqa: E501
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
			field_dict['along_vector'] = along_vector
		if edge_id is not UNSET:
			field_dict['edge_id'] = edge_id
		if object_id is not UNSET:
			field_dict['object_id'] = object_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[UA], src_dict: Dict[str, Any]) -> UA:
		d = src_dict.copy()
		_along_vector = d.pop("along_vector", UNSET)
		along_vector: Union[Unset, Point3d]
		if isinstance(_along_vector, Unset):
			along_vector = UNSET
		else:
			along_vector = _along_vector # type: ignore[arg-type]

		edge_id = d.pop("edge_id", UNSET)

		object_id = d.pop("object_id", UNSET)

		type = d.pop("type", UNSET)


		solid3d_get_all_opposite_edges = cls(
			along_vector= along_vector,
			edge_id= edge_id,
			object_id= object_id,
			type= type,
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




TN = TypeVar("TN", bound="solid3d_get_opposite_edge")

@attr.s(auto_attribs=True)
class solid3d_get_opposite_edge:
	""" Gets the edge opposite the given edge, along the given face. """ # noqa: E501
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
			field_dict['edge_id'] = edge_id
		if face_id is not UNSET:
			field_dict['face_id'] = face_id
		if object_id is not UNSET:
			field_dict['object_id'] = object_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[TN], src_dict: Dict[str, Any]) -> TN:
		d = src_dict.copy()
		edge_id = d.pop("edge_id", UNSET)

		face_id = d.pop("face_id", UNSET)

		object_id = d.pop("object_id", UNSET)

		type = d.pop("type", UNSET)


		solid3d_get_opposite_edge = cls(
			edge_id= edge_id,
			face_id= face_id,
			object_id= object_id,
			type= type,
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




MZ = TypeVar("MZ", bound="solid3d_get_next_adjacent_edge")

@attr.s(auto_attribs=True)
class solid3d_get_next_adjacent_edge:
	""" Gets the next adjacent edge for the given edge, along the given face. """ # noqa: E501
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
			field_dict['edge_id'] = edge_id
		if face_id is not UNSET:
			field_dict['face_id'] = face_id
		if object_id is not UNSET:
			field_dict['object_id'] = object_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[MZ], src_dict: Dict[str, Any]) -> MZ:
		d = src_dict.copy()
		edge_id = d.pop("edge_id", UNSET)

		face_id = d.pop("face_id", UNSET)

		object_id = d.pop("object_id", UNSET)

		type = d.pop("type", UNSET)


		solid3d_get_next_adjacent_edge = cls(
			edge_id= edge_id,
			face_id= face_id,
			object_id= object_id,
			type= type,
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




UG = TypeVar("UG", bound="solid3d_get_prev_adjacent_edge")

@attr.s(auto_attribs=True)
class solid3d_get_prev_adjacent_edge:
	""" Gets the previous adjacent edge for the given edge, along the given face. """ # noqa: E501
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
			field_dict['edge_id'] = edge_id
		if face_id is not UNSET:
			field_dict['face_id'] = face_id
		if object_id is not UNSET:
			field_dict['object_id'] = object_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[UG], src_dict: Dict[str, Any]) -> UG:
		d = src_dict.copy()
		edge_id = d.pop("edge_id", UNSET)

		face_id = d.pop("face_id", UNSET)

		object_id = d.pop("object_id", UNSET)

		type = d.pop("type", UNSET)


		solid3d_get_prev_adjacent_edge = cls(
			edge_id= edge_id,
			face_id= face_id,
			object_id= object_id,
			type= type,
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




CY = TypeVar("CY", bound="send_object")

@attr.s(auto_attribs=True)
class send_object:
	""" Sends object to front or back. """ # noqa: E501
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
			field_dict['front'] = front
		if object_id is not UNSET:
			field_dict['object_id'] = object_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[CY], src_dict: Dict[str, Any]) -> CY:
		d = src_dict.copy()
		front = d.pop("front", UNSET)

		object_id = d.pop("object_id", UNSET)

		type = d.pop("type", UNSET)


		send_object = cls(
			front= front,
			object_id= object_id,
			type= type,
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




NZ = TypeVar("NZ", bound="entity_set_opacity")

@attr.s(auto_attribs=True)
class entity_set_opacity:
	""" Set opacity of the entity. """ # noqa: E501
	entity_id: Union[Unset, str] = UNSET
	opacity:  Union[Unset, float] = UNSET
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
			field_dict['entity_id'] = entity_id
		if opacity is not UNSET:
			field_dict['opacity'] = opacity
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[NZ], src_dict: Dict[str, Any]) -> NZ:
		d = src_dict.copy()
		entity_id = d.pop("entity_id", UNSET)

		opacity = d.pop("opacity", UNSET)

		type = d.pop("type", UNSET)


		entity_set_opacity = cls(
			entity_id= entity_id,
			opacity= opacity,
			type= type,
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




LI = TypeVar("LI", bound="entity_fade")

@attr.s(auto_attribs=True)
class entity_fade:
	""" Fade the entity in or out. """ # noqa: E501
	duration_seconds:  Union[Unset, float] = UNSET
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
			field_dict['duration_seconds'] = duration_seconds
		if entity_id is not UNSET:
			field_dict['entity_id'] = entity_id
		if fade_in is not UNSET:
			field_dict['fade_in'] = fade_in
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[LI], src_dict: Dict[str, Any]) -> LI:
		d = src_dict.copy()
		duration_seconds = d.pop("duration_seconds", UNSET)

		entity_id = d.pop("entity_id", UNSET)

		fade_in = d.pop("fade_in", UNSET)

		type = d.pop("type", UNSET)


		entity_fade = cls(
			duration_seconds= duration_seconds,
			entity_id= entity_id,
			fade_in= fade_in,
			type= type,
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




LO = TypeVar("LO", bound="make_plane")

@attr.s(auto_attribs=True)
class make_plane:
	""" Make a plane. """ # noqa: E501
	clobber: Union[Unset, bool] = False
	origin: Union[Unset, Point3d] = UNSET
	size:  Union[Unset, float] = UNSET
	type: str = "make_plane"
	x_axis: Union[Unset, Point3d] = UNSET
	y_axis: Union[Unset, Point3d] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		clobber = self.clobber
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
			field_dict['clobber'] = clobber
		if origin is not UNSET:
			field_dict['origin'] = origin
		if size is not UNSET:
			field_dict['size'] = size
		field_dict['type'] = type
		if x_axis is not UNSET:
			field_dict['x_axis'] = x_axis
		if y_axis is not UNSET:
			field_dict['y_axis'] = y_axis

		return field_dict

	@classmethod
	def from_dict(cls: Type[LO], src_dict: Dict[str, Any]) -> LO:
		d = src_dict.copy()
		clobber = d.pop("clobber", UNSET)

		_origin = d.pop("origin", UNSET)
		origin: Union[Unset, Point3d]
		if isinstance(_origin, Unset):
			origin = UNSET
		else:
			origin = _origin # type: ignore[arg-type]

		size = d.pop("size", UNSET)

		type = d.pop("type", UNSET)

		_x_axis = d.pop("x_axis", UNSET)
		x_axis: Union[Unset, Point3d]
		if isinstance(_x_axis, Unset):
			x_axis = UNSET
		else:
			x_axis = _x_axis # type: ignore[arg-type]

		_y_axis = d.pop("y_axis", UNSET)
		y_axis: Union[Unset, Point3d]
		if isinstance(_y_axis, Unset):
			y_axis = UNSET
		else:
			y_axis = _y_axis # type: ignore[arg-type]


		make_plane = cls(
			clobber= clobber,
			origin= origin,
			size= size,
			type= type,
			x_axis= x_axis,
			y_axis= y_axis,
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




XJ = TypeVar("XJ", bound="plane_set_color")

@attr.s(auto_attribs=True)
class plane_set_color:
	""" Set the plane's color. """ # noqa: E501
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
			field_dict['color'] = color
		if plane_id is not UNSET:
			field_dict['plane_id'] = plane_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[XJ], src_dict: Dict[str, Any]) -> XJ:
		d = src_dict.copy()
		_color = d.pop("color", UNSET)
		color: Union[Unset, Color]
		if isinstance(_color, Unset):
			color = UNSET
		else:
			color = _color # type: ignore[arg-type]

		plane_id = d.pop("plane_id", UNSET)

		type = d.pop("type", UNSET)


		plane_set_color = cls(
			color= color,
			plane_id= plane_id,
			type= type,
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




OW = TypeVar("OW", bound="set_tool")

@attr.s(auto_attribs=True)
class set_tool:
	""" Set the active tool. """ # noqa: E501
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
			field_dict['tool'] = tool
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[OW], src_dict: Dict[str, Any]) -> OW:
		d = src_dict.copy()
		_tool = d.pop("tool", UNSET)
		tool: Union[Unset, SceneToolType]
		if isinstance(_tool, Unset):
			tool = UNSET
		else:
			tool = _tool # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		set_tool = cls(
			tool= tool,
			type= type,
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




JQ = TypeVar("JQ", bound="mouse_move")

@attr.s(auto_attribs=True)
class mouse_move:
	""" Send a mouse move event. """ # noqa: E501
	sequence:  Union[Unset, int] = UNSET
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
			field_dict['sequence'] = sequence
		field_dict['type'] = type
		if window is not UNSET:
			field_dict['window'] = window

		return field_dict

	@classmethod
	def from_dict(cls: Type[JQ], src_dict: Dict[str, Any]) -> JQ:
		d = src_dict.copy()
		sequence = d.pop("sequence", UNSET)

		type = d.pop("type", UNSET)

		_window = d.pop("window", UNSET)
		window: Union[Unset, Point2d]
		if isinstance(_window, Unset):
			window = UNSET
		else:
			window = _window # type: ignore[arg-type]


		mouse_move = cls(
			sequence= sequence,
			type= type,
			window= window,
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




PQ = TypeVar("PQ", bound="mouse_click")

@attr.s(auto_attribs=True)
class mouse_click:
	""" Send a mouse click event. Updates modified/selected entities. """ # noqa: E501
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
		field_dict['type'] = type
		if window is not UNSET:
			field_dict['window'] = window

		return field_dict

	@classmethod
	def from_dict(cls: Type[PQ], src_dict: Dict[str, Any]) -> PQ:
		d = src_dict.copy()
		type = d.pop("type", UNSET)

		_window = d.pop("window", UNSET)
		window: Union[Unset, Point2d]
		if isinstance(_window, Unset):
			window = UNSET
		else:
			window = _window # type: ignore[arg-type]


		mouse_click = cls(
			type= type,
			window= window,
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




IM = TypeVar("IM", bound="sketch_mode_enable")

@attr.s(auto_attribs=True)
class sketch_mode_enable:
	""" Enable sketch mode on the given plane. """ # noqa: E501
	animated: Union[Unset, bool] = False
	ortho: Union[Unset, bool] = False
	plane_id: Union[Unset, str] = UNSET
	type: str = "sketch_mode_enable"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		animated = self.animated
		ortho = self.ortho
		plane_id = self.plane_id
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if animated is not UNSET:
			field_dict['animated'] = animated
		if ortho is not UNSET:
			field_dict['ortho'] = ortho
		if plane_id is not UNSET:
			field_dict['plane_id'] = plane_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[IM], src_dict: Dict[str, Any]) -> IM:
		d = src_dict.copy()
		animated = d.pop("animated", UNSET)

		ortho = d.pop("ortho", UNSET)

		plane_id = d.pop("plane_id", UNSET)

		type = d.pop("type", UNSET)


		sketch_mode_enable = cls(
			animated= animated,
			ortho= ortho,
			plane_id= plane_id,
			type= type,
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




OU = TypeVar("OU", bound="sketch_mode_disable")

@attr.s(auto_attribs=True)
class sketch_mode_disable:
	""" Disable sketch mode. """ # noqa: E501
	type: str = "sketch_mode_disable"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[OU], src_dict: Dict[str, Any]) -> OU:
		d = src_dict.copy()
		type = d.pop("type", UNSET)


		sketch_mode_disable = cls(
			type= type,
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




KL = TypeVar("KL", bound="curve_get_type")

@attr.s(auto_attribs=True)
class curve_get_type:
	""" Get type of a given curve. """ # noqa: E501
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
			field_dict['curve_id'] = curve_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[KL], src_dict: Dict[str, Any]) -> KL:
		d = src_dict.copy()
		curve_id = d.pop("curve_id", UNSET)

		type = d.pop("type", UNSET)


		curve_get_type = cls(
			curve_id= curve_id,
			type= type,
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




XI = TypeVar("XI", bound="curve_get_control_points")

@attr.s(auto_attribs=True)
class curve_get_control_points:
	""" Get control points of a given curve. """ # noqa: E501
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
			field_dict['curve_id'] = curve_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[XI], src_dict: Dict[str, Any]) -> XI:
		d = src_dict.copy()
		curve_id = d.pop("curve_id", UNSET)

		type = d.pop("type", UNSET)


		curve_get_control_points = cls(
			curve_id= curve_id,
			type= type,
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




PO = TypeVar("PO", bound="take_snapshot")

@attr.s(auto_attribs=True)
class take_snapshot:
	""" Take a snapshot. """ # noqa: E501
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
			field_dict['format'] = format
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[PO], src_dict: Dict[str, Any]) -> PO:
		d = src_dict.copy()
		_format = d.pop("format", UNSET)
		format: Union[Unset, ImageFormat]
		if isinstance(_format, Unset):
			format = UNSET
		else:
			format = _format # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		take_snapshot = cls(
			format= format,
			type= type,
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




PS = TypeVar("PS", bound="make_axes_gizmo")

@attr.s(auto_attribs=True)
class make_axes_gizmo:
	""" Add a gizmo showing the axes. """ # noqa: E501
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
			field_dict['clobber'] = clobber
		if gizmo_mode is not UNSET:
			field_dict['gizmo_mode'] = gizmo_mode
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[PS], src_dict: Dict[str, Any]) -> PS:
		d = src_dict.copy()
		clobber = d.pop("clobber", UNSET)

		gizmo_mode = d.pop("gizmo_mode", UNSET)

		type = d.pop("type", UNSET)


		make_axes_gizmo = cls(
			clobber= clobber,
			gizmo_mode= gizmo_mode,
			type= type,
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




WR = TypeVar("WR", bound="path_get_info")

@attr.s(auto_attribs=True)
class path_get_info:
	""" Query the given path """ # noqa: E501
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
			field_dict['path_id'] = path_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[WR], src_dict: Dict[str, Any]) -> WR:
		d = src_dict.copy()
		path_id = d.pop("path_id", UNSET)

		type = d.pop("type", UNSET)


		path_get_info = cls(
			path_id= path_id,
			type= type,
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




XL = TypeVar("XL", bound="path_get_curve_uuids_for_vertices")

@attr.s(auto_attribs=True)
class path_get_curve_uuids_for_vertices:
	""" Get curves for vertices within a path """ # noqa: E501
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
			field_dict['path_id'] = path_id
		field_dict['type'] = type
		if vertex_ids is not UNSET:
			field_dict['vertex_ids'] = vertex_ids

		return field_dict

	@classmethod
	def from_dict(cls: Type[XL], src_dict: Dict[str, Any]) -> XL:
		d = src_dict.copy()
		path_id = d.pop("path_id", UNSET)

		type = d.pop("type", UNSET)

		vertex_ids = cast(List[str], d.pop("vertex_ids", UNSET))


		path_get_curve_uuids_for_vertices = cls(
			path_id= path_id,
			type= type,
			vertex_ids= vertex_ids,
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




ZX = TypeVar("ZX", bound="handle_mouse_drag_start")

@attr.s(auto_attribs=True)
class handle_mouse_drag_start:
	""" Start dragging mouse. """ # noqa: E501
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
		field_dict['type'] = type
		if window is not UNSET:
			field_dict['window'] = window

		return field_dict

	@classmethod
	def from_dict(cls: Type[ZX], src_dict: Dict[str, Any]) -> ZX:
		d = src_dict.copy()
		type = d.pop("type", UNSET)

		_window = d.pop("window", UNSET)
		window: Union[Unset, Point2d]
		if isinstance(_window, Unset):
			window = UNSET
		else:
			window = _window # type: ignore[arg-type]


		handle_mouse_drag_start = cls(
			type= type,
			window= window,
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




FT = TypeVar("FT", bound="handle_mouse_drag_move")

@attr.s(auto_attribs=True)
class handle_mouse_drag_move:
	""" Continue dragging mouse. """ # noqa: E501
	sequence:  Union[Unset, int] = UNSET
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
			field_dict['sequence'] = sequence
		field_dict['type'] = type
		if window is not UNSET:
			field_dict['window'] = window

		return field_dict

	@classmethod
	def from_dict(cls: Type[FT], src_dict: Dict[str, Any]) -> FT:
		d = src_dict.copy()
		sequence = d.pop("sequence", UNSET)

		type = d.pop("type", UNSET)

		_window = d.pop("window", UNSET)
		window: Union[Unset, Point2d]
		if isinstance(_window, Unset):
			window = UNSET
		else:
			window = _window # type: ignore[arg-type]


		handle_mouse_drag_move = cls(
			sequence= sequence,
			type= type,
			window= window,
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




NX = TypeVar("NX", bound="handle_mouse_drag_end")

@attr.s(auto_attribs=True)
class handle_mouse_drag_end:
	""" Stop dragging mouse. """ # noqa: E501
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
		field_dict['type'] = type
		if window is not UNSET:
			field_dict['window'] = window

		return field_dict

	@classmethod
	def from_dict(cls: Type[NX], src_dict: Dict[str, Any]) -> NX:
		d = src_dict.copy()
		type = d.pop("type", UNSET)

		_window = d.pop("window", UNSET)
		window: Union[Unset, Point2d]
		if isinstance(_window, Unset):
			window = UNSET
		else:
			window = _window # type: ignore[arg-type]


		handle_mouse_drag_end = cls(
			type= type,
			window= window,
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




SC = TypeVar("SC", bound="remove_scene_objects")

@attr.s(auto_attribs=True)
class remove_scene_objects:
	""" Remove scene objects. """ # noqa: E501
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
			field_dict['object_ids'] = object_ids
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[SC], src_dict: Dict[str, Any]) -> SC:
		d = src_dict.copy()
		object_ids = cast(List[str], d.pop("object_ids", UNSET))

		type = d.pop("type", UNSET)


		remove_scene_objects = cls(
			object_ids= object_ids,
			type= type,
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




TX = TypeVar("TX", bound="plane_intersect_and_project")

@attr.s(auto_attribs=True)
class plane_intersect_and_project:
	""" Utility method. Performs both a ray cast and projection to plane-local coordinates. Returns the plane coordinates for the given window coordinates. """ # noqa: E501
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
			field_dict['plane_id'] = plane_id
		field_dict['type'] = type
		if window is not UNSET:
			field_dict['window'] = window

		return field_dict

	@classmethod
	def from_dict(cls: Type[TX], src_dict: Dict[str, Any]) -> TX:
		d = src_dict.copy()
		plane_id = d.pop("plane_id", UNSET)

		type = d.pop("type", UNSET)

		_window = d.pop("window", UNSET)
		window: Union[Unset, Point2d]
		if isinstance(_window, Unset):
			window = UNSET
		else:
			window = _window # type: ignore[arg-type]


		plane_intersect_and_project = cls(
			plane_id= plane_id,
			type= type,
			window= window,
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




JA = TypeVar("JA", bound="curve_get_end_points")

@attr.s(auto_attribs=True)
class curve_get_end_points:
	""" Find the start and end of a curve. """ # noqa: E501
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
			field_dict['curve_id'] = curve_id
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[JA], src_dict: Dict[str, Any]) -> JA:
		d = src_dict.copy()
		curve_id = d.pop("curve_id", UNSET)

		type = d.pop("type", UNSET)


		curve_get_end_points = cls(
			curve_id= curve_id,
			type= type,
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




SK = TypeVar("SK", bound="reconfigure_stream")

@attr.s(auto_attribs=True)
class reconfigure_stream:
	""" Reconfigure the stream. """ # noqa: E501
	fps:  Union[Unset, int] = UNSET
	height:  Union[Unset, int] = UNSET
	type: str = "reconfigure_stream"
	width:  Union[Unset, int] = UNSET

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
			field_dict['fps'] = fps
		if height is not UNSET:
			field_dict['height'] = height
		field_dict['type'] = type
		if width is not UNSET:
			field_dict['width'] = width

		return field_dict

	@classmethod
	def from_dict(cls: Type[SK], src_dict: Dict[str, Any]) -> SK:
		d = src_dict.copy()
		fps = d.pop("fps", UNSET)

		height = d.pop("height", UNSET)

		type = d.pop("type", UNSET)

		width = d.pop("width", UNSET)


		reconfigure_stream = cls(
			fps= fps,
			height= height,
			type= type,
			width= width,
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




UK = TypeVar("UK", bound="import_files")

@attr.s(auto_attribs=True)
class import_files:
	""" Import files to the current model. """ # noqa: E501
	from ..models.import_file import ImportFile
	files: Union[Unset, List[ImportFile]] = UNSET
	type: str = "import_files"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		from ..models.import_file import ImportFile
		files: Union[Unset, List[ImportFile]] = UNSET
		if not isinstance(self.files, Unset):
			files = self.files
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if files is not UNSET:
			field_dict['files'] = files
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[UK], src_dict: Dict[str, Any]) -> UK:
		d = src_dict.copy()
		from ..models.import_file import ImportFile
		files = cast(List[ImportFile], d.pop("files", UNSET))

		type = d.pop("type", UNSET)


		import_files = cls(
			files= files,
			type= type,
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




CX = TypeVar("CX", bound="mass")

@attr.s(auto_attribs=True)
class mass:
	""" Get the mass of entities in the scene or the default scene. """ # noqa: E501
	entity_ids: Union[Unset, List[str]] = UNSET
	material_density:  Union[Unset, float] = UNSET
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
			field_dict['entity_ids'] = entity_ids
		if material_density is not UNSET:
			field_dict['material_density'] = material_density
		if material_density_unit is not UNSET:
			field_dict['material_density_unit'] = material_density_unit
		if output_unit is not UNSET:
			field_dict['output_unit'] = output_unit
		if source_unit is not UNSET:
			field_dict['source_unit'] = source_unit
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[CX], src_dict: Dict[str, Any]) -> CX:
		d = src_dict.copy()
		entity_ids = cast(List[str], d.pop("entity_ids", UNSET))

		material_density = d.pop("material_density", UNSET)

		_material_density_unit = d.pop("material_density_unit", UNSET)
		material_density_unit: Union[Unset, UnitDensity]
		if isinstance(_material_density_unit, Unset):
			material_density_unit = UNSET
		else:
			material_density_unit = _material_density_unit # type: ignore[arg-type]

		_output_unit = d.pop("output_unit", UNSET)
		output_unit: Union[Unset, UnitMass]
		if isinstance(_output_unit, Unset):
			output_unit = UNSET
		else:
			output_unit = _output_unit # type: ignore[arg-type]

		_source_unit = d.pop("source_unit", UNSET)
		source_unit: Union[Unset, UnitLength]
		if isinstance(_source_unit, Unset):
			source_unit = UNSET
		else:
			source_unit = _source_unit # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		mass = cls(
			entity_ids= entity_ids,
			material_density= material_density,
			material_density_unit= material_density_unit,
			output_unit= output_unit,
			source_unit= source_unit,
			type= type,
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




MT = TypeVar("MT", bound="density")

@attr.s(auto_attribs=True)
class density:
	""" Get the density of entities in the scene or the default scene. """ # noqa: E501
	entity_ids: Union[Unset, List[str]] = UNSET
	material_mass:  Union[Unset, float] = UNSET
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
			field_dict['entity_ids'] = entity_ids
		if material_mass is not UNSET:
			field_dict['material_mass'] = material_mass
		if material_mass_unit is not UNSET:
			field_dict['material_mass_unit'] = material_mass_unit
		if output_unit is not UNSET:
			field_dict['output_unit'] = output_unit
		if source_unit is not UNSET:
			field_dict['source_unit'] = source_unit
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[MT], src_dict: Dict[str, Any]) -> MT:
		d = src_dict.copy()
		entity_ids = cast(List[str], d.pop("entity_ids", UNSET))

		material_mass = d.pop("material_mass", UNSET)

		_material_mass_unit = d.pop("material_mass_unit", UNSET)
		material_mass_unit: Union[Unset, UnitMass]
		if isinstance(_material_mass_unit, Unset):
			material_mass_unit = UNSET
		else:
			material_mass_unit = _material_mass_unit # type: ignore[arg-type]

		_output_unit = d.pop("output_unit", UNSET)
		output_unit: Union[Unset, UnitDensity]
		if isinstance(_output_unit, Unset):
			output_unit = UNSET
		else:
			output_unit = _output_unit # type: ignore[arg-type]

		_source_unit = d.pop("source_unit", UNSET)
		source_unit: Union[Unset, UnitLength]
		if isinstance(_source_unit, Unset):
			source_unit = UNSET
		else:
			source_unit = _source_unit # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		density = cls(
			entity_ids= entity_ids,
			material_mass= material_mass,
			material_mass_unit= material_mass_unit,
			output_unit= output_unit,
			source_unit= source_unit,
			type= type,
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




LJ = TypeVar("LJ", bound="volume")

@attr.s(auto_attribs=True)
class volume:
	""" Get the volume of entities in the scene or the default scene. """ # noqa: E501
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
			field_dict['entity_ids'] = entity_ids
		if output_unit is not UNSET:
			field_dict['output_unit'] = output_unit
		if source_unit is not UNSET:
			field_dict['source_unit'] = source_unit
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[LJ], src_dict: Dict[str, Any]) -> LJ:
		d = src_dict.copy()
		entity_ids = cast(List[str], d.pop("entity_ids", UNSET))

		_output_unit = d.pop("output_unit", UNSET)
		output_unit: Union[Unset, UnitVolume]
		if isinstance(_output_unit, Unset):
			output_unit = UNSET
		else:
			output_unit = _output_unit # type: ignore[arg-type]

		_source_unit = d.pop("source_unit", UNSET)
		source_unit: Union[Unset, UnitLength]
		if isinstance(_source_unit, Unset):
			source_unit = UNSET
		else:
			source_unit = _source_unit # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		volume = cls(
			entity_ids= entity_ids,
			output_unit= output_unit,
			source_unit= source_unit,
			type= type,
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




TF = TypeVar("TF", bound="center_of_mass")

@attr.s(auto_attribs=True)
class center_of_mass:
	""" Get the center of mass of entities in the scene or the default scene. """ # noqa: E501
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
			field_dict['entity_ids'] = entity_ids
		if output_unit is not UNSET:
			field_dict['output_unit'] = output_unit
		if source_unit is not UNSET:
			field_dict['source_unit'] = source_unit
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[TF], src_dict: Dict[str, Any]) -> TF:
		d = src_dict.copy()
		entity_ids = cast(List[str], d.pop("entity_ids", UNSET))

		_output_unit = d.pop("output_unit", UNSET)
		output_unit: Union[Unset, UnitLength]
		if isinstance(_output_unit, Unset):
			output_unit = UNSET
		else:
			output_unit = _output_unit # type: ignore[arg-type]

		_source_unit = d.pop("source_unit", UNSET)
		source_unit: Union[Unset, UnitLength]
		if isinstance(_source_unit, Unset):
			source_unit = UNSET
		else:
			source_unit = _source_unit # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		center_of_mass = cls(
			entity_ids= entity_ids,
			output_unit= output_unit,
			source_unit= source_unit,
			type= type,
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




HF = TypeVar("HF", bound="surface_area")

@attr.s(auto_attribs=True)
class surface_area:
	""" Get the surface area of entities in the scene or the default scene. """ # noqa: E501
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
			field_dict['entity_ids'] = entity_ids
		if output_unit is not UNSET:
			field_dict['output_unit'] = output_unit
		if source_unit is not UNSET:
			field_dict['source_unit'] = source_unit
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[HF], src_dict: Dict[str, Any]) -> HF:
		d = src_dict.copy()
		entity_ids = cast(List[str], d.pop("entity_ids", UNSET))

		_output_unit = d.pop("output_unit", UNSET)
		output_unit: Union[Unset, UnitArea]
		if isinstance(_output_unit, Unset):
			output_unit = UNSET
		else:
			output_unit = _output_unit # type: ignore[arg-type]

		_source_unit = d.pop("source_unit", UNSET)
		source_unit: Union[Unset, UnitLength]
		if isinstance(_source_unit, Unset):
			source_unit = UNSET
		else:
			source_unit = _source_unit # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		surface_area = cls(
			entity_ids= entity_ids,
			output_unit= output_unit,
			source_unit= source_unit,
			type= type,
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

ModelingCmd = Union[start_path, move_path_pen, extend_path, extrude, close_path, camera_drag_start, camera_drag_move, camera_drag_end, default_camera_look_at, default_camera_zoom, default_camera_enable_sketch_mode, default_camera_disable_sketch_mode, export, entity_get_parent_id, entity_get_num_children, entity_get_child_uuid, entity_get_all_child_uuids, edit_mode_enter, edit_mode_exit, select_with_point, select_clear, select_add, select_remove, select_replace, select_get, highlight_set_entity, highlight_set_entities, new_annotation, update_annotation, object_visible, get_entity_type, solid3d_get_all_edge_faces, solid3d_get_all_opposite_edges, solid3d_get_opposite_edge, solid3d_get_next_adjacent_edge, solid3d_get_prev_adjacent_edge, send_object, entity_set_opacity, entity_fade, make_plane, plane_set_color, set_tool, mouse_move, mouse_click, sketch_mode_enable, sketch_mode_disable, curve_get_type, curve_get_control_points, take_snapshot, make_axes_gizmo, path_get_info, path_get_curve_uuids_for_vertices, handle_mouse_drag_start, handle_mouse_drag_move, handle_mouse_drag_end, remove_scene_objects, plane_intersect_and_project, curve_get_end_points, reconfigure_stream, import_files, mass, density, volume, center_of_mass, surface_area]
