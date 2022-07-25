from enum import Enum


class UnitDataTransferRateFormat(str, Enum):
    BYTES_PER_SECOND = 'bytes_per_second'
    EXABYTES_PER_SECOND = 'exabytes_per_second'
    BITS_PER_SECOND = 'bits_per_second'
    EXABITS_PER_SECOND = 'exabits_per_second'

    def __str__(self) -> str:
        return str(self.value)
