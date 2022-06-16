import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.uuid import Uuid
from ..models.api_call_status import APICallStatus
from ..models.async_api_call_type import AsyncAPICallType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AsyncApiCall")


@attr.s(auto_attribs=True)
class AsyncApiCall:
    """ """
    completed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    error: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    input: Union[Unset, Any] = UNSET
    output: Union[Unset, Any] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, APICallStatus] = UNSET
    type: Union[Unset, AsyncAPICallType] = UNSET
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
        error = self.error
        id = self.id
        input = self.input
        output = self.output
        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value
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
        if error is not UNSET:
            field_dict['error'] = error
        if id is not UNSET:
            field_dict['id'] = id
        if input is not UNSET:
            field_dict['input'] = input
        if output is not UNSET:
            field_dict['output'] = output
        if started_at is not UNSET:
            field_dict['started_at'] = started_at
        if status is not UNSET:
            field_dict['status'] = status
        if type is not UNSET:
            field_dict['type'] = type
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

        error = d.pop("error", UNSET)

        id = d.pop("id", UNSET)

        input = d.pop("input", UNSET)
        output = d.pop("output", UNSET)
        _started_at = d.pop("started_at", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        _status = d.pop("status", UNSET)
        status: Union[Unset, APICallStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APICallStatus(_status)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AsyncAPICallType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AsyncAPICallType(_type)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user_id = d.pop("user_id", UNSET)

        worker = d.pop("worker", UNSET)

        async_api_call = cls(
            completed_at=completed_at,
            created_at=created_at,
            error=error,
            id=id,
            input=input,
            output=output,
            started_at=started_at,
            status=status,
            type=type,
            updated_at=updated_at,
            user_id=user_id,
            worker=worker,
        )

        async_api_call.additional_properties = d
        return async_api_call

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
