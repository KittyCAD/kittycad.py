from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

U = TypeVar("U", bound="AppClientInfo")


@attr.s(auto_attribs=True)
class AppClientInfo:
    """Information about a third party app client."""  # noqa: E501

    url: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[U], src_dict: Dict[str, Any]) -> U:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        app_client_info = cls(
            url=url,
        )

        app_client_info.additional_properties = d
        return app_client_info

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
