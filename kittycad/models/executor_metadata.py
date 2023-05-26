from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.docker_system_info import DockerSystemInfo
from ..models.environment import Environment
from ..types import UNSET, Unset

E = TypeVar("E", bound="ExecutorMetadata")


@attr.s(auto_attribs=True)
class ExecutorMetadata:
    """Metadata about our currently running server.

    This is mostly used for internal purposes and debugging."""  # noqa: E501

    docker_info: Union[Unset, DockerSystemInfo] = UNSET
    environment: Union[Unset, Environment] = UNSET
    git_hash: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.docker_info, Unset):
            docker_info = self.docker_info
        if not isinstance(self.environment, Unset):
            environment = self.environment
        git_hash = self.git_hash

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if docker_info is not UNSET:
            field_dict["docker_info"] = docker_info
        if environment is not UNSET:
            field_dict["environment"] = environment
        if git_hash is not UNSET:
            field_dict["git_hash"] = git_hash

        return field_dict

    @classmethod
    def from_dict(cls: Type[E], src_dict: Dict[str, Any]) -> E:
        d = src_dict.copy()
        _docker_info = d.pop("docker_info", UNSET)
        docker_info: Union[Unset, DockerSystemInfo]
        if isinstance(_docker_info, Unset):
            docker_info = UNSET
        else:
            docker_info = DockerSystemInfo(_docker_info)

        _environment = d.pop("environment", UNSET)
        environment: Union[Unset, Environment]
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = Environment(_environment)

        git_hash = d.pop("git_hash", UNSET)

        executor_metadata = cls(
            docker_info=docker_info,
            environment=environment,
            git_hash=git_hash,
        )

        executor_metadata.additional_properties = d
        return executor_metadata

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
