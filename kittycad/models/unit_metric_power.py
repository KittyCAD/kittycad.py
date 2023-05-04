from enum import Enum


class UnitMetricPower(str, Enum):
    """The valid types of metric unit formats."""  # noqa: E501

    """# Atto (symbol a) is a unit prefix in the metric system denoting a factor of 10^−18 or 0.000000000000000001. <https://en.wikipedia.org/wiki/Atto-> """  # noqa: E501
    ATTO = "atto"
    """# Femto (symbol f) is a unit prefix in the metric system denoting a factor of 10^-15. <https://en.wikipedia.org/wiki/Femto-> """  # noqa: E501
    FEMTO = "femto"
    """# Pico (unit symbol p) is a unit prefix in the metric system denoting a factor of one trillionth in the short scale and one billionth in the long scale (0.000000000001); that is, 10^−12. <https://en.wikipedia.org/wiki/Pico-> """  # noqa: E501
    PICO = "pico"
    """# Nano (symbol n) is a unit prefix meaning "one billionth". Used primarily with the metric system, this prefix denotes a factor of 10^−9 or 0.000000001. <https://en.wikipedia.org/wiki/Nano-> """  # noqa: E501
    NANO = "nano"
    """# Micro (Greek letter μ (U+03BC) or the legacy symbol µ (U+00B5)) is a unit prefix in the metric system denoting a factor of 10^−6 (one millionth). <https://en.wikipedia.org/wiki/Micro-> """  # noqa: E501
    MICRO = "micro"
    """# Milli (symbol m) is a unit prefix in the metric system denoting a factor of one thousandth (10^−3). <https://en.wikipedia.org/wiki/Milli-> """  # noqa: E501
    MILLI = "milli"
    """# Centi (symbol c) is a unit prefix in the metric system denoting a factor of one hundredth. <https://en.wikipedia.org/wiki/Centi-> """  # noqa: E501
    CENTI = "centi"
    """# Deci (symbol d) is a decimal unit prefix in the metric system denoting a factor of one tenth. <https://en.wikipedia.org/wiki/Deci-> """  # noqa: E501
    DECI = "deci"
    """# One metric unit. """  # noqa: E501
    UNIT = "unit"
    """# Deca is a decimal unit prefix in the metric system denoting a factor of ten. <https://en.wikipedia.org/wiki/Deca-> """  # noqa: E501
    DECA = "deca"
    """# Hecto (symbol: h) is a decimal unit prefix in the metric system denoting a factor of one hundred. <https://en.wikipedia.org/wiki/Hecto-> """  # noqa: E501
    HECTO = "hecto"
    """# Kilo is a decimal unit prefix in the metric system denoting multiplication by one thousand (10^3). <https://en.wikipedia.org/wiki/Kilo-> """  # noqa: E501
    KILO = "kilo"
    """# Mega is a unit prefix in metric systems of units denoting a factor of one million (10^6 or 1000000). <https://en.wikipedia.org/wiki/Mega-> """  # noqa: E501
    MEGA = "mega"
    """# Giga is a unit prefix in the metric system denoting a factor of a short-scale billion or long-scale milliard (10^9 or 1000000000). <https://en.wikipedia.org/wiki/Giga-> """  # noqa: E501
    GIGA = "giga"
    """# Tera is a unit prefix in the metric system denoting multiplication by one trillion, or 10^12 or 1000000000000 (one trillion short scale; one billion long scale). <https://en.wikipedia.org/wiki/Tera-> """  # noqa: E501
    TERA = "tera"
    """# Peta is a decimal unit prefix in the metric system denoting multiplication by one quadrillion, or 10^15 (1000000000000000). <https://en.wikipedia.org/wiki/Peta-> """  # noqa: E501
    PETA = "peta"
    """# Exa is a decimal unit prefix in the metric system denoting 10^18 or 1000000000000000000. <https://en.wikipedia.org/wiki/Exa-> """  # noqa: E501
    EXA = "exa"

    def __str__(self) -> str:
        return str(self.value)
