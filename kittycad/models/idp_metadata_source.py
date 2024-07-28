import datetime
from typing import Any, Dict, List, Literal, Optional, Type, TypeVar, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict, Field, RootModel
from pydantic_extra_types.phone_numbers import PhoneNumber
from typing_extensions import Annotated

from .base64data import Base64Data


class url(BaseModel):
    """A URL to the identity provider metadata descriptor."""

    type: Literal["url"] = "url"

    url: str

    model_config = ConfigDict(protected_namespaces=())


class base64_encoded_xml(BaseModel):
    """A base64 encoded XML document containing the identity provider metadata descriptor."""

    data: Base64Data

    type: Literal["base64_encoded_xml"] = "base64_encoded_xml"

    model_config = ConfigDict(protected_namespaces=())


IdpMetadataSource = RootModel[
    Annotated[
        Union[
            url,
            base64_encoded_xml,
        ],
        Field(discriminator="type"),
    ]
]
