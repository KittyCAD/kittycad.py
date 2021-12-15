import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.file_conversion_status import FileConversionStatus
from ..models.valid_file_types import ValidFileTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileConversion")


@attr.s(auto_attribs=True)
class FileConversion:
    """ """

    completed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    output: Union[Unset, str] = UNSET
    output_format: Union[Unset, ValidFileTypes] = UNSET
    src_format: Union[Unset, ValidFileTypes] = UNSET
    status: Union[Unset, FileConversionStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id
        output = self.output
        output_format: Union[Unset, str] = UNSET
        if not isinstance(self.output_format, Unset):
            output_format = self.output_format.value

        src_format: Union[Unset, str] = UNSET
        if not isinstance(self.src_format, Unset):
            src_format = self.src_format.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if output is not UNSET:
            field_dict["output"] = output
        if output_format is not UNSET:
            field_dict["output_format"] = output_format
        if src_format is not UNSET:
            field_dict["src_format"] = src_format
        if status is not UNSET:
            field_dict["status"] = status

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

        id = d.pop("id", UNSET)

        output = d.pop("output", UNSET)

        _output_format = d.pop("output_format", UNSET)
        output_format: Union[Unset, ValidFileTypes]
        if isinstance(_output_format, Unset):
            output_format = UNSET
        else:
            output_format = ValidFileTypes(_output_format)

        _src_format = d.pop("src_format", UNSET)
        src_format: Union[Unset, ValidFileTypes]
        if isinstance(_src_format, Unset):
            src_format = UNSET
        else:
            src_format = ValidFileTypes(_src_format)

        _status = d.pop("status", UNSET)
        status: Union[Unset, FileConversionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = FileConversionStatus(_status)

        file_conversion = cls(
            completed_at=completed_at,
            created_at=created_at,
            id=id,
            output=output,
            output_format=output_format,
            src_format=src_format,
            status=status,
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
