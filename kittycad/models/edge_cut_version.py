from enum import Enum


class EdgeCutVersion(str, Enum):
    """Edge cut algorithm version."""  # noqa: E501

    """# Let the engine choose whichever version it wants."""  # noqa: E501

    V0 = "v0"

    """# The original fillet algorithm Zoo 1.0 shipped with. Limitations: doesn't support rolling ball fillets, has several bugs that will not be fixed."""  # noqa: E501

    V1 = "v1"

    """# Adds support for rolling ball fillets. Fixes bugs from V1. Still experimental."""  # noqa: E501

    V2 = "v2"

    def __str__(self) -> str:
        return str(self.value)
