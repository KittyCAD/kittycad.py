from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.modeling_cmd import ModelingCmd
from ..models.modeling_cmd_id import ModelingCmdId
from ..types import UNSET, Unset

Q = TypeVar("Q", bound="ModelingCmdReq")


@attr.s(auto_attribs=True)
class ModelingCmdReq:
    """A graphics command submitted to the KittyCAD engine via the Modeling API."""  # noqa: E501

    cmd: Union[Unset, ModelingCmd] = UNSET
    cmd_id: Union[Unset, ModelingCmdId] = UNSET
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
    def from_dict(cls: Type[Q], src_dict: Dict[str, Any]) -> Q:
        d = src_dict.copy()
        _cmd = d.pop("cmd", UNSET)
        cmd: Union[Unset, ModelingCmd]
        if isinstance(_cmd, Unset):
            cmd = UNSET
        else:
            cmd = _cmd  # type: ignore[arg-type]

        _cmd_id = d.pop("cmd_id", UNSET)
        cmd_id: Union[Unset, ModelingCmdId]
        if isinstance(_cmd_id, Unset):
            cmd_id = UNSET
        else:
            cmd_id = ModelingCmdId(_cmd_id)

        file_id = d.pop("file_id", UNSET)

        modeling_cmd_req = cls(
            cmd=cmd,
            cmd_id=cmd_id,
            file_id=file_id,
        )

        modeling_cmd_req.additional_properties = d
        return modeling_cmd_req

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
