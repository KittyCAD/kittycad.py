"""Tests for pagination functionality."""

from typing import AsyncIterator, Iterator, List, Optional
from unittest.mock import AsyncMock, Mock

import pytest
from pydantic import BaseModel

from kittycad.pagination import AsyncPageIterator, SyncPageIterator


# Mock data models for testing
class MockItem(BaseModel):
    id: str
    name: str


class MockPage(BaseModel):
    items: List[MockItem]
    next_page: Optional[str] = None


def test_sync_page_iterator_single_page():
    """Test sync pagination with a single page."""
    # Create mock data
    items = [
        MockItem(id="1", name="Item 1"),
        MockItem(id="2", name="Item 2"),
    ]
    page = MockPage(items=items, next_page=None)

    # Create mock page fetcher
    mock_fetcher = Mock(return_value=page)

    # Create iterator
    iterator = SyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={"limit": 10},
        item_type=MockItem,
    )

    # Collect all items
    result_items: list[MockItem] = list(iterator)

    # Verify results
    assert len(result_items) == 2
    assert result_items[0].id == "1"
    assert result_items[0].name == "Item 1"
    assert result_items[1].id == "2"
    assert result_items[1].name == "Item 2"

    # Verify fetcher was called once with initial kwargs
    mock_fetcher.assert_called_once_with(limit=10)


def test_sync_page_iterator_multiple_pages():
    """Test sync pagination with multiple pages."""
    # Create mock data for multiple pages
    page1_items = [MockItem(id="1", name="Item 1"), MockItem(id="2", name="Item 2")]
    page2_items = [MockItem(id="3", name="Item 3"), MockItem(id="4", name="Item 4")]
    page3_items = [MockItem(id="5", name="Item 5")]

    page1 = MockPage(items=page1_items, next_page="token2")
    page2 = MockPage(items=page2_items, next_page="token3")
    page3 = MockPage(items=page3_items, next_page=None)

    # Create mock page fetcher that returns different pages based on token
    def mock_fetch_page(**kwargs):
        if "page_token" not in kwargs:
            return page1
        elif kwargs["page_token"] == "token2":
            return page2
        elif kwargs["page_token"] == "token3":
            return page3
        else:
            raise ValueError(f"Unexpected page token: {kwargs['page_token']}")

    mock_fetcher = Mock(side_effect=mock_fetch_page)

    # Create iterator
    iterator = SyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={"limit": 2},
        item_type=MockItem,
    )

    # Collect all items
    result_items: list[MockItem] = list(iterator)

    # Verify results
    assert len(result_items) == 5
    assert [item.id for item in result_items] == ["1", "2", "3", "4", "5"]
    assert [item.name for item in result_items] == [
        "Item 1",
        "Item 2",
        "Item 3",
        "Item 4",
        "Item 5",
    ]

    # Verify fetcher was called three times with correct arguments
    assert mock_fetcher.call_count == 3
    mock_fetcher.assert_any_call(limit=2)  # First call
    mock_fetcher.assert_any_call(limit=2, page_token="token2")  # Second call
    mock_fetcher.assert_any_call(limit=2, page_token="token3")  # Third call


def test_sync_page_iterator_empty_page():
    """Test sync pagination with empty pages."""
    empty_page = MockPage(items=[], next_page=None)
    mock_fetcher = Mock(return_value=empty_page)

    iterator = SyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={},
        item_type=MockItem,
    )

    result_items: list[MockItem] = list(iterator)

    assert len(result_items) == 0
    mock_fetcher.assert_called_once_with()


@pytest.mark.asyncio
async def test_async_page_iterator_single_page():
    """Test async pagination with a single page."""
    # Create mock data
    items = [
        MockItem(id="1", name="Item 1"),
        MockItem(id="2", name="Item 2"),
    ]
    page = MockPage(items=items, next_page=None)

    # Create async mock page fetcher
    mock_fetcher = AsyncMock(return_value=page)

    # Create async iterator
    iterator = AsyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={"limit": 10},
        item_type=MockItem,
    )

    # Collect all items
    result_items: list[MockItem] = []
    item: MockItem
    async for item in iterator:
        result_items.append(item)

    # Verify results
    assert len(result_items) == 2
    assert result_items[0].id == "1"
    assert result_items[0].name == "Item 1"
    assert result_items[1].id == "2"
    assert result_items[1].name == "Item 2"

    # Verify fetcher was called once with initial kwargs
    mock_fetcher.assert_called_once_with(limit=10)


@pytest.mark.asyncio
async def test_async_page_iterator_multiple_pages():
    """Test async pagination with multiple pages."""
    # Create mock data for multiple pages
    page1_items = [MockItem(id="1", name="Item 1"), MockItem(id="2", name="Item 2")]
    page2_items = [MockItem(id="3", name="Item 3"), MockItem(id="4", name="Item 4")]
    page3_items = [MockItem(id="5", name="Item 5")]

    page1 = MockPage(items=page1_items, next_page="token2")
    page2 = MockPage(items=page2_items, next_page="token3")
    page3 = MockPage(items=page3_items, next_page=None)

    # Create async mock page fetcher that returns different pages based on token
    async def mock_fetch_page(**kwargs):
        if "page_token" not in kwargs:
            return page1
        elif kwargs["page_token"] == "token2":
            return page2
        elif kwargs["page_token"] == "token3":
            return page3
        else:
            raise ValueError(f"Unexpected page token: {kwargs['page_token']}")

    mock_fetcher = AsyncMock(side_effect=mock_fetch_page)

    # Create async iterator
    iterator = AsyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={"limit": 2},
        item_type=MockItem,
    )

    # Collect all items
    result_items: list[MockItem] = []
    item: MockItem
    async for item in iterator:
        result_items.append(item)

    # Verify results
    assert len(result_items) == 5
    assert [item.id for item in result_items] == ["1", "2", "3", "4", "5"]
    assert [item.name for item in result_items] == [
        "Item 1",
        "Item 2",
        "Item 3",
        "Item 4",
        "Item 5",
    ]

    # Verify fetcher was called three times with correct arguments
    assert mock_fetcher.call_count == 3
    mock_fetcher.assert_any_call(limit=2)  # First call
    mock_fetcher.assert_any_call(limit=2, page_token="token2")  # Second call
    mock_fetcher.assert_any_call(limit=2, page_token="token3")  # Third call


@pytest.mark.asyncio
async def test_async_page_iterator_empty_page():
    """Test async pagination with empty pages."""
    empty_page = MockPage(items=[], next_page=None)
    mock_fetcher = AsyncMock(return_value=empty_page)

    iterator = AsyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={},
        item_type=MockItem,
    )

    result_items: list[MockItem] = []
    item: MockItem
    async for item in iterator:
        result_items.append(item)

    assert len(result_items) == 0
    mock_fetcher.assert_called_once_with()


def test_sync_page_iterator_preserves_initial_kwargs():
    """Test that initial kwargs are preserved across page requests."""
    page1 = MockPage(items=[MockItem(id="1", name="Item 1")], next_page="token2")
    page2 = MockPage(items=[MockItem(id="2", name="Item 2")], next_page=None)

    def mock_fetch_page(**kwargs):
        # Verify that sort_by is always passed
        assert kwargs["sort_by"] == "created_at"
        if "page_token" not in kwargs:
            return page1
        else:
            return page2

    mock_fetcher = Mock(side_effect=mock_fetch_page)

    iterator = SyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={"sort_by": "created_at", "limit": 1},
        item_type=MockItem,
    )

    # Trigger pagination
    result_items: list[MockItem] = list(iterator)

    assert len(result_items) == 2
    assert mock_fetcher.call_count == 2


@pytest.mark.asyncio
async def test_async_page_iterator_preserves_initial_kwargs():
    """Test that async initial kwargs are preserved across page requests."""
    page1 = MockPage(items=[MockItem(id="1", name="Item 1")], next_page="token2")
    page2 = MockPage(items=[MockItem(id="2", name="Item 2")], next_page=None)

    async def mock_fetch_page(**kwargs):
        # Verify that sort_by is always passed
        assert kwargs["sort_by"] == "created_at"
        if "page_token" not in kwargs:
            return page1
        else:
            return page2

    mock_fetcher = AsyncMock(side_effect=mock_fetch_page)

    iterator = AsyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={"sort_by": "created_at", "limit": 1},
        item_type=MockItem,
    )

    # Trigger pagination
    result_items: list[MockItem] = []
    item: MockItem
    async for item in iterator:
        result_items.append(item)

    assert len(result_items) == 2
    assert mock_fetcher.call_count == 2


def test_sync_page_iterator_handles_none_items():
    """Test sync pagination handles None items gracefully."""

    # Page with None items attribute
    class BadPage:
        items = None
        next_page = None

    mock_fetcher = Mock(return_value=BadPage())

    iterator = SyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={},
        item_type=MockItem,
    )

    result_items: list[MockItem] = list(iterator)
    assert len(result_items) == 0


@pytest.mark.asyncio
async def test_async_page_iterator_handles_none_items():
    """Test async pagination handles None items gracefully."""

    # Page with None items attribute
    class BadPage:
        items = None
        next_page = None

    mock_fetcher = AsyncMock(return_value=BadPage())

    iterator = AsyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={},
        item_type=MockItem,
    )

    result_items: list[MockItem] = []
    item: MockItem
    async for item in iterator:
        result_items.append(item)

    assert len(result_items) == 0


def test_sync_page_iterator_multiple_iteration():
    """Test that sync iterator can be iterated multiple times."""
    items = [MockItem(id="1", name="Item 1")]
    page = MockPage(items=items, next_page=None)
    mock_fetcher = Mock(return_value=page)

    iterator = SyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={},
        item_type=MockItem,
    )

    # First iteration
    result1: list[MockItem] = list(iterator)
    # Second iteration should start fresh
    result2: list[MockItem] = list(iterator)

    assert len(result1) == 1
    assert len(result2) == 1
    # Should have called fetcher twice (once per iteration)
    assert mock_fetcher.call_count == 2


@pytest.mark.asyncio
async def test_async_page_iterator_multiple_iteration():
    """Test that async iterator can be iterated multiple times."""
    items = [MockItem(id="1", name="Item 1")]
    page = MockPage(items=items, next_page=None)
    mock_fetcher = AsyncMock(return_value=page)

    iterator = AsyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={},
        item_type=MockItem,
    )

    # First iteration
    result1: list[MockItem] = []
    item: MockItem
    async for item in iterator:
        result1.append(item)

    # Second iteration should start fresh
    result2: list[MockItem] = []
    # Use same item variable for second iteration
    async for item in iterator:
        result2.append(item)

    assert len(result1) == 1
    assert len(result2) == 1
    # Should have called fetcher twice (once per iteration)
    assert mock_fetcher.call_count == 2


def test_sync_page_iterator_scan_immutability():
    """Test that scan parameters cannot be changed mid-iteration (scan immutability)."""
    page1 = MockPage(items=[MockItem(id="1", name="Item A")], next_page="token2")
    page2 = MockPage(items=[MockItem(id="2", name="Item B")], next_page=None)

    def mock_fetch_page(**kwargs):
        # Verify that sort_by remains consistent across pages
        assert kwargs["sort_by"] == "name_ascending", (
            f"Sort changed to {kwargs.get('sort_by')}"
        )
        if "page_token" not in kwargs:
            return page1
        else:
            return page2

    mock_fetcher = Mock(side_effect=mock_fetch_page)

    iterator = SyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={"sort_by": "name_ascending", "limit": 1},
        item_type=MockItem,
    )

    # Start iteration
    iter_obj: Iterator[MockItem] = iter(iterator)
    first_item = next(iter_obj)
    assert first_item.id == "1"

    # Attempt to modify the iterator's initial kwargs (should not affect ongoing iteration)
    iterator._initial_kwargs["sort_by"] = "name_descending"

    # Continue iteration - should still use original sort
    second_item = next(iter_obj)
    assert second_item.id == "2"

    # Verify fetcher was called with original sort both times
    assert mock_fetcher.call_count == 2


@pytest.mark.asyncio
async def test_async_page_iterator_scan_immutability():
    """Test that async scan parameters cannot be changed mid-iteration."""
    page1 = MockPage(items=[MockItem(id="1", name="Item A")], next_page="token2")
    page2 = MockPage(items=[MockItem(id="2", name="Item B")], next_page=None)

    async def mock_fetch_page(**kwargs):
        # Verify that sort_by remains consistent across pages
        assert kwargs["sort_by"] == "name_ascending", (
            f"Sort changed to {kwargs.get('sort_by')}"
        )
        if "page_token" not in kwargs:
            return page1
        else:
            return page2

    mock_fetcher = AsyncMock(side_effect=mock_fetch_page)

    iterator = AsyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={"sort_by": "name_ascending", "limit": 1},
        item_type=MockItem,
    )

    # Start async iteration
    aiter_obj: AsyncIterator[MockItem] = iterator.__aiter__()
    first_item = await aiter_obj.__anext__()
    assert first_item.id == "1"

    # Attempt to modify the iterator's initial kwargs (should not affect ongoing iteration)
    iterator._initial_kwargs["sort_by"] = "name_descending"

    # Continue iteration - should still use original sort
    second_item = await aiter_obj.__anext__()
    assert second_item.id == "2"

    # Verify fetcher was called with original sort both times
    assert mock_fetcher.call_count == 2


def test_sync_page_iterator_extra_params_carry_across_pages():
    """Test that extra required query params are carried across all pages."""
    page1 = MockPage(items=[MockItem(id="1", name="Item 1")], next_page="token2")
    page2 = MockPage(items=[MockItem(id="2", name="Item 2")], next_page=None)

    def mock_fetch_page(**kwargs):
        # Verify all extra params are present in every request
        assert kwargs["user_id"] == "user123"
        assert kwargs["org_id"] == "org456"
        assert kwargs["include_deleted"]
        if "page_token" not in kwargs:
            return page1
        else:
            return page2

    mock_fetcher = Mock(side_effect=mock_fetch_page)

    iterator = SyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={
            "user_id": "user123",
            "org_id": "org456",
            "include_deleted": True,
            "limit": 1,
        },
        item_type=MockItem,
    )

    result_items: list[MockItem] = list(iterator)

    assert len(result_items) == 2
    assert mock_fetcher.call_count == 2


@pytest.mark.asyncio
async def test_async_page_iterator_extra_params_carry_across_pages():
    """Test that async extra required query params are carried across all pages."""
    page1 = MockPage(items=[MockItem(id="1", name="Item 1")], next_page="token2")
    page2 = MockPage(items=[MockItem(id="2", name="Item 2")], next_page=None)

    async def mock_fetch_page(**kwargs):
        # Verify all extra params are present in every request
        assert kwargs["user_id"] == "user123"
        assert kwargs["org_id"] == "org456"
        assert kwargs["include_deleted"]
        if "page_token" not in kwargs:
            return page1
        else:
            return page2

    mock_fetcher = AsyncMock(side_effect=mock_fetch_page)

    iterator = AsyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={
            "user_id": "user123",
            "org_id": "org456",
            "include_deleted": True,
            "limit": 1,
        },
        item_type=MockItem,
    )

    result_items: list[MockItem] = []
    item: MockItem
    async for item in iterator:
        result_items.append(item)

    assert len(result_items) == 2
    assert mock_fetcher.call_count == 2


def test_sync_page_iterator_memory_efficiency():
    """Test that sync pagination uses O(1) memory (yields as we fetch)."""
    # Create a large number of pages with small page sizes to test memory efficiency
    num_pages = 100
    items_per_page = 10

    page_call_count = 0

    def mock_fetch_page(**kwargs):
        nonlocal page_call_count
        page_call_count += 1

        # Generate items for this page
        start_id = (page_call_count - 1) * items_per_page + 1
        items = [
            MockItem(id=str(start_id + i), name=f"Item {start_id + i}")
            for i in range(items_per_page)
        ]

        # Determine next page token
        next_page = (
            f"token{page_call_count + 1}" if page_call_count < num_pages else None
        )

        return MockPage(items=items, next_page=next_page)

    mock_fetcher = Mock(side_effect=mock_fetch_page)

    iterator = SyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={"limit": items_per_page},
        item_type=MockItem,
    )

    # Process items one by one and verify they come in order
    item_count = 0
    item: MockItem
    for item in iterator:
        item_count += 1
        # Mypy needs help with early break - cast to avoid Never type
        typed_item: MockItem = item
        assert typed_item.id == str(item_count)
        assert typed_item.name == f"Item {item_count}"

        # Stop after a reasonable number to avoid excessive test time
        if item_count >= 50:
            break

    # Verify that we only fetched the pages we needed (not all 100)
    expected_pages = (50 // items_per_page) + (1 if 50 % items_per_page > 0 else 0)
    assert page_call_count == expected_pages
    assert item_count == 50


@pytest.mark.asyncio
async def test_async_page_iterator_memory_efficiency():
    """Test that async pagination uses O(1) memory (yields as we fetch)."""
    # Create a large number of pages with small page sizes to test memory efficiency
    num_pages = 100
    items_per_page = 10

    page_call_count = 0

    async def mock_fetch_page(**kwargs):
        nonlocal page_call_count
        page_call_count += 1

        # Generate items for this page
        start_id = (page_call_count - 1) * items_per_page + 1
        items = [
            MockItem(id=str(start_id + i), name=f"Item {start_id + i}")
            for i in range(items_per_page)
        ]

        # Determine next page token
        next_page = (
            f"token{page_call_count + 1}" if page_call_count < num_pages else None
        )

        return MockPage(items=items, next_page=next_page)

    mock_fetcher = AsyncMock(side_effect=mock_fetch_page)

    iterator = AsyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={"limit": items_per_page},
        item_type=MockItem,
    )

    # Process items one by one and verify they come in order
    item_count = 0
    item: MockItem
    async for item in iterator:
        item_count += 1
        # Mypy needs help with early break - cast to avoid Never type
        typed_item: MockItem = item
        assert typed_item.id == str(item_count)
        assert typed_item.name == f"Item {item_count}"

        # Stop after a reasonable number to avoid excessive test time
        if item_count >= 50:
            break

    # Verify that we only fetched the pages we needed (not all 100)
    expected_pages = (50 // items_per_page) + (1 if 50 % items_per_page > 0 else 0)
    assert page_call_count == expected_pages
    assert item_count == 50


def test_sync_page_iterator_large_dataset():
    """Test sync iteration over a large dataset to verify N items are yielded."""
    total_items = 257  # Non-round number to test edge cases
    items_per_page = 25

    def mock_fetch_page(**kwargs):
        # Determine which page we're on based on page_token
        if "page_token" not in kwargs:
            page_num = 0
        else:
            page_num = int(kwargs["page_token"].replace("page", "")) - 1

        # Calculate items for this page
        start_id = page_num * items_per_page + 1
        end_id = min(start_id + items_per_page, total_items + 1)

        items = [MockItem(id=str(i), name=f"Item {i}") for i in range(start_id, end_id)]

        # Determine next page
        next_page = f"page{page_num + 2}" if end_id <= total_items else None

        return MockPage(items=items, next_page=next_page)

    mock_fetcher = Mock(side_effect=mock_fetch_page)

    iterator = SyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={"limit": items_per_page},
        item_type=MockItem,
    )

    # Collect all items
    result_items: list[MockItem] = list(iterator)

    # Verify we got exactly the expected number of items
    assert len(result_items) == total_items

    # Verify all items are in order
    for i, item in enumerate(result_items, 1):
        assert item.id == str(i)
        assert item.name == f"Item {i}"

    # Verify correct number of page fetches
    expected_pages = (total_items + items_per_page - 1) // items_per_page
    assert mock_fetcher.call_count == expected_pages


@pytest.mark.asyncio
async def test_async_page_iterator_large_dataset():
    """Test async iteration over a large dataset to verify N items are yielded."""
    total_items = 257  # Non-round number to test edge cases
    items_per_page = 25

    async def mock_fetch_page(**kwargs):
        # Determine which page we're on based on page_token
        if "page_token" not in kwargs:
            page_num = 0
        else:
            page_num = int(kwargs["page_token"].replace("page", "")) - 1

        # Calculate items for this page
        start_id = page_num * items_per_page + 1
        end_id = min(start_id + items_per_page, total_items + 1)

        items = [MockItem(id=str(i), name=f"Item {i}") for i in range(start_id, end_id)]

        # Determine next page
        next_page = f"page{page_num + 2}" if end_id <= total_items else None

        return MockPage(items=items, next_page=next_page)

    mock_fetcher = AsyncMock(side_effect=mock_fetch_page)

    iterator = AsyncPageIterator(
        page_fetcher=mock_fetcher,
        initial_kwargs={"limit": items_per_page},
        item_type=MockItem,
    )

    # Collect all items
    result_items: list[MockItem] = []
    item: MockItem
    async for item in iterator:
        result_items.append(item)

    # Verify we got exactly the expected number of items
    assert len(result_items) == total_items

    # Verify all items are in order
    for i, item in enumerate(result_items, 1):
        assert item.id == str(i)
        assert item.name == f"Item {i}"

    # Verify correct number of page fetches
    expected_pages = (total_items + items_per_page - 1) // items_per_page
    assert mock_fetcher.call_count == expected_pages
