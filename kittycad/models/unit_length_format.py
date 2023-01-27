from enum import Enum


class UnitLengthFormat(str, Enum):
    METER = 'meter'
    MILLIMETER = 'millimeter'
    CENTIMETER = 'centimeter'
    KILOMETER = 'kilometer'
    FOOT = 'foot'
    MIL = 'mil'
    INCH = 'inch'
    MILE = 'mile'
    NAUTICAL_MILE = 'nautical_mile'
    ASTRONOMICAL_UNIT = 'astronomical_unit'
    LIGHTYEAR = 'lightyear'
    PARSEC = 'parsec'
    ANGSTROM = 'angstrom'
    CUBIT = 'cubit'
    FATHOM = 'fathom'
    CHAIN = 'chain'
    FURLONG = 'furlong'
    HAND = 'hand'
    LEAGUE = 'league'
    NAUTICAL_LEAGUE = 'nautical_league'
    YARD = 'yard'

    def __str__(self) -> str:
        return str(self.value)
