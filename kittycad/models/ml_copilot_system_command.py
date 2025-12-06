from enum import Enum


class MlCopilotSystemCommand(str, Enum):
    """The type of system command that can be sent to the ML Copilot."""  # noqa: E501

    """# Reset the conversation state, by creating a new state."""  # noqa: E501

    NEW = "new"

    """# Disconnect the client, which can be used to end the session."""  # noqa: E501

    BYE = "bye"

    """# Interrupt the current prompt that is being processed."""  # noqa: E501

    INTERRUPT = "interrupt"

    def __str__(self) -> str:
        return str(self.value)
