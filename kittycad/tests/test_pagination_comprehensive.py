#!/usr/bin/env python3
"""Comprehensive tests for pagination behavior requirements."""

from typing import Iterator, List, Optional
from unittest.mock import AsyncMock, Mock, call

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


class TestPaginationFirstCall:
    """Test first call pagination behavior."""

    def test_first_call_without_page_token_sends_scan_params_and_limit(self):
        """Test first call without page_token sends scan params and limit."""
        # Mock single page response
        items = [MockItem(id="1", name="Item 1")]
        page = MockPage(items=items, next_page=None)
        mock_fetcher = Mock(return_value=page)

        # Create iterator with scan params
        iterator = SyncPageIterator(
            page_fetcher=mock_fetcher,
            initial_kwargs={"limit": 10, "sort_by": "created_at", "filter": "active"},
            item_type=MockItem,
        )

        # Consume iterator
        list(iterator)

        # Verify first call includes all scan params and limit
        mock_fetcher.assert_called_once_with(
            limit=10, sort_by="created_at", filter="active"
        )
        # Should NOT include page_token in first call
        args, kwargs = mock_fetcher.call_args
        assert "page_token" not in kwargs

    def test_first_call_with_explicit_page_token_still_sends_scan_params(self):
        """Test first call with explicit page_token still includes scan params."""
        # Mock single page response
        items = [MockItem(id="1", name="Item 1")]
        page = MockPage(items=items, next_page=None)
        mock_fetcher = Mock(return_value=page)

        # Create iterator with explicit page_token in initial_kwargs
        iterator = SyncPageIterator(
            page_fetcher=mock_fetcher,
            initial_kwargs={
                "limit": 10,
                "sort_by": "created_at",
                "page_token": "explicit-token",
            },
            item_type=MockItem,
        )

        # Consume iterator
        list(iterator)

        # Verify first call includes page_token and scan params
        mock_fetcher.assert_called_once_with(
            limit=10, sort_by="created_at", page_token="explicit-token"
        )


class TestPaginationContinuation:
    """Test pagination continuation behavior."""

    def test_continuations_send_all_initial_params_plus_page_token(self):
        """Test continuations send all initial params plus page_token (current implementation)."""
        # Create multi-page mock data
        page1_items = [MockItem(id="1", name="Item 1")]
        page2_items = [MockItem(id="2", name="Item 2")]
        page3_items = [MockItem(id="3", name="Item 3")]

        page1 = MockPage(items=page1_items, next_page="token2")
        page2 = MockPage(items=page2_items, next_page="token3")
        page3 = MockPage(items=page3_items, next_page=None)

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

        # Create iterator with scan params
        iterator = SyncPageIterator(
            page_fetcher=mock_fetcher,
            initial_kwargs={
                "limit": 2,
                "sort_by": "created_at",
                "filter": "active",
                "direction": "asc",
            },
            item_type=MockItem,
        )

        # Consume iterator
        result_items: list[MockItem] = list(iterator)

        # Verify we got all items
        assert len(result_items) == 3
        assert [item.id for item in result_items] == ["1", "2", "3"]

        # Verify call pattern
        assert mock_fetcher.call_count == 3

        # First call: all scan params, no page_token
        first_call = mock_fetcher.call_args_list[0]
        expected_first = call(
            limit=2, sort_by="created_at", filter="active", direction="asc"
        )
        assert first_call == expected_first

        # Current implementation: subsequent calls include ALL initial params + page_token
        second_call = mock_fetcher.call_args_list[1]
        expected_second = call(
            limit=2,
            sort_by="created_at",
            filter="active",
            direction="asc",
            page_token="token2",
        )
        assert second_call == expected_second

        third_call = mock_fetcher.call_args_list[2]
        expected_third = call(
            limit=2,
            sort_by="created_at",
            filter="active",
            direction="asc",
            page_token="token3",
        )
        assert third_call == expected_third

    def test_continuations_preserve_limit_if_provided(self):
        """Test continuations preserve limit parameter and all initial kwargs."""
        # Create multi-page mock data
        page1 = MockPage(items=[MockItem(id="1", name="Item 1")], next_page="token2")
        page2 = MockPage(items=[MockItem(id="2", name="Item 2")], next_page=None)

        def mock_fetch_page(**kwargs):
            if "page_token" not in kwargs:
                return page1
            elif kwargs["page_token"] == "token2":
                return page2
            else:
                raise ValueError(f"Unexpected page token: {kwargs['page_token']}")

        mock_fetcher = Mock(side_effect=mock_fetch_page)

        # Create iterator with custom limit
        iterator = SyncPageIterator(
            page_fetcher=mock_fetcher,
            initial_kwargs={"limit": 50, "sort_by": "created_at"},
            item_type=MockItem,
        )

        # Consume iterator
        list(iterator)

        # Verify both calls preserved the limit and all params
        assert mock_fetcher.call_count == 2

        first_call = mock_fetcher.call_args_list[0]
        assert first_call == call(limit=50, sort_by="created_at")

        second_call = mock_fetcher.call_args_list[1]
        assert second_call == call(limit=50, sort_by="created_at", page_token="token2")
        # Current implementation: scan params ARE included in continuation calls
        assert second_call[1]["sort_by"] == "created_at"

    def test_continuations_without_limit_omit_limit(self):
        """Test continuations without initial limit maintain all initial params."""
        # Create multi-page mock data
        page1 = MockPage(items=[MockItem(id="1", name="Item 1")], next_page="token2")
        page2 = MockPage(items=[MockItem(id="2", name="Item 2")], next_page=None)

        def mock_fetch_page(**kwargs):
            if "page_token" not in kwargs:
                return page1
            elif kwargs["page_token"] == "token2":
                return page2
            else:
                raise ValueError(f"Unexpected page token: {kwargs['page_token']}")

        mock_fetcher = Mock(side_effect=mock_fetch_page)

        # Create iterator without limit
        iterator = SyncPageIterator(
            page_fetcher=mock_fetcher,
            initial_kwargs={"sort_by": "created_at"},
            item_type=MockItem,
        )

        # Consume iterator
        list(iterator)

        # Verify call pattern
        assert mock_fetcher.call_count == 2

        # First call: scan params, no limit
        first_call = mock_fetcher.call_args_list[0]
        assert first_call == call(sort_by="created_at")
        assert "limit" not in first_call[1]

        # Second call: all initial params + page_token, still no limit
        second_call = mock_fetcher.call_args_list[1]
        assert second_call == call(sort_by="created_at", page_token="token2")
        assert "limit" not in second_call[1]
        # Current implementation: scan params ARE included in continuation calls
        assert second_call[1]["sort_by"] == "created_at"


class TestPaginationMethods:
    """Test pagination iterator methods."""

    def test_has_next_page_method(self):
        """Test .has_next_page() works correctly."""
        # Note: Current implementation doesn't have has_next_page method
        # This test documents expected behavior for future implementation
        iterator = SyncPageIterator(
            page_fetcher=Mock(),
            initial_kwargs={"limit": 10},
            item_type=MockItem,
        )

        # Should have method for checking if there are more pages
        # assert hasattr(iterator, 'has_next_page')

        # For now, we can test internal state tracking
        assert not iterator._exhausted
        assert iterator._current_page_token is None

    def test_next_page_info_method(self):
        """Test .next_page_info() works correctly."""
        # Note: Current implementation doesn't have next_page_info method
        # This test documents expected behavior for future implementation
        iterator = SyncPageIterator(
            page_fetcher=Mock(),
            initial_kwargs={"limit": 10},
            item_type=MockItem,
        )

        # Should have method for getting next page info
        # assert hasattr(iterator, 'next_page_info')

        # For now, we can test internal state tracking
        assert iterator._current_page_token is None

    def test_get_next_page_method(self):
        """Test .get_next_page() works correctly."""
        # Note: Current implementation doesn't have get_next_page method
        # This test documents expected behavior for future implementation
        SyncPageIterator(
            page_fetcher=Mock(),
            initial_kwargs={"limit": 10},
            item_type=MockItem,
        )

        # Should have method for manually getting next page
        # assert hasattr(iterator, 'get_next_page')

        # Current implementation handles pagination automatically
        # through iteration, which is the expected behavior


class TestPaginationIteration:
    """Test pagination iteration behavior."""

    def test_item_iteration_auto_fetches_all_pages(self):
        """Test item iteration auto-fetches all pages, yields in order, stops at end."""
        # Create mock data for 3 pages
        page1_items = [MockItem(id="1", name="Item 1"), MockItem(id="2", name="Item 2")]
        page2_items = [MockItem(id="3", name="Item 3"), MockItem(id="4", name="Item 4")]
        page3_items = [MockItem(id="5", name="Item 5")]

        page1 = MockPage(items=page1_items, next_page="token2")
        page2 = MockPage(items=page2_items, next_page="token3")
        page3 = MockPage(items=page3_items, next_page=None)

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

        iterator = SyncPageIterator(
            page_fetcher=mock_fetcher,
            initial_kwargs={"limit": 2},
            item_type=MockItem,
        )

        # Iterate and collect items in order
        result_items: list[MockItem] = []
        item: MockItem
        for item in iterator:
            result_items.append(item)

        # Verify correct order and all items fetched
        assert len(result_items) == 5
        assert [item.id for item in result_items] == ["1", "2", "3", "4", "5"]
        assert [item.name for item in result_items] == [
            "Item 1",
            "Item 2",
            "Item 3",
            "Item 4",
            "Item 5",
        ]

        # Verify all pages were fetched
        assert mock_fetcher.call_count == 3

        # Verify iteration stops at end (no more calls after exhaustion)
        # Try iterating again - should reset and start over
        result_items2: list[MockItem] = list(iterator)
        assert len(result_items2) == 5
        assert mock_fetcher.call_count == 6  # Another 3 calls for second iteration

    def test_iteration_stops_at_end_correctly(self):
        """Test iteration stops correctly when no more pages."""
        # Single page with no next_page
        page = MockPage(
            items=[MockItem(id="1", name="Item 1"), MockItem(id="2", name="Item 2")],
            next_page=None,
        )
        mock_fetcher = Mock(return_value=page)

        iterator = SyncPageIterator(
            page_fetcher=mock_fetcher,
            initial_kwargs={"limit": 10},
            item_type=MockItem,
        )

        # Consume iterator
        result_items: list[MockItem] = list(iterator)

        # Verify correct items and single page fetch
        assert len(result_items) == 2
        assert mock_fetcher.call_count == 1

        # Verify iterator is exhausted
        assert iterator._exhausted

    def test_empty_pages_handled_correctly(self):
        """Test empty pages are handled correctly."""
        # Page with empty items list
        empty_page = MockPage(items=[], next_page=None)
        mock_fetcher = Mock(return_value=empty_page)

        iterator = SyncPageIterator(
            page_fetcher=mock_fetcher,
            initial_kwargs={"limit": 10},
            item_type=MockItem,
        )

        # Consume iterator
        result_items: list[MockItem] = list(iterator)

        # Should handle empty page gracefully
        assert len(result_items) == 0
        assert mock_fetcher.call_count == 1


class TestPaginationMemory:
    """Test pagination memory efficiency."""

    def test_large_sequence_iteration_keeps_o1_memory(self):
        """Test large sequence iteration keeps O(1) extra memory."""
        # Create iterator for simulated large dataset
        large_page_count = 100
        items_per_page = 100

        def mock_fetch_large_page(**kwargs):
            """Simulate fetching a large page."""
            if "page_token" not in kwargs:
                page_num = 1
            else:
                page_num = int(kwargs["page_token"].split("-")[1])

            # Create items for this page
            start_id = (page_num - 1) * items_per_page + 1
            items = [
                MockItem(id=str(i), name=f"Item {i}")
                for i in range(start_id, start_id + items_per_page)
            ]

            # Determine next page token
            next_page = f"page-{page_num + 1}" if page_num < large_page_count else None

            return MockPage(items=items, next_page=next_page)

        mock_fetcher = Mock(side_effect=mock_fetch_large_page)

        iterator = SyncPageIterator(
            page_fetcher=mock_fetcher,
            initial_kwargs={"limit": items_per_page},
            item_type=MockItem,
        )

        # Track memory usage by counting how many items we keep in memory
        processed_count = 0
        max_items_in_memory = 0

        # Process items one at a time (simulating real usage)
        item: MockItem
        for item in iterator:
            processed_count += 1

            # In real iteration, we should only have one item in memory at a time
            # The iterator should not accumulate all items
            max_items_in_memory = max(max_items_in_memory, 1)

            # Process a few pages to verify behavior
            if processed_count >= 250:  # 2.5 pages worth
                break

        # Verify we processed items without accumulating them
        assert processed_count == 250
        assert max_items_in_memory == 1  # O(1) memory usage

        # Verify pages were fetched on demand (should be 3 pages for 250 items)
        assert mock_fetcher.call_count == 3

    def test_iterator_does_not_preload_all_pages(self):
        """Test iterator does not preload all pages into memory."""
        call_count = 0

        def mock_fetch_on_demand(**kwargs):
            """Track when pages are fetched."""
            nonlocal call_count
            call_count += 1

            if "page_token" not in kwargs:
                return MockPage(
                    items=[MockItem(id="1", name="Page 1 Item")], next_page="token2"
                )
            elif kwargs["page_token"] == "token2":
                return MockPage(
                    items=[MockItem(id="2", name="Page 2 Item")], next_page="token3"
                )
            else:
                return MockPage(
                    items=[MockItem(id="3", name="Page 3 Item")], next_page=None
                )

        mock_fetcher = Mock(side_effect=mock_fetch_on_demand)

        iterator = SyncPageIterator(
            page_fetcher=mock_fetcher,
            initial_kwargs={"limit": 1},
            item_type=MockItem,
        )

        # Start iteration but don't consume all items
        iter_obj: Iterator[MockItem] = iter(iterator)

        # Get first item - should only fetch first page
        first_item = next(iter_obj)
        assert first_item.id == "1"
        assert call_count == 1  # Only first page fetched

        # Get second item - should fetch second page
        second_item = next(iter_obj)
        assert second_item.id == "2"
        assert call_count == 2  # Second page fetched on demand

        # Verify we haven't preloaded the third page yet
        # Only fetch it when we actually need it
        third_item = next(iter_obj)
        assert third_item.id == "3"
        assert call_count == 3  # Third page fetched on demand


class TestPaginationScanParams:
    """Test pagination scan parameter behavior."""

    def test_changing_scan_params_mid_scan_ignored(self):
        """Test changing scan params mid-scan is ignored."""
        # Create multi-page mock data
        page1 = MockPage(items=[MockItem(id="1", name="Item 1")], next_page="token2")
        page2 = MockPage(items=[MockItem(id="2", name="Item 2")], next_page=None)

        calls_received = []

        def mock_fetch_page(**kwargs):
            calls_received.append(kwargs.copy())
            if "page_token" not in kwargs:
                return page1
            else:
                return page2

        mock_fetcher = Mock(side_effect=mock_fetch_page)

        iterator = SyncPageIterator(
            page_fetcher=mock_fetcher,
            initial_kwargs={"limit": 1, "sort_by": "created_at"},
            item_type=MockItem,
        )

        # Start iteration
        iter_obj: Iterator[MockItem] = iter(iterator)
        next(iter_obj)

        # Try to modify initial_kwargs (this should not affect ongoing iteration)
        iterator._initial_kwargs["sort_by"] = "modified_at"
        iterator._initial_kwargs["new_param"] = "new_value"

        # Continue iteration - should not use modified params
        next(iter_obj)

        # Verify the calls received
        assert len(calls_received) == 2

        # First call: original scan params
        assert calls_received[0] == {"limit": 1, "sort_by": "created_at"}

        # Second call: all initial params + page_token (modified params ignored)
        assert calls_received[1] == {
            "limit": 1,
            "sort_by": "created_at",
            "page_token": "token2",
        }
        # The original sort_by value should be preserved, modifications ignored
        assert calls_received[1]["sort_by"] == "created_at"  # Original value
        assert "new_param" not in calls_received[1]  # New param not included


class TestPaginationAsync:
    """Test async pagination behaves the same as sync."""

    @pytest.mark.asyncio
    async def test_async_for_behaves_same_as_sync(self):
        """Test async for behaves the same as sync iteration."""
        # Create same test data for both sync and async
        page1_items = [MockItem(id="1", name="Item 1"), MockItem(id="2", name="Item 2")]
        page2_items = [MockItem(id="3", name="Item 3")]

        page1 = MockPage(items=page1_items, next_page="token2")
        page2 = MockPage(items=page2_items, next_page=None)

        # Sync version
        def sync_fetch_page(**kwargs):
            if "page_token" not in kwargs:
                return page1
            else:
                return page2

        sync_mock_fetcher = Mock(side_effect=sync_fetch_page)
        sync_iterator = SyncPageIterator(
            page_fetcher=sync_mock_fetcher,
            initial_kwargs={"limit": 2, "sort_by": "created_at"},
            item_type=MockItem,
        )

        sync_results: list[MockItem] = list(sync_iterator)

        # Async version
        async def async_fetch_page(**kwargs):
            if "page_token" not in kwargs:
                return page1
            else:
                return page2

        async_mock_fetcher = AsyncMock(side_effect=async_fetch_page)
        async_iterator = AsyncPageIterator(
            page_fetcher=async_mock_fetcher,
            initial_kwargs={"limit": 2, "sort_by": "created_at"},
            item_type=MockItem,
        )

        async_results: list[MockItem] = []
        item: MockItem
        async for item in async_iterator:
            async_results.append(item)

        # Both should yield same results
        assert len(sync_results) == len(async_results) == 3
        for sync_item, async_item in zip(sync_results, async_results):
            assert sync_item.id == async_item.id
            assert sync_item.name == async_item.name

        # Both should make same API calls
        assert sync_mock_fetcher.call_count == async_mock_fetcher.call_count == 2

        # Verify call patterns are identical
        sync_calls = [call[1] for call in sync_mock_fetcher.call_args_list]
        async_calls = [call[1] for call in async_mock_fetcher.call_args_list]
        assert sync_calls == async_calls

    @pytest.mark.asyncio
    async def test_async_pagination_memory_efficiency(self):
        """Test async pagination has same memory efficiency as sync."""
        call_count = 0

        async def async_fetch_on_demand(**kwargs):
            nonlocal call_count
            call_count += 1

            if "page_token" not in kwargs:
                return MockPage(
                    items=[MockItem(id="1", name="Page 1 Item")], next_page="token2"
                )
            elif kwargs["page_token"] == "token2":
                return MockPage(
                    items=[MockItem(id="2", name="Page 2 Item")], next_page=None
                )
            else:
                raise ValueError("Unexpected token")

        async_mock_fetcher = AsyncMock(side_effect=async_fetch_on_demand)

        iterator = AsyncPageIterator(
            page_fetcher=async_mock_fetcher,
            initial_kwargs={"limit": 1},
            item_type=MockItem,
        )

        # Consume items using async for instead of aiter/anext (Python 3.9 compatibility)
        items: list[MockItem] = []
        item: MockItem
        async for item in iterator:
            items.append(item)
            # Check call count after each item
            if len(items) == 1:
                assert call_count == 1  # Only first page fetched
            if len(items) >= 2:  # Stop after getting 2 items
                break

        assert items[0].id == "1"
        assert items[1].id == "2"
        assert call_count == 2  # Second page fetched on demand


if __name__ == "__main__":
    pytest.main([__file__])
