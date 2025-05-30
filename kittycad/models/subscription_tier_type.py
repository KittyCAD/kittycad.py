from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated


class OptionIndividual(BaseModel):
    """A subscription tier that can be applied to individuals only."""

    type: Literal["individual"] = "individual"

    model_config = ConfigDict(protected_namespaces=())


class OptionOrganization(BaseModel):
    """An subscription tier that can be applied to organizations only."""

    saml_sso: bool

    type: Literal["organization"] = "organization"

    model_config = ConfigDict(protected_namespaces=())


SubscriptionTierType = RootModel[
    Annotated[
        Union[
            OptionIndividual,
            OptionOrganization,
        ],
        Field(discriminator="type"),
    ]
]
