from typing import Union

from pydantic import RootModel

from .execution_input_artifact import ExecutionInputArtifact
from .execution_input_batch import ExecutionInputBatch

ExecutionInputUploadResponse = RootModel[
    Union[
        ExecutionInputArtifact,
        ExecutionInputBatch,
    ]
]
