from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.modeling_cmd_req import ModelingCmdReq
from ..types import UNSET, Unset

XL = TypeVar("XL", bound="ModelingCmdReqBatch")


@attr.s(auto_attribs=True)
class ModelingCmdReqBatch:
    """A batch set of graphics commands submitted to the KittyCAD engine via the Modeling API."""  # noqa: E501

    from ..models.modeling_cmd_req import ModelingCmdReq

    cmds: Union[Unset, Dict[str, ModelingCmdReq]] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cmds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cmds, Unset):
            new_dict: Dict[str, Any] = {}
            for key, value in self.cmds.items():
                new_dict[key] = value.to_dict()
            cmds = new_dict

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cmds is not UNSET:
            field_dict["cmds"] = cmds

        return field_dict

    @classmethod
    def from_dict(cls: Type[XL], src_dict: Dict[str, Any]) -> XL:
        d = src_dict.copy()
        _cmds = d.pop("cmds", UNSET)
        if isinstance(_cmds, Unset):
            cmds = UNSET
        else:
            new_map: Dict[str, ModelingCmdReq] = {}
            for k, v in _cmds.items():
                new_map[k] = ModelingCmdReq.from_dict(v)  # type: ignore
            cmds = new_map  # type: ignore

        modeling_cmd_req_batch = cls(
            cmds=cmds,
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
