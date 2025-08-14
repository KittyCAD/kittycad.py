from pydantic import BaseModel, ConfigDict


class TwistExtrude(BaseModel):
    """The response from the `TwistExtrude` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
