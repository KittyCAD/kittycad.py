import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.api_call_status import ApiCallStatus
from ..models.file_export_format import FileExportFormat
from ..models.file_import_format import FileImportFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileConversion")


@attr.s(auto_attribs=True)
class FileConversion:
    """A file conversion."""  # noqa: E501

    completed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    error: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    output: Union[Unset, str] = UNSET
    output_format: Union[Unset, FileExportFormat] = UNSET
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
        output = self.output
        output_format: Union[Unset, str] = UNSET
        if not isinstance(self.output_format, Unset):
            output_format = self.output_format
        src_format: Union[Unset, str] = UNSET
        if not isinstance(self.src_format, Unset):
            src_format = self.src_format
        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()
        status: Union[Unset, str] = UNSET
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        id = d.pop("id", UNSET)

        output = d.pop("output", UNSET)

        _output_format = d.pop("output_format", UNSET)
        output_format: Union[Unset, FileExportFormat]
        if isinstance(_output_format, Unset):
            output_format = UNSET
        else:
            output_format = FileExportFormat(_output_format)

        _src_format = d.pop("src_format", UNSET)
        src_format: Union[Unset, FileImportFormat]
        if isinstance(_src_format, Unset):
            src_format = UNSET
        else:
            src_format = FileImportFormat(_src_format)

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
            status = ApiCallStatus(_status)

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
            src_format=src_format,
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


T = TypeVar("T", bound="FileCenterOfMass")


@attr.s(auto_attribs=True)
class FileCenterOfMass:
    """File center of mass."""  # noqa: E501

    center_of_mass: Union[Unset, List[float]] = UNSET
    completed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    error: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    src_format: Union[Unset, FileImportFormat] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, ApiCallStatus] = UNSET
    type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user_id: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        center_of_mass: Union[Unset, List[float]] = UNSET
        if not isinstance(self.center_of_mass, Unset):
            center_of_mass = self.center_of_mass
        completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()
        error = self.error
        id = self.id
        src_format: Union[Unset, str] = UNSET
        if not isinstance(self.src_format, Unset):
            src_format = self.src_format
        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()
        status: Union[Unset, str] = UNSET
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
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if error is not UNSET:
            field_dict["error"] = error
        if id is not UNSET:
            field_dict["id"] = id
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        center_of_mass = cast(List[float], d.pop("center_of_mass", UNSET))

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

        id = d.pop("id", UNSET)

        _src_format = d.pop("src_format", UNSET)
        src_format: Union[Unset, FileImportFormat]
        if isinstance(_src_format, Unset):
            src_format = UNSET
        else:
            src_format = FileImportFormat(_src_format)

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
            status = ApiCallStatus(_status)

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
            completed_at=completed_at,
            created_at=created_at,
            error=error,
            id=id,
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


T = TypeVar("T", bound="FileMass")


@attr.s(auto_attribs=True)
class FileMass:
    """A file mass."""  # noqa: E501

    completed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    error: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    mass: Union[Unset, float] = UNSET
    material_density: Union[Unset, float] = UNSET
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
        material_density = self.material_density
        src_format: Union[Unset, str] = UNSET
        if not isinstance(self.src_format, Unset):
            src_format = self.src_format
        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()
        status: Union[Unset, str] = UNSET
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
        if material_density is not UNSET:
            field_dict["material_density"] = material_density
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        id = d.pop("id", UNSET)

        mass = d.pop("mass", UNSET)

        material_density = d.pop("material_density", UNSET)

        _src_format = d.pop("src_format", UNSET)
        src_format: Union[Unset, FileImportFormat]
        if isinstance(_src_format, Unset):
            src_format = UNSET
        else:
            src_format = FileImportFormat(_src_format)

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
            status = ApiCallStatus(_status)

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
            material_density=material_density,
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


T = TypeVar("T", bound="FileVolume")


@attr.s(auto_attribs=True)
class FileVolume:
    """A file volume."""  # noqa: E501

    completed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    error: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    src_format: Union[Unset, FileImportFormat] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, ApiCallStatus] = UNSET
    type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user_id: Union[Unset, str] = UNSET
    volume: Union[Unset, float] = UNSET

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
        src_format: Union[Unset, str] = UNSET
        if not isinstance(self.src_format, Unset):
            src_format = self.src_format
        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status
        type = self.type
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()
        user_id = self.user_id
        volume = self.volume

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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        id = d.pop("id", UNSET)

        _src_format = d.pop("src_format", UNSET)
        src_format: Union[Unset, FileImportFormat]
        if isinstance(_src_format, Unset):
            src_format = UNSET
        else:
            src_format = FileImportFormat(_src_format)

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
            status = ApiCallStatus(_status)

        type = d.pop("type", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user_id = d.pop("user_id", UNSET)

        volume = d.pop("volume", UNSET)

        file_volume = cls(
            completed_at=completed_at,
            created_at=created_at,
            error=error,
            id=id,
            src_format=src_format,
            started_at=started_at,
            status=status,
            type=type,
            updated_at=updated_at,
            user_id=user_id,
            volume=volume,
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


T = TypeVar("T", bound="FileDensity")


@attr.s(auto_attribs=True)
class FileDensity:
    """A file density."""  # noqa: E501

    completed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    density: Union[Unset, float] = UNSET
    error: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    material_mass: Union[Unset, float] = UNSET
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
        density = self.density
        error = self.error
        id = self.id
        material_mass = self.material_mass
        src_format: Union[Unset, str] = UNSET
        if not isinstance(self.src_format, Unset):
            src_format = self.src_format
        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()
        status: Union[Unset, str] = UNSET
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
        if density is not UNSET:
            field_dict["density"] = density
        if error is not UNSET:
            field_dict["error"] = error
        if id is not UNSET:
            field_dict["id"] = id
        if material_mass is not UNSET:
            field_dict["material_mass"] = material_mass
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        density = d.pop("density", UNSET)

        error = d.pop("error", UNSET)

        id = d.pop("id", UNSET)

        material_mass = d.pop("material_mass", UNSET)

        _src_format = d.pop("src_format", UNSET)
        src_format: Union[Unset, FileImportFormat]
        if isinstance(_src_format, Unset):
            src_format = UNSET
        else:
            src_format = FileImportFormat(_src_format)

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
            status = ApiCallStatus(_status)

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
            density=density,
            error=error,
            id=id,
            material_mass=material_mass,
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


T = TypeVar("T", bound="FileSurfaceArea")


@attr.s(auto_attribs=True)
class FileSurfaceArea:
    """A file surface area."""  # noqa: E501

    completed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    error: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    src_format: Union[Unset, FileImportFormat] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, ApiCallStatus] = UNSET
    surface_area: Union[Unset, float] = UNSET
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
        src_format: Union[Unset, str] = UNSET
        if not isinstance(self.src_format, Unset):
            src_format = self.src_format
        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status
        surface_area = self.surface_area
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
        if src_format is not UNSET:
            field_dict["src_format"] = src_format
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if surface_area is not UNSET:
            field_dict["surface_area"] = surface_area
        if type is not UNSET:
            field_dict["type"] = type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        id = d.pop("id", UNSET)

        _src_format = d.pop("src_format", UNSET)
        src_format: Union[Unset, FileImportFormat]
        if isinstance(_src_format, Unset):
            src_format = UNSET
        else:
            src_format = FileImportFormat(_src_format)

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
            status = ApiCallStatus(_status)

        surface_area = d.pop("surface_area", UNSET)

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
            src_format=src_format,
            started_at=started_at,
            status=status,
            surface_area=surface_area,
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