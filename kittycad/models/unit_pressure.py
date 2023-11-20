from enum import Enum


class UnitPressure(str, Enum):
    """The valid types of pressure units."""  # noqa: E501

    """# Atmospheres <https://en.wikipedia.org/wiki/Standard_atmosphere_(unit)> """  # noqa: E501
    ATMOSPHERES = "atmospheres"
    """# Bars <https://en.wikipedia.org/wiki/Bar_(unit)> """  # noqa: E501
    BARS = "bars"
    """# Hectopascals <https://en.wikipedia.org/wiki/Hectopascal> """  # noqa: E501
    HECTOPASCALS = "hectopascals"
    """# Kilopascals <https://en.wikipedia.org/wiki/Kilopascal> """  # noqa: E501
    KILOPASCALS = "kilopascals"
    """# Millibars <https://en.wikipedia.org/wiki/Bar_(unit)> """  # noqa: E501
    MILLIBARS = "millibars"
    """# Pascals <https://en.wikipedia.org/wiki/Pascal_(unit)> """  # noqa: E501
    PASCALS = "pascals"
    """# Pounds per square inch (PSI) - <https://en.wikipedia.org/wiki/Pound_per_square_inch> """  # noqa: E501
    PSI = "psi"

    def __str__(self) -> str:
        return str(self.value)
