import datetime
import json
from typing import Any, Dict

from kittycad.models.api_call_with_price import ApiCallWithPrice
from kittycad.models.method import Method
from kittycad.models.uuid import Uuid


def test_optional_datetime_omitted_vs_null():
    """Test that optional datetime fields can be omitted from JSON or set to null."""

    # Base data for ApiCallWithPrice without completed_at (testing optional field)
    base_data: Dict[str, Any] = {
        "created_at": "2023-08-18T10:00:00Z",
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "method": "GET",
        "token": "550e8400-e29b-41d4-a716-446655440002",
        "updated_at": "2023-08-18T10:05:00Z",
        "user_agent": "test-agent",
        "user_id": "550e8400-e29b-41d4-a716-446655440001",
    }

    # Test 1: Field completely omitted from JSON
    json_omitted = json.dumps(base_data)
    call_omitted = ApiCallWithPrice.model_validate_json(json_omitted)
    assert call_omitted.completed_at is None

    # Test 2: Field explicitly set to null in JSON
    data_with_null = base_data.copy()
    data_with_null["completed_at"] = None
    json_with_null = json.dumps(data_with_null)
    call_with_null = ApiCallWithPrice.model_validate_json(json_with_null)
    assert call_with_null.completed_at is None

    # Test 3: Field set to valid datetime
    data_with_datetime = base_data.copy()
    data_with_datetime["completed_at"] = "2023-08-18T10:05:00Z"
    json_with_datetime = json.dumps(data_with_datetime)
    call_with_datetime = ApiCallWithPrice.model_validate_json(json_with_datetime)
    assert call_with_datetime.completed_at is not None
    assert isinstance(call_with_datetime.completed_at, datetime.datetime)

    # Verify all three instances are otherwise identical
    assert call_omitted.id == call_with_null.id == call_with_datetime.id


def test_optional_datetime_serialization():
    """Test that optional datetime fields serialize correctly when None."""

    # Create instance with None completed_at
    call = ApiCallWithPrice(
        created_at=datetime.datetime(
            2023, 8, 18, 10, 0, 0, tzinfo=datetime.timezone.utc
        ),
        id=Uuid("550e8400-e29b-41d4-a716-446655440000"),
        updated_at=datetime.datetime(
            2023, 8, 18, 10, 5, 0, tzinfo=datetime.timezone.utc
        ),
        token=Uuid("750e8400-e29b-41d4-a716-446655440000"),
        method=Method.GET,
        user_id=Uuid("550e8400-e29b-41d4-a716-446655440001"),
        user_agent="Firefox",
        completed_at=None,
    )

    # Serialize to JSON and verify completed_at is null
    json_str = call.model_dump_json()
    data = json.loads(json_str)
    assert "completed_at" in data
    assert data["completed_at"] is None

    # Verify round-trip parsing works
    call_roundtrip = ApiCallWithPrice.model_validate_json(json_str)
    assert call_roundtrip.completed_at is None
    assert call_roundtrip.id == call.id
