from enum import Enum


class ApiEndpoint(str, Enum):
    """Types of API endpoints."""  # noqa: E501

    """# The modeling API."""  # noqa: E501

    MODELING = "modeling"

    """# Machine learning API."""  # noqa: E501

    ML = "ml"

    """# File API."""  # noqa: E501

    FILE = "file"

    def __str__(self) -> str:
        return str(self.value)
