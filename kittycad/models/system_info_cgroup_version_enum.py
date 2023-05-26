from enum import Enum


class SystemInfoCgroupVersionEnum(str, Enum):
    EMPTY = ""
    ONE = "1"
    TWO = "2"

    def __str__(self) -> str:
        return str(self.value)
