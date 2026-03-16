from enum import Enum


class AccountProvider(str, Enum):
    """An account provider."""  # noqa: E501

    """# The Apple account provider."""  # noqa: E501

    APPLE = "apple"

    """# The Discord account provider."""  # noqa: E501

    DISCORD = "discord"

    """# The Google account provider."""  # noqa: E501

    GOOGLE = "google"

    """# The GitHub account provider."""  # noqa: E501

    GITHUB = "github"

    """# The Microsoft account provider."""  # noqa: E501

    MICROSOFT = "microsoft"

    """# The SAML account provider."""  # noqa: E501

    SAML = "saml"

    """# The Tencent QQ account provider."""  # noqa: E501

    TENCENT = "tencent"

    """# Test provider for integration tests (only available during testing)."""  # noqa: E501

    TEST_PROVIDER = "test_provider"

    def __str__(self) -> str:
        return str(self.value)
