from enum import Enum


class CodeOption(str, Enum):
    """Code option for running and verifying kcl.

    <details><summary>JSON schema</summary>

    ```json { "title": "CodeOption", "description": "Code option for running and verifying kcl.", "type": "string", "enum": [ "parse", "execute", "cleanup", "mock_execute" ] } ``` </details>"""  # noqa: E501

    PARSE = "parse"

    EXECUTE = "execute"

    CLEANUP = "cleanup"

    MOCK_EXECUTE = "mock_execute"

    def __str__(self) -> str:
        return str(self.value)
