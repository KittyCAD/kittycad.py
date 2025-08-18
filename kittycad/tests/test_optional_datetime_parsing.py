import datetime
import json

from kittycad.models.api_call_status import ApiCallStatus
from kittycad.models.async_api_call import AsyncApiCall
from kittycad.models.async_api_call_type import AsyncApiCallType
from kittycad.models.uuid import Uuid


def test_optional_datetime_omitted_vs_null():
    """Test that optional datetime fields can be omitted from JSON or set to null."""

    # Base data for AsyncApiCall without completed_at
    base_data = {
        "attempts": 1,
        "created_at": "2023-08-18T10:00:00Z",
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "status": "completed",
        "type": "file_conversion",
        "updated_at": "2023-08-18T10:05:00Z",
        "user_id": "550e8400-e29b-41d4-a716-446655440001",
    }

    # Test 1: Field completely omitted from JSON
    json_omitted = json.dumps(base_data)
    call_omitted = AsyncApiCall.model_validate_json(json_omitted)
    assert call_omitted.completed_at is None

    # Test 2: Field explicitly set to null in JSON
    data_with_null = base_data.copy()
    data_with_null["completed_at"] = None
    json_with_null = json.dumps(data_with_null)
    call_with_null = AsyncApiCall.model_validate_json(json_with_null)
    assert call_with_null.completed_at is None

    # Test 3: Field set to valid datetime
    data_with_datetime = base_data.copy()
    data_with_datetime["completed_at"] = "2023-08-18T10:05:00Z"
    json_with_datetime = json.dumps(data_with_datetime)
    call_with_datetime = AsyncApiCall.model_validate_json(json_with_datetime)
    assert call_with_datetime.completed_at is not None
    assert isinstance(call_with_datetime.completed_at, datetime.datetime)

    # Verify all three instances are otherwise identical
    assert call_omitted.id == call_with_null.id == call_with_datetime.id
    assert call_omitted.status == call_with_null.status == call_with_datetime.status


def test_optional_datetime_serialization():
    """Test that optional datetime fields serialize correctly when None."""

    # Create instance with None completed_at
    call = AsyncApiCall(
        attempts=1,
        created_at=datetime.datetime(
            2023, 8, 18, 10, 0, 0, tzinfo=datetime.timezone.utc
        ),
        id=Uuid("550e8400-e29b-41d4-a716-446655440000"),
        status=ApiCallStatus.COMPLETED,
        type=AsyncApiCallType.FILE_CONVERSION,
        updated_at=datetime.datetime(
            2023, 8, 18, 10, 5, 0, tzinfo=datetime.timezone.utc
        ),
        user_id=Uuid("550e8400-e29b-41d4-a716-446655440001"),
        completed_at=None,
    )

    # Serialize to JSON and verify completed_at is null
    json_str = call.model_dump_json()
    data = json.loads(json_str)
    assert "completed_at" in data
    assert data["completed_at"] is None

    # Verify round-trip parsing works
    call_roundtrip = AsyncApiCall.model_validate_json(json_str)
    assert call_roundtrip.completed_at is None
    assert call_roundtrip.id == call.id
