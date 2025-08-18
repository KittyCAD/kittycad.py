from typing import Literal, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.plan_interval import PlanInterval
from .base import KittyCadBaseModel


class OptionFlat(KittyCadBaseModel):
    """A flat price that we publicly list."""

    interval: PlanInterval

    price: float

    type: Literal["flat"] = "flat"


class OptionPerUser(KittyCadBaseModel):
    """A per user price that we publicly list."""

    interval: PlanInterval

    price: float

    type: Literal["per_user"] = "per_user"


class OptionEnterprise(KittyCadBaseModel):
    """Enterprise: The price is not listed and the user needs to contact sales."""

    type: Literal["enterprise"] = "enterprise"


SubscriptionTierPrice = RootModel[
    Annotated[
        Union[
            OptionFlat,
            OptionPerUser,
            OptionEnterprise,
        ],
        Field(discriminator="type"),
    ]
]
