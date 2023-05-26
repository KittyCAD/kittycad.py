from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.country_code import CountryCode
from ..types import UNSET, Unset

B = TypeVar("B", bound="NewAddress")


@attr.s(auto_attribs=True)
class NewAddress:
    """The struct that is used to create a new record. This is automatically generated and has all the same fields as the main struct only it is missing the `id`."""  # noqa: E501

    city: Union[Unset, str] = UNSET
    country: Union[Unset, CountryCode] = UNSET
    state: Union[Unset, str] = UNSET
    street1: Union[Unset, str] = UNSET
    street2: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    zip: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        city = self.city
        if not isinstance(self.country, Unset):
            country = self.country
        state = self.state
        street1 = self.street1
        street2 = self.street2
        user_id = self.user_id
        zip = self.zip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if state is not UNSET:
            field_dict["state"] = state
        if street1 is not UNSET:
            field_dict["street1"] = street1
        if street2 is not UNSET:
            field_dict["street2"] = street2
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if zip is not UNSET:
            field_dict["zip"] = zip

        return field_dict

    @classmethod
    def from_dict(cls: Type[B], src_dict: Dict[str, Any]) -> B:
        d = src_dict.copy()
        city = d.pop("city", UNSET)

        _country = d.pop("country", UNSET)
        country: Union[Unset, CountryCode]
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = CountryCode(_country)

        state = d.pop("state", UNSET)

        street1 = d.pop("street1", UNSET)

        street2 = d.pop("street2", UNSET)

        user_id = d.pop("user_id", UNSET)

        zip = d.pop("zip", UNSET)

        new_address = cls(
            city=city,
            country=country,
            state=state,
            street1=street1,
            street2=street2,
            user_id=user_id,
            zip=zip,
        )

        new_address.additional_properties = d
        return new_address

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
