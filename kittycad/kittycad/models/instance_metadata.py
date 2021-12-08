from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.instance_metadata_environment import InstanceMetadataEnvironment
from ..types import UNSET, Unset

T = TypeVar("T", bound="InstanceMetadata")


@attr.s(auto_attribs=True)
class InstanceMetadata:
    """ """

    cpu_platform: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    environment: Union[Unset, InstanceMetadataEnvironment] = UNSET
    git_hash: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    image: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    machine_type: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    zone: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cpu_platform = self.cpu_platform
        description = self.description
        environment: Union[Unset, str] = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.value

        git_hash = self.git_hash
        hostname = self.hostname
        id = self.id
        image = self.image
        ip_address = self.ip_address
        machine_type = self.machine_type
        name = self.name
        zone = self.zone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu_platform is not UNSET:
            field_dict["cpu_platform"] = cpu_platform
        if description is not UNSET:
            field_dict["description"] = description
        if environment is not UNSET:
            field_dict["environment"] = environment
        if git_hash is not UNSET:
            field_dict["git_hash"] = git_hash
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if id is not UNSET:
            field_dict["id"] = id
        if image is not UNSET:
            field_dict["image"] = image
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if machine_type is not UNSET:
            field_dict["machine_type"] = machine_type
        if name is not UNSET:
            field_dict["name"] = name
        if zone is not UNSET:
            field_dict["zone"] = zone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cpu_platform = d.pop("cpu_platform", UNSET)

        description = d.pop("description", UNSET)

        _environment = d.pop("environment", UNSET)
        environment: Union[Unset, InstanceMetadataEnvironment]
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = InstanceMetadataEnvironment(_environment)

        git_hash = d.pop("git_hash", UNSET)

        hostname = d.pop("hostname", UNSET)

        id = d.pop("id", UNSET)

        image = d.pop("image", UNSET)

        ip_address = d.pop("ip_address", UNSET)

        machine_type = d.pop("machine_type", UNSET)

        name = d.pop("name", UNSET)

        zone = d.pop("zone", UNSET)

        instance_metadata = cls(
            cpu_platform=cpu_platform,
            description=description,
            environment=environment,
            git_hash=git_hash,
            hostname=hostname,
            id=id,
            image=image,
            ip_address=ip_address,
            machine_type=machine_type,
            name=name,
            zone=zone,
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
