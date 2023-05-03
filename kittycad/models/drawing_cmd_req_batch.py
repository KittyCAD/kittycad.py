from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.drawing_cmd_req import DrawingCmdReq
from ..types import UNSET, Unset

T = TypeVar("T", bound="DrawingCmdReqBatch")


@attr.s(auto_attribs=True)
class DrawingCmdReqBatch:
    """ """

    cmds: Union[Unset, Any] = UNSET
    file_id: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cmds = self.cmds
        file_id = self.file_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cmds is not UNSET:
            field_dict["cmds"] = cmds
        if file_id is not UNSET:
            field_dict["file_id"] = file_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cmds = d.pop("cmds", UNSET)
        file_id = d.pop("file_id", UNSET)

        drawing_cmd_req_batch = cls(
            cmds=cmds,
            file_id=file_id,
        )

        drawing_cmd_req_batch.additional_properties = d
        return drawing_cmd_req_batch

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
