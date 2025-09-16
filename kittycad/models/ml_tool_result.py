from typing import Dict, Literal, Optional, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from .base import KittyCadBaseModel


class OptionTextToCad(KittyCadBaseModel):
    """Response from the `TextToCad` tool."""

    error: Optional[str] = None

    outputs: Optional[Dict[str, str]] = None

    project_name: Optional[str] = None

    status_code: int

    type: Literal["text_to_cad"] = "text_to_cad"


class OptionEditKclCode(KittyCadBaseModel):
    """Response from the `EditKclCode` tool."""

    error: Optional[str] = None

    outputs: Optional[Dict[str, str]] = None

    project_name: Optional[str] = None

    status_code: int

    type: Literal["edit_kcl_code"] = "edit_kcl_code"


class OptionMechanicalKnowledgeBase(KittyCadBaseModel):
    """Mechanical knowledge base response."""

    response: str

    type: Literal["mechanical_knowledge_base"] = "mechanical_knowledge_base"


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
