import datetime
from typing import Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated

from ..models.modeling_app_event_type import ModelingAppEventType


class modeling_app_event(BaseModel):
    """An event related to modeling app files"""

    attachment_uri: Optional[str] = None

    created_at: datetime.datetime

    event_type: ModelingAppEventType

    last_compiled_at: Optional[datetime.datetime] = None

    project_description: Optional[str] = None

    project_name: str

    source_id: str

    type: Literal["modeling_app_event"] = "modeling_app_event"

    user_id: str

    model_config = ConfigDict(protected_namespaces=())


Event = RootModel[Annotated[Union[modeling_app_event,], Field(discriminator="type")]]
