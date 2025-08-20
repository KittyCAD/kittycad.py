from typing import Literal, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from .base import KittyCadBaseModel


class OptionIndividual(KittyCadBaseModel):
    """A subscription tier that can be applied to individuals only."""

    type: Literal["individual"] = "individual"


class OptionOrganization(KittyCadBaseModel):
    """An subscription tier that can be applied to organizations only."""

    saml_sso: bool

    type: Literal["organization"] = "organization"


SubscriptionTierType = RootModel[
    Annotated[
        Union[
            OptionIndividual,
            OptionOrganization,
        ],
        Field(discriminator="type"),
    ]
]
