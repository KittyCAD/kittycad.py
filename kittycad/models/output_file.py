from typing import Optional

from pydantic import BaseModel, ConfigDict



class OutputFile(BaseModel):
    """Output file contents.

    <details><summary>JSON schema</summary>

    ```json { \"description\": \"Output file contents.\", \"type\": \"object\", \"properties\": { \"contents\": { \"description\": \"The contents of the file. This is base64 encoded so we can ensure it is UTF-8 for JSON.\", \"type\": \"string\" }, \"name\": { \"description\": \"The name of the file.\", \"default\": \"\", \"type\": \"string\" } } } ``` </details>
    """

    contents: Optional[str] = None

    name: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
