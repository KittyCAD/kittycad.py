import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_call_status import ApiCallStatus
from ..models.file_export_format import FileExportFormat
from ..models.file_import_format import FileImportFormat
from ..models.input_format import InputFormat
from ..models.output_format import OutputFormat
from ..models.point3d import Point3d
from ..models.unit_area import UnitArea
from ..models.unit_density import UnitDensity
from ..models.unit_length import UnitLength
from ..models.unit_mass import UnitMass
from ..models.unit_volume import UnitVolume
from ..models.uuid import Uuid
from ..types import UNSET, Unset

LB = TypeVar("LB", bound="FileConversion")


@attr.s(auto_attribs=True)
class FileConversion:
    """A file conversion."""  # noqa: E501

    completed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    error: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    output: Union[Unset, str] = UNSET
    output_format: Union[Unset, FileExportFormat] = UNSET
    output_format_options: Union[Unset, OutputFormat] = UNSET
    outputs: Union[Unset, Any] = UNSET
    src_format: Union[Unset, FileImportFormat] = UNSET
    src_format_options: Union[Unset, InputFormat] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, ApiCallStatus] = UNSET
    type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user_id: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()
        error = self.error
        id = self.id
        output = self.output
        if not isinstance(self.output_format, Unset):
            output_format = self.output_format
        if not isinstance(self.output_format_options, Unset):
            output_format_options = self.output_format_options
        outputs = self.outputs
        if not isinstance(self.src_format, Unset):
            src_format = self.src_format
        if not isinstance(self.src_format_options, Unset):
            src_format_options = self.src_format_options
        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()
        if not isinstance(self.status, Unset):
            status = self.status
        type = self.type
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if error is not UNSET:
            field_dict["error"] = error
        if id is not UNSET:
            field_dict["id"] = id
        if output is not UNSET:
            field_dict["output"] = output
        if output_format is not UNSET:
            field_dict["output_format"] = output_format
        if output_format_options is not UNSET:
            field_dict["output_format_options"] = output_format_options
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if src_format is not UNSET:
            field_dict["src_format"] = src_format
        if src_format_options is not UNSET:
            field_dict["src_format_options"] = src_format_options
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if type is not UNSET:
            field_dict["type"] = type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[LB], src_dict: Dict[str, Any]) -> LB:
        d = src_dict.copy()
        _completed_at = d.pop("completed_at", UNSET)
        completed_at: Union[Unset, datetime.datetime]
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        error = d.pop("error", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, Uuid]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = _id  # type: ignore[arg-type]

        output = d.pop("output", UNSET)

        _output_format = d.pop("output_format", UNSET)
        output_format: Union[Unset, FileExportFormat]
        if isinstance(_output_format, Unset):
            output_format = UNSET
        else:
            output_format = _output_format  # type: ignore[arg-type]

        _output_format_options = d.pop("output_format_options", UNSET)
        output_format_options: Union[Unset, OutputFormat]
        if isinstance(_output_format_options, Unset):
            output_format_options = UNSET
        else:
            output_format_options = _output_format_options  # type: ignore[arg-type]

        outputs = d.pop("outputs", UNSET)
        _src_format = d.pop("src_format", UNSET)
        src_format: Union[Unset, FileImportFormat]
        if isinstance(_src_format, Unset):
            src_format = UNSET
        else:
            src_format = _src_format  # type: ignore[arg-type]

        _src_format_options = d.pop("src_format_options", UNSET)
        src_format_options: Union[Unset, InputFormat]
        if isinstance(_src_format_options, Unset):
            src_format_options = UNSET
        else:
            src_format_options = _src_format_options  # type: ignore[arg-type]

        _started_at = d.pop("started_at", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ApiCallStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = _status  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user_id = d.pop("user_id", UNSET)

        file_conversion = cls(
            completed_at=completed_at,
            created_at=created_at,
            error=error,
            id=id,
            output=output,
            output_format=output_format,
            output_format_options=output_format_options,
            outputs=outputs,
            src_format=src_format,
            src_format_options=src_format_options,
            started_at=started_at,
            status=status,
            type=type,
            updated_at=updated_at,
            user_id=user_id,
        )

        file_conversion.additional_properties = d
        return file_conversion

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


NE = TypeVar("NE", bound="FileCenterOfMass")


@attr.s(auto_attribs=True)
class FileCenterOfMass:
    """File center of mass."""  # noqa: E501

    center_of_mass: Union[Unset, Point3d] = UNSET
    centers_of_mass: Union[Unset, Any] = UNSET
    completed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    error: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    output_unit: Union[Unset, UnitLength] = UNSET
    src_format: Union[Unset, FileImportFormat] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, ApiCallStatus] = UNSET
    type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user_id: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.center_of_mass, Unset):
            center_of_mass = self.center_of_mass
        centers_of_mass = self.centers_of_mass
        completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()
        error = self.error
        id = self.id
        if not isinstance(self.output_unit, Unset):
            output_unit = self.output_unit
        if not isinstance(self.src_format, Unset):
            src_format = self.src_format
        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()
        if not isinstance(self.status, Unset):
            status = self.status
        type = self.type
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if center_of_mass is not UNSET:
            field_dict["center_of_mass"] = center_of_mass
        if centers_of_mass is not UNSET:
            field_dict["centers_of_mass"] = centers_of_mass
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if error is not UNSET:
            field_dict["error"] = error
        if id is not UNSET:
            field_dict["id"] = id
        if output_unit is not UNSET:
            field_dict["output_unit"] = output_unit
        if src_format is not UNSET:
            field_dict["src_format"] = src_format
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if type is not UNSET:
            field_dict["type"] = type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[NE], src_dict: Dict[str, Any]) -> NE:
        d = src_dict.copy()
        _center_of_mass = d.pop("center_of_mass", UNSET)
        center_of_mass: Union[Unset, Point3d]
        if isinstance(_center_of_mass, Unset):
            center_of_mass = UNSET
        else:
            center_of_mass = _center_of_mass  # type: ignore[arg-type]

        centers_of_mass = d.pop("centers_of_mass", UNSET)
        _completed_at = d.pop("completed_at", UNSET)
        completed_at: Union[Unset, datetime.datetime]
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        error = d.pop("error", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, Uuid]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = _id  # type: ignore[arg-type]

        _output_unit = d.pop("output_unit", UNSET)
        output_unit: Union[Unset, UnitLength]
        if isinstance(_output_unit, Unset):
            output_unit = UNSET
        else:
            output_unit = _output_unit  # type: ignore[arg-type]

        _src_format = d.pop("src_format", UNSET)
        src_format: Union[Unset, FileImportFormat]
        if isinstance(_src_format, Unset):
            src_format = UNSET
        else:
            src_format = _src_format  # type: ignore[arg-type]

        _started_at = d.pop("started_at", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ApiCallStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = _status  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user_id = d.pop("user_id", UNSET)

        file_center_of_mass = cls(
            center_of_mass=center_of_mass,
            centers_of_mass=centers_of_mass,
            completed_at=completed_at,
            created_at=created_at,
            error=error,
            id=id,
            output_unit=output_unit,
            src_format=src_format,
            started_at=started_at,
            status=status,
            type=type,
            updated_at=updated_at,
            user_id=user_id,
        )

        file_center_of_mass.additional_properties = d
        return file_center_of_mass

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


TL = TypeVar("TL", bound="FileMass")


@attr.s(auto_attribs=True)
class FileMass:
    """A file mass."""  # noqa: E501

    completed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    error: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    mass: Union[Unset, float] = UNSET
    masses: Union[Unset, Any] = UNSET
    material_density: Union[Unset, float] = UNSET
    material_density_unit: Union[Unset, UnitDensity] = UNSET
    output_unit: Union[Unset, UnitMass] = UNSET
    src_format: Union[Unset, FileImportFormat] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, ApiCallStatus] = UNSET
    type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user_id: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()
        error = self.error
        id = self.id
        mass = self.mass
        masses = self.masses
        material_density = self.material_density
        if not isinstance(self.material_density_unit, Unset):
            material_density_unit = self.material_density_unit
        if not isinstance(self.output_unit, Unset):
            output_unit = self.output_unit
        if not isinstance(self.src_format, Unset):
            src_format = self.src_format
        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()
        if not isinstance(self.status, Unset):
            status = self.status
        type = self.type
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if error is not UNSET:
            field_dict["error"] = error
        if id is not UNSET:
            field_dict["id"] = id
        if mass is not UNSET:
            field_dict["mass"] = mass
        if masses is not UNSET:
            field_dict["masses"] = masses
        if material_density is not UNSET:
            field_dict["material_density"] = material_density
        if material_density_unit is not UNSET:
            field_dict["material_density_unit"] = material_density_unit
        if output_unit is not UNSET:
            field_dict["output_unit"] = output_unit
        if src_format is not UNSET:
            field_dict["src_format"] = src_format
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if type is not UNSET:
            field_dict["type"] = type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[TL], src_dict: Dict[str, Any]) -> TL:
        d = src_dict.copy()
        _completed_at = d.pop("completed_at", UNSET)
        completed_at: Union[Unset, datetime.datetime]
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        error = d.pop("error", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, Uuid]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = _id  # type: ignore[arg-type]

        mass = d.pop("mass", UNSET)

        masses = d.pop("masses", UNSET)
        material_density = d.pop("material_density", UNSET)

        _material_density_unit = d.pop("material_density_unit", UNSET)
        material_density_unit: Union[Unset, UnitDensity]
        if isinstance(_material_density_unit, Unset):
            material_density_unit = UNSET
        else:
            material_density_unit = _material_density_unit  # type: ignore[arg-type]

        _output_unit = d.pop("output_unit", UNSET)
        output_unit: Union[Unset, UnitMass]
        if isinstance(_output_unit, Unset):
            output_unit = UNSET
        else:
            output_unit = _output_unit  # type: ignore[arg-type]

        _src_format = d.pop("src_format", UNSET)
        src_format: Union[Unset, FileImportFormat]
        if isinstance(_src_format, Unset):
            src_format = UNSET
        else:
            src_format = _src_format  # type: ignore[arg-type]

        _started_at = d.pop("started_at", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ApiCallStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = _status  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user_id = d.pop("user_id", UNSET)

        file_mass = cls(
            completed_at=completed_at,
            created_at=created_at,
            error=error,
            id=id,
            mass=mass,
            masses=masses,
            material_density=material_density,
            material_density_unit=material_density_unit,
            output_unit=output_unit,
            src_format=src_format,
            started_at=started_at,
            status=status,
            type=type,
            updated_at=updated_at,
            user_id=user_id,
        )

        file_mass.additional_properties = d
        return file_mass

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


MN = TypeVar("MN", bound="FileVolume")


@attr.s(auto_attribs=True)
class FileVolume:
    """A file volume."""  # noqa: E501

    completed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    error: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    output_unit: Union[Unset, UnitVolume] = UNSET
    src_format: Union[Unset, FileImportFormat] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, ApiCallStatus] = UNSET
    type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user_id: Union[Unset, str] = UNSET
    volume: Union[Unset, float] = UNSET
    volumes: Union[Unset, Any] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()
        error = self.error
        id = self.id
        if not isinstance(self.output_unit, Unset):
            output_unit = self.output_unit
        if not isinstance(self.src_format, Unset):
            src_format = self.src_format
        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()
        if not isinstance(self.status, Unset):
            status = self.status
        type = self.type
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()
        user_id = self.user_id
        volume = self.volume
        volumes = self.volumes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if error is not UNSET:
            field_dict["error"] = error
        if id is not UNSET:
            field_dict["id"] = id
        if output_unit is not UNSET:
            field_dict["output_unit"] = output_unit
        if src_format is not UNSET:
            field_dict["src_format"] = src_format
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if type is not UNSET:
            field_dict["type"] = type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if volume is not UNSET:
            field_dict["volume"] = volume
        if volumes is not UNSET:
            field_dict["volumes"] = volumes

        return field_dict

    @classmethod
    def from_dict(cls: Type[MN], src_dict: Dict[str, Any]) -> MN:
        d = src_dict.copy()
        _completed_at = d.pop("completed_at", UNSET)
        completed_at: Union[Unset, datetime.datetime]
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        error = d.pop("error", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, Uuid]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = _id  # type: ignore[arg-type]

        _output_unit = d.pop("output_unit", UNSET)
        output_unit: Union[Unset, UnitVolume]
        if isinstance(_output_unit, Unset):
            output_unit = UNSET
        else:
            output_unit = _output_unit  # type: ignore[arg-type]

        _src_format = d.pop("src_format", UNSET)
        src_format: Union[Unset, FileImportFormat]
        if isinstance(_src_format, Unset):
            src_format = UNSET
        else:
            src_format = _src_format  # type: ignore[arg-type]

        _started_at = d.pop("started_at", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ApiCallStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = _status  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user_id = d.pop("user_id", UNSET)

        volume = d.pop("volume", UNSET)

        volumes = d.pop("volumes", UNSET)

        file_volume = cls(
            completed_at=completed_at,
            created_at=created_at,
            error=error,
            id=id,
            output_unit=output_unit,
            src_format=src_format,
            started_at=started_at,
            status=status,
            type=type,
            updated_at=updated_at,
            user_id=user_id,
            volume=volume,
            volumes=volumes,
        )

        file_volume.additional_properties = d
        return file_volume

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


JV = TypeVar("JV", bound="FileDensity")


@attr.s(auto_attribs=True)
class FileDensity:
    """A file density."""  # noqa: E501

    completed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    densities: Union[Unset, Any] = UNSET
    density: Union[Unset, float] = UNSET
    error: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    material_mass: Union[Unset, float] = UNSET
    material_mass_unit: Union[Unset, UnitMass] = UNSET
    output_unit: Union[Unset, UnitDensity] = UNSET
    src_format: Union[Unset, FileImportFormat] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, ApiCallStatus] = UNSET
    type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user_id: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()
        densities = self.densities
        density = self.density
        error = self.error
        id = self.id
        material_mass = self.material_mass
        if not isinstance(self.material_mass_unit, Unset):
            material_mass_unit = self.material_mass_unit
        if not isinstance(self.output_unit, Unset):
            output_unit = self.output_unit
        if not isinstance(self.src_format, Unset):
            src_format = self.src_format
        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()
        if not isinstance(self.status, Unset):
            status = self.status
        type = self.type
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if densities is not UNSET:
            field_dict["densities"] = densities
        if density is not UNSET:
            field_dict["density"] = density
        if error is not UNSET:
            field_dict["error"] = error
        if id is not UNSET:
            field_dict["id"] = id
        if material_mass is not UNSET:
            field_dict["material_mass"] = material_mass
        if material_mass_unit is not UNSET:
            field_dict["material_mass_unit"] = material_mass_unit
        if output_unit is not UNSET:
            field_dict["output_unit"] = output_unit
        if src_format is not UNSET:
            field_dict["src_format"] = src_format
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if type is not UNSET:
            field_dict["type"] = type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[JV], src_dict: Dict[str, Any]) -> JV:
        d = src_dict.copy()
        _completed_at = d.pop("completed_at", UNSET)
        completed_at: Union[Unset, datetime.datetime]
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        densities = d.pop("densities", UNSET)
        density = d.pop("density", UNSET)

        error = d.pop("error", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, Uuid]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = _id  # type: ignore[arg-type]

        material_mass = d.pop("material_mass", UNSET)

        _material_mass_unit = d.pop("material_mass_unit", UNSET)
        material_mass_unit: Union[Unset, UnitMass]
        if isinstance(_material_mass_unit, Unset):
            material_mass_unit = UNSET
        else:
            material_mass_unit = _material_mass_unit  # type: ignore[arg-type]

        _output_unit = d.pop("output_unit", UNSET)
        output_unit: Union[Unset, UnitDensity]
        if isinstance(_output_unit, Unset):
            output_unit = UNSET
        else:
            output_unit = _output_unit  # type: ignore[arg-type]

        _src_format = d.pop("src_format", UNSET)
        src_format: Union[Unset, FileImportFormat]
        if isinstance(_src_format, Unset):
            src_format = UNSET
        else:
            src_format = _src_format  # type: ignore[arg-type]

        _started_at = d.pop("started_at", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ApiCallStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = _status  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user_id = d.pop("user_id", UNSET)

        file_density = cls(
            completed_at=completed_at,
            created_at=created_at,
            densities=densities,
            density=density,
            error=error,
            id=id,
            material_mass=material_mass,
            material_mass_unit=material_mass_unit,
            output_unit=output_unit,
            src_format=src_format,
            started_at=started_at,
            status=status,
            type=type,
            updated_at=updated_at,
            user_id=user_id,
        )

        file_density.additional_properties = d
        return file_density

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


IO = TypeVar("IO", bound="FileSurfaceArea")


@attr.s(auto_attribs=True)
class FileSurfaceArea:
    """A file surface area."""  # noqa: E501

    completed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    error: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    output_unit: Union[Unset, UnitArea] = UNSET
    src_format: Union[Unset, FileImportFormat] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, ApiCallStatus] = UNSET
    surface_area: Union[Unset, float] = UNSET
    surface_areas: Union[Unset, Any] = UNSET
    type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user_id: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()
        error = self.error
        id = self.id
        if not isinstance(self.output_unit, Unset):
            output_unit = self.output_unit
        if not isinstance(self.src_format, Unset):
            src_format = self.src_format
        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()
        if not isinstance(self.status, Unset):
            status = self.status
        surface_area = self.surface_area
        surface_areas = self.surface_areas
        type = self.type
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if error is not UNSET:
            field_dict["error"] = error
        if id is not UNSET:
            field_dict["id"] = id
        if output_unit is not UNSET:
            field_dict["output_unit"] = output_unit
        if src_format is not UNSET:
            field_dict["src_format"] = src_format
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if surface_area is not UNSET:
            field_dict["surface_area"] = surface_area
        if surface_areas is not UNSET:
            field_dict["surface_areas"] = surface_areas
        if type is not UNSET:
            field_dict["type"] = type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[IO], src_dict: Dict[str, Any]) -> IO:
        d = src_dict.copy()
        _completed_at = d.pop("completed_at", UNSET)
        completed_at: Union[Unset, datetime.datetime]
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        error = d.pop("error", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, Uuid]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = _id  # type: ignore[arg-type]

        _output_unit = d.pop("output_unit", UNSET)
        output_unit: Union[Unset, UnitArea]
        if isinstance(_output_unit, Unset):
            output_unit = UNSET
        else:
            output_unit = _output_unit  # type: ignore[arg-type]

        _src_format = d.pop("src_format", UNSET)
        src_format: Union[Unset, FileImportFormat]
        if isinstance(_src_format, Unset):
            src_format = UNSET
        else:
            src_format = _src_format  # type: ignore[arg-type]

        _started_at = d.pop("started_at", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ApiCallStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = _status  # type: ignore[arg-type]

        surface_area = d.pop("surface_area", UNSET)

        surface_areas = d.pop("surface_areas", UNSET)
        type = d.pop("type", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user_id = d.pop("user_id", UNSET)

        file_surface_area = cls(
            completed_at=completed_at,
            created_at=created_at,
            error=error,
            id=id,
            output_unit=output_unit,
            src_format=src_format,
            started_at=started_at,
            status=status,
            surface_area=surface_area,
            surface_areas=surface_areas,
            type=type,
            updated_at=updated_at,
            user_id=user_id,
        )

        file_surface_area.additional_properties = d
        return file_surface_area

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


AsyncApiCallOutput = Union[
    FileConversion, FileCenterOfMass, FileMass, FileVolume, FileDensity, FileSurfaceArea
]
