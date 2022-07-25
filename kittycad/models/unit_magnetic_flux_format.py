from enum import Enum


class UnitMagneticFluxFormat(str, Enum):
    WEBER = 'weber'
    MAXWELL = 'maxwell'

    def __str__(self) -> str:
        return str(self.value)
