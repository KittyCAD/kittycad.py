import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.method import Method
from ..models.uuid import Uuid
from ..types import UNSET, Unset

S = TypeVar("S", bound="ApiCallWithPrice")


@attr.s(auto_attribs=True)
class ApiCallWithPrice:
    """An API call with the price.

    This is a join of the `ApiCall` and `ApiCallPrice` tables."""  # noqa: E501

    completed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    duration: Union[Unset, int] = UNSET
    email: Union[Unset, str] = UNSET
    endpoint: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    litterbox: Union[Unset, bool] = False
    method: Union[Unset, Method] = UNSET
    minutes: Union[Unset, int] = UNSET
    origin: Union[Unset, str] = UNSET
    price: Union[Unset, float] = UNSET
    request_body: Union[Unset, str] = UNSET
    request_query_params: Union[Unset, str] = UNSET
    response_body: Union[Unset, str] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    status_code: Union[Unset, int] = UNSET
    stripe_invoice_item_id: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user_agent: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()
        duration = self.duration
        email = self.email
        endpoint = self.endpoint
        id = self.id
        ip_address = self.ip_address
        litterbox = self.litterbox
        if not isinstance(self.method, Unset):
            method = self.method
        minutes = self.minutes
        origin = self.origin
        price = self.price
        request_body = self.request_body
        request_query_params = self.request_query_params
        response_body = self.response_body
        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()
        status_code = self.status_code
        stripe_invoice_item_id = self.stripe_invoice_item_id
        token = self.token
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()
        user_agent = self.user_agent
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if duration is not UNSET:
            field_dict["duration"] = duration
        if email is not UNSET:
            field_dict["email"] = email
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if id is not UNSET:
            field_dict["id"] = id
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if litterbox is not UNSET:
            field_dict["litterbox"] = litterbox
        if method is not UNSET:
            field_dict["method"] = method
        if minutes is not UNSET:
            field_dict["minutes"] = minutes
        if origin is not UNSET:
            field_dict["origin"] = origin
        if price is not UNSET:
            field_dict["price"] = price
        if request_body is not UNSET:
            field_dict["request_body"] = request_body
        if request_query_params is not UNSET:
            field_dict["request_query_params"] = request_query_params
        if response_body is not UNSET:
            field_dict["response_body"] = response_body
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status_code is not UNSET:
            field_dict["status_code"] = status_code
        if stripe_invoice_item_id is not UNSET:
            field_dict["stripe_invoice_item_id"] = stripe_invoice_item_id
        if token is not UNSET:
            field_dict["token"] = token
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[S], src_dict: Dict[str, Any]) -> S:
        d = src_dict.copy()
        _completed_at = d.pop("completed_at", UNSET)
        completed_at: Union[Unset, datetime.datetime]
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        duration = d.pop("duration", UNSET)

        email = d.pop("email", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, Uuid]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = Uuid(_id)

        ip_address = d.pop("ip_address", UNSET)

        litterbox = d.pop("litterbox", UNSET)

        _method = d.pop("method", UNSET)
        method: Union[Unset, Method]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = Method(_method)

        minutes = d.pop("minutes", UNSET)

        origin = d.pop("origin", UNSET)

        price = d.pop("price", UNSET)

        request_body = d.pop("request_body", UNSET)

        request_query_params = d.pop("request_query_params", UNSET)

        response_body = d.pop("response_body", UNSET)

        _started_at = d.pop("started_at", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        status_code = d.pop("status_code", UNSET)

        stripe_invoice_item_id = d.pop("stripe_invoice_item_id", UNSET)

        _token = d.pop("token", UNSET)
        token: Union[Unset, Uuid]
        if isinstance(_token, Unset):
            token = UNSET
        else:
            token = Uuid(_token)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user_agent = d.pop("user_agent", UNSET)

        user_id = d.pop("user_id", UNSET)

        api_call_with_price = cls(
            completed_at=completed_at,
            created_at=created_at,
            duration=duration,
            email=email,
            endpoint=endpoint,
            id=id,
            ip_address=ip_address,
            litterbox=litterbox,
            method=method,
            minutes=minutes,
            origin=origin,
            price=price,
            request_body=request_body,
            request_query_params=request_query_params,
            response_body=response_body,
            started_at=started_at,
            status_code=status_code,
            stripe_invoice_item_id=stripe_invoice_item_id,
            token=token,
            updated_at=updated_at,
            user_agent=user_agent,
            user_id=user_id,
        )

        api_call_with_price.additional_properties = d
        return api_call_with_price

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
