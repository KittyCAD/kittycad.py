from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

AU = TypeVar("AU", bound="Solid3dGetAllOppositeEdges")

@attr.s(auto_attribs=True)
class Solid3dGetAllOppositeEdges:
	""" The response from the `Solid3dGetAllOppositeEdges` command. """ # noqa: E501
	edges: Union[Unset, List[str]] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		edges: Union[Unset, List[str]] = UNSET
		if not isinstance(self.edges, Unset):
			edges = self.edges

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if edges is not UNSET:
			field_dict['edges'] = edges

		return field_dict

	@classmethod
	def from_dict(cls: Type[AU], src_dict: Dict[str, Any]) -> AU:
		d = src_dict.copy()
		edges = cast(List[str], d.pop("edges", UNSET))


		solid3d_get_all_opposite_edges = cls(
			edges= edges,
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
