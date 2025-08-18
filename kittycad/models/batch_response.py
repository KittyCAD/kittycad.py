from typing import Union

from pydantic import RootModel

from .base import KittyCadBaseModel


class Response(KittyCadBaseModel):
    """Response to the modeling command."""


class Errors(KittyCadBaseModel):
    """Errors that occurred during the modeling command."""


BatchResponse = RootModel[
    Union[
        Response,
        Errors,
    ]
]
