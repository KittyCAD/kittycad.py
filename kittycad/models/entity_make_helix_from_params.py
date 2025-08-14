from pydantic import BaseModel, ConfigDict


class Entitymakehelixfromparams(BaseModel):
    """The response from the `EntityMakeHelixFromParams` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
