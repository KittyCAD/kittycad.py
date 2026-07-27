from enum import Enum


class MlCopilotMode(str, Enum):
    """The mode to have the agent work in."""  # noqa: E501

    """# Use a combination of models and reasoning effort for fast results."""  # noqa: E501

    FAST = "fast"

    """# Use a model and effort that results in thoughtful responses."""  # noqa: E501

    THOUGHTFUL = "thoughtful"

    """# Let the system automatically choose the model and reasoning effort."""  # noqa: E501

    AUTO = "auto"

    """# Use the private Zoo Pro model for internal Zookeeper workflows."""  # noqa: E501

    ZOOKEEPER_PRO = "zookeeper_pro"

    """# Use the Zoo Ultra model for internal Zookeeper workflows."""  # noqa: E501

    ZOOKEEPER_ULTRA = "zookeeper_ultra"

    def __str__(self) -> str:
        return str(self.value)
