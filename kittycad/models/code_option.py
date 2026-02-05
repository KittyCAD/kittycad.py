from enum import Enum


class CodeOption(str, Enum):
    """`CodeOption`

    <details><summary>JSON schema</summary>

    ```json { "type": "string", "enum": [ "parse", "mock_execute", "execute" ] } ``` </details>"""  # noqa: E501

    PARSE = "parse"

    MOCK_EXECUTE = "mock_execute"

    EXECUTE = "execute"

    def __str__(self) -> str:
        return str(self.value)
