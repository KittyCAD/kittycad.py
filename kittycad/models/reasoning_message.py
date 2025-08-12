from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated


class OptionText(BaseModel):
    """Plain text reasoning."""

    content: str

    type: Literal["text"] = "text"

    model_config = ConfigDict(protected_namespaces=())


class OptionKclDocs(BaseModel):
    """Reasoning that contains the KCL docs relevant to the reasoning."""

    content: str

    type: Literal["kcl_docs"] = "kcl_docs"

    model_config = ConfigDict(protected_namespaces=())


class OptionKclCodeExamples(BaseModel):
    """Reasoning that contains the KCL code examples relevant to the reasoning."""

    content: str

    type: Literal["kcl_code_examples"] = "kcl_code_examples"

    model_config = ConfigDict(protected_namespaces=())


class OptionFeatureTreeOutline(BaseModel):
    """Reasoning that contains a feature tree outline."""

    content: str

    type: Literal["feature_tree_outline"] = "feature_tree_outline"

    model_config = ConfigDict(protected_namespaces=())


class OptionGeneratedKclCode(BaseModel):
    """Reasoning that contains potential KCL code, this code has not been executed yet. It might not even compile or be valid KCL code."""

    code: str

    type: Literal["generated_kcl_code"] = "generated_kcl_code"

    model_config = ConfigDict(protected_namespaces=())


class OptionKclCodeError(BaseModel):
    """Reasoning containing an error message from executing the KCL code."""

    error: str

    type: Literal["kcl_code_error"] = "kcl_code_error"

    model_config = ConfigDict(protected_namespaces=())


class OptionCreatedKclFile(BaseModel):
    """A KCL file that is being created by the AI. This might contain invalid KCL code."""

    content: str

    file_name: str

    type: Literal["created_kcl_file"] = "created_kcl_file"

    model_config = ConfigDict(protected_namespaces=())


class OptionUpdatedKclFile(BaseModel):
    """A KCL file that is being updated by the AI. This might contain invalid KCL code."""

    content: str

    file_name: str

    type: Literal["updated_kcl_file"] = "updated_kcl_file"

    model_config = ConfigDict(protected_namespaces=())


class OptionDeletedKclFile(BaseModel):
    """A KCL file that is being deleted by the AI."""

    file_name: str

    type: Literal["deleted_kcl_file"] = "deleted_kcl_file"

    model_config = ConfigDict(protected_namespaces=())


ReasoningMessage = RootModel[
    Annotated[
        Union[
            OptionText,
            OptionKclDocs,
            OptionKclCodeExamples,
            OptionFeatureTreeOutline,
            OptionGeneratedKclCode,
            OptionKclCodeError,
            OptionCreatedKclFile,
            OptionUpdatedKclFile,
            OptionDeletedKclFile,
        ],
        Field(discriminator="type"),
    ]
]
