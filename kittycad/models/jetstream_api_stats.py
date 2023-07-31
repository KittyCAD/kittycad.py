from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

K = TypeVar("K", bound="JetstreamApiStats")


@attr.s(auto_attribs=True)
class JetstreamApiStats:
    """Jetstream API statistics."""  # noqa: E501

    errors: Union[Unset, int] = UNSET
    inflight: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        errors = self.errors
        inflight = self.inflight
        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if inflight is not UNSET:
            field_dict["inflight"] = inflight
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[K], src_dict: Dict[str, Any]) -> K:
        d = src_dict.copy()
        errors = d.pop("errors", UNSET)

        inflight = d.pop("inflight", UNSET)

        total = d.pop("total", UNSET)

        jetstream_api_stats = cls(
            errors=errors,
            inflight=inflight,
            total=total,
        )

        jetstream_api_stats.additional_properties = d
        return jetstream_api_stats

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
