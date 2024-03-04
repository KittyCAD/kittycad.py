from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated

from ..models.plan_interval import PlanInterval


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
