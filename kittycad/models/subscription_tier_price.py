import datetime
from typing import Any, Dict, List, Literal, Optional, Type, TypeVar, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict, Field, RootModel
from pydantic_extra_types.phone_numbers import PhoneNumber
from typing_extensions import Annotated

from ..models.plan_interval import PlanInterval
from .base64data import Base64Data


class flat(BaseModel):
    """A flat price that we publicly list."""

    interval: PlanInterval

    price: float

    type: Literal["flat"] = "flat"

    model_config = ConfigDict(protected_namespaces=())


class per_user(BaseModel):
    """A per user price that we publicly list."""

    interval: PlanInterval

    price: float

    type: Literal["per_user"] = "per_user"

    model_config = ConfigDict(protected_namespaces=())


class enterprise(BaseModel):
    """Enterprise: The price is not listed and the user needs to contact sales."""

    type: Literal["enterprise"] = "enterprise"

    model_config = ConfigDict(protected_namespaces=())


SubscriptionTierPrice = RootModel[
    Annotated[
        Union[
            flat,
            per_user,
            enterprise,
        ],
        Field(discriminator="type"),
    ]
]
