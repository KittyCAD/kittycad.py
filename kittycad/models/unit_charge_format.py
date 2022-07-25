from enum import Enum


class UnitChargeFormat(str, Enum):
    COULOMB = 'coulomb'
    AMPERE_HOUR = 'ampere_hour'

    def __str__(self) -> str:
        return str(self.value)
