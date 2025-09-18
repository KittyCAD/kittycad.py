import time
from pathlib import Path

import pytest

from kittycad import KittyCAD
from kittycad.models.api_call_status import ApiCallStatus
from kittycad.models.async_api_call_output import OptionTextToCadMultiFileIteration
from kittycad.models.text_to_cad_multi_file_iteration_body import (
    TextToCadMultiFileIterationBody,
)


def test_text_to_cad_multi_file_iteration_returns_both_files(tmp_path: Path):
    """Test that a project with main.kcl and subdir/main.kcl is echoed back as two files.

    This hits the real Zoo API (no mocks). It posts a two-file KCL project
    and verifies the async operation returns outputs for both files using
    their original relative paths.
    """

    # Create project files
    main_kcl_code = "// Glorious cube\n\nsideLength = 10"
    subdir_main_kcl_code = "// Glorious cylinder\n\nheight = 20"

    main_path = tmp_path / "main.kcl"
    subdir_path = tmp_path / "subdir" / "main.kcl"
    subdir_path.parent.mkdir(parents=True, exist_ok=True)
    main_path.write_text(main_kcl_code)
    subdir_path.write_text(subdir_main_kcl_code)

    body = TextToCadMultiFileIterationBody(
        prompt=("Add a simple cube to main.kcl and a cylinder to subdir/main.kcl"),
        source_ranges=[],
        kcl_version="1.0",
        project_name="Glorious cube and cylinder",
    )

    # Use real API; token and optional ZOO_HOST are read by KittyCAD()
    with KittyCAD() as client:
        created = client.ml.create_text_to_cad_multi_file_iteration(
            body=body,
            file_attachments={
                "main.kcl": str(main_path),
                "subdir/main.kcl": str(subdir_path),
            },
        )

        # Poll async operation until completion
        op_id = str(created.id)
        deadline = time.time() + 180  # 3 minutes
        last_status = None

        while time.time() < deadline:
            call_out = client.api_calls.get_async_operation(id=op_id)
            result = call_out.root
            last_status = str(result.status)
            if result.status == ApiCallStatus.COMPLETED:
                # Ensure we got the correct output type
                assert isinstance(result, OptionTextToCadMultiFileIteration), (
                    f"Unexpected result type: {type(result)}"
                )

                # Validate basic shape
                assert hasattr(result, "model_version")  # may be empty on some releases
                assert result.outputs is not None

                outputs = result.outputs
                # Exactly two files, with expected relative paths
                assert len(outputs) == 2
                assert "main.kcl" in outputs
                assert "subdir/main.kcl" in outputs
                return

            if result.status == ApiCallStatus.FAILED:
                pytest.fail(f"Async operation failed: {getattr(result, 'error', '')}")

            time.sleep(2)

        pytest.fail(f"Async operation did not complete in time (status={last_status})")
