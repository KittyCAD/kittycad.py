from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.output_file import OutputFile


class CodeOutput(BaseModel):
    """Output of the code being executed.

    <details><summary>JSON schema</summary>

    ```json { \"description\": \"Output of the code being executed.\", \"type\": \"object\", \"properties\": { \"output_files\": { \"description\": \"The contents of the files requested if they were passed.\", \"type\": \"array\", \"items\": { \"$ref\": \"#/components/schemas/OutputFile\" } }, \"stderr\": { \"description\": \"The stderr of the code.\", \"default\": \"\", \"type\": \"string\" }, \"stdout\": { \"description\": \"The stdout of the code.\", \"default\": \"\", \"type\": \"string\" } } } ``` </details>
    """

    output_files: Optional[List[OutputFile]] = None

    stderr: Optional[str] = None

    stdout: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
