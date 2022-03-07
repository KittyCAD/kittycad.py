from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GPUDevice")


@attr.s(auto_attribs=True)
class GPUDevice:
    """ """
    id: Union[Unset, int] = UNSET
    memory_bus_width: Union[Unset, int] = UNSET
    memory_clock_rate: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    peak_memory_bandwidth: Union[Unset, int] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        memory_bus_width = self.memory_bus_width
        memory_clock_rate = self.memory_clock_rate
        name = self.name
        peak_memory_bandwidth = self.peak_memory_bandwidth

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict['id'] = id
        if memory_bus_width is not UNSET:
            field_dict['memory_bus_width'] = memory_bus_width
        if memory_clock_rate is not UNSET:
            field_dict['memory_clock_rate'] = memory_clock_rate
        if name is not UNSET:
            field_dict['name'] = name
        if peak_memory_bandwidth is not UNSET:
            field_dict['peak_memory_bandwidth'] = peak_memory_bandwidth

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        memory_bus_width = d.pop("memory_bus_width", UNSET)

        memory_clock_rate = d.pop("memory_clock_rate", UNSET)

        name = d.pop("name", UNSET)

        peak_memory_bandwidth = d.pop("peak_memory_bandwidth", UNSET)

        gpu_device = cls(
            id=id,
            memory_bus_width=memory_bus_width,
            memory_clock_rate=memory_clock_rate,
            name=name,
            peak_memory_bandwidth=peak_memory_bandwidth,
        )

        gpu_device.additional_properties = d
        return gpu_device

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
