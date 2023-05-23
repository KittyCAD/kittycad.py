from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegistryServiceConfig")


@attr.s(auto_attribs=True)
class RegistryServiceConfig:
    """RegistryServiceConfig stores daemon registry services configuration."""  # noqa: E501

    allow_nondistributable_artifacts_cid_rs: Union[Unset, List[str]] = UNSET
    allow_nondistributable_artifacts_hostnames: Union[Unset, List[str]] = UNSET
    index_configs: Union[Unset, Any] = UNSET
    insecure_registry_cid_rs: Union[Unset, List[str]] = UNSET
    mirrors: Union[Unset, List[str]] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allow_nondistributable_artifacts_cid_rs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allow_nondistributable_artifacts_cid_rs, Unset):
            allow_nondistributable_artifacts_cid_rs = (
                self.allow_nondistributable_artifacts_cid_rs
            )
        allow_nondistributable_artifacts_hostnames: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allow_nondistributable_artifacts_hostnames, Unset):
            allow_nondistributable_artifacts_hostnames = (
                self.allow_nondistributable_artifacts_hostnames
            )
        index_configs = self.index_configs
        insecure_registry_cid_rs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.insecure_registry_cid_rs, Unset):
            insecure_registry_cid_rs = self.insecure_registry_cid_rs
        mirrors: Union[Unset, List[str]] = UNSET
        if not isinstance(self.mirrors, Unset):
            mirrors = self.mirrors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_nondistributable_artifacts_cid_rs is not UNSET:
            field_dict[
                "allow_nondistributable_artifacts_cid_rs"
            ] = allow_nondistributable_artifacts_cid_rs
        if allow_nondistributable_artifacts_hostnames is not UNSET:
            field_dict[
                "allow_nondistributable_artifacts_hostnames"
            ] = allow_nondistributable_artifacts_hostnames
        if index_configs is not UNSET:
            field_dict["index_configs"] = index_configs
        if insecure_registry_cid_rs is not UNSET:
            field_dict["insecure_registry_cid_rs"] = insecure_registry_cid_rs
        if mirrors is not UNSET:
            field_dict["mirrors"] = mirrors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        allow_nondistributable_artifacts_cid_rs = cast(
            List[str], d.pop("allow_nondistributable_artifacts_cid_rs", UNSET)
        )

        allow_nondistributable_artifacts_hostnames = cast(
            List[str], d.pop("allow_nondistributable_artifacts_hostnames", UNSET)
        )

        index_configs = d.pop("index_configs", UNSET)
        insecure_registry_cid_rs = cast(
            List[str], d.pop("insecure_registry_cid_rs", UNSET)
        )

        mirrors = cast(List[str], d.pop("mirrors", UNSET))

        registry_service_config = cls(
            allow_nondistributable_artifacts_cid_rs=allow_nondistributable_artifacts_cid_rs,
            allow_nondistributable_artifacts_hostnames=allow_nondistributable_artifacts_hostnames,
            index_configs=index_configs,
            insecure_registry_cid_rs=insecure_registry_cid_rs,
            mirrors=mirrors,
        )

        registry_service_config.additional_properties = d
        return registry_service_config

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
