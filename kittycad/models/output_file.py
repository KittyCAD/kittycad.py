import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class OutputFile(BaseModel):
    """Output file contents.

    <details><summary>JSON schema</summary>

    ```json { \"description\": \"Output file contents.\", \"type\": \"object\", \"properties\": { \"contents\": { \"description\": \"The contents of the file. This is base64 encoded so we can ensure it is UTF-8 for JSON.\", \"type\": \"string\" }, \"name\": { \"description\": \"The name of the file.\", \"default\": \"\", \"type\": \"string\" } } } ``` </details>
    """

    contents: Optional[str] = None

    name: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
