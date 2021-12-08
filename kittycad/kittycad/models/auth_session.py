import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthSession")


@attr.s(auto_attribs=True)
class AuthSession:
    """ """

    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    is_valid: Union[Unset, bool] = False
    token: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id
        ip_address = self.ip_address
        is_valid = self.is_valid
        token = self.token
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if is_valid is not UNSET:
            field_dict["is_valid"] = is_valid
        if token is not UNSET:
            field_dict["token"] = token
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        id = d.pop("id", UNSET)

        ip_address = d.pop("ip_address", UNSET)

        is_valid = d.pop("is_valid", UNSET)

        token = d.pop("token", UNSET)

        user_id = d.pop("user_id", UNSET)

        auth_session = cls(
            created_at=created_at,
            id=id,
            ip_address=ip_address,
            is_valid=is_valid,
            token=token,
            user_id=user_id,
        )

        auth_session.additional_properties = d
        return auth_session

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
