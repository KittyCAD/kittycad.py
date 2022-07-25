from enum import Enum


class UnitDensityFormat(str, Enum):
    KILOGRAMS_PER_CUBIC_METER = 'kilograms_per_cubic_meter'
    GRAMS_PER_MILLILITER = 'grams_per_milliliter'
    KILOGRAMS_PER_LITER = 'kilograms_per_liter'
    OUNCES_PER_CUBIC_FOOT = 'ounces_per_cubic_foot'
    OUNCES_PER_CUBIC_INCH = 'ounces_per_cubic_inch'
    OUNCES_PER_GALLON = 'ounces_per_gallon'
    POUNDS_PER_CUBIC_FOOT = 'pounds_per_cubic_foot'
    POUNDS_PER_CUBIC_INCH = 'pounds_per_cubic_inch'
    POUNDS_PER_GALLON = 'pounds_per_gallon'
    SLUGS_PER_CUBIC_FOOT = 'slugs_per_cubic_foot'

    def __str__(self) -> str:
        return str(self.value)
