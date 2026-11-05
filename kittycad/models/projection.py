from typing import Literal, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from .base import KittyCadBaseModel


class OptionOrthographic(KittyCadBaseModel):
    """Orthographic (parallel) projection."""

    type: Literal["orthographic"] = "orthographic"


class OptionPerspective(KittyCadBaseModel):
    """Perspective projection."""

    type: Literal["perspective"] = "perspective"


Projection = RootModel[
    Annotated[
        Union[
            OptionOrthographic,
            OptionPerspective,
        ],
        Field(discriminator="type"),
    ]
]
