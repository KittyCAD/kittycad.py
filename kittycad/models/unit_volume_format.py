from enum import Enum


class UnitVolumeFormat(str, Enum):
    CUBIC_METER = 'cubic_meter'
    CUBIC_CENTIMETER = 'cubic_centimeter'
    CUBIC_MILLIMETER = 'cubic_millimeter'
    CUBIC_KILOMETER = 'cubic_kilometer'
    LITER = 'liter'
    CUBIC_INCH = 'cubic_inch'
    CUBIC_FOOT = 'cubic_foot'
    CUBIC_YARD = 'cubic_yard'
    CUBIC_MILE = 'cubic_mile'
    GALLON = 'gallon'
    QUART = 'quart'
    PINT = 'pint'
    CUP = 'cup'
    FLUID_OUNCE = 'fluid_ounce'
    BARREL = 'barrel'
    BUSHEL = 'bushel'
    CORD = 'cord'
    CUBIC_FATHOM = 'cubic_fathom'
    TABLESPOON = 'tablespoon'
    TEASPOON = 'teaspoon'
    PINCH = 'pinch'
    DASH = 'dash'
    DROP = 'drop'
    FIFTH = 'fifth'
    DRAM = 'dram'
    GILL = 'gill'
    PECK = 'peck'
    SACK = 'sack'
    SHOT = 'shot'
    STRIKE = 'strike'

    def __str__(self) -> str:
        return str(self.value)
