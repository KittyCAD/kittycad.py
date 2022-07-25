from enum import Enum


class UnitForceFormat(str, Enum):
    NEWTON = 'newton'
    POUND = 'pound'
    DYNE = 'dyne'
    KILOPOUND = 'kilopound'
    POUNDAL = 'poundal'

    def __str__(self) -> str:
        return str(self.value)
