from enum import Enum


class CutStrategy(str, Enum):
    """What strategy (algorithm) should be used for cutting? Defaults to Automatic."""  # noqa: E501

    """# Basic fillet cut. This has limitations, like the filletted edges can't touch each other. But it's very fast and simple."""  # noqa: E501

    BASIC = "basic"

    """# More complicated fillet cut. It works for more use-cases, like edges that touch each other. But it's slower than the Basic method."""  # noqa: E501

    CSG = "csg"

    """# Tries the Basic method, and if that doesn't work, tries the CSG strategy."""  # noqa: E501

    AUTOMATIC = "automatic"

    def __str__(self) -> str:
        return str(self.value)
