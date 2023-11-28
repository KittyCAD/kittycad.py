import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.ai_feedback import AiFeedback
from ..models.ai_prompt_type import AiPromptType
from ..models.api_call_status import ApiCallStatus
from ..models.uuid import Uuid
from ..models.uuid_binary import UuidBinary
from ..types import UNSET, Unset

GO = TypeVar("GO", bound="AiPrompt")


@attr.s(auto_attribs=True)
class AiPrompt:
    """An AI prompt."""  # noqa: E501

    completed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    error: Union[Unset, str] = UNSET
    feedback: Union[Unset, AiFeedback] = UNSET
    id: Union[Unset, UuidBinary] = UNSET
    metadata: Union[Unset, Any] = UNSET
    model_version: Union[Unset, str] = UNSET
    output_file: Union[Unset, str] = UNSET
    prompt: Union[Unset, str] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, ApiCallStatus] = UNSET
    type: Union[Unset, AiPromptType] = UNSET
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
        if not isinstance(self.feedback, Unset):
            feedback = self.feedback
        if not isinstance(self.id, Unset):
            id = self.id
        metadata = self.metadata
        model_version = self.model_version
        output_file = self.output_file
        prompt = self.prompt
        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()
        if not isinstance(self.status, Unset):
            status = self.status
        if not isinstance(self.type, Unset):
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
        if feedback is not UNSET:
            field_dict["feedback"] = feedback
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if model_version is not UNSET:
            field_dict["model_version"] = model_version
        if output_file is not UNSET:
            field_dict["output_file"] = output_file
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
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
    def from_dict(cls: Type[GO], src_dict: Dict[str, Any]) -> GO:
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

        _feedback = d.pop("feedback", UNSET)
        feedback: Union[Unset, AiFeedback]
        if isinstance(_feedback, Unset):
            feedback = UNSET
        if _feedback is None:
            feedback = UNSET
        else:
            feedback = _feedback

        _id = d.pop("id", UNSET)
        id: Union[Unset, UuidBinary]
        if isinstance(_id, Unset):
            id = UNSET
        if _id is None:
            id = UNSET
        else:
            id = _id

        metadata = d.pop("metadata", UNSET)
        model_version = d.pop("model_version", UNSET)

        output_file = d.pop("output_file", UNSET)

        prompt = d.pop("prompt", UNSET)

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
        if _status is None:
            status = UNSET
        else:
            status = _status

        _type = d.pop("type", UNSET)
        type: Union[Unset, AiPromptType]
        if isinstance(_type, Unset):
            type = UNSET
        if _type is None:
            type = UNSET
        else:
            type = _type

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _user_id = d.pop("user_id", UNSET)
        user_id: Union[Unset, Uuid]
        if isinstance(_user_id, Unset):
            user_id = UNSET
        if _user_id is None:
            user_id = UNSET
        else:
            user_id = _user_id

        ai_prompt = cls(
            completed_at=completed_at,
            created_at=created_at,
            error=error,
            feedback=feedback,
            id=id,
            metadata=metadata,
            model_version=model_version,
            output_file=output_file,
            prompt=prompt,
            started_at=started_at,
            status=status,
            type=type,
            updated_at=updated_at,
            user_id=user_id,
        )

        ai_prompt.additional_properties = d
        return ai_prompt

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
