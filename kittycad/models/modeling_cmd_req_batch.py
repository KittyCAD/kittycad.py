from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

F = TypeVar("F", bound="ModelingCmdReqBatch")


@attr.s(auto_attribs=True)
class ModelingCmdReqBatch:
    """A batch set of graphics commands submitted to the KittyCAD engine via the Modeling API."""  # noqa: E501

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
    def from_dict(cls: Type[F], src_dict: Dict[str, Any]) -> F:
        d = src_dict.copy()
        cmds = d.pop("cmds", UNSET)
        file_id = d.pop("file_id", UNSET)

        modeling_cmd_req_batch = cls(
            cmds=cmds,
            file_id=file_id,
        )

        modeling_cmd_req_batch.additional_properties = d
        return modeling_cmd_req_batch

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
