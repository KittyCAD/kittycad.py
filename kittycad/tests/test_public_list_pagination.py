"""Exercise regenerated list methods through their real HTTP and model paths."""

from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime, timezone

import httpx
import pytest

from kittycad import AsyncKittyCAD, KittyCAD
from kittycad.models import (
    BillingInfo,
    FactoryCustomerCatalogOption,
    KclProjectShareLinkAccessMode,
    OrgSkillResponse,
    PaymentMethod,
    PaymentMethodType,
    ProjectShareLinkResponse,
    PublicProjectOwnerResponse,
    PublicProjectResponse,
    Uuid,
)
from kittycad.models.base import KittyCadBaseModel
from kittycad.pagination import AsyncPageIterator, SyncPageIterator

PROJECT_ID = Uuid("00000000-0000-4000-8000-000000000001")
CREATED_AT = datetime(2026, 1, 1, tzinfo=timezone.utc)
PAYMENT_METHOD = PaymentMethod(
    billing_info=BillingInfo(), created_at=CREATED_AT, type=PaymentMethodType.CARD
)
CATALOG_OPTION = FactoryCustomerCatalogOption(name="Standard")


@dataclass(frozen=True)
class ListEndpoint:
    path: str
    item: KittyCadBaseModel
    sync_call: Callable[[KittyCAD], SyncPageIterator]
    async_call: Callable[[AsyncKittyCAD], AsyncPageIterator]


ENDPOINTS = [
    ListEndpoint(
        "/org/skills",
        OrgSkillResponse(
            id=PROJECT_ID, name="Example", description="Example skill", markdown="Skill"
        ),
        lambda client: client.orgs.list_org_skills(limit=1),
        lambda client: client.orgs.list_org_skills(limit=1),
    ),
    ListEndpoint(
        "/org/payment/methods",
        PAYMENT_METHOD,
        lambda client: client.payments.list_payment_methods_for_org(limit=1),
        lambda client: client.payments.list_payment_methods_for_org(limit=1),
    ),
    ListEndpoint(
        "/user/payment/methods",
        PAYMENT_METHOD,
        lambda client: client.payments.list_payment_methods_for_user(limit=1),
        lambda client: client.payments.list_payment_methods_for_user(limit=1),
    ),
    ListEndpoint(
        "/projects/public",
        PublicProjectResponse(
            id=PROJECT_ID,
            title="Example",
            description="Example project",
            categories=[],
            like_count=0,
            owner=PublicProjectOwnerResponse(username="example"),
            published_at=CREATED_AT,
        ),
        lambda client: client.projects.list_public_projects(limit=1),
        lambda client: client.projects.list_public_projects(limit=1),
    ),
    ListEndpoint(
        f"/user/projects/{PROJECT_ID}/share-links",
        ProjectShareLinkResponse(
            access_mode=KclProjectShareLinkAccessMode.ANYONE_WITH_LINK,
            created_at=CREATED_AT,
            updated_at=CREATED_AT,
            key="example",
            url="https://example.com/share/example",
        ),
        lambda client: client.projects.list_project_share_links(PROJECT_ID, limit=1),
        lambda client: client.projects.list_project_share_links(PROJECT_ID, limit=1),
    ),
    ListEndpoint(
        "/user/factory/materials",
        CATALOG_OPTION,
        lambda client: client.factory.get_user_factory_materials(limit=1),
        lambda client: client.factory.get_user_factory_materials(limit=1),
    ),
    ListEndpoint(
        "/user/factory/finishes",
        CATALOG_OPTION,
        lambda client: client.factory.get_user_factory_finishes(limit=1),
        lambda client: client.factory.get_user_factory_finishes(limit=1),
    ),
]


def page_transport(
    endpoint: ListEndpoint, requests: list[httpx.Request]
) -> httpx.MockTransport:
    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        assert len(requests) <= 2
        assert request.method == "GET"
        assert request.url.path == endpoint.path
        assert request.headers["Authorization"] == "Bearer test-token"
        assert request.url.params == httpx.QueryParams(
            {"limit": "1"}
            if len(requests) == 1
            else {"limit": "1", "page_token": "next-page"}
        )
        return httpx.Response(
            200,
            json={
                "items": [endpoint.item.model_dump(mode="json")],
                "next_page": "next-page" if len(requests) == 1 else None,
            },
        )

    return httpx.MockTransport(handle)


@pytest.mark.parametrize("endpoint", ENDPOINTS, ids=lambda endpoint: endpoint.path)
def test_sync_public_list_fetches_all_pages(endpoint: ListEndpoint) -> None:
    requests: list[httpx.Request] = []
    with httpx.Client(transport=page_transport(endpoint, requests)) as http_client:
        client = KittyCAD(
            token="test-token", base_url="https://example.com", http_client=http_client
        )
        assert list(endpoint.sync_call(client)) == [endpoint.item, endpoint.item]
    assert len(requests) == 2


@pytest.mark.asyncio
@pytest.mark.parametrize("endpoint", ENDPOINTS, ids=lambda endpoint: endpoint.path)
async def test_async_public_list_fetches_all_pages(endpoint: ListEndpoint) -> None:
    requests: list[httpx.Request] = []
    async with httpx.AsyncClient(
        transport=page_transport(endpoint, requests)
    ) as http_client:
        client = AsyncKittyCAD(
            token="test-token", base_url="https://example.com", http_client=http_client
        )
        item: KittyCadBaseModel
        items: list[KittyCadBaseModel] = []
        async for item in endpoint.async_call(client):
            items.append(item)
        assert items == [endpoint.item, endpoint.item]
    assert len(requests) == 2
