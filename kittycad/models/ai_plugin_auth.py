from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ai_plugin_auth_type import AiPluginAuthType
from ..models.ai_plugin_http_auth_type import AiPluginHttpAuthType
from ..types import UNSET, Unset

B = TypeVar("B", bound="AiPluginAuth")


@attr.s(auto_attribs=True)
class AiPluginAuth:
    """AI plugin auth information."""  # noqa: E501

    authorization_type: Union[Unset, AiPluginHttpAuthType] = UNSET
    type: Union[Unset, AiPluginAuthType] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.authorization_type, Unset):
            authorization_type = self.authorization_type
        if not isinstance(self.type, Unset):
            type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorization_type is not UNSET:
            field_dict["authorization_type"] = authorization_type
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[B], src_dict: Dict[str, Any]) -> B:
        d = src_dict.copy()
        _authorization_type = d.pop("authorization_type", UNSET)
        authorization_type: Union[Unset, AiPluginHttpAuthType]
        if isinstance(_authorization_type, Unset):
            authorization_type = UNSET
        else:
            authorization_type = AiPluginHttpAuthType(_authorization_type)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AiPluginAuthType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AiPluginAuthType(_type)

        ai_plugin_auth = cls(
            authorization_type=authorization_type,
            type=type,
        )

        ai_plugin_auth.additional_properties = d
        return ai_plugin_auth

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
