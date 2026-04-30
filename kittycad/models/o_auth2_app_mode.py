from enum import Enum


class OAuth2AppMode(str, Enum):
    """The deployment mode for an OAuth 2.0 app."""  # noqa: E501

    """# Development mode permits HTTPS redirect URIs and local HTTP redirect URIs. Only the app owner, or an org admin for organization apps, can authorize development apps."""  # noqa: E501

    DEVELOPMENT = "development"

    """# Production mode only permits secure non-local redirect URIs."""  # noqa: E501

    PRODUCTION = "production"

    def __str__(self) -> str:
        return str(self.value)
