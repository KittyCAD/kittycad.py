from typing import List, Optional

from ..models.output_file import OutputFile
from .base import KittyCadBaseModel


class CodeOutput(KittyCadBaseModel):
    """Output of the code being executed.

    <details><summary>JSON schema</summary>

    ```json { \"description\": \"Output of the code being executed.\", \"type\": \"object\", \"properties\": { \"output_files\": { \"description\": \"The contents of the files requested if they were passed.\", \"type\": \"array\", \"items\": { \"$ref\": \"#/components/schemas/OutputFile\" } }, \"stderr\": { \"description\": \"The stderr of the code.\", \"default\": \"\", \"type\": \"string\" }, \"stdout\": { \"description\": \"The stdout of the code.\", \"default\": \"\", \"type\": \"string\" } } } ``` </details>"""

    output_files: Optional[List[OutputFile]] = None

    stderr: str = ""

    stdout: str = ""
