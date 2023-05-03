from enum import Enum


class AccountProvider(str, Enum):
    """An account provider."""  # noqa: E501

    """# The Google account provider. """  # noqa: E501
    GOOGLE = "google"
    """# The GitHub account provider. """  # noqa: E501
    GITHUB = "github"

    def __str__(self) -> str:
        return str(self.value)
