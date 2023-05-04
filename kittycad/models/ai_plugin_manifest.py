from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ai_plugin_api import AiPluginApi
from ..models.ai_plugin_auth import AiPluginAuth
from ..types import UNSET, Unset

N = TypeVar("N", bound="AiPluginManifest")


@attr.s(auto_attribs=True)
class AiPluginManifest:
    """AI plugin manifest.

    This is used for OpenAI's ChatGPT plugins. You can read more about them [here](https://platform.openai.com/docs/plugins/getting-started/plugin-manifest)."""  # noqa: E501

    api: Union[Unset, AiPluginApi] = UNSET
    auth: Union[Unset, AiPluginAuth] = UNSET
    contact_email: Union[Unset, str] = UNSET
    description_for_human: Union[Unset, str] = UNSET
    description_for_model: Union[Unset, str] = UNSET
    legal_info_url: Union[Unset, str] = UNSET
    logo_url: Union[Unset, str] = UNSET
    name_for_human: Union[Unset, str] = UNSET
    name_for_model: Union[Unset, str] = UNSET
    schema_version: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.api, Unset):
            api = self.api
        if not isinstance(self.auth, Unset):
            auth = self.auth
        contact_email = self.contact_email
        description_for_human = self.description_for_human
        description_for_model = self.description_for_model
        legal_info_url = self.legal_info_url
        logo_url = self.logo_url
        name_for_human = self.name_for_human
        name_for_model = self.name_for_model
        schema_version = self.schema_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api is not UNSET:
            field_dict["api"] = api
        if auth is not UNSET:
            field_dict["auth"] = auth
        if contact_email is not UNSET:
            field_dict["contact_email"] = contact_email
        if description_for_human is not UNSET:
            field_dict["description_for_human"] = description_for_human
        if description_for_model is not UNSET:
            field_dict["description_for_model"] = description_for_model
        if legal_info_url is not UNSET:
            field_dict["legal_info_url"] = legal_info_url
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if name_for_human is not UNSET:
            field_dict["name_for_human"] = name_for_human
        if name_for_model is not UNSET:
            field_dict["name_for_model"] = name_for_model
        if schema_version is not UNSET:
            field_dict["schema_version"] = schema_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[N], src_dict: Dict[str, Any]) -> N:
        d = src_dict.copy()
        _api = d.pop("api", UNSET)
        api: Union[Unset, AiPluginApi]
        if isinstance(_api, Unset):
            api = UNSET
        else:
            api = AiPluginApi(_api)

        _auth = d.pop("auth", UNSET)
        auth: Union[Unset, AiPluginAuth]
        if isinstance(_auth, Unset):
            auth = UNSET
        else:
            auth = AiPluginAuth(_auth)

        contact_email = d.pop("contact_email", UNSET)

        description_for_human = d.pop("description_for_human", UNSET)

        description_for_model = d.pop("description_for_model", UNSET)

        legal_info_url = d.pop("legal_info_url", UNSET)

        logo_url = d.pop("logo_url", UNSET)

        name_for_human = d.pop("name_for_human", UNSET)

        name_for_model = d.pop("name_for_model", UNSET)

        schema_version = d.pop("schema_version", UNSET)

        ai_plugin_manifest = cls(
            api=api,
            auth=auth,
            contact_email=contact_email,
            description_for_human=description_for_human,
            description_for_model=description_for_model,
            legal_info_url=legal_info_url,
            logo_url=logo_url,
            name_for_human=name_for_human,
            name_for_model=name_for_model,
            schema_version=schema_version,
        )

        ai_plugin_manifest.additional_properties = d
        return ai_plugin_manifest

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
