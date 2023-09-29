from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.fbx_storage import FbxStorage
from ..models.gltf_presentation import GltfPresentation
from ..models.gltf_storage import GltfStorage
from ..models.ply_storage import PlyStorage
from ..models.stl_storage import StlStorage
from ..models.system import System
from ..models.unit_length import UnitLength
from ..types import UNSET, Unset

BM = TypeVar("BM", bound="fbx")

@attr.s(auto_attribs=True)
class fbx:
	""" Autodesk Filmbox (FBX) format. """ # noqa: E501
	storage: Union[Unset, FbxStorage] = UNSET
	type: str = "fbx"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.storage, Unset):
			storage = self.storage
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if storage is not UNSET:
			field_dict['storage'] = storage
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[BM], src_dict: Dict[str, Any]) -> BM:
		d = src_dict.copy()
		_storage = d.pop("storage", UNSET)
		storage: Union[Unset, FbxStorage]
		if isinstance(_storage, Unset):
			storage = UNSET
		else:
			storage = _storage # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		fbx = cls(
			storage= storage,
			type= type,
		)

		fbx.additional_properties = d
		return fbx

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




TY = TypeVar("TY", bound="gltf")

@attr.s(auto_attribs=True)
class gltf:
	""" glTF 2.0. We refer to this as glTF since that is how our customers refer to it, although by default it will be in binary format and thus technically (glb). If you prefer ascii output, you can set that option for the export. """ # noqa: E501
	presentation: Union[Unset, GltfPresentation] = UNSET
	storage: Union[Unset, GltfStorage] = UNSET
	type: str = "gltf"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.presentation, Unset):
			presentation = self.presentation
		if not isinstance(self.storage, Unset):
			storage = self.storage
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if presentation is not UNSET:
			field_dict['presentation'] = presentation
		if storage is not UNSET:
			field_dict['storage'] = storage
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[TY], src_dict: Dict[str, Any]) -> TY:
		d = src_dict.copy()
		_presentation = d.pop("presentation", UNSET)
		presentation: Union[Unset, GltfPresentation]
		if isinstance(_presentation, Unset):
			presentation = UNSET
		else:
			presentation = _presentation # type: ignore[arg-type]

		_storage = d.pop("storage", UNSET)
		storage: Union[Unset, GltfStorage]
		if isinstance(_storage, Unset):
			storage = UNSET
		else:
			storage = _storage # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		gltf = cls(
			presentation= presentation,
			storage= storage,
			type= type,
		)

		gltf.additional_properties = d
		return gltf

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




NC = TypeVar("NC", bound="obj")

@attr.s(auto_attribs=True)
class obj:
	""" Wavefront OBJ format. """ # noqa: E501
	coords: Union[Unset, System] = UNSET
	type: str = "obj"
	units: Union[Unset, UnitLength] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.coords, Unset):
			coords = self.coords
		type = self.type
		if not isinstance(self.units, Unset):
			units = self.units

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if coords is not UNSET:
			field_dict['coords'] = coords
		field_dict['type'] = type
		if units is not UNSET:
			field_dict['units'] = units

		return field_dict

	@classmethod
	def from_dict(cls: Type[NC], src_dict: Dict[str, Any]) -> NC:
		d = src_dict.copy()
		_coords = d.pop("coords", UNSET)
		coords: Union[Unset, System]
		if isinstance(_coords, Unset):
			coords = UNSET
		else:
			coords = _coords # type: ignore[arg-type]

		type = d.pop("type", UNSET)

		_units = d.pop("units", UNSET)
		units: Union[Unset, UnitLength]
		if isinstance(_units, Unset):
			units = UNSET
		else:
			units = _units # type: ignore[arg-type]


		obj = cls(
			coords= coords,
			type= type,
			units= units,
		)

		obj.additional_properties = d
		return obj

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




GP = TypeVar("GP", bound="ply")

@attr.s(auto_attribs=True)
class ply:
	""" The PLY Polygon File Format. """ # noqa: E501
	coords: Union[Unset, System] = UNSET
	storage: Union[Unset, PlyStorage] = UNSET
	type: str = "ply"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.coords, Unset):
			coords = self.coords
		if not isinstance(self.storage, Unset):
			storage = self.storage
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if coords is not UNSET:
			field_dict['coords'] = coords
		if storage is not UNSET:
			field_dict['storage'] = storage
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[GP], src_dict: Dict[str, Any]) -> GP:
		d = src_dict.copy()
		_coords = d.pop("coords", UNSET)
		coords: Union[Unset, System]
		if isinstance(_coords, Unset):
			coords = UNSET
		else:
			coords = _coords # type: ignore[arg-type]

		_storage = d.pop("storage", UNSET)
		storage: Union[Unset, PlyStorage]
		if isinstance(_storage, Unset):
			storage = UNSET
		else:
			storage = _storage # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		ply = cls(
			coords= coords,
			storage= storage,
			type= type,
		)

		ply.additional_properties = d
		return ply

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




FF = TypeVar("FF", bound="step")

@attr.s(auto_attribs=True)
class step:
	""" ISO 10303-21 (STEP) format. """ # noqa: E501
	coords: Union[Unset, System] = UNSET
	type: str = "step"

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.coords, Unset):
			coords = self.coords
		type = self.type

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if coords is not UNSET:
			field_dict['coords'] = coords
		field_dict['type'] = type

		return field_dict

	@classmethod
	def from_dict(cls: Type[FF], src_dict: Dict[str, Any]) -> FF:
		d = src_dict.copy()
		_coords = d.pop("coords", UNSET)
		coords: Union[Unset, System]
		if isinstance(_coords, Unset):
			coords = UNSET
		else:
			coords = _coords # type: ignore[arg-type]

		type = d.pop("type", UNSET)


		step = cls(
			coords= coords,
			type= type,
		)

		step.additional_properties = d
		return step

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




YO = TypeVar("YO", bound="stl")

@attr.s(auto_attribs=True)
class stl:
	""" *ST**ereo**L**ithography format. """ # noqa: E501
	coords: Union[Unset, System] = UNSET
	storage: Union[Unset, StlStorage] = UNSET
	type: str = "stl"
	units: Union[Unset, UnitLength] = UNSET

	additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

	def to_dict(self) -> Dict[str, Any]:
		if not isinstance(self.coords, Unset):
			coords = self.coords
		if not isinstance(self.storage, Unset):
			storage = self.storage
		type = self.type
		if not isinstance(self.units, Unset):
			units = self.units

		field_dict: Dict[str, Any] = {}
		field_dict.update(self.additional_properties)
		field_dict.update({})
		if coords is not UNSET:
			field_dict['coords'] = coords
		if storage is not UNSET:
			field_dict['storage'] = storage
		field_dict['type'] = type
		if units is not UNSET:
			field_dict['units'] = units

		return field_dict

	@classmethod
	def from_dict(cls: Type[YO], src_dict: Dict[str, Any]) -> YO:
		d = src_dict.copy()
		_coords = d.pop("coords", UNSET)
		coords: Union[Unset, System]
		if isinstance(_coords, Unset):
			coords = UNSET
		else:
			coords = _coords # type: ignore[arg-type]

		_storage = d.pop("storage", UNSET)
		storage: Union[Unset, StlStorage]
		if isinstance(_storage, Unset):
			storage = UNSET
		else:
			storage = _storage # type: ignore[arg-type]

		type = d.pop("type", UNSET)

		_units = d.pop("units", UNSET)
		units: Union[Unset, UnitLength]
		if isinstance(_units, Unset):
			units = UNSET
		else:
			units = _units # type: ignore[arg-type]


		stl = cls(
			coords= coords,
			storage= storage,
			type= type,
			units= units,
		)

		stl.additional_properties = d
		return stl

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

OutputFormat = Union[fbx, gltf, obj, ply, step, stl]
