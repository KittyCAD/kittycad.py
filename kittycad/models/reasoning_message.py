from typing import List, Literal, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.plan_step import PlanStep
from .base import KittyCadBaseModel


class OptionText(KittyCadBaseModel):
    """Plain text reasoning."""

    content: str

    type: Literal["text"] = "text"


class OptionMarkdown(KittyCadBaseModel):
    """Markdown formatted reasoning."""

    content: str

    type: Literal["markdown"] = "markdown"


class OptionKclDocs(KittyCadBaseModel):
    """Reasoning that contains the KCL docs relevant to the reasoning."""

    content: str

    type: Literal["kcl_docs"] = "kcl_docs"


class OptionKclCodeExamples(KittyCadBaseModel):
    """Reasoning that contains the KCL code examples relevant to the reasoning."""

    content: str

    type: Literal["kcl_code_examples"] = "kcl_code_examples"


class OptionFeatureTreeOutline(KittyCadBaseModel):
    """Reasoning that contains a feature tree outline."""

    content: str

    type: Literal["feature_tree_outline"] = "feature_tree_outline"


class OptionDesignPlan(KittyCadBaseModel):
    """Reasoning that contains a design plan with steps."""

    steps: List[PlanStep]

    type: Literal["design_plan"] = "design_plan"


class OptionGeneratedKclCode(KittyCadBaseModel):
    """Reasoning that contains potential KCL code, this code has not been executed yet. It might not even compile or be valid KCL code."""

    code: str

    type: Literal["generated_kcl_code"] = "generated_kcl_code"


class OptionKclCodeError(KittyCadBaseModel):
    """Reasoning containing an error message from executing the KCL code."""

    error: str

    type: Literal["kcl_code_error"] = "kcl_code_error"


class OptionCreatedKclFile(KittyCadBaseModel):
    """A KCL file that is being created by the AI. This might contain invalid KCL code."""

    content: str

    file_name: str

    type: Literal["created_kcl_file"] = "created_kcl_file"


class OptionUpdatedKclFile(KittyCadBaseModel):
    """A KCL file that is being updated by the AI. This might contain invalid KCL code."""

    content: str

    file_name: str

    type: Literal["updated_kcl_file"] = "updated_kcl_file"


class OptionDeletedKclFile(KittyCadBaseModel):
    """A KCL file that is being deleted by the AI."""

    file_name: str

    type: Literal["deleted_kcl_file"] = "deleted_kcl_file"


ReasoningMessage = RootModel[
    Annotated[
        Union[
            OptionText,
            OptionMarkdown,
            OptionKclDocs,
            OptionKclCodeExamples,
            OptionFeatureTreeOutline,
            OptionDesignPlan,
            OptionGeneratedKclCode,
            OptionKclCodeError,
            OptionCreatedKclFile,
            OptionUpdatedKclFile,
            OptionDeletedKclFile,
        ],
        Field(discriminator="type"),
    ]
]
