from typing import Union

from pydantic import BaseModel, ConfigDict, RootModel



class response(BaseModel):
    """Response to the modeling command."""

    model_config = ConfigDict(protected_namespaces=())


class errors(BaseModel):
    """Errors that occurred during the modeling command."""

    model_config = ConfigDict(protected_namespaces=())


BatchResponse = RootModel[
    Union[
        response,
        errors,
    ]
]
