import datetime
from typing import Any, Dict, List, Literal, Optional, Type, TypeVar, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict, Field, RootModel
from pydantic_extra_types.phone_numbers import PhoneNumber
from typing_extensions import Annotated

from .base64data import Base64Data


class individual(BaseModel):
    """A subscription tier that can be applied to individuals only."""

    type: Literal["individual"] = "individual"

    model_config = ConfigDict(protected_namespaces=())


class organization(BaseModel):
    """An subscription tier that can be applied to organizations only."""

    saml_sso: bool

    type: Literal["organization"] = "organization"

    model_config = ConfigDict(protected_namespaces=())


SubscriptionTierType = RootModel[
    Annotated[
        Union[
            individual,
            organization,
        ],
        Field(discriminator="type"),
    ]
]
