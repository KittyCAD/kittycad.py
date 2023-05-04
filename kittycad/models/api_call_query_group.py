from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

P = TypeVar("P", bound="ApiCallQueryGroup")


@attr.s(auto_attribs=True)
class ApiCallQueryGroup:
    """A response for a query on the API call table that is grouped by something."""  # noqa: E501

    count: Union[Unset, int] = UNSET
    query: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        query = self.query

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: Type[P], src_dict: Dict[str, Any]) -> P:
        d = src_dict.copy()
        count = d.pop("count", UNSET)

        query = d.pop("query", UNSET)

        api_call_query_group = cls(
            count=count,
            query=query,
        )

        api_call_query_group.additional_properties = d
        return api_call_query_group

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
