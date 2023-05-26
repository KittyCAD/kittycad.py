from enum import Enum


class SystemInfoIsolationEnum(str, Enum):
    EMPTY = ""
    DEFAULT = "default"
    HYPERV = "hyperv"
    PROCESS = "process"

    def __str__(self) -> str:
        return str(self.value)
