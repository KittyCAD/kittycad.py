from typing import Literal, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from .base import KittyCadBaseModel


class OptionCreated(KittyCadBaseModel):
    """The file was created by Zookeeper."""

    contents: str

    path: str

    status: Literal["created"] = "created"


class OptionModified(KittyCadBaseModel):
    """The file was modified by Zookeeper."""

    diff: str

    path: str

    status: Literal["modified"] = "modified"


class OptionDeleted(KittyCadBaseModel):
    """The file was deleted by Zookeeper."""

    path: str

    previous_contents: str

    status: Literal["deleted"] = "deleted"


ZookeeperEditPatchFile = RootModel[
    Annotated[
        Union[
            OptionCreated,
            OptionModified,
            OptionDeleted,
        ],
        Field(discriminator="status"),
    ]
]
