"""Org dataset model behavior."""

import json

import pytest
from pydantic import ValidationError

from kittycad.models.create_org_dataset import CreateOrgDataset
from kittycad.models.org_dataset import OrgDataset
from kittycad.models.org_dataset_source import OrgDatasetSource
from kittycad.models.org_dataset_status import OrgDatasetStatus
from kittycad.models.storage_provider import StorageProvider
from kittycad.models.update_org_dataset import UpdateOrgDataset


def test_create_org_dataset_description_can_be_omitted():
    body = CreateOrgDataset(
        name="training-data",
        source=OrgDatasetSource(provider=StorageProvider.ZOO_MANAGED),
    )

    assert body.description is None
    assert json.loads(body.model_dump_json(exclude_unset=True)) == {
        "name": "training-data",
        "source": {"provider": "zoo_managed"},
    }


def test_update_org_dataset_distinguishes_omitted_description_from_null():
    assert json.loads(UpdateOrgDataset().model_dump_json(exclude_unset=True)) == {}

    clear_description = UpdateOrgDataset(description=None)

    assert json.loads(clear_description.model_dump_json(exclude_unset=True)) == {
        "description": None
    }


def test_response_validation_can_ignore_future_fields():
    server_json = {
        "access_role_arn": "zoo-managed",
        "created_at": "2026-05-11T00:00:00Z",
        "description": None,
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "name": "training-data",
        "org_id": "550e8400-e29b-41d4-a716-446655440001",
        "source_uri": "zoo://bucket/test/datasets/550e8400-e29b-41d4-a716-446655440000",
        "status": OrgDatasetStatus.ACTIVE,
        "storage_provider": StorageProvider.ZOO_MANAGED,
        "updated_at": "2026-05-11T00:00:00Z",
        "future_api_field": "do not explode",
    }

    with pytest.raises(ValidationError):
        OrgDataset.model_validate(server_json)

    model = OrgDataset.model_validate(server_json, extra="ignore")

    assert model.name == "training-data"
    assert not hasattr(model, "future_api_field")
