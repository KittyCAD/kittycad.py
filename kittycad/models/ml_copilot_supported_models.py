from enum import Enum


class MlCopilotSupportedModels(str, Enum):
    """AI models that we support using with the system. In theory any model with reasoning capabilities can work."""  # noqa: E501

    """# gpt-5-nano"""  # noqa: E501

    GPT5_NANO = "gpt5_nano"

    """# gpt-5-mini"""  # noqa: E501

    GPT5_MINI = "gpt5_mini"

    """# gpt-5-codex"""  # noqa: E501

    GPT5_CODEX = "gpt5_codex"

    """# gpt-5"""  # noqa: E501

    GPT5 = "gpt5"

    """# o3-mini"""  # noqa: E501

    O3_MINI = "o3_mini"

    """# azure o3-mini"""  # noqa: E501

    AZURE_O3_MINI = "azure_o3_mini"

    """# azure gpt-4o"""  # noqa: E501

    AZURE_GPT4O = "azure_gpt4o"

    """# azure gpt-4o-mini"""  # noqa: E501

    AZURE_GPT4O_MINI = "azure_gpt4o_mini"

    def __str__(self) -> str:
        return str(self.value)
