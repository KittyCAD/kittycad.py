from typing import Union

from pydantic import BaseModel, ConfigDict, RootModel


class Response(BaseModel):
    """Response to the modeling command."""

    model_config = ConfigDict(protected_namespaces=())


class Errors(BaseModel):
    """Errors that occurred during the modeling command."""

    model_config = ConfigDict(protected_namespaces=())


BatchResponse = RootModel[
    Union[
        Response,
        Errors,
    ]
]
