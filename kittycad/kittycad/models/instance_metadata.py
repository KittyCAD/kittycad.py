from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.instance_metadata_environment import InstanceMetadataEnvironment
from ..types import UNSET, Unset

T = TypeVar("T", bound="InstanceMetadata")


@attr.s(auto_attribs=True)
class InstanceMetadata:
    """ """

    id: Union[Unset, str] = UNSET
    git_hash: Union[Unset, str] = UNSET
    environment: Union[Unset, InstanceMetadataEnvironment] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    zone: Union[Unset, str] = UNSET
    image: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    cpu_platform: Union[Unset, str] = UNSET
    machine_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        git_hash = self.git_hash
        environment: Union[Unset, str] = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.value

        name = self.name
        description = self.description
        ip_address = self.ip_address
        zone = self.zone
        image = self.image
        hostname = self.hostname
        cpu_platform = self.cpu_platform
        machine_type = self.machine_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if git_hash is not UNSET:
            field_dict["git_hash"] = git_hash
        if environment is not UNSET:
            field_dict["environment"] = environment
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if zone is not UNSET:
            field_dict["zone"] = zone
        if image is not UNSET:
            field_dict["image"] = image
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if cpu_platform is not UNSET:
            field_dict["cpu_platform"] = cpu_platform
        if machine_type is not UNSET:
            field_dict["machine_type"] = machine_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        git_hash = d.pop("git_hash", UNSET)

        _environment = d.pop("environment", UNSET)
        environment: Union[Unset, InstanceMetadataEnvironment]
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = InstanceMetadataEnvironment(_environment)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        ip_address = d.pop("ip_address", UNSET)

        zone = d.pop("zone", UNSET)

        image = d.pop("image", UNSET)

        hostname = d.pop("hostname", UNSET)

        cpu_platform = d.pop("cpu_platform", UNSET)

        machine_type = d.pop("machine_type", UNSET)

        instance_metadata = cls(
            id=id,
            git_hash=git_hash,
            environment=environment,
            name=name,
            description=description,
            ip_address=ip_address,
            zone=zone,
            image=image,
            hostname=hostname,
            cpu_platform=cpu_platform,
            machine_type=machine_type,
        )

        instance_metadata.additional_properties = d
        return instance_metadata

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
