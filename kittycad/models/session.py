import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.uuid import Uuid
from ..types import UNSET, Unset

D = TypeVar("D", bound="Session")


@attr.s(auto_attribs=True)
class Session:
    """An authentication session.

    For our UIs, these are automatically created by Next.js."""  # noqa: E501

    created_at: Union[Unset, datetime.datetime] = UNSET
    expires: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    session_token: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user_id: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()
        expires: Union[Unset, str] = UNSET
        if not isinstance(self.expires, Unset):
            expires = self.expires.isoformat()
        id = self.id
        session_token = self.session_token
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if expires is not UNSET:
            field_dict["expires"] = expires
        if id is not UNSET:
            field_dict["id"] = id
        if session_token is not UNSET:
            field_dict["session_token"] = session_token
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[D], src_dict: Dict[str, Any]) -> D:
        d = src_dict.copy()
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _expires = d.pop("expires", UNSET)
        expires: Union[Unset, datetime.datetime]
        if isinstance(_expires, Unset):
            expires = UNSET
        else:
            expires = isoparse(_expires)

        id = d.pop("id", UNSET)

        _session_token = d.pop("session_token", UNSET)
        session_token: Union[Unset, Uuid]
        if isinstance(_session_token, Unset):
            session_token = UNSET
        else:
            session_token = Uuid(_session_token)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user_id = d.pop("user_id", UNSET)

        session = cls(
            created_at=created_at,
            expires=expires,
            id=id,
            session_token=session_token,
            updated_at=updated_at,
            user_id=user_id,
        )

        session.additional_properties = d
        return session

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
