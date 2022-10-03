from enum import Enum


class UnitMetricPower(str, Enum):
    ATTO = 'atto'
    FEMTO = 'femto'
    PICO = 'pico'
    NANO = 'nano'
    MICRO = 'micro'
    MILLI = 'milli'
    CENTI = 'centi'
    DECI = 'deci'
    UNIT = 'unit'
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
