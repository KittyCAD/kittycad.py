from enum import Enum


class RegionVersion(str, Enum):
    """Region-creation algorithm version."""  # noqa: E501

    """# The original region creation method. This should NOT be used anymore, but is maintained to avoid breaking old models."""  # noqa: E501

    V0 = "V0"

    """# Fixes the bug in V0 where creating a region would shuffle the mapping from segment names/IDs to actual segment geometry."""  # noqa: E501

    V1 = "V1"

    def __str__(self) -> str:
        return str(self.value)
