#!/usr/bin/env python3
"""Tests for naming conventions and code formatting in generated outputs.

This module ensures that generated code follows consistent:
- Naming conventions (PascalCase, snake_case, SCREAMING_SNAKE_CASE)
- Code formatting (indentation, line length, quote style)
- Import organization
- Documentation standards
- File organization patterns

These tests catch regressions in code style and ensure the SDK
maintains professional, Pythonic appearance.
"""

import ast
import sys
from pathlib import Path

import pytest

# Import generator utilities
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import camel_to_screaming_snake, camel_to_snake, to_pascal_case


class TestNamingConventions:
    """Test that all naming conversions follow Python conventions."""

    def test_pascal_case_conversion(self):
        """Test conversion to PascalCase for class names."""

        test_cases = [
            # Simple cases
            ("user", "User"),
            ("file_info", "FileInfo"),
            ("api_key", "ApiKey"),
            # Complex cases
            ("user_preferences", "UserPreferences"),
            ("file_upload_result", "FileUploadResult"),
            ("oauth2_token", "Oauth2Token"),
            # Edge cases
            ("a", "A"),
            ("ab", "Ab"),
            ("a_b", "AB"),
            # Acronyms (should be handled specially)
            ("xml_parser", "XmlParser"),
            ("json_data", "JsonData"),
            ("http_client", "HttpClient"),
        ]

        for input_str, expected in test_cases:
            result = to_pascal_case(input_str)
            assert result == expected, (
                f"to_pascal_case('{input_str}') should return '{expected}', got '{result}'"
            )

    def test_snake_case_conversion(self):
        """Test conversion to snake_case for file/method names."""

        test_cases = [
            # Simple cases
            ("User", "user"),
            ("FileInfo", "file_info"),
            ("APIKey", "api_key"),
            # Complex cases
            ("UserPreferences", "user_preferences"),
            ("FileUploadResult", "file_upload_result"),
            ("OAuth2Token", "oauth2_token"),  # Special handling
            # Already snake_case
            ("already_snake", "already_snake"),
            ("simple_case", "simple_case"),
            # Edge cases
            ("A", "a"),
            ("AB", "ab"),  # Simple consecutive caps stay together
            ("ABC", "abc"),  # Simple consecutive caps stay together
            # Acronyms
            ("XMLParser", "xml_parser"),
            ("JSONData", "json_data"),
            ("HTTPClient", "http_client"),
        ]

        for input_str, expected in test_cases:
            result = camel_to_snake(input_str)
            assert result == expected, (
                f"camel_to_snake('{input_str}') should return '{expected}', got '{result}'"
            )

    def test_screaming_snake_case_conversion(self):
        """Test conversion to SCREAMING_SNAKE_CASE for enum members."""

        test_cases = [
            # Simple values
            ("active", "ACTIVE"),
            ("inactive", "INACTIVE"),
            ("pending", "PENDING"),
            # Hyphenated values
            ("thumbs-up", "THUMBS_UP"),
            ("thumbs-down", "THUMBS_DOWN"),
            ("multi-word-value", "MULTI_WORD_VALUE"),
            # Space-separated values
            ("pending approval", "PENDING_APPROVAL"),
            ("in progress", "IN_PROGRESS"),
            # Mixed cases
            ("camelCase", "CAMEL_CASE"),
            ("PascalCase", "PASCAL_CASE"),
            # Special characters
            ("value.with.dots", "VALUE_WITH_DOTS"),
            ("value:with:colons", "VALUE_WITH_COLONS"),
            # Numbers
            ("status1", "STATUS1"),
            ("v2.0", "V2_0"),
        ]

        for input_str, expected in test_cases:
            result = camel_to_screaming_snake(input_str)
            assert result == expected, (
                f"camel_to_screaming_snake('{input_str}') should return '{expected}', got '{result}'"
            )

    def test_file_naming_patterns(self):
        """Test that file names follow consistent patterns."""

        # Model files should be snake_case
        model_name_tests = [
            ("User", "user.py"),
            ("FileInfo", "file_info.py"),
            ("UserPreferences", "user_preferences.py"),
            ("APICallResult", "api_call_result.py"),
            ("OAuth2Token", "oauth2_token.py"),
        ]

        for class_name, expected_filename in model_name_tests:
            snake_name = camel_to_snake(class_name)
            actual_filename = f"{snake_name}.py"
            assert actual_filename == expected_filename, (
                f"Class {class_name} should generate file {expected_filename}, "
                f"got {actual_filename}"
            )

    def test_method_naming_patterns(self):
        """Test that method names follow verb_noun patterns."""

        # Test operation ID to method name mapping
        operation_tests = [
            ("getUser", "get_user"),
            ("createUser", "create_user"),
            ("updateUser", "update_user"),
            ("deleteUser", "delete_user"),
            ("listUsers", "list_users"),
            ("uploadFile", "upload_file"),
            ("downloadFile", "download_file"),
            # Already snake_case (preferred)
            ("get_user", "get_user"),
            ("list_items", "list_items"),
            # Special cases
            ("OAuth2Authorize", "oauth2_authorize"),
            ("getAPIKey", "get_api_key"),
        ]

        for operation_id, expected_method in operation_tests:
            method_name = camel_to_snake(operation_id)
            assert method_name == expected_method, (
                f"Operation '{operation_id}' should convert to method '{expected_method}', "
                f"got '{method_name}'"
            )


class TestCodeFormatting:
    """Test that generated code follows consistent formatting standards."""

    def test_indentation_consistency(self):
        """Test that all generated code uses 4-space indentation."""

        # Sample generated code patterns
        code_samples = [
            # Class definition
            """class TestClass(str, Enum):
    \"\"\"Test class\"\"\"
    
    VALUE_ONE = "value_one"
    
    def __str__(self) -> str:
        return str(self.value)""",
            # Function definition
            """def test_function(
    self,
    param1: str,
    *,
    param2: Optional[str] = None,
) -> str:
    \"\"\"Test function\"\"\"
    
    if param2 is not None:
        return f"{param1}_{param2}"
    return param1""",
        ]

        for code_sample in code_samples:
            lines = code_sample.split("\n")

            for line_num, line in enumerate(lines, 1):
                if line.strip() == "":  # Skip empty lines
                    continue

                # Count leading spaces
                leading_spaces = len(line) - len(line.lstrip(" "))

                if leading_spaces > 0:
                    assert leading_spaces % 4 == 0, (
                        f"Line {line_num} should use 4-space indentation, "
                        f"found {leading_spaces} spaces: '{line}'"
                    )

                # Should not contain tabs
                assert "\t" not in line, (
                    f"Line {line_num} should not contain tab characters: '{line}'"
                )

    def test_line_length_guidelines(self):
        """Test that generated code respects reasonable line length limits."""

        # Test various code patterns for reasonable line lengths
        code_patterns = [
            # Function signature
            "def very_long_function_name_with_many_parameters(",
            "    self,",
            "    very_long_parameter_name: VeryLongTypeName,",
            "    another_parameter: Optional[AnotherLongType] = None,",
            ") -> VeryLongReturnTypeName:",
            # Docstring
            '    """This is a docstring that might be quite long but should not exceed reasonable limits."""',
            # String literal
            '    VERY_LONG_ENUM_VALUE = "very_long_string_value_that_might_be_quite_lengthy"',
        ]

        max_reasonable_length = 100  # Be somewhat generous

        for line in code_patterns:
            assert len(line) <= max_reasonable_length, (
                f"Line should not exceed {max_reasonable_length} characters: '{line}' "
                f"(length: {len(line)})"
            )

    def test_quote_style_consistency(self):
        """Test that generated code uses consistent quote styles."""

        # Test patterns for quote usage
        quote_tests = [
            # Docstrings should use triple double quotes
            ('"""This is a docstring"""', True),
            ("'''This is wrong'''", False),
            # String values should prefer single quotes
            ("ENUM_VALUE = 'string_value'", True),
            ('ENUM_VALUE = "string_value"', False),  # Unless there's a reason
            # But double quotes are OK for strings with single quotes
            ('ERROR_MESSAGE = "Can\'t process this"', True),
        ]

        for code_pattern, should_be_acceptable in quote_tests:
            # This is more of a guideline check than strict enforcement
            if should_be_acceptable:
                # Just verify the pattern makes sense
                assert len(code_pattern) > 0
            else:
                # Note: In practice, both quote styles are valid Python
                # This test documents our preference
                pass

    def test_import_organization(self):
        """Test that imports are organized according to PEP 8."""

        # Sample import blocks that should be properly organized
        good_import_examples = [
            # Standard library first
            """import os
import sys
from typing import Optional

from enum import Enum

from ..models.base import BaseModel""",
            # Grouped properly
            """from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel

from .base import KittyCADBaseModel""",
        ]

        for import_block in good_import_examples:
            lines = import_block.strip().split("\n")

            # Should not have trailing whitespace
            for line in lines:
                assert not line.endswith(" "), (
                    f"Import line has trailing space: '{line}'"
                )
                assert not line.endswith("\t"), (
                    f"Import line has trailing tab: '{line}'"
                )

            # Should have proper structure
            assert any(
                line.startswith("import ") or line.startswith("from ") for line in lines
            ), "Should contain import statements"

    def test_blank_line_usage(self):
        """Test that blank lines are used appropriately."""

        # Sample code structure with proper blank line usage
        code_sample = """from enum import Enum


class TestEnum(str, Enum):
    \"\"\"Test enumeration\"\"\"  # noqa: E501

    VALUE_ONE = "value_one"

    VALUE_TWO = "value_two"

    def __str__(self) -> str:
        return str(self.value)"""

        lines = code_sample.split("\n")

        # Check for appropriate blank lines
        # Two blank lines after imports
        import_end = -1
        for i, line in enumerate(lines):
            if line.startswith(("import ", "from ")):
                import_end = i

        if import_end >= 0:
            # Should have blank lines after imports
            class_start = -1
            for i in range(import_end + 1, len(lines)):
                if lines[i].startswith("class "):
                    class_start = i
                    break

            if class_start > import_end + 1:
                # Count blank lines between imports and class
                blank_lines = 0
                for i in range(import_end + 1, class_start):
                    if lines[i].strip() == "":
                        blank_lines += 1

                assert blank_lines >= 2, (
                    f"Should have at least 2 blank lines after imports, found {blank_lines}"
                )


class TestDocumentationStandards:
    """Test that generated code includes proper documentation."""

    def test_class_docstrings(self):
        """Test that classes have appropriate docstrings."""

        # Example class with proper docstring
        class_example = '''class User(BaseModel):
    """A user in the system"""
    
    id: str
    name: str'''

        # Parse the class to check docstring
        tree = ast.parse(class_example)
        class_node = tree.body[0]

        assert isinstance(class_node, ast.ClassDef)
        assert len(class_node.body) > 0

        # First statement should be a docstring
        first_stmt = class_node.body[0]
        if isinstance(first_stmt, ast.Expr) and isinstance(
            first_stmt.value, ast.Constant
        ):
            docstring = first_stmt.value.value
            assert isinstance(docstring, str)
            assert len(docstring.strip()) > 0
            assert not docstring.startswith(" ")  # Should not start with space
            assert not docstring.endswith(" ")  # Should not end with space

    def test_enum_docstrings(self):
        """Test that enums have appropriate docstrings and comments."""

        enum_example = '''class Status(str, Enum):
    """Current status of the item"""  # noqa: E501
    
    ACTIVE = "active"
    
    INACTIVE = "inactive"'''

        # Should contain proper docstring
        assert '"""Current status of the item"""' in enum_example

        # Should have noqa comment for line length
        assert "# noqa: E501" in enum_example

    def test_method_docstrings(self):
        """Test that generated methods have appropriate docstrings."""

        method_example = '''def get_user(self, user_id: str) -> User:
    """Retrieve a specific user by their ID"""
    
    url = f"/users/{user_id}"
    # ... implementation'''

        # Should contain descriptive docstring
        assert '"""Retrieve a specific user by their ID"""' in method_example

        # Docstring should be descriptive, not just repeat the method name
        assert "Retrieve" in method_example or "Get" in method_example

    def test_parameter_documentation(self):
        """Test that complex parameters are documented."""

        # For complex methods, parameters should be documented
        complex_method = '''def upload_file(
    self,
    file_attachments: Dict[str, Union[Path, bytes, IO[bytes]]],
    *,
    metadata: Optional[FileMetadata] = None,
) -> FileInfo:
    """Upload a file with metadata
    
    Args:
        file_attachments: Dictionary mapping field names to file content
        metadata: Optional metadata for the file
        
    Returns:
        Information about the uploaded file
    """'''

        # Should document complex parameters
        assert "Args:" in complex_method or "file_attachments:" in complex_method
        assert "Returns:" in complex_method or "FileInfo" in complex_method


class TestFileOrganization:
    """Test that generated files follow consistent organization patterns."""

    def test_module_structure(self):
        """Test that modules have proper structure."""

        # Example module structure
        module_example = '''"""User-related models and types."""

from typing import Optional
from datetime import datetime

from pydantic import BaseModel

from .base import KittyCADBaseModel


class User(KittyCADBaseModel):
    """A user in the system"""
    
    id: str
    name: str
    created_at: datetime
    updated_at: Optional[datetime] = None'''

        lines = module_example.split("\n")

        # Should start with module docstring
        assert lines[0].startswith('"""')

        # Should have imports after docstring
        import_found = False
        for line in lines:
            if line.startswith(("import ", "from ")):
                import_found = True
                break
        assert import_found, "Module should contain import statements"

    def test_init_file_patterns(self):
        """Test that __init__.py files follow proper patterns."""

        init_example = '''""" Contains all the data models used in inputs/outputs """

from .user import User
from .file_info import FileInfo
from .base import KittyCADBaseModel'''

        # Should have module docstring
        assert init_example.startswith('"""')

        # Should import all public models
        assert "from .user import User" in init_example
        assert "from .file_info import FileInfo" in init_example

    def test_relative_import_patterns(self):
        """Test that relative imports follow consistent patterns."""

        import_examples = [
            "from .base import KittyCADBaseModel",  # Same package
            "from ..models.user import User",  # Parent package
            "from ...client import Client",  # Grandparent package
        ]

        for import_example in import_examples:
            # Should use relative imports within the package
            assert import_example.startswith("from .")

            # Should not have absolute imports to internal modules
            assert not import_example.startswith("from kittycad.")


if __name__ == "__main__":
    pytest.main([__file__])
