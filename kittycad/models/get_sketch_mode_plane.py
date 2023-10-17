from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.point3d import Point3d
from ..types import UNSET, Unset

TP = TypeVar("TP", bound="GetSketchModePlane")

@attr.s(auto_attribs=True)
class GetSketchModePlane:
	""" The plane for sketch mode. """ # noqa: E501
	x_axis: Union[Unset, Point3d] = UNSET
	y_axis: Union[Unset, Point3d] = UNSET
	z_axis: Union[Unset, Point3d] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.x_axis, Unset):
			x_axis = self.x_axis
		if not isinstance(self.y_axis, Unset):
			y_axis = self.y_axis
		if not isinstance(self.z_axis, Unset):
			z_axis = self.z_axis

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if x_axis is not UNSET:
			field_dict['x_axis'] = x_axis
		if y_axis is not UNSET:
			field_dict['y_axis'] = y_axis
		if z_axis is not UNSET:
			field_dict['z_axis'] = z_axis

		return field_dict

	@classmethod
	def from_dict(cls: Type[TP], src_dict: Dict[str, Any]) -> TP:
		d = src_dict.copy()
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

		_z_axis = d.pop("z_axis", UNSET)
		z_axis: Union[Unset, Point3d]
		if isinstance(_z_axis, Unset):
			z_axis = UNSET
		else:
			z_axis = _z_axis # type: ignore[arg-type]


		get_sketch_mode_plane = cls(
			x_axis= x_axis,
			y_axis= y_axis,
			z_axis= z_axis,
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
