from enum import Enum


class MlReasoningEffort(str, Enum):
    """Specify the amount of effort used in reasoning. Read the following for more info: https://platform.openai.com/docs/guides/reasoning#how-reasoning-works"""  # noqa: E501

    """# Low reasoning"""  # noqa: E501

    LOW = "low"

    """# Medium reasoning"""  # noqa: E501

    MEDIUM = "medium"

    """# High reasoning"""  # noqa: E501

    HIGH = "high"

    def __str__(self) -> str:
        return str(self.value)
