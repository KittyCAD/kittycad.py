from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

KU = TypeVar("KU", bound="Solid3dGetPrevAdjacentEdge")

@attr.s(auto_attribs=True)
class Solid3dGetPrevAdjacentEdge:
	""" The response from the `Solid3dGetPrevAdjacentEdge` command. """ # noqa: E501
	edge: Union[Unset, str] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		edge = self.edge

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if edge is not UNSET:
			field_dict['edge'] = edge

		return field_dict

	@classmethod
	def from_dict(cls: Type[KU], src_dict: Dict[str, Any]) -> KU:
		d = src_dict.copy()
		edge = d.pop("edge", UNSET)


		solid3d_get_prev_adjacent_edge = cls(
			edge= edge,
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
