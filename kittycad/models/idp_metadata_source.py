from typing import Literal, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from .base import KittyCadBaseModel
from .base64data import Base64Data


class OptionUrl(KittyCadBaseModel):
    """A URL to the identity provider metadata descriptor."""

    type: Literal["url"] = "url"

    url: str


class OptionBase64EncodedXml(KittyCadBaseModel):
    """A base64 encoded XML document containing the identity provider metadata descriptor."""

    data: Base64Data

    type: Literal["base64_encoded_xml"] = "base64_encoded_xml"


IdpMetadataSource = RootModel[
    Annotated[
        Union[
            OptionUrl,
            OptionBase64EncodedXml,
        ],
        Field(discriminator="type"),
    ]
]
