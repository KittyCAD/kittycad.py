"""Request serialization behavior."""

import json
from email.parser import BytesParser
from email.policy import default
from typing import cast

import httpx

from kittycad import KittyCAD
from kittycad.models import (
    ApiCallStatus,
    Axis,
    AxisDirectionPair,
    ConversionParams,
    Direction,
    FileConversion,
    InputFormat3d,
    OutputFormat3d,
    System,
    UnitLength,
)
from kittycad.models.input_format3d import OptionStl
from kittycad.models.output_format3d import OptionObj as OutputOptionObj
from kittycad.models.update_org_dataset import UpdateOrgDataset
from kittycad.types import serialize_request_body


def test_request_serialization_omits_default_none_but_keeps_explicit_null():
    assert json.loads(serialize_request_body(UpdateOrgDataset())) == {}

    assert json.loads(serialize_request_body(UpdateOrgDataset(description=None))) == {
        "description": None
    }


def test_request_serialization_keeps_union_discriminator_defaults():
    body = _conversion_body()

    payload = json.loads(serialize_request_body(body))

    assert payload["src_format"]["type"] == "stl"
    assert payload["output_format"]["type"] == "obj"


def test_file_conversion_options_round_trips_real_request_and_response_types(tmp_path):
    input_file = tmp_path / "input.stl"
    input_file.write_bytes(b"solid test\nendsolid test\n")
    seen: dict[str, object] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["request"] = request
        seen["multipart"] = _multipart_fields(request)
        return httpx.Response(
            200,
            json=_file_conversion_response(),
            request=request,
        )

    http_client = httpx.Client(transport=httpx.MockTransport(handler))
    client = KittyCAD(
        token="test-token",
        base_url="https://api.example.test",
        http_client=http_client,
    )

    result = client.file.create_file_conversion_options(
        body=_conversion_body(),
        file_attachments={"input.stl": input_file},
    )

    request = cast(httpx.Request, seen["request"])
    assert request.url.path == "/file/conversion"

    multipart = cast(dict[str, bytes], seen["multipart"])
    payload = json.loads(multipart["body"].decode())

    assert payload["src_format"]["type"] == "stl"
    assert payload["output_format"]["type"] == "obj"
    assert b"solid test" in multipart["input.stl"]

    assert isinstance(result, FileConversion)
    assert result.status == ApiCallStatus.COMPLETED
    assert result.src_format_options is not None
    assert isinstance(result.src_format_options.root, OptionStl)
    assert result.output_format_options is not None
    assert isinstance(result.output_format_options.root, OutputOptionObj)


def _conversion_body() -> ConversionParams:
    coords = System(
        forward=AxisDirectionPair(
            axis=Axis.Y,
            direction=Direction.NEGATIVE,
        ),
        up=AxisDirectionPair(
            axis=Axis.Z,
            direction=Direction.POSITIVE,
        ),
    )
    body = ConversionParams(
        src_format=InputFormat3d(
            OptionStl(
                coords=coords,
                units=UnitLength.MM,
            )
        ),
        output_format=OutputFormat3d(
            OutputOptionObj(
                coords=coords,
                units=UnitLength.MM,
            )
        ),
    )
    return body


def _multipart_fields(request: httpx.Request) -> dict[str, bytes]:
    content_type = request.headers["content-type"]
    message = BytesParser(policy=default).parsebytes(
        b"Content-Type: "
        + content_type.encode()
        + b"\r\nMIME-Version: 1.0\r\n\r\n"
        + request.read()
    )

    fields: dict[str, bytes] = {}
    for part in message.iter_parts():
        name = part.get_param("name", header="content-disposition")
        payload = part.get_payload(decode=True)
        if isinstance(name, str) and isinstance(payload, bytes):
            fields[name] = payload
    return fields


def _file_conversion_response() -> dict[str, object]:
    return {
        "completed_at": "2026-05-11T00:00:01Z",
        "created_at": "2026-05-11T00:00:00Z",
        "error": None,
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "output_format": "obj",
        "output_format_options": {
            "coords": _coords_json(),
            "type": "obj",
            "units": "mm",
        },
        "outputs": None,
        "src_format": "stl",
        "src_format_options": {
            "coords": _coords_json(),
            "type": "stl",
            "units": "mm",
        },
        "started_at": "2026-05-11T00:00:00Z",
        "status": "completed",
        "updated_at": "2026-05-11T00:00:01Z",
        "user_id": "550e8400-e29b-41d4-a716-446655440001",
    }


def _coords_json() -> dict[str, dict[str, str]]:
    return {
        "forward": {"axis": "y", "direction": "negative"},
        "up": {"axis": "z", "direction": "positive"},
    }
