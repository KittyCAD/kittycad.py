from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodeOutput")


@attr.s(auto_attribs=True)
class CodeOutput:
    """ """
    output: Union[Unset, str] = UNSET
    stderr: Union[Unset, str] = UNSET
    stdout: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        output = self.output
        stderr = self.stderr
        stdout = self.stdout

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if output is not UNSET:
            field_dict['output'] = output
        if stderr is not UNSET:
            field_dict['stderr'] = stderr
        if stdout is not UNSET:
            field_dict['stdout'] = stdout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        output = d.pop("output", UNSET)

        stderr = d.pop("stderr", UNSET)

        stdout = d.pop("stdout", UNSET)

        code_output = cls(
            output=output,
            stderr=stderr,
            stdout=stdout,
        )

        code_output.additional_properties = d
        return code_output

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
