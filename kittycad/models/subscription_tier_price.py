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


class OptionContract(KittyCadBaseModel):
    """Contract-managed pricing. The price is not self-serve and the customer must contact sales."""

    type: Literal["contract"] = "contract"


SubscriptionTierPrice = RootModel[
    Annotated[
        Union[
            OptionFlat,
            OptionPerUser,
            OptionContract,
        ],
        Field(discriminator="type"),
    ]
]
