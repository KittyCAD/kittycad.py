from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.jetstream_api_stats import JetstreamApiStats
from ..types import UNSET, Unset

R = TypeVar("R", bound="JetstreamStats")


@attr.s(auto_attribs=True)
class JetstreamStats:
    """Jetstream statistics."""  # noqa: E501

    accounts: Union[Unset, int] = UNSET
    api: Union[Unset, JetstreamApiStats] = UNSET
    ha_assets: Union[Unset, int] = UNSET
    memory: Union[Unset, int] = UNSET
    reserved_memory: Union[Unset, int] = UNSET
    reserved_store: Union[Unset, int] = UNSET
    store: Union[Unset, int] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accounts = self.accounts
        if not isinstance(self.api, Unset):
            api = self.api
        ha_assets = self.ha_assets
        memory = self.memory
        reserved_memory = self.reserved_memory
        reserved_store = self.reserved_store
        store = self.store

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if api is not UNSET:
            field_dict["api"] = api
        if ha_assets is not UNSET:
            field_dict["ha_assets"] = ha_assets
        if memory is not UNSET:
            field_dict["memory"] = memory
        if reserved_memory is not UNSET:
            field_dict["reserved_memory"] = reserved_memory
        if reserved_store is not UNSET:
            field_dict["reserved_store"] = reserved_store
        if store is not UNSET:
            field_dict["store"] = store

        return field_dict

    @classmethod
    def from_dict(cls: Type[R], src_dict: Dict[str, Any]) -> R:
        d = src_dict.copy()
        accounts = d.pop("accounts", UNSET)

        _api = d.pop("api", UNSET)
        api: Union[Unset, JetstreamApiStats]
        if isinstance(_api, Unset):
            api = UNSET
        else:
            api = JetstreamApiStats(_api)

        ha_assets = d.pop("ha_assets", UNSET)

        memory = d.pop("memory", UNSET)

        reserved_memory = d.pop("reserved_memory", UNSET)

        reserved_store = d.pop("reserved_store", UNSET)

        store = d.pop("store", UNSET)

        jetstream_stats = cls(
            accounts=accounts,
            api=api,
            ha_assets=ha_assets,
            memory=memory,
            reserved_memory=reserved_memory,
            reserved_store=reserved_store,
            store=store,
        )

        jetstream_stats.additional_properties = d
        return jetstream_stats

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
