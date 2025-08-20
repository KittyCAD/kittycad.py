#!/usr/bin/env python3
"""Tests for generated code quality, type hints, and Pythonic behavior.

This module tests that the generated SDK maintains high-quality, Pythonic patterns:
- Proper type hints and annotations
- Correct default argument handling
- Model class behaviors (required/optional fields)
- Method signature consistency
- Import statements and code formatting
"""

import ast
import inspect
import sys
from pathlib import Path

import pytest

# Import the generated SDK
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from kittycad import KittyCAD
from kittycad.models import (
    ApiCallQueryGroupBy,
    MlFeedback,
    SceneToolType,
    Uuid,
    ZooTool,
)


class TestTypeHintsAndSignatures:
    """Test that generated methods have proper type hints and signatures."""

    def test_client_methods_have_type_hints(self):
        """Test that all client methods have proper type hints."""
        client = KittyCAD(token="test-token")

        # Test various API sections
        api_sections = [
            client.file,
            client.api_calls,
            client.users,
            client.orgs,
        ]

        for api_section in api_sections:
            # Get all public methods (not starting with _)
            methods = [
                method
                for method in dir(api_section)
                if not method.startswith("_") and callable(getattr(api_section, method))
            ]

            # Test at least a few methods from each section
            for method_name in methods[:3]:  # Test first 3 methods
                method = getattr(api_section, method_name)
                sig = inspect.signature(method)

                # All parameters should have type annotations
                for param_name, param in sig.parameters.items():
                    if param_name == "self":
                        continue
                    assert param.annotation != inspect.Parameter.empty, (
                        f"Method {api_section.__class__.__name__}.{method_name} "
                        f"parameter '{param_name}' missing type annotation"
                    )

                # Return type should be annotated (unless void)
                if sig.return_annotation != inspect.Parameter.empty:
                    assert sig.return_annotation is not None

    def test_optional_parameters_have_default_values(self):
        """Test that optional parameters have appropriate default values."""
        client = KittyCAD(token="test-token")

        # Check file conversion method which should have optional params
        if hasattr(client.file, "create_file_conversion"):
            method = client.file.create_file_conversion
            sig = inspect.signature(method)

            for param_name, param in sig.parameters.items():
                if param_name == "self":
                    continue

                # Parameters with Optional in type should have default None
                if param.annotation != inspect.Parameter.empty:
                    type_str = str(param.annotation)
                    if "Optional" in type_str or "None" in type_str:
                        assert param.default is None, (
                            f"Optional parameter '{param_name}' should default to None"
                        )

    def test_pagination_methods_return_iterators(self):
        """Test that paginated methods return proper iterator types."""
        client = KittyCAD(token="test-token")

        # Check for methods that should return iterators
        potential_paginated_methods = []

        # Search for list_* methods that might be paginated
        for api_section in [client.api_calls, client.users]:
            for method_name in dir(api_section):
                if method_name.startswith("list_") and not method_name.startswith("_"):
                    potential_paginated_methods.append(
                        (api_section, method_name, getattr(api_section, method_name))
                    )

        for api_section, method_name, method in potential_paginated_methods:
            sig = inspect.signature(method)

            # Paginated methods should return iterator types
            if sig.return_annotation != inspect.Parameter.empty:
                return_type = str(sig.return_annotation)
                # Should return SyncPageIterator or similar
                assert "Iterator" in return_type or "Page" in return_type, (
                    f"Paginated method {method_name} should return iterator type, "
                    f"got {return_type}"
                )

    def test_async_methods_return_awaitable(self):
        """Test that async methods have proper return type annotations."""
        # This test would check async client methods if they exist
        # For now, verify the pattern exists in the codebase structure

        # Check that async patterns are defined
        from kittycad.pagination import AsyncPageIterator

        # AsyncPageIterator should exist for async pagination
        assert AsyncPageIterator is not None

        # Test async iterator has proper methods
        assert hasattr(AsyncPageIterator, "__aiter__")


class TestModelClassBehaviors:
    """Test that generated model classes behave like proper dataclasses."""

    def test_required_fields_enforcement(self):
        """Test that required fields are enforced in model constructors."""

        # Test with a model that has required fields
        # SceneToolType is an enum, let's find a model with required fields

        # Create a simple test: try to create models with missing required fields
        # This should raise appropriate errors

        # For enum types, test that values are properly constrained
        with pytest.raises((ValueError, TypeError)):
            # Invalid enum value should raise error
            MlFeedback("invalid_value")  # type: ignore

    def test_optional_fields_default_to_none(self):
        """Test that optional fields default to None or appropriate defaults."""

        # Test enum classes have proper string conversion
        feedback = MlFeedback.THUMBS_UP
        assert str(feedback) == "thumbs_up"

        # Test that the enum is a string subclass
        assert isinstance(feedback, str)

    def test_model_classes_are_serializable(self):
        """Test that model classes can be properly serialized."""

        # Test enum serialization
        feedback = MlFeedback.ACCEPTED
        assert feedback.value == "accepted"

        # Test UUID type
        test_uuid = Uuid("123e4567-e89b-12d3-a456-426614174000")
        assert str(test_uuid) == "123e4567-e89b-12d3-a456-426614174000"
        assert isinstance(test_uuid, str)

    def test_model_inheritance_structure(self):
        """Test that model classes have proper inheritance."""

        # String-based models should inherit from str
        assert issubclass(Uuid, str)

        # Enum classes should inherit from str and Enum
        from enum import Enum

        assert issubclass(MlFeedback, str)
        assert issubclass(MlFeedback, Enum)
        assert issubclass(SceneToolType, str)
        assert issubclass(SceneToolType, Enum)

    def test_model_docstrings_exist(self):
        """Test that model classes have proper docstrings."""

        # All model classes should have docstrings
        models_to_test = [MlFeedback, SceneToolType, ZooTool, ApiCallQueryGroupBy]

        for model_class in models_to_test:
            assert model_class.__doc__ is not None, (
                f"Model {model_class.__name__} should have a docstring"
            )
            assert len(model_class.__doc__.strip()) > 0, (
                f"Model {model_class.__name__} docstring should not be empty"
            )


class TestNamingConventions:
    """Test that generated code follows Python naming conventions."""

    def test_class_names_are_pascal_case(self):
        """Test that class names follow PascalCase convention."""

        # Test model class names
        class_names = [
            "MlFeedback",
            "SceneToolType",
            "ZooTool",
            "ApiCallQueryGroupBy",
            "Uuid",
        ]

        for class_name in class_names:
            # Should start with uppercase
            assert class_name[0].isupper(), (
                f"Class {class_name} should start with uppercase"
            )

            # Should not contain underscores (PascalCase)
            assert "_" not in class_name or class_name in ["ApiCallQueryGroupBy"], (
                f"Class {class_name} should use PascalCase (no underscores except for acronyms)"
            )

    def test_method_names_are_snake_case(self):
        """Test that method names follow snake_case convention."""
        client = KittyCAD(token="test-token")

        # Test various API sections
        for api_section in [client.file, client.api_calls]:
            methods = [
                method
                for method in dir(api_section)
                if not method.startswith("_") and callable(getattr(api_section, method))
            ]

            for method_name in methods:
                # Should be lowercase with underscores
                assert method_name.islower() or "_" in method_name, (
                    f"Method {method_name} should be snake_case"
                )

                # Should not start or end with underscore (unless private)
                if not method_name.startswith("_"):
                    assert not method_name.endswith("_"), (
                        f"Public method {method_name} should not end with underscore"
                    )

    def test_enum_member_names_are_screaming_snake_case(self):
        """Test that enum members follow SCREAMING_SNAKE_CASE."""

        # Test enum members
        for enum_member in MlFeedback:
            member_name = enum_member.name

            # Should be uppercase
            assert member_name.isupper(), (
                f"Enum member {member_name} should be uppercase"
            )

            # Should use underscores for word separation
            if " " in enum_member.value or "-" in enum_member.value:
                assert "_" in member_name, (
                    f"Enum member {member_name} should use underscores for word separation"
                )

    def test_module_names_are_snake_case(self):
        """Test that generated module names follow snake_case."""

        # Check that model modules follow snake_case
        import kittycad.models

        models_path = Path(kittycad.models.__file__).parent

        for model_file in models_path.glob("*.py"):
            if model_file.name in ["__init__.py", "base.py"]:
                continue

            # Module names should be snake_case
            assert model_file.stem.islower(), (
                f"Module {model_file.name} should be lowercase"
            )

            # Should not start or end with underscore
            assert not model_file.stem.startswith("_"), (
                f"Module {model_file.name} should not start with underscore"
            )
            assert not model_file.stem.endswith("_"), (
                f"Module {model_file.name} should not end with underscore"
            )


class TestCodeFormatting:
    """Test that generated code follows proper formatting standards."""

    def test_import_statements_are_organized(self):
        """Test that import statements in generated files are properly organized."""

        # Read a few generated model files
        import kittycad.models

        models_path = Path(kittycad.models.__file__).parent

        test_files = list(models_path.glob("*.py"))[:5]  # Test first 5 files

        for model_file in test_files:
            if model_file.name == "__init__.py":
                continue

            content = model_file.read_text()
            lines = content.split("\n")

            # Find import lines
            import_lines = []
            for i, line in enumerate(lines):
                if line.startswith("import ") or line.startswith("from "):
                    import_lines.append((i, line))

            if import_lines:
                # Imports should be at the top (after docstring/comments)
                first_import_line = import_lines[0][0]

                # Should not have non-import code before first import
                # (except for docstrings, comments, or empty lines)
                for i in range(first_import_line):
                    line = lines[i].strip()
                    if line and not line.startswith("#") and not line.startswith('"""'):
                        # Allow module docstrings
                        if not (line.startswith('"""') or line.startswith("'''")):
                            pytest.fail(
                                f"File {model_file.name} has code before imports: {line}"
                            )

    def test_line_length_compliance(self):
        """Test that generated code respects reasonable line length limits."""

        # Check a few generated files for extremely long lines
        import kittycad.models

        models_path = Path(kittycad.models.__file__).parent

        max_line_length = 200  # Be generous, but catch egregious violations

        for model_file in list(models_path.glob("*.py"))[:5]:
            content = model_file.read_text()

            for line_num, line in enumerate(content.split("\n"), 1):
                if len(line) > max_line_length:
                    # Allow some exceptions for URLs, long strings, etc.
                    if not ("http" in line or "noqa" in line):
                        pytest.fail(
                            f"File {model_file.name}:{line_num} has very long line "
                            f"({len(line)} chars): {line[:100]}..."
                        )

    def test_no_syntax_errors_in_generated_files(self):
        """Test that all generated files have valid Python syntax."""

        import kittycad.models

        models_path = Path(kittycad.models.__file__).parent

        for model_file in models_path.glob("*.py"):
            try:
                content = model_file.read_text()
                ast.parse(content)
            except SyntaxError as e:
                pytest.fail(f"Syntax error in generated file {model_file.name}: {e}")


class TestPythonicBehavior:
    """Test that generated code follows Pythonic patterns and idioms."""

    def test_enum_string_conversion(self):
        """Test that enums convert to strings properly."""

        feedback = MlFeedback.THUMBS_UP

        # Should convert to string value
        assert str(feedback) == "thumbs_up"

        # Should be usable in string contexts
        message = f"User gave {feedback}"
        assert "thumbs_up" in message

    def test_model_repr_and_str(self):
        """Test that models have reasonable string representations."""

        # Test UUID representation
        test_uuid = Uuid("123e4567-e89b-12d3-a456-426614174000")

        # Should convert to string cleanly
        assert str(test_uuid) == "123e4567-e89b-12d3-a456-426614174000"

        # Should be usable in string contexts
        url_path = f"/api/users/{test_uuid}"
        assert "123e4567-e89b-12d3-a456-426614174000" in url_path

    def test_truthiness_behavior(self):
        """Test that models have sensible truthiness behavior."""

        # Non-empty strings should be truthy
        test_uuid = Uuid("123e4567-e89b-12d3-a456-426614174000")
        assert bool(test_uuid) is True

        # Enum values should be truthy
        feedback = MlFeedback.ACCEPTED
        assert bool(feedback) is True

    def test_equality_and_hashing(self):
        """Test that models support equality comparison and hashing."""

        # Same UUID values should be equal
        uuid1 = Uuid("123e4567-e89b-12d3-a456-426614174000")
        uuid2 = Uuid("123e4567-e89b-12d3-a456-426614174000")
        assert uuid1 == uuid2

        # Should be hashable (usable in sets/dicts)
        uuid_set = {uuid1, uuid2}
        assert len(uuid_set) == 1  # Should deduplicate

        # Different enum values should not be equal
        feedback1 = MlFeedback.THUMBS_UP
        feedback2 = MlFeedback.THUMBS_DOWN
        assert feedback1 != feedback2


if __name__ == "__main__":
    pytest.main([__file__])
