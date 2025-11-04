from enum import Enum


class MlCopilotMode(str, Enum):
    """The mode to have the agent work in."""  # noqa: E501

    """# Use a combination of models and reasoning effort for fast results."""  # noqa: E501

    FAST = "fast"

    """# Use a model and effort that results in thoughtful responses."""  # noqa: E501

    THOUGHTFUL = "thoughtful"

    def __str__(self) -> str:
        return str(self.value)
