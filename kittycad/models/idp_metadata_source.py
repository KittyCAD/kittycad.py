from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated

from .base64data import Base64Data


class OptionUrl(BaseModel):
    """A URL to the identity provider metadata descriptor."""

    type: Literal["url"] = "url"

    url: str

    model_config = ConfigDict(protected_namespaces=())


class OptionBase64EncodedXml(BaseModel):
    """A base64 encoded XML document containing the identity provider metadata descriptor."""

    data: Base64Data

    type: Literal["base64_encoded_xml"] = "base64_encoded_xml"

    model_config = ConfigDict(protected_namespaces=())


IdpMetadataSource = RootModel[
    Annotated[
        Union[
            OptionUrl,
            OptionBase64EncodedXml,
        ],
        Field(discriminator="type"),
    ]
]
