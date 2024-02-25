
from pydantic import BaseModel, ConfigDict



class PrivacySettings(BaseModel):
    """Privacy settings for an org or user."""

    can_train_on_data: bool

    model_config = ConfigDict(protected_namespaces=())
