import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.uuid import Uuid
from ..models.file_conversion_output_format import FileConversionOutputFormat
from ..models.file_conversion_source_format import FileConversionSourceFormat
from ..models.file_conversion_status import FileConversionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileConversion")


@attr.s(auto_attribs=True)
class FileConversion:
    """ """
    completed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, Uuid] = UNSET
    output_file_link: Union[Unset, str] = UNSET
    output_format: Union[Unset, FileConversionOutputFormat] = UNSET
    src_file_link: Union[Unset, str] = UNSET
    src_format: Union[Unset, FileConversionSourceFormat] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, FileConversionStatus] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user_id: Union[Unset, str] = UNSET
    worker: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.value
        output_file_link = self.output_file_link
        output_format: Union[Unset, str] = UNSET
        if not isinstance(self.output_format, Unset):
            output_format = self.output_format.value
        src_file_link = self.src_file_link
        src_format: Union[Unset, str] = UNSET
        if not isinstance(self.src_format, Unset):
            src_format = self.src_format.value
        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()
        user_id = self.user_id
        worker = self.worker

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completed_at is not UNSET:
            field_dict['completed_at'] = completed_at
        if created_at is not UNSET:
            field_dict['created_at'] = created_at
        if id is not UNSET:
            field_dict['id'] = id
        if output_file_link is not UNSET:
            field_dict['output_file_link'] = output_file_link
        if output_format is not UNSET:
            field_dict['output_format'] = output_format
        if src_file_link is not UNSET:
            field_dict['src_file_link'] = src_file_link
        if src_format is not UNSET:
            field_dict['src_format'] = src_format
        if started_at is not UNSET:
            field_dict['started_at'] = started_at
        if status is not UNSET:
            field_dict['status'] = status
        if updated_at is not UNSET:
            field_dict['updated_at'] = updated_at
        if user_id is not UNSET:
            field_dict['user_id'] = user_id
        if worker is not UNSET:
            field_dict['worker'] = worker

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

        _id = d.pop("id", UNSET)
        id: Union[Unset, Uuid]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = Uuid(_id)

        output_file_link = d.pop("output_file_link", UNSET)

        _output_format = d.pop("output_format", UNSET)
        output_format: Union[Unset, FileConversionOutputFormat]
        if isinstance(_output_format, Unset):
            output_format = UNSET
        else:
            output_format = FileConversionOutputFormat(_output_format)

        src_file_link = d.pop("src_file_link", UNSET)

        _src_format = d.pop("src_format", UNSET)
        src_format: Union[Unset, FileConversionSourceFormat]
        if isinstance(_src_format, Unset):
            src_format = UNSET
        else:
            src_format = FileConversionSourceFormat(_src_format)

        _started_at = d.pop("started_at", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        _status = d.pop("status", UNSET)
        status: Union[Unset, FileConversionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = FileConversionStatus(_status)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user_id = d.pop("user_id", UNSET)

        worker = d.pop("worker", UNSET)

        file_conversion = cls(
            completed_at=completed_at,
            created_at=created_at,
            id=id,
            output_file_link=output_file_link,
            output_format=output_format,
            src_file_link=src_file_link,
            src_format=src_format,
            started_at=started_at,
            status=status,
            updated_at=updated_at,
            user_id=user_id,
            worker=worker,
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
