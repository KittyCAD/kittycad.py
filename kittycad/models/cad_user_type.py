from enum import Enum


class CadUserType(str, Enum):
    """Strict CAD user-type enum for onboarding/CRM form submissions."""  # noqa: E501

    """# Student or researcher persona."""  # noqa: E501

    STUDENT_OR_RESEARCHER = "student_or_researcher"

    """# Hobbyist persona."""  # noqa: E501

    HOBBYIST = "hobbyist"

    """# Professional persona."""  # noqa: E501

    PROFESSIONAL = "professional"

    def __str__(self) -> str:
        return str(self.value)
