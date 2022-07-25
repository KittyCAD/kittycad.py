from enum import Enum


class UnitConcentrationFormat(str, Enum):
    PARTS_PER_MILLION = 'parts_per_million'
    PARTS_PER_BILLION = 'parts_per_billion'
    PARTS_PER_TRILLION = 'parts_per_trillion'
    PERCENT = 'percent'

    def __str__(self) -> str:
        return str(self.value)
