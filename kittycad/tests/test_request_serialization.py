"""Request serialization behavior."""

import json

from kittycad.models import (
    Axis,
    AxisDirectionPair,
    ConversionParams,
    Direction,
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
