from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.modeling_cmd_id import ModelingCmdId
from ..models.path_command import PathCommand
from ..types import UNSET, Unset

UE = TypeVar("UE", bound="PathSegmentInfo")


@attr.s(auto_attribs=True)
class PathSegmentInfo:
    """Info about a path segment"""  # noqa: E501

    command: Union[Unset, PathCommand] = UNSET
    command_id: Union[Unset, ModelingCmdId] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.command, Unset):
            command = self.command
        if not isinstance(self.command_id, Unset):
            command_id = self.command_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if command is not UNSET:
            field_dict["command"] = command
        if command_id is not UNSET:
            field_dict["command_id"] = command_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[UE], src_dict: Dict[str, Any]) -> UE:
        d = src_dict.copy()
        _command = d.pop("command", UNSET)
        command: Union[Unset, PathCommand]
        if isinstance(_command, Unset):
            command = UNSET
        else:
            command = _command  # type: ignore[arg-type]

        _command_id = d.pop("command_id", UNSET)
        command_id: Union[Unset, ModelingCmdId]
        if isinstance(_command_id, Unset):
            command_id = UNSET
        else:
            command_id = _command_id  # type: ignore[arg-type]

        path_segment_info = cls(
            command=command,
            command_id=command_id,
        )

        path_segment_info.additional_properties = d
        return path_segment_info

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
