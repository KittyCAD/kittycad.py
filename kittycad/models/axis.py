from enum import Enum


class Axis(str, Enum):
    """Co-ordinate axis specifier.

    See [cglearn.eu] for background reading.

    [cglearn.eu]: https://cglearn.eu/pub/computer-graphics/introduction-to-geometry#material-coordinate-systems-1
    """  # noqa: E501

    """# 'Y' axis. """  # noqa: E501
    Y = "y"
    """# 'Z' axis. """  # noqa: E501
    Z = "z"

    def __str__(self) -> str:
        return str(self.value)
