from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.point2d import Point2d
from ..types import UNSET, Unset

HR = TypeVar("HR", bound="PlaneIntersectAndProject")

@attr.s(auto_attribs=True)
class PlaneIntersectAndProject:
	""" Corresponding coordinates of given window coordinates, intersected on given plane. """ # noqa: E501
	plane_coordinates: Union[Unset, Point2d] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.plane_coordinates, Unset):
			plane_coordinates = self.plane_coordinates

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if plane_coordinates is not UNSET:
			field_dict['plane_coordinates'] = plane_coordinates

		return field_dict

	@classmethod
	def from_dict(cls: Type[HR], src_dict: Dict[str, Any]) -> HR:
		d = src_dict.copy()
		_plane_coordinates = d.pop("plane_coordinates", UNSET)
		plane_coordinates: Union[Unset, Point2d]
		if isinstance(_plane_coordinates, Unset):
			plane_coordinates = UNSET
		else:
			plane_coordinates = _plane_coordinates # type: ignore[arg-type]


		plane_intersect_and_project = cls(
			plane_coordinates= plane_coordinates,
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
