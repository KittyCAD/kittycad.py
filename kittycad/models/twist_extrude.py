from pydantic import BaseModel, ConfigDict


class Twistextrude(BaseModel):
    """The response from the `TwistExtrude` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
