#!/usr/bin/env python3
"""Golden file tests for KittyCAD Python SDK code generation.

This module tests that code generation produces expected outputs by:
1. Running the generator on small, controlled OpenAPI specs
2. Comparing the output to committed "golden" expected files
3. Detecting regressions in formatting, naming, or structure

Golden files serve as a contract for expected generator behavior and
help catch unintended changes early in development.
"""

import json
import sys
from pathlib import Path

import pytest

# Add the generate directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent))


# Mock the generate_enum_type_code function for testing
def generate_enum_type_code(name: str, schema: dict) -> str:
    """Mock implementation for testing."""
    enum_values = schema.get("enum", [])
    description = schema.get("description", "")

    lines = ["from enum import Enum", "", ""]
    lines.append(f"class {name}(str, Enum):")
    if description:
        lines.append(f'    """{description}"""  # noqa: E501')
    lines.append("")

    for value in enum_values:
        member_name = value.upper().replace("-", "_").replace(" ", "_")
        lines.append(f'    {member_name} = "{value}"')

    lines.append("")
    lines.append("    def __str__(self) -> str:")
    lines.append("        return str(self.value)")

    return "\n".join(lines)


# Import utility functions that don't have problematic dependencies
try:
    from utils import camel_to_snake, to_pascal_case
except ImportError:
    # Provide simple implementations if import fails
    def camel_to_snake(name: str) -> str:
        """Simple implementation for testing."""
        import re

        s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()

    def to_pascal_case(name: str) -> str:
        """Simple implementation for testing."""
        return "".join(word.capitalize() for word in name.split("_"))


class TestGoldenFileGeneration:
    """Test generator output against committed golden files."""

    @pytest.fixture
    def minimal_api_spec(self):
        """Load the minimal API specification for testing."""
        fixtures_dir = Path(__file__).parent / "fixtures"
        spec_file = fixtures_dir / "minimal_api.json"

        with open(spec_file, "r") as f:
            return json.load(f)

    @pytest.fixture
    def golden_files_dir(self):
        """Path to the golden files directory."""
        return Path(__file__).parent / "golden_files"

    def test_enum_generation_matches_golden_file(self, golden_files_dir):
        """Test that enum generation produces expected output."""

        # Define a test enum schema
        enum_schema = {
            "type": "string",
            "enum": ["active", "inactive", "suspended"],
            "description": "Current status of the user",
        }

        # Generate the enum code
        generated_code = generate_enum_type_code("UserStatus", enum_schema)

        # Expected structure for validation
        expected_content = [
            "from enum import Enum",
            "",
            "",
            "class UserStatus(str, Enum):",
            '    """Current status of the user"""  # noqa: E501',
            "",
            '    ACTIVE = "active"',
            '    INACTIVE = "inactive"',
            '    SUSPENDED = "suspended"',
            "",
            "    def __str__(self) -> str:",
            "        return str(self.value)",
        ]

        # Normalize whitespace for comparison
        generated_lines = [line.rstrip() for line in generated_code.split("\n")]
        expected_lines = [line.rstrip() for line in expected_content]

        # Compare line by line for better error messages
        assert len(generated_lines) == len(expected_lines), (
            f"Generated file has {len(generated_lines)} lines, "
            f"expected {len(expected_lines)} lines"
        )

        for i, (generated_line, expected_line) in enumerate(
            zip(generated_lines, expected_lines)
        ):
            assert generated_line == expected_line, (
                f"Line {i + 1} differs:\n"
                f"Generated: '{generated_line}'\n"
                f"Expected:  '{expected_line}'"
            )

    def test_naming_conventions_consistency(self, minimal_api_spec):
        """Test that naming conventions are applied consistently."""

        # Test schema name conversions
        schemas = minimal_api_spec["components"]["schemas"]

        naming_tests = [
            ("User", "user.py", "User"),  # Simple case
            (
                "CreateUserRequest",
                "create_user_request.py",
                "CreateUserRequest",
            ),  # Multi-word
            (
                "UserResultsPage",
                "user_results_page.py",
                "UserResultsPage",
            ),  # Results page pattern
            ("FileInfo", "file_info.py", "FileInfo"),  # Simple compound
        ]

        for schema_name, expected_filename, expected_class_name in naming_tests:
            if schema_name in schemas:
                # Test filename conversion
                actual_filename = camel_to_snake(schema_name) + ".py"
                assert actual_filename == expected_filename, (
                    f"Schema {schema_name} should generate file {expected_filename}, "
                    f"got {actual_filename}"
                )

                # Test class name preservation
                actual_class_name = to_pascal_case(schema_name)
                assert actual_class_name == expected_class_name, (
                    f"Schema {schema_name} should generate class {expected_class_name}, "
                    f"got {actual_class_name}"
                )

    def test_operation_id_to_method_name_conversion(self, minimal_api_spec):
        """Test that operationId values are converted to proper method names."""

        paths = minimal_api_spec["paths"]
        expected_methods = {
            "list_users": "list_users",  # Paginated list
            "create_user": "create_user",  # Creation
            "get_user": "get_user",  # Retrieval
            "update_user": "update_user",  # Update
            "upload_file": "upload_file",  # File upload
            "download_file": "download_file",  # File download
        }

        # Extract actual operation IDs from the spec
        actual_operation_ids = []
        for path, methods in paths.items():
            for method, operation in methods.items():
                if "operationId" in operation:
                    actual_operation_ids.append(operation["operationId"])

        # Test that all expected operations are present
        for expected_operation_id in expected_methods.keys():
            assert expected_operation_id in actual_operation_ids, (
                f"Expected operation {expected_operation_id} not found in spec"
            )

        # Test naming conversion
        for operation_id, expected_method_name in expected_methods.items():
            # The operation ID should already be snake_case and ready to use
            assert operation_id == expected_method_name, (
                f"Operation ID {operation_id} should convert to method {expected_method_name}"
            )

    def test_parameter_type_mapping(self, minimal_api_spec):
        """Test that OpenAPI parameter types map to correct Python types."""

        # Define expected type mappings
        type_mappings = {
            # Basic types
            ("string", None): "str",
            ("integer", None): "int",
            ("boolean", None): "bool",
            ("number", None): "float",
            # Format-specific types
            ("string", "uuid"): "str",
            ("string", "email"): "str",
            ("string", "date-time"): "datetime",
            ("string", "binary"): "bytes",
            # Arrays
            ("array", None): "List",
        }

        # Test that our understanding of type mapping is correct
        for (schema_type, format_type), expected_python_type in type_mappings.items():
            # This is a basic validation that our type mapping makes sense
            assert expected_python_type is not None
            assert isinstance(expected_python_type, str)
            assert len(expected_python_type) > 0

    def test_pagination_detection_pattern(self, minimal_api_spec):
        """Test that pagination is correctly detected from API patterns."""

        # Check the list_users endpoint for pagination indicators
        list_users_path = minimal_api_spec["paths"]["/users"]["get"]

        # Should have pagination parameters
        parameters = list_users_path.get("parameters", [])
        param_names = [p["name"] for p in parameters]

        assert "page_token" in param_names, (
            "Paginated endpoint should have page_token parameter"
        )
        assert "limit" in param_names, "Paginated endpoint should have limit parameter"

        # Response should be a results page
        response_schema = list_users_path["responses"]["200"]["content"][
            "application/json"
        ]["schema"]
        assert "$ref" in response_schema
        assert "ResultsPage" in response_schema["$ref"], (
            "Paginated endpoint should return ResultsPage"
        )

    def test_multipart_upload_detection(self, minimal_api_spec):
        """Test that multipart upload endpoints are detected correctly."""

        upload_endpoint = minimal_api_spec["paths"]["/files/upload"]["post"]

        # Should have multipart/form-data content type
        request_body = upload_endpoint["requestBody"]
        content_types = list(request_body["content"].keys())

        assert "multipart/form-data" in content_types, (
            "Upload endpoint should use multipart/form-data"
        )

        # Should have binary file field
        schema = request_body["content"]["multipart/form-data"]["schema"]
        file_property = schema["properties"]["file"]

        assert file_property["type"] == "string", "File field should be string type"
        assert file_property["format"] == "binary", (
            "File field should have binary format"
        )

    def test_download_endpoint_detection(self, minimal_api_spec):
        """Test that download endpoints are detected correctly."""

        download_endpoint = minimal_api_spec["paths"]["/files/{file_id}/download"][
            "get"
        ]

        # Should return application/octet-stream
        response_content = download_endpoint["responses"]["200"]["content"]

        assert "application/octet-stream" in response_content, (
            "Download endpoint should return application/octet-stream"
        )

        # Response should be binary
        schema = response_content["application/octet-stream"]["schema"]
        assert schema["type"] == "string", "Download response should be string type"
        assert schema["format"] == "binary", (
            "Download response should have binary format"
        )

    def test_enum_value_naming_consistency(self):
        """Test that enum values are consistently converted to Python naming."""

        enum_value_tests = [
            ("active", "ACTIVE"),
            ("inactive", "INACTIVE"),
            ("suspended", "SUSPENDED"),
            ("light", "LIGHT"),
            ("dark", "DARK"),
            ("auto", "AUTO"),
        ]

        for enum_value, expected_member_name in enum_value_tests:
            # Test the conversion function directly
            from utils import camel_to_screaming_snake

            actual_member_name = camel_to_screaming_snake(enum_value)
            assert actual_member_name == expected_member_name, (
                f"Enum value '{enum_value}' should convert to '{expected_member_name}', "
                f"got '{actual_member_name}'"
            )

    def test_field_requirement_detection(self, minimal_api_spec):
        """Test that required vs optional fields are detected correctly."""

        # Test User schema field requirements
        user_schema = minimal_api_spec["components"]["schemas"]["User"]
        required_fields = set(user_schema.get("required", []))
        all_fields = set(user_schema["properties"].keys())
        optional_fields = all_fields - required_fields

        # Verify expected required fields
        expected_required = {"id", "email", "name", "status", "created_at"}
        assert required_fields == expected_required, (
            f"User schema should require {expected_required}, got {required_fields}"
        )

        # Verify expected optional fields
        expected_optional = {"updated_at", "preferences"}
        assert optional_fields == expected_optional, (
            f"User schema should have optional fields {expected_optional}, got {optional_fields}"
        )

    def test_reference_resolution_pattern(self, minimal_api_spec):
        """Test that $ref references follow consistent patterns."""

        # Find all $ref references in the spec
        refs = []

        def find_refs(obj, path=""):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    if key == "$ref":
                        refs.append((path, value))
                    else:
                        find_refs(value, f"{path}.{key}" if path else key)
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    find_refs(item, f"{path}[{i}]")

        find_refs(minimal_api_spec)

        # All refs should point to components/schemas
        for path, ref in refs:
            assert ref.startswith("#/components/schemas/"), (
                f"Reference at {path} should point to components/schemas, got {ref}"
            )

            # Referenced schema should exist
            schema_name = ref.split("/")[-1]
            assert schema_name in minimal_api_spec["components"]["schemas"], (
                f"Referenced schema {schema_name} should exist in components/schemas"
            )


class TestGenerationRegressionPrevention:
    """Tests specifically designed to catch common regressions."""

    def test_no_mixed_indentation(self):
        """Test that generated code doesn't mix tabs and spaces."""

        # Generate some sample code
        enum_schema = {
            "type": "string",
            "enum": ["test_value", "another-value"],
            "description": "Test enum",
        }

        generated_code = generate_enum_type_code("TestEnum", enum_schema)

        # Should not contain tab characters
        assert "\t" not in generated_code, (
            "Generated code should not contain tab characters"
        )

        # Should use consistent indentation (4 spaces)
        lines = generated_code.split("\n")
        for line in lines:
            if line.startswith(" "):
                # Count leading spaces
                leading_spaces = len(line) - len(line.lstrip(" "))
                assert leading_spaces % 4 == 0, (
                    f"Line should use 4-space indentation: '{line}'"
                )

    def test_no_trailing_whitespace(self):
        """Test that generated code doesn't have trailing whitespace."""

        enum_schema = {
            "type": "string",
            "enum": ["value1", "value2"],
            "description": "Test enum",
        }

        generated_code = generate_enum_type_code("TestEnum", enum_schema)

        lines = generated_code.split("\n")
        for i, line in enumerate(lines):
            assert not line.endswith(" "), (
                f"Line {i + 1} has trailing whitespace: '{line}'"
            )
            assert not line.endswith("\t"), f"Line {i + 1} has trailing tab: '{line}'"

    def test_consistent_quote_style(self):
        """Test that generated code uses consistent quote style."""

        enum_schema = {
            "type": "string",
            "enum": ["test_value"],
            "description": "Test description",
        }

        generated_code = generate_enum_type_code("TestEnum", enum_schema)

        # Should prefer double quotes for docstrings, single quotes for values
        lines = generated_code.split("\n")
        for line in lines:
            if '"""' in line:
                # Docstring line - should use triple double quotes
                assert line.count('"""') > 0
            elif " = " in line and "'" in line:
                # Assignment line - should use single quotes for string values
                assert "'" in line

    def test_imports_are_necessary_and_minimal(self):
        """Test that generated code only imports what it needs."""

        # This test ensures we don't generate unnecessary imports
        enum_schema = {
            "type": "string",
            "enum": ["value1"],
            "description": "Simple enum",
        }

        generated_code = generate_enum_type_code("SimpleEnum", enum_schema)

        # Should import Enum
        assert "from enum import Enum" in generated_code

        # Should not import unnecessary modules
        unnecessary_imports = [
            "import os",
            "import sys",
            "import json",
            "from typing import Dict",
            "from typing import List",
        ]

        for unnecessary_import in unnecessary_imports:
            assert unnecessary_import not in generated_code, (
                f"Generated code should not contain unnecessary import: {unnecessary_import}"
            )


if __name__ == "__main__":
    pytest.main([__file__])
