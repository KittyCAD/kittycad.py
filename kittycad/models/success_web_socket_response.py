from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.ok_web_socket_response_data import OkWebSocketResponseData
from ..types import UNSET, Unset

ZV = TypeVar("ZV", bound="SuccessWebSocketResponse")


@attr.s(auto_attribs=True)
class SuccessWebSocketResponse:
    """Successful Websocket response."""  # noqa: E501

    request_id: Union[Unset, str] = UNSET
    resp: Union[Unset, OkWebSocketResponseData] = UNSET
    success: Union[Unset, bool] = False

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id
        resp: Union[Unset, OkWebSocketResponseData] = UNSET
        if not isinstance(self.resp, Unset):
            resp = self.resp
        success = self.success

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if resp is not UNSET:
            _resp: OkWebSocketResponseData = cast(OkWebSocketResponseData, resp)
            field_dict["resp"] = _resp.to_dict()
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: Type[ZV], src_dict: Dict[str, Any]) -> ZV:
        d = src_dict.copy()
        request_id = d.pop("request_id", UNSET)

        _resp = d.pop("resp", UNSET)
        resp: Union[Unset, OkWebSocketResponseData]
        if isinstance(_resp, Unset):
            resp = UNSET
        if _resp is None:
            resp = UNSET
        else:
            resp = OkWebSocketResponseData.from_dict(_resp)

        success = d.pop("success", UNSET)

        success_web_socket_response = cls(
            request_id=request_id,
            resp=resp,
            success=success,
        )

        success_web_socket_response.additional_properties = d
        return success_web_socket_response

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
