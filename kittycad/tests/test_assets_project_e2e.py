import time
from pathlib import Path
from typing import Dict

import pytest

from kittycad import KittyCAD
from kittycad._io_types import SyncUpload
from kittycad.models.api_call_status import ApiCallStatus
from kittycad.models.text_to_cad_multi_file_iteration_body import (
    TextToCadMultiFileIterationBody,
)
from kittycad.models.text_to_cad_response import OptionTextToCadMultiFileIteration


def test_assets_kcl_project_roundtrip_outputs_match_inputs():
    """E2E: iterate on the assets/test_kcl_project and verify all files are returned.

    - Uploads every .kcl file under assets/test_kcl_project (preserving relative paths)
    - Calls create_text_to_cad_multi_file_iteration
    - Polls get_text_to_cad_parts_for_user until Completed/Failed
    - Asserts the number of outputs equals the number of input attachments
    """

    # Locate the project directory from repo root (kittycad/tests/ -> repo root)
    repo_root = Path(__file__).resolve().parents[2]
    proj_path = repo_root / "assets" / "test_kcl_project"
    assert proj_path.is_dir(), f"Project directory not found: {proj_path}"

    # Gather all .kcl files and build attachment map with relative keys
    file_paths = [p for p in proj_path.rglob("*") if p.is_file() and p.suffix == ".kcl"]
    assert file_paths, "No .kcl files found in test project"
    # Ensure the fixture project shape: exactly 3 KCL files
    assert len(file_paths) == 3, (
        f"Expected 3 input .kcl files, found {len(file_paths)}: {[str(p.relative_to(proj_path)) for p in file_paths]}"
    )

    file_attachments: Dict[str, SyncUpload] = {
        str(fp.relative_to(proj_path)): fp for fp in file_paths
    }

    body = TextToCadMultiFileIterationBody(
        prompt="make the bench longer",
        source_ranges=[],
        kcl_version="1.0",
        project_name="test_kcl_project",
    )

    with KittyCAD() as client:
        created = client.ml.create_text_to_cad_multi_file_iteration(
            body=body, file_attachments=file_attachments
        )

        deadline = time.time() + 180  # allow up to 3 minutes
        last_status = None
        while time.time() < deadline:
            result = client.ml.get_text_to_cad_parts_for_user(id=str(created.id))
            root = result.root
            last_status = str(root.status)

            if root.status == ApiCallStatus.COMPLETED:
                assert isinstance(root, OptionTextToCadMultiFileIteration), (
                    f"Unexpected result type: {type(root)}"
                )
                assert root.outputs is not None, "Completed response missing outputs"

                actual_keys = set(root.outputs.keys())
                expected_keys = set(file_attachments.keys())

                assert actual_keys == expected_keys, (
                    f"Output keys mismatch. expected={sorted(expected_keys)} actual={sorted(actual_keys)}"
                )
                assert len(actual_keys) == 3, (
                    f"Expected 3 outputs, got {len(actual_keys)} with keys: {sorted(actual_keys)}"
                )
                return

            if root.status == ApiCallStatus.FAILED:
                pytest.fail(f"Async operation failed: {getattr(root, 'error', '')}")

            time.sleep(2)

        pytest.fail(f"Async operation did not complete in time (status={last_status})")
