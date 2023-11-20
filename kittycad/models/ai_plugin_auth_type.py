from enum import Enum


class AiPluginAuthType(str, Enum):
    """AI plugin auth type."""  # noqa: E501

    """# None. """  # noqa: E501
    NONE = "none"
    """# User http. """  # noqa: E501
    USER_HTTP = "user_http"
    """# Service http. """  # noqa: E501
    SERVICE_HTTP = "service_http"
    """# OAuth. """  # noqa: E501
    OAUTH = "oauth"

    def __str__(self) -> str:
        return str(self.value)
