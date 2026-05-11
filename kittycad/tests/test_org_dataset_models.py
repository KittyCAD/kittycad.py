"""Org dataset model behavior."""

import json

from kittycad.models.create_org_dataset import CreateOrgDataset
from kittycad.models.org_dataset_source import OrgDatasetSource
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
