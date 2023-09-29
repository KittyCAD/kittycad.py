from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

NH = TypeVar("NH", bound="CurveGetControlPoints")

@attr.s(auto_attribs=True)
class CurveGetControlPoints:
	""" The response from the `CurveGetControlPoints` command. """ # noqa: E501
	from ..models.point3d import Point3d
	control_points: Union[Unset, List[Point3d]] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		from ..models.point3d import Point3d
		control_points: Union[Unset, List[Point3d]] = UNSET
		if not isinstance(self.control_points, Unset):
			control_points = self.control_points

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if control_points is not UNSET:
			field_dict['control_points'] = control_points

		return field_dict

	@classmethod
	def from_dict(cls: Type[NH], src_dict: Dict[str, Any]) -> NH:
		d = src_dict.copy()
		from ..models.point3d import Point3d
		control_points = cast(List[Point3d], d.pop("control_points", UNSET))


		curve_get_control_points = cls(
			control_points= control_points,
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
