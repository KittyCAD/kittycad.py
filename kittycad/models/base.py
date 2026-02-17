"""Base model classes for KittyCAD SDK."""

from typing import Any, Dict

from pydantic import BaseModel, ConfigDict


class KittyCadBaseModel(BaseModel):
    """Base model for all KittyCAD API models.

    Provides common configuration and methods for all models in the SDK.
    """

    model_config = ConfigDict(
        protected_namespaces=(),
        # Enable alias usage for API field mapping
        populate_by_name=True,
        # Forbid extra fields for stricter validation
        extra="forbid",
        # Use enum values in serialization
        use_enum_values=True,
    )

    def __repr__(self) -> str:
        """User-friendly string representation."""
        # Show class name and key fields (up to 3)
        fields = []
        field_count = 0

        for field_name, field_value in self.__dict__.items():
            if field_count >= 3:
                break
            if not field_name.startswith("_") and field_value is not None:
                if isinstance(field_value, str) and len(field_value) > 50:
                    # Truncate long strings
                    field_value = field_value[:47] + "..."
                fields.append(f"{field_name}={field_value!r}")
                field_count += 1

        fields_str = ", ".join(fields)
        if len(self.__dict__) > 3:
            fields_str += "..."

        return f"{self.__class__.__name__}({fields_str})"

    def to_dict(self) -> Dict[str, Any]:
        """Convert model to dictionary with alias support.

        Returns:
            Dictionary representation of the model.
        """
        return self.model_dump(by_alias=True, exclude_none=True)

    def to_json(self) -> str:
        """Convert model to JSON string with alias support.

        Returns:
            JSON string representation of the model.
        """
        return self.model_dump_json(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "KittyCadBaseModel":
        """Create model instance from dictionary.

        Args:
            data: Dictionary containing model data.

        Returns:
            Model instance.

        Example:
            user_data = {"id": "123", "name": "John"}
            user = User.from_dict(user_data)
        """
        return cls.model_validate(data)

    @classmethod
    def from_json(cls, json_str: str) -> "KittyCadBaseModel":
        """Create model instance from JSON string.

        Args:
            json_str: JSON string containing model data.

        Returns:
            Model instance.

        Example:
            user_json = '{"id": "123", "name": "John"}'
            user = User.from_json(user_json)
        """
        return cls.model_validate_json(json_str)
