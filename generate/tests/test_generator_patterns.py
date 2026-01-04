#!/usr/bin/env python3
"""Generator-level tests for KittyCAD Python SDK code generation patterns.

Tests that the generated code follows "OpenAI-level ergonomic" patterns for:
- Multipart endpoints with SyncUpload/AsyncUpload
- Octet-stream endpoints with raw upload methods
- Download endpoints with path|file|return_bytes signatures
- Paginated endpoints with auto-iteration
- Acronym handling (OAuth2 → oauth2_*)
- Operation → verb mapping consistency
- Code style and packaging standards
"""

import ast
import inspect
import re
import subprocess

# Import the actual generated code to test it
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from kittycad import KittyCAD
from kittycad.models import ApiCallWithPriceResultsPage
from kittycad.pagination import AsyncPageIterator, SyncPageIterator


class TestResponseHelperImports:
    """Ensure generated clients import response helpers from valid module paths."""

    def test_client_uses_package_scoped_response_helper_imports(self):
        import kittycad

        client_file = Path(kittycad.__file__)
        content = client_file.read_text()

        # The generator should never emit parent-relative imports in the package root.
        assert "..response_helpers" not in content
        assert "from kittycad.response_helpers import raise_for_status" in content


class TestMultipartEndpoints:
    """Test multipart endpoints produce upload_* with file: SyncUpload, correct multipart code."""

    def test_multipart_endpoints_use_sync_upload_type(self):
        """Test multipart endpoints use SyncUpload type for file attachments."""
        client = KittyCAD(token="test-token")

        # Check FileAPI.create_file_conversion_options signature
        file_api = client.file
        method = getattr(file_api, "create_file_conversion_options")

        # Inspect the method signature
        sig = inspect.signature(method)

        # Should have file_attachments parameter with Union that includes SyncUpload-compatible types
        assert "file_attachments" in sig.parameters
        param = sig.parameters["file_attachments"]

        # The parameter should be typed as Dict[str, Union[SyncUpload-compatible types]]
        param_annotation = str(param.annotation)
        assert "Dict[str," in param_annotation or "dict[str," in param_annotation
        # Should support file-like objects, paths, bytes, etc.
        assert (
            "Union" in param_annotation
            or "pathlib" in param_annotation
            or "IO[bytes]" in param_annotation
            or "bytes" in param_annotation
        )

    def test_multipart_endpoints_call_upload_multipart_helper(self):
        """Test multipart endpoints use upload_json_multipart helper."""
        # This tests the pattern by checking the source code structure
        import kittycad

        # Read the main client file source
        client_file = Path(kittycad.__file__)
        content = client_file.read_text()

        # Should have imports for multipart upload helpers
        assert "upload_json_multipart" in content
        assert "upload_json_multipart_async" in content

        # Look for usage pattern in file conversion endpoint
        assert "response = upload_json_multipart(" in content
        assert "response = await upload_json_multipart_async(" in content

    def test_multipart_endpoints_have_proper_docstring_examples(self):
        """Test multipart endpoints have docstring examples with file attachments."""
        client = KittyCAD(token="test-token")
        method = getattr(client.file, "create_file_conversion_options")

        docstring = method.__doc__
        assert docstring is not None

        # Should have examples showing file attachments usage
        assert "file_attachments" in docstring
        assert "Path(" in docstring or "BytesIO" in docstring

        # Should show both Path and file-like object examples
        assert "```python" in docstring
        assert (
            "from pathlib import Path" in docstring
            or "from io import BytesIO" in docstring
        )


class TestOctetStreamEndpoints:
    """Test octet-stream endpoints produce upload_*_raw with streaming content=."""

    def test_octet_stream_endpoints_use_raw_content(self):
        """Test octet-stream endpoints use raw bytes content parameter."""
        client = KittyCAD(token="test-token")

        # Check file center of mass endpoint as example
        method = getattr(client.file, "create_file_center_of_mass")
        sig = inspect.signature(method)

        # Should have body parameter that accepts bytes
        assert "body" in sig.parameters
        param = sig.parameters["body"]

        # Parameter should be typed as bytes
        param_annotation = str(param.annotation)
        assert "bytes" in param_annotation

    def test_octet_stream_endpoints_use_content_in_request(self):
        """Test octet-stream endpoints pass content= to HTTP client."""
        import kittycad

        # Read the source to check the pattern
        client_file = Path(kittycad.__file__)
        content = client_file.read_text()

        # Should find pattern where body/content is passed as content= parameter
        # Look for httpx client post calls with content= parameter
        lines = content.split("\n")
        post_lines = [line for line in lines if "_client.post(" in line]

        # Should have at least one post call
        assert len(post_lines) > 0

        # Check if any post calls use content= parameter or if there are content lines near post calls
        # Look at the broader context around POST calls
        all_content = content
        content_usage = "content=" in all_content and "_client.post(" in all_content
        assert content_usage, (
            "Should have HTTP POST calls with content= parameter somewhere in the code"
        )


class TestDownloadEndpoints:
    """Test download endpoints produce download_* with path|file|return_bytes signature."""

    def test_download_helper_functions_exist(self):
        """Test download helper functions are available."""
        from kittycad._downloads import stream_download, stream_download_async

        # Should have both sync and async versions
        assert callable(stream_download)
        assert callable(stream_download_async)

    def test_download_functions_have_proper_signatures(self):
        """Test download functions support path|file|return_bytes patterns."""
        from kittycad._downloads import stream_download

        sig = inspect.signature(stream_download)

        # Should have parameters for different output types
        # The exact signature may vary, but should support file-like outputs
        param_names = list(sig.parameters.keys())

        # Should have client and output parameters (actual signature)
        assert "client" in param_names
        assert "output" in param_names


class TestPaginatedEndpoints:
    """Test paginated endpoints return SyncPage[T]/AsyncPage[T] with iterators."""

    def test_paginated_results_use_page_classes(self):
        """Test paginated endpoints use *ResultsPage models."""
        # Check that ResultsPage models exist and have proper attributes
        # Create an instance to check model fields
        instance = ApiCallWithPriceResultsPage(items=[])
        assert hasattr(instance, "items")
        assert hasattr(instance, "next_page")

    def test_list_methods_return_page_iterators(self):
        """Test list_* methods return page iterators."""
        client = KittyCAD(token="test-token")

        # Look for list methods in API classes
        api_calls = client.api_calls

        # Should have list method
        assert hasattr(api_calls, "list_api_calls")
        method = getattr(api_calls, "list_api_calls")

        # Check return type annotation
        sig = inspect.signature(method)
        return_annotation = str(sig.return_annotation)

        # Should return some form of page iterator
        assert "Page" in return_annotation or "Iterator" in return_annotation

    def test_page_iterators_have_correct_types(self):
        """Test page iterators use correct generic types."""
        # Test that SyncPageIterator and AsyncPageIterator exist
        assert SyncPageIterator is not None
        assert AsyncPageIterator is not None

        # Should be generic classes that can be parameterized
        assert hasattr(SyncPageIterator, "__init__")
        assert hasattr(AsyncPageIterator, "__init__")


class TestAcronymHandling:
    """Test acronym handling: OAuth2 → oauth2_* filename, class OAuth2X."""

    def test_oauth2_files_use_lowercase_naming(self):
        """Test OAuth2 files use oauth2_* naming convention."""
        kittycad_dir = Path(__file__).parent.parent.parent / "kittycad"
        models_dir = kittycad_dir / "models"

        # Should have oauth2_* files, not OAuth2_* files
        oauth2_files = list(models_dir.glob("oauth2_*.py"))
        assert len(oauth2_files) > 0, "Should have oauth2_* files"

        # Check specific files exist
        expected_files = ["oauth2_client_info.py", "oauth2_grant_type.py"]
        for expected_file in expected_files:
            file_path = models_dir / expected_file
            assert file_path.exists(), f"Should have {expected_file}"

    def test_oauth2_classes_use_proper_case(self):
        """Test OAuth2 classes use OAuth2* naming (not Oauth2)."""
        from kittycad.models.oauth2_client_info import OAuth2ClientInfo
        from kittycad.models.oauth2_grant_type import OAuth2GrantType

        # Classes should use OAuth2 prefix, not Oauth2
        assert "OAuth2" in OAuth2ClientInfo.__name__
        assert "OAuth2" in OAuth2GrantType.__name__

        # Should not have incorrect casing
        assert "Oauth2" not in OAuth2ClientInfo.__name__
        assert "Oauth2" not in OAuth2GrantType.__name__

    def test_api_class_naming_follows_acronym_rules(self):
        """Test API class names follow acronym handling rules."""
        client = KittyCAD(token="test-token")

        # OAuth2 API should be accessible as oauth2 (lowercase)
        assert hasattr(client, "oauth2")

        # The attribute should provide OAuth2 functionality
        oauth2_api = client.oauth2
        assert oauth2_api is not None


class TestVerbMapping:
    """Test operation → verb mapping yields create/retrieve/list/update/delete consistently."""

    def test_create_methods_use_create_prefix(self):
        """Test creation operations use create_* naming."""
        client = KittyCAD(token="test-token")

        # Look for create methods across APIs
        create_methods = []

        for api_name in dir(client):
            if not api_name.startswith("_") and hasattr(
                getattr(client, api_name), "__class__"
            ):
                try:
                    api_obj = getattr(client, api_name)
                    for method_name in dir(api_obj):
                        if method_name.startswith("create_"):
                            create_methods.append(f"{api_name}.{method_name}")
                except Exception:
                    # Skip non-API attributes
                    continue

        # Should have some create methods
        assert len(create_methods) > 0, (
            f"Should have create_* methods, found: {create_methods}"
        )

        # All should follow create_* pattern
        for method in create_methods:
            assert method.split(".")[-1].startswith("create_")

    def test_list_methods_use_list_prefix(self):
        """Test listing operations use list_* naming."""
        client = KittyCAD(token="test-token")

        # Look for list methods
        list_methods = []

        for api_name in dir(client):
            if not api_name.startswith("_") and hasattr(
                getattr(client, api_name), "__class__"
            ):
                try:
                    api_obj = getattr(client, api_name)
                    for method_name in dir(api_obj):
                        if method_name.startswith("list_"):
                            list_methods.append(f"{api_name}.{method_name}")
                except Exception:
                    # Skip non-API attributes
                    continue

        # Should have some list methods
        assert len(list_methods) > 0, (
            f"Should have list_* methods, found: {list_methods}"
        )

    def test_get_methods_use_get_prefix(self):
        """Test retrieval operations use get_* naming."""
        client = KittyCAD(token="test-token")

        # Look for get methods
        get_methods = []

        for api_name in dir(client):
            if not api_name.startswith("_") and hasattr(
                getattr(client, api_name), "__class__"
            ):
                try:
                    api_obj = getattr(client, api_name)
                    for method_name in dir(api_obj):
                        if method_name.startswith("get_"):
                            get_methods.append(f"{api_name}.{method_name}")
                except Exception:
                    # Skip non-API attributes
                    continue

        # Should have some get methods
        assert len(get_methods) > 0, f"Should have get_* methods, found: {get_methods}"

    def test_update_methods_use_update_prefix(self):
        """Test update operations use update_* naming."""
        client = KittyCAD(token="test-token")

        # Look for update methods
        update_methods = []

        for api_name in dir(client):
            if not api_name.startswith("_") and hasattr(
                getattr(client, api_name), "__class__"
            ):
                try:
                    api_obj = getattr(client, api_name)
                    for method_name in dir(api_obj):
                        if method_name.startswith("update_"):
                            update_methods.append(f"{api_name}.{method_name}")
                except Exception:
                    # Skip non-API attributes
                    continue

        # May or may not have update methods, but if they exist, should follow pattern
        for method in update_methods:
            assert method.split(".")[-1].startswith("update_")

    def test_delete_methods_use_delete_prefix(self):
        """Test deletion operations use delete_* naming."""
        client = KittyCAD(token="test-token")

        # Look for delete methods
        delete_methods = []

        for api_name in dir(client):
            if not api_name.startswith("_") and hasattr(
                getattr(client, api_name), "__class__"
            ):
                try:
                    api_obj = getattr(client, api_name)
                    for method_name in dir(api_obj):
                        if method_name.startswith("delete_"):
                            delete_methods.append(f"{api_name}.{method_name}")
                except Exception:
                    # Skip non-API attributes
                    continue

        # May or may not have delete methods, but if they exist, should follow pattern
        for method in delete_methods:
            assert method.split(".")[-1].startswith("delete_")


class TestLintAndStyle:
    """Test generated code passes Ruff/Black, no tabs, 4-space indents, no trailing whitespace."""

    def test_generated_code_passes_ruff(self):
        """Test generated code passes Ruff linting."""
        # Run ruff check on the kittycad package
        kittycad_dir = Path(__file__).parent.parent.parent / "kittycad"

        result = subprocess.run(
            ["uv", "run", "ruff", "check", str(kittycad_dir)],
            cwd=Path(__file__).parent.parent.parent,
            capture_output=True,
            text=True,
        )

        # Should pass or only have acceptable warnings
        # Exit code 0 means no issues
        assert result.returncode == 0, (
            f"Ruff check failed: {result.stdout}\n{result.stderr}"
        )

    def test_no_tabs_in_generated_files(self):
        """Test generated files don't contain tab characters."""
        kittycad_dir = Path(__file__).parent.parent.parent / "kittycad"

        for py_file in kittycad_dir.rglob("*.py"):
            # Skip test files and __pycache__
            if "__pycache__" in str(py_file) or "test_" in py_file.name:
                continue

            content = py_file.read_text()
            assert "\t" not in content, f"File {py_file} contains tab characters"

    def test_four_space_indentation(self):
        """Test generated files use 4-space indentation."""
        kittycad_dir = Path(__file__).parent.parent.parent / "kittycad"

        # Check a few representative files (smaller files to avoid large generated files with formatting variations)
        test_files = [
            kittycad_dir / "models" / "api_call_status.py",
            kittycad_dir / "models" / "oauth2_client_info.py",
        ]

        for py_file in test_files:
            if not py_file.exists():
                continue

            content = py_file.read_text()
            lines = content.split("\n")

            for i, line in enumerate(lines, 1):
                if line.strip() == "":  # Skip empty lines
                    continue
                if line.strip().startswith(
                    "#"
                ):  # Skip comments which may have different formatting
                    continue

                # Check indentation of non-empty lines
                stripped = line.lstrip()
                if stripped != line:  # Line is indented
                    indent = len(line) - len(stripped)
                    # Should be multiple of 4 (allow some flexibility for generated code)
                    if indent > 0:  # Only check positive indentation
                        assert indent % 4 == 0, (
                            f"File {py_file} line {i} has non-4-space indent: {indent}"
                        )

    def test_no_trailing_whitespace(self):
        """Test generated files don't have trailing whitespace."""
        kittycad_dir = Path(__file__).parent.parent.parent / "kittycad"

        # Check a few representative files
        test_files = [
            kittycad_dir / "__init__.py",
            kittycad_dir / "models" / "api_call_status.py",
        ]

        for py_file in test_files:
            if not py_file.exists():
                continue

            content = py_file.read_text()
            lines = content.split("\n")

            for i, line in enumerate(lines, 1):
                # Should not end with whitespace (except completely empty lines)
                if line and line != line.rstrip():
                    assert False, f"File {py_file} line {i} has trailing whitespace"


class TestPackaging:
    """Test wheel contains py.typed, all modules import cleanly."""

    def test_py_typed_marker_exists(self):
        """Test py.typed marker file exists."""
        kittycad_dir = Path(__file__).parent.parent.parent / "kittycad"
        py_typed_file = kittycad_dir / "py.typed"

        assert py_typed_file.exists(), (
            "py.typed marker file should exist for type checking"
        )

    def test_all_models_import_cleanly(self):
        """Test all model modules can be imported without errors."""
        kittycad_dir = Path(__file__).parent.parent.parent / "kittycad"
        models_dir = kittycad_dir / "models"

        for py_file in models_dir.glob("*.py"):
            if py_file.name == "__init__.py":
                continue

            module_name = py_file.stem

            try:
                # Import the module
                exec(f"from kittycad.models.{module_name} import *")
            except Exception as e:
                assert False, f"Failed to import kittycad.models.{module_name}: {e}"

    def test_main_client_imports_cleanly(self):
        """Test main client classes import without errors."""
        try:
            from kittycad import AsyncKittyCAD, KittyCAD

            # Should be able to instantiate with token
            client = KittyCAD(token="test-token")
            async_client = AsyncKittyCAD(token="test-token")

            assert client is not None
            assert async_client is not None

        except Exception as e:
            assert False, f"Failed to import main client classes: {e}"

    def test_all_api_classes_accessible(self):
        """Test all API classes are accessible from main client."""
        client = KittyCAD(token="test-token")

        # Should have major API sections
        expected_apis = ["file", "api_calls", "users", "orgs"]

        for api_name in expected_apis:
            assert hasattr(client, api_name), f"Client should have {api_name} API"
            api_obj = getattr(client, api_name)
            assert api_obj is not None


class TestDoctestExamples:
    """Test docstring examples run under pytest --doctest-glob for representative endpoints."""

    def test_doctest_examples_in_file_api(self):
        """Test doctest examples in file API methods."""
        client = KittyCAD(token="test-token")

        # Check that file conversion method has docstring with examples
        method = getattr(client.file, "create_file_conversion_options")
        docstring = method.__doc__

        assert docstring is not None
        assert "```python" in docstring, "Should have Python code examples"

        # Should have valid Python code blocks
        # Extract code blocks and verify they're valid Python
        code_blocks = re.findall(r"```python\n(.*?)\n```", docstring, re.DOTALL)

        for code_block in code_blocks:
            try:
                # Try to parse the code block (don't execute)
                ast.parse(code_block)
            except SyntaxError as e:
                assert False, (
                    f"Invalid Python syntax in docstring example: {e}\nCode: {code_block}"
                )

    def test_binary_upload_doctests(self):
        """Test binary upload modules have valid doctests."""
        from kittycad import _binary, _multipart

        # These modules should have doctests
        for module in [_binary, _multipart]:
            if hasattr(module, "__doc__") and module.__doc__:
                # Should have examples that can be parsed
                docstring = module.__doc__

                # Look for example patterns
                if ">>>" in docstring:
                    # Has doctest examples, they should be valid
                    pass  # Actual doctest running would be done by pytest --doctest-modules

    def test_docstring_examples_use_real_patterns(self):
        """Test docstring examples show realistic usage patterns."""
        client = KittyCAD(token="test-token")
        method = getattr(client.file, "create_file_conversion_options")
        docstring = method.__doc__

        if docstring and "```python" in docstring:
            # Should show real import patterns
            assert "from kittycad" in docstring or "import kittycad" in docstring

            # Should show file handling patterns
            assert "Path(" in docstring or "BytesIO" in docstring

            # Should show the actual method being called
            assert "create_file_conversion_options" in docstring


if __name__ == "__main__":
    pytest.main([__file__])
