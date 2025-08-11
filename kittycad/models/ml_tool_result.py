from typing import Dict, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated


class OptionTextToCad(BaseModel):
    """Response from the `TextToCad` tool."""

    error: Optional[str] = None

    outputs: Optional[Dict[str, str]] = None

    project_name: Optional[str] = None

    status_code: int

    type: Literal["text_to_cad"] = "text_to_cad"

    model_config = ConfigDict(protected_namespaces=())


class OptionEditKclCode(BaseModel):
    """Response from the `EditKclCode` tool."""

    error: Optional[str] = None

    outputs: Optional[Dict[str, str]] = None

    project_name: Optional[str] = None

    status_code: int

    type: Literal["edit_kcl_code"] = "edit_kcl_code"

    model_config = ConfigDict(protected_namespaces=())


class OptionMechanicalKnowledgeBase(BaseModel):
    """Mechanical knowledge base response."""

    response: str

    type: Literal["mechanical_knowledge_base"] = "mechanical_knowledge_base"

    model_config = ConfigDict(protected_namespaces=())


MlToolResult = RootModel[
    Annotated[
        Union[
            OptionTextToCad,
            OptionEditKclCode,
            OptionMechanicalKnowledgeBase,
        ],
        Field(discriminator="type"),
    ]
]
