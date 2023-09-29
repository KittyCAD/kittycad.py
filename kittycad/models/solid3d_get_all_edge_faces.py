from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

ZB = TypeVar("ZB", bound="Solid3dGetAllEdgeFaces")

@attr.s(auto_attribs=True)
class Solid3dGetAllEdgeFaces:
	""" The response from the `Solid3dGetAllEdgeFaces` command. """ # noqa: E501
	faces: Union[Unset, List[str]] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		faces: Union[Unset, List[str]] = UNSET
		if not isinstance(self.faces, Unset):
			faces = self.faces

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if faces is not UNSET:
			field_dict['faces'] = faces

		return field_dict

	@classmethod
	def from_dict(cls: Type[ZB], src_dict: Dict[str, Any]) -> ZB:
		d = src_dict.copy()
		faces = cast(List[str], d.pop("faces", UNSET))


		solid3d_get_all_edge_faces = cls(
			faces= faces,
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
