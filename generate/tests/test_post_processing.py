"""Tests for examples post-processing helpers."""

import os
import sys
from pathlib import Path

# Add the parent directory to the path to import generate modules.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from post_processing import _alias_conflicting_model_imports


def _write_test_file(tmp_path: Path, content: str) -> Path:
    file_path = tmp_path / "test_examples.py"
    file_path.write_text(content)
    return file_path


def test_alias_conflicting_model_imports_aliases_duplicate_symbols(
    tmp_path: Path,
) -> None:
    file_path = _write_test_file(
        tmp_path,
        """from kittycad.models.input_format3d import InputFormat3d, OptionPly
from kittycad.models.output_format3d import OptionPly, OutputFormat3d

def build_payloads() -> None:
    InputFormat3d(OptionPly(type="ply"))
    OutputFormat3d(OptionPly(type="ply"))
""",
    )

    _alias_conflicting_model_imports(str(file_path))

    updated_content = file_path.read_text()
    assert (
        "from kittycad.models.output_format3d import OptionPly as OutputFormat3dOptionPly, OutputFormat3d"
        in updated_content
    )
    assert 'OutputFormat3d(OutputFormat3dOptionPly(type="ply"))' in updated_content
    assert 'InputFormat3d(OptionPly(type="ply"))' in updated_content


def test_alias_conflicting_model_imports_is_noop_for_unique_symbols(
    tmp_path: Path,
) -> None:
    file_path = _write_test_file(
        tmp_path,
        """from kittycad.models.input_format3d import InputFormat3d, OptionPly
from kittycad.models.output_format3d import OutputFormat3d
""",
    )

    _alias_conflicting_model_imports(str(file_path))

    updated_content = file_path.read_text()
    assert (
        "from kittycad.models.input_format3d import InputFormat3d, OptionPly"
        in updated_content
    )
    assert (
        "from kittycad.models.output_format3d import OutputFormat3d" in updated_content
    )
