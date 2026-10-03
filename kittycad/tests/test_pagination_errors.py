"""Exercise pagination failures through the generated public HTTP clients."""

from collections.abc import AsyncIterator, Callable, Iterator

import httpx
import pytest

from kittycad import AsyncKittyCAD, KittyCAD
from kittycad.exceptions import KittyCADAPIError
from kittycad.models import OrgSkillResponse, Uuid

SKILL = OrgSkillResponse(
    id=Uuid("00000000-0000-4000-8000-000000000001"),
    name="Example",
    description="Example skill",
    markdown="Skill",
)


def page(next_page: str | None, *, empty: bool = False) -> httpx.Response:
    return httpx.Response(
        200,
        json={
            "items": [] if empty else [SKILL.model_dump(mode="json")],
            "next_page": next_page,
        },
    )


def response_transport(
    responses: list[httpx.Response], requests: list[httpx.Request]
) -> httpx.MockTransport:
    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        assert len(requests) <= len(responses), "Unexpected continuation request"
        assert request.url.path == "/org/skills"
        assert request.headers["Authorization"] == "Bearer test-token"
        return responses[len(requests) - 1]

    return httpx.MockTransport(handle)


INVALID_PAGES = [
    pytest.param(lambda: httpx.Response(200), id="empty-200"),
    pytest.param(lambda: httpx.Response(204), id="empty-204"),
    pytest.param(lambda: httpx.Response(200, text="null"), id="null-page"),
    pytest.param(lambda: httpx.Response(200, json=[]), id="legacy-array"),
    pytest.param(lambda: httpx.Response(200, json={"items": []}), id="missing-cursor"),
    pytest.param(
        lambda: httpx.Response(200, json={"next_page": None}), id="missing-items"
    ),
    pytest.param(
        lambda: httpx.Response(200, json={"items": None, "next_page": None}),
        id="null-items",
    ),
    pytest.param(
        lambda: httpx.Response(200, json={"items": [], "next_page": 1}),
        id="nonstring-cursor",
    ),
    pytest.param(lambda: page(""), id="empty-cursor"),
    pytest.param(lambda: page(" "), id="whitespace-cursor"),
    pytest.param(lambda: page("next-page"), id="repeated-cursor"),
]


@pytest.mark.parametrize("invalid_page", INVALID_PAGES)
def test_sync_invalid_page_raises_before_yielding_its_items(
    invalid_page: Callable[[], httpx.Response],
) -> None:
    requests: list[httpx.Request] = []
    with KittyCAD(
        token="test-token",
        base_url="https://example.test",
        http_client=httpx.Client(
            transport=response_transport([page("next-page"), invalid_page()], requests)
        ),
    ) as client:
        iterator: Iterator[OrgSkillResponse] = iter(
            client.orgs.list_org_skills(limit=1)
        )
        assert next(iterator) == SKILL
        with pytest.raises(ValueError):
            next(iterator)
    assert len(requests) == 2


@pytest.mark.asyncio
@pytest.mark.parametrize("invalid_page", INVALID_PAGES)
async def test_async_invalid_page_raises_before_yielding_its_items(
    invalid_page: Callable[[], httpx.Response],
) -> None:
    requests: list[httpx.Request] = []
    async with AsyncKittyCAD(
        token="test-token",
        base_url="https://example.test",
        http_client=httpx.AsyncClient(
            transport=response_transport([page("next-page"), invalid_page()], requests)
        ),
    ) as client:
        iterator: AsyncIterator[OrgSkillResponse] = aiter(
            client.orgs.list_org_skills(limit=1)
        )
        assert await anext(iterator) == SKILL
        with pytest.raises(ValueError):
            await anext(iterator)
    assert len(requests) == 2


@pytest.mark.parametrize("status", [401, 403, 404, 429, 500])
def test_sync_later_http_error_aborts_collection(status: int) -> None:
    requests: list[httpx.Request] = []
    with KittyCAD(
        token="test-token",
        base_url="https://example.test",
        http_client=httpx.Client(
            transport=response_transport(
                [page("next-page"), httpx.Response(status)], requests
            )
        ),
    ) as client:
        with pytest.raises(KittyCADAPIError):
            list(client.orgs.list_org_skills(limit=1))
    assert len(requests) == 2


@pytest.mark.asyncio
@pytest.mark.parametrize("status", [401, 403, 404, 429, 500])
async def test_async_later_http_error_aborts_collection(status: int) -> None:
    requests: list[httpx.Request] = []
    async with AsyncKittyCAD(
        token="test-token",
        base_url="https://example.test",
        http_client=httpx.AsyncClient(
            transport=response_transport(
                [page("next-page"), httpx.Response(status)], requests
            )
        ),
    ) as client:
        with pytest.raises(KittyCADAPIError):
            _ = [skill async for skill in client.orgs.list_org_skills(limit=1)]
    assert len(requests) == 2


def test_sync_empty_middle_page_initial_cursor_and_reuse() -> None:
    requests: list[httpx.Request] = []
    with KittyCAD(
        token="test-token",
        base_url="https://example.test",
        http_client=httpx.Client(
            transport=response_transport(
                [page("middle"), page("last", empty=True), page(None)] * 2, requests
            )
        ),
    ) as client:
        iterator = client.orgs.list_org_skills(limit=1, page_token="start")
        assert list(iterator) == [SKILL, SKILL]
        assert list(iterator) == [SKILL, SKILL]
    assert [request.url.params["page_token"] for request in requests] == [
        "start",
        "middle",
        "last",
        "start",
        "middle",
        "last",
    ]


@pytest.mark.asyncio
async def test_async_empty_middle_page_initial_cursor_and_reuse() -> None:
    requests: list[httpx.Request] = []
    async with AsyncKittyCAD(
        token="test-token",
        base_url="https://example.test",
        http_client=httpx.AsyncClient(
            transport=response_transport(
                [page("middle"), page("last", empty=True), page(None)] * 2, requests
            )
        ),
    ) as client:
        iterator = client.orgs.list_org_skills(limit=1, page_token="start")
        first_pass: list[OrgSkillResponse] = []
        second_pass: list[OrgSkillResponse] = []
        skill: OrgSkillResponse
        async for skill in iterator:
            first_pass.append(skill)
        async for skill in iterator:
            second_pass.append(skill)
        assert first_pass == [SKILL, SKILL]
        assert second_pass == [SKILL, SKILL]
    assert [request.url.params["page_token"] for request in requests] == [
        "start",
        "middle",
        "last",
        "start",
        "middle",
        "last",
    ]


def test_sync_rejects_cycle_to_explicit_initial_cursor() -> None:
    requests: list[httpx.Request] = []
    with KittyCAD(
        token="test-token",
        base_url="https://example.test",
        http_client=httpx.Client(
            transport=response_transport([page("start")], requests)
        ),
    ) as client:
        with pytest.raises(ValueError):
            next(iter(client.orgs.list_org_skills(page_token="start")))
    assert len(requests) == 1


@pytest.mark.asyncio
async def test_async_rejects_cycle_to_explicit_initial_cursor() -> None:
    requests: list[httpx.Request] = []
    async with AsyncKittyCAD(
        token="test-token",
        base_url="https://example.test",
        http_client=httpx.AsyncClient(
            transport=response_transport([page("start")], requests)
        ),
    ) as client:
        with pytest.raises(ValueError):
            await anext(aiter(client.orgs.list_org_skills(page_token="start")))
    assert len(requests) == 1
