from enum import Enum


class UnitMassFormat(str, Enum):
    GRAM = 'gram'
    METRIC_TON = 'metric_ton'
    POUND = 'pound'
    LONG_TON = 'long_ton'
    SHORT_TON = 'short_ton'
    STONE = 'stone'
    OUNCE = 'ounce'
    CARAT = 'carat'
    SLUG = 'slug'

    def __str__(self) -> str:
        return str(self.value)
