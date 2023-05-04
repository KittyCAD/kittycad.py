from enum import Enum


class AiPluginApiType(str, Enum):
    """AI plugin api type."""  # noqa: E501

    """# An OpenAPI specification. """  # noqa: E501
    OPENAPI = "openapi"

    def __str__(self) -> str:
        return str(self.value)
