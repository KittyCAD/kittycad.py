from enum import Enum


class MlCopilotTool(str, Enum):
    """The tools that can be used by the ML Copilot."""  # noqa: E501

    """# The tool for generating or editing KCL code based on user prompts."""  # noqa: E501

    EDIT_KCL_CODE = "edit_kcl_code"

    """# The tool for generating CAD models from textual descriptions."""  # noqa: E501

    TEXT_TO_CAD = "text_to_cad"

    """# The tool for querying a mechanical knowledge base."""  # noqa: E501

    MECHANICAL_KNOWLEDGE_BASE = "mechanical_knowledge_base"

    """# The tool for searching the web for information."""  # noqa: E501

    WEB_SEARCH = "web_search"

    def __str__(self) -> str:
        return str(self.value)
