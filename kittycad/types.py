"""Contains some shared types for properties"""

import json
from typing import (
    Any,
    BinaryIO,
    Generic,
    MutableMapping,
    Optional,
    TextIO,
    Tuple,
    TypeVar,
    Union,
)

import attr
from pydantic import BaseModel, RootModel


class Unset:
    def __bool__(self) -> bool:
        return False


UNSET: Unset = Unset()

FileJsonType = Tuple[Optional[str], Union[BinaryIO, TextIO], Optional[str]]


@attr.s(auto_attribs=True)
class File:
    """Contains information for file uploads"""

    payload: Union[BinaryIO, TextIO]
    file_name: Optional[str] = None
    mime_type: Optional[str] = None

    def to_tuple(self) -> FileJsonType:
        """Return a tuple representation that httpx will accept for multipart/form-data"""  # noqa: E501
        return self.file_name, self.payload, self.mime_type


T = TypeVar("T")


@attr.s(auto_attribs=True)
class Response(Generic[T]):
    """A response from an endpoint"""  # noqa: E501

    status_code: int
    content: bytes
    headers: MutableMapping[str, str]
    parsed: T


def serialize_request_body(body: Any) -> str:
    """Serialize a request body without dropping explicit API semantics."""
    if isinstance(body, BaseModel):
        payload = body.model_dump(mode="json", by_alias=True, exclude_none=True)
        payload = _restore_explicit_nulls(body, payload)
        return json.dumps(payload, separators=(",", ":"))

    return json.dumps(body, separators=(",", ":"))


def _restore_explicit_nulls(value: Any, payload: Any) -> Any:
    if isinstance(value, RootModel):
        return _restore_explicit_nulls(value.root, payload)

    if isinstance(value, BaseModel) and isinstance(payload, dict):
        for field_name, field in type(value).model_fields.items():
            key = _serialized_field_name(field_name, field)
            field_value = getattr(value, field_name)

            if field_name in value.model_fields_set and field_value is None:
                payload[key] = None
            elif key in payload:
                payload[key] = _restore_explicit_nulls(field_value, payload[key])

        return payload

    if isinstance(value, (list, tuple)) and isinstance(payload, list):
        for index, item in enumerate(value):
            if index < len(payload):
                payload[index] = _restore_explicit_nulls(item, payload[index])
        return payload

    if isinstance(value, dict) and isinstance(payload, dict):
        for key, item in value.items():
            if key in payload:
                payload[key] = _restore_explicit_nulls(item, payload[key])
        return payload

    return payload


def _serialized_field_name(field_name: str, field: Any) -> str:
    key = field.serialization_alias or field.alias or field_name
    if isinstance(key, str):
        return key
    return field_name


__all__ = ["File", "Response", "FileJsonType", "serialize_request_body"]
