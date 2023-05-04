from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.drawing_cmd import DrawingCmd
from ..models.drawing_cmd_id import DrawingCmdId
from ..types import UNSET, Unset

L = TypeVar("L", bound="DrawingCmdReq")


@attr.s(auto_attribs=True)
class DrawingCmdReq:
    """A graphics command submitted to the KittyCAD engine via the Drawing API."""  # noqa: E501

    cmd: Union[Unset, DrawingCmd] = UNSET
    cmd_id: Union[Unset, DrawingCmdId] = UNSET
    file_id: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.cmd, Unset):
            cmd = self.cmd
        if not isinstance(self.cmd_id, Unset):
            cmd_id = self.cmd_id
        file_id = self.file_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cmd is not UNSET:
            field_dict["cmd"] = cmd
        if cmd_id is not UNSET:
            field_dict["cmd_id"] = cmd_id
        if file_id is not UNSET:
            field_dict["file_id"] = file_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[L], src_dict: Dict[str, Any]) -> L:
        d = src_dict.copy()
        _cmd = d.pop("cmd", UNSET)
        cmd: Union[Unset, DrawingCmd]
        if isinstance(_cmd, Unset):
            cmd = UNSET
        else:
            cmd = _cmd  # type: ignore[arg-type]

        _cmd_id = d.pop("cmd_id", UNSET)
        cmd_id: Union[Unset, DrawingCmdId]
        if isinstance(_cmd_id, Unset):
            cmd_id = UNSET
        else:
            cmd_id = DrawingCmdId(_cmd_id)

        file_id = d.pop("file_id", UNSET)

        drawing_cmd_req = cls(
            cmd=cmd,
            cmd_id=cmd_id,
            file_id=file_id,
        )

        drawing_cmd_req.additional_properties = d
        return drawing_cmd_req

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
