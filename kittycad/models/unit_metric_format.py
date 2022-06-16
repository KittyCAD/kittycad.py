from enum import Enum


class UnitMetricFormat(str, Enum):
    ATTO = 'atto'
    FEMTO = 'femto'
    PICO = 'pico'
    NANO = 'nano'
    MICRO = 'micro'
    MILLI = 'milli'
    CENTI = 'centi'
    DECI = 'deci'
    METRIC_UNIT = 'metric_unit'
    DECA = 'deca'
    HECTO = 'hecto'
    KILO = 'kilo'
    MEGA = 'mega'
    GIGA = 'giga'
    TERA = 'tera'
    PETA = 'peta'
    EXA = 'exa'

    def __str__(self) -> str:
        return str(self.value)
