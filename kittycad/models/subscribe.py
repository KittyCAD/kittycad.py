from pydantic import BaseModel, ConfigDict


class Subscribe(BaseModel):
    """The data for subscribing a user to the newsletter."""

    email: str

    model_config = ConfigDict(protected_namespaces=())
