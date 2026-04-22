from enum import Enum


class CadExperienceLevel(str, Enum):
    """Strict CAD/API experience-level enum for onboarding/CRM form submissions."""  # noqa: E501

    """# Beginner experience level."""  # noqa: E501

    BEGINNER = "beginner"

    """# Intermediate experience level."""  # noqa: E501

    INTERMEDIATE = "intermediate"

    """# Advanced experience level."""  # noqa: E501

    ADVANCED = "advanced"

    def __str__(self) -> str:
        return str(self.value)
