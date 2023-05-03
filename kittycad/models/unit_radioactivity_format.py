from enum import Enum


class UnitRadioactivityFormat(str, Enum):
    """The valid types of radioactivity unit formats. These describe the amount of radiation emitted by a radioactive material."""  # noqa: E501

    """# <https://en.wikipedia.org/wiki/Becquerel> """  # noqa: E501
    BECQUEREL = "becquerel"
    """# <https://en.wikipedia.org/wiki/Curie_(unit)> """  # noqa: E501
    CURIE = "curie"
    """# <https://en.wikipedia.org/wiki/Rutherford_(unit)> """  # noqa: E501
    RUTHERFORD = "rutherford"

    def __str__(self) -> str:
        return str(self.value)
