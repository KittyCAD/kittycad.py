from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated


class TextData(BaseModel):
    """The content of the reasoning."""

    model_config = ConfigDict(protected_namespaces=())


class OptionText(BaseModel):
    """Plain text reasoning."""

    content: TextData

    type: Literal["text"] = "text"

    model_config = ConfigDict(protected_namespaces=())


ReasoningMessage = RootModel[Annotated[Union[OptionText,], Field(discriminator="type")]]
