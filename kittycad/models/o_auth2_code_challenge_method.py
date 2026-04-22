from enum import Enum


class OAuth2CodeChallengeMethod(str, Enum):
    """The PKCE code challenge method."""  # noqa: E501

    """# Plain code challenge comparison."""  # noqa: E501

    PLAIN = "PLAIN"

    """# SHA-256 based PKCE challenge."""  # noqa: E501

    S256 = "S256"

    def __str__(self) -> str:
        return str(self.value)
