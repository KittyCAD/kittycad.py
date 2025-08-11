from typing import Union

from pydantic import RootModel

from .text_to_cad import TextToCad
from .text_to_cad_iteration import TextToCadIteration
from .text_to_cad_multi_file_iteration import TextToCadMultiFileIteration

TextToCadResponse = RootModel[
    Union[
        TextToCad,
        TextToCadIteration,
        TextToCadMultiFileIteration,
    ]
]
