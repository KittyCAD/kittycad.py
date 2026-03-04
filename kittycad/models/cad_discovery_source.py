from enum import Enum


class CadDiscoverySource(str, Enum):
    """Strict acquisition-source enum used by the website CAD user info form."""  # noqa: E501

    """# Found via Google search."""  # noqa: E501

    GOOGLE = "google"

    """# Found via X/Twitter."""  # noqa: E501

    X = "x"

    """# Found via TikTok."""  # noqa: E501

    TIKTOK = "tiktok"

    """# Found via Reddit."""  # noqa: E501

    REDDIT = "reddit"

    """# Found via Payload Space."""  # noqa: E501

    PAYLOAD_SPACE = "payload_space"

    """# Found via YouTube."""  # noqa: E501

    YOUTUBE = "youtube"

    """# Found via Instagram."""  # noqa: E501

    INSTAGRAM = "instagram"

    """# Found via Facebook."""  # noqa: E501

    FACEBOOK = "facebook"

    """# Found through friend referral or word of mouth."""  # noqa: E501

    WORD_OF_MOUTH = "word_of_mouth"

    """# Found through another source described in free text."""  # noqa: E501

    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
