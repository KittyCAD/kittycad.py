from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ai_plugin_api_type import AiPluginApiType
from ..types import UNSET, Unset

S = TypeVar("S", bound="AiPluginApi")


@attr.s(auto_attribs=True)
class AiPluginApi:
    """AI plugin api information."""  # noqa: E501

    is_user_authenticated: Union[Unset, bool] = False
    type: Union[Unset, AiPluginApiType] = UNSET
    url: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_user_authenticated = self.is_user_authenticated
        if not isinstance(self.type, Unset):
            type = self.type
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_user_authenticated is not UNSET:
            field_dict["is_user_authenticated"] = is_user_authenticated
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[S], src_dict: Dict[str, Any]) -> S:
        d = src_dict.copy()
        is_user_authenticated = d.pop("is_user_authenticated", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AiPluginApiType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AiPluginApiType(_type)

        url = d.pop("url", UNSET)

        ai_plugin_api = cls(
            is_user_authenticated=is_user_authenticated,
            type=type,
            url=url,
        )

        ai_plugin_api.additional_properties = d
        return ai_plugin_api

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
