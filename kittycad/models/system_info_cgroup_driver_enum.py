from enum import Enum


class SystemInfoCgroupDriverEnum(str, Enum):
    EMPTY = ""
    CGROUPFS = "cgroupfs"
    SYSTEMD = "systemd"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
