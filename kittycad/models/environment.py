from enum import Enum


class Environment(str, Enum):
    """The environment the server is running in."""  # noqa: E501

    """# The development environment. This is for running locally. """  # noqa: E501
    DEVELOPMENT = "DEVELOPMENT"
    """# The preview environment. This is when PRs are created and a service is deployed for testing. """  # noqa: E501
    PREVIEW = "PREVIEW"
    """# The production environment. """  # noqa: E501
    PRODUCTION = "PRODUCTION"

    def __str__(self) -> str:
        return str(self.value)
