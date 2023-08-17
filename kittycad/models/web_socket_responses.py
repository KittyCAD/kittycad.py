from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.modeling_cmd_id import ModelingCmdId
from ..models.rtc_ice_candidate import RtcIceCandidate
from ..models.rtc_session_description import RtcSessionDescription
from ..models.snake_case_result import SnakeCaseResult
from ..types import UNSET, Unset

CM = TypeVar("CM", bound="trickle_ice")


@attr.s(auto_attribs=True)
class trickle_ice:
    """The trickle ICE candidate response."""  # noqa: E501

    candidate: Union[Unset, RtcIceCandidate] = UNSET
    type: str = "trickle_ice"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.candidate, Unset):
            candidate = self.candidate
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if candidate is not UNSET:
            field_dict["candidate"] = candidate
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[CM], src_dict: Dict[str, Any]) -> CM:
        d = src_dict.copy()
        _candidate = d.pop("candidate", UNSET)
        candidate: Union[Unset, RtcIceCandidate]
        if isinstance(_candidate, Unset):
            candidate = UNSET
        else:
            candidate = _candidate  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        trickle_ice = cls(
            candidate=candidate,
            type=type,
        )

        trickle_ice.additional_properties = d
        return trickle_ice

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


OS = TypeVar("OS", bound="sdp_answer")


@attr.s(auto_attribs=True)
class sdp_answer:
    """The SDP answer response."""  # noqa: E501

    answer: Union[Unset, RtcSessionDescription] = UNSET
    type: str = "sdp_answer"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.answer, Unset):
            answer = self.answer
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if answer is not UNSET:
            field_dict["answer"] = answer
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[OS], src_dict: Dict[str, Any]) -> OS:
        d = src_dict.copy()
        _answer = d.pop("answer", UNSET)
        answer: Union[Unset, RtcSessionDescription]
        if isinstance(_answer, Unset):
            answer = UNSET
        else:
            answer = _answer  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        sdp_answer = cls(
            answer=answer,
            type=type,
        )

        sdp_answer.additional_properties = d
        return sdp_answer

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


WP = TypeVar("WP", bound="ice_server_info")


@attr.s(auto_attribs=True)
class ice_server_info:
    """The ICE server info response."""  # noqa: E501

    from ..models.ice_server import IceServer

    ice_servers: Union[Unset, List[IceServer]] = UNSET
    type: str = "ice_server_info"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ice_server import IceServer

        ice_servers: Union[Unset, List[IceServer]] = UNSET
        if not isinstance(self.ice_servers, Unset):
            ice_servers = self.ice_servers
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ice_servers is not UNSET:
            field_dict["ice_servers"] = ice_servers
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[WP], src_dict: Dict[str, Any]) -> WP:
        d = src_dict.copy()
        from ..models.ice_server import IceServer

        ice_servers = cast(List[IceServer], d.pop("ice_servers", UNSET))

        type = d.pop("type", UNSET)

        ice_server_info = cls(
            ice_servers=ice_servers,
            type=type,
        )

        ice_server_info.additional_properties = d
        return ice_server_info

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


XO = TypeVar("XO", bound="modeling")


@attr.s(auto_attribs=True)
class modeling:
    """The modeling command response."""  # noqa: E501

    cmd_id: Union[Unset, ModelingCmdId] = UNSET
    result: Union[Unset, SnakeCaseResult] = UNSET
    type: str = "modeling"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.cmd_id, Unset):
            cmd_id = self.cmd_id
        if not isinstance(self.result, Unset):
            result = self.result
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cmd_id is not UNSET:
            field_dict["cmd_id"] = cmd_id
        if result is not UNSET:
            field_dict["result"] = result
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[XO], src_dict: Dict[str, Any]) -> XO:
        d = src_dict.copy()
        _cmd_id = d.pop("cmd_id", UNSET)
        cmd_id: Union[Unset, ModelingCmdId]
        if isinstance(_cmd_id, Unset):
            cmd_id = UNSET
        else:
            cmd_id = _cmd_id  # type: ignore[arg-type]

        _result = d.pop("result", UNSET)
        result: Union[Unset, SnakeCaseResult]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = _result  # type: ignore[arg-type]

        type = d.pop("type", UNSET)

        modeling = cls(
            cmd_id=cmd_id,
            result=result,
            type=type,
        )

        modeling.additional_properties = d
        return modeling

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


LN = TypeVar("LN", bound="export")


@attr.s(auto_attribs=True)
class export:
    """The export command response, this is sent as binary."""  # noqa: E501

    from ..models.raw_file import RawFile

    files: Union[Unset, List[RawFile]] = UNSET
    type: str = "export"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.raw_file import RawFile

        files: Union[Unset, List[RawFile]] = UNSET
        if not isinstance(self.files, Unset):
            files = self.files
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[LN], src_dict: Dict[str, Any]) -> LN:
        d = src_dict.copy()
        from ..models.raw_file import RawFile

        files = cast(List[RawFile], d.pop("files", UNSET))

        type = d.pop("type", UNSET)

        export = cls(
            files=files,
            type=type,
        )

        export.additional_properties = d
        return export

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


WebSocketResponses = Union[trickle_ice, sdp_answer, ice_server_info, modeling, export]
