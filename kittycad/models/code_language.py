from enum import Enum


class CodeLanguage(str, Enum):
    """The language code is written in.

    <details><summary>JSON schema</summary>

    ```json { "description": "The language code is written in.", "oneOf": [ { "description": "The `go` programming language.", "type": "string", "enum": [ "go" ] }, { "description": "The `python` programming language.", "type": "string", "enum": [ "python" ] }, { "description": "The `node` programming language.", "type": "string", "enum": [ "node" ] } ] } ``` </details>
    """  # noqa: E501

    """# The `go` programming language. """  # noqa: E501
    GO = "go"
    """# The `python` programming language. """  # noqa: E501
    PYTHON = "python"
    """# The `node` programming language. """  # noqa: E501
    NODE = "node"

    def __str__(self) -> str:
        return str(self.value)
