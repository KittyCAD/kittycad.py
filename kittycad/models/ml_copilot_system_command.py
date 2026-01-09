from enum import Enum


class MlCopilotSystemCommand(str, Enum):
    """The type of system command that can be sent to the ML Copilot."""  # noqa: E501

    """# Reset the conversation state, by creating a new state."""  # noqa: E501

    NEW = "new"

    """# Disconnect the client, which can be used to end the session."""  # noqa: E501

    BYE = "bye"

    """# Interrupt the current prompt that is being processed."""  # noqa: E501

    INTERRUPT = "interrupt"

    """# Cancel the current prompt that is being processed."""  # noqa: E501

    CANCEL = "cancel"

    """# Answer now, which forces the AI to finish the current response."""  # noqa: E501

    ANSWER_NOW = "answer_now"

    def __str__(self) -> str:
        return str(self.value)
