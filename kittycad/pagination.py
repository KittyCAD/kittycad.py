"""Pagination support for KittyCAD API with OpenAI-style auto-iteration."""

from typing import Any, AsyncIterator, Callable, Dict, Iterator, Optional, Type, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class SyncPageIterator:
    """Synchronous iterator for paginated API responses.

    Provides OpenAI-style auto-pagination that handles page tokens automatically.
    """

    def __init__(
        self,
        page_fetcher: Callable[..., BaseModel],
        initial_kwargs: Dict[str, Any],
        item_type: Optional[Type[T]] = None,
    ):
        """Initialize the sync page iterator.

        Args:
            page_fetcher: Function to fetch a page (e.g., client.api_calls.list_api_calls)
            initial_kwargs: Initial arguments for the first request
            item_type: Type of items being paginated
        """
        self._page_fetcher = page_fetcher
        self._initial_kwargs = initial_kwargs
        self._item_type = item_type
        self._current_page_token: Optional[str] = None
        self._exhausted = False

    def __iter__(self) -> Iterator[T]:
        """Return iterator that yields individual items across all pages."""
        # Reset state for new iteration
        self._current_page_token = None
        self._exhausted = False

        kwargs = self._initial_kwargs.copy()

        while not self._exhausted:
            # Add page token if we have one
            if self._current_page_token:
                kwargs["page_token"] = self._current_page_token
            # Note: Don't remove page_token from kwargs if it exists in initial_kwargs
            # This allows users to explicitly start pagination from a specific token

            # Fetch the page
            page = self._page_fetcher(**kwargs)

            # Extract items and yield them
            items = getattr(page, "items", [])
            # Handle case where items might be None
            if items is not None:
                for item in items:
                    yield item

            # Check for next page
            next_page_token = getattr(page, "next_page", None)
            if next_page_token:
                self._current_page_token = next_page_token
            else:
                self._exhausted = True
                break


class AsyncPageIterator:
    """Asynchronous iterator for paginated API responses.

    Provides OpenAI-style async auto-pagination that handles page tokens automatically.
    """

    def __init__(
        self,
        page_fetcher: Callable[..., Any],  # Returns Awaitable[BaseModel]
        initial_kwargs: Dict[str, Any],
        item_type: Optional[Type[T]] = None,
    ):
        """Initialize the async page iterator.

        Args:
            page_fetcher: Async function to fetch a page (e.g., client.api_calls.list_api_calls)
            initial_kwargs: Initial arguments for the first request
            item_type: Type of items being paginated
        """
        self._page_fetcher = page_fetcher
        self._initial_kwargs = initial_kwargs
        self._item_type = item_type
        self._current_page_token: Optional[str] = None
        self._exhausted = False

    def __aiter__(self) -> AsyncIterator[T]:
        """Return async iterator that yields individual items across all pages."""
        # Reset state for new iteration
        self._current_page_token = None
        self._exhausted = False
        return self._async_iter()

    async def _async_iter(self) -> AsyncIterator[T]:
        """Internal async iterator implementation."""
        kwargs = self._initial_kwargs.copy()

        while not self._exhausted:
            # Add page token if we have one
            if self._current_page_token:
                kwargs["page_token"] = self._current_page_token
            # Note: Don't remove page_token from kwargs if it exists in initial_kwargs
            # This allows users to explicitly start pagination from a specific token

            # Fetch the page
            page = await self._page_fetcher(**kwargs)

            # Extract items and yield them
            items = getattr(page, "items", [])
            # Handle case where items might be None
            if items is not None:
                for item in items:
                    yield item

            # Check for next page
            next_page_token = getattr(page, "next_page", None)
            if next_page_token:
                self._current_page_token = next_page_token
            else:
                self._exhausted = True
                break


def create_sync_page_iterator(
    page_fetcher: Callable[..., BaseModel],
    kwargs: Dict[str, Any],
    item_type: Optional[Type[T]] = None,
) -> SyncPageIterator:
    """Create a synchronous page iterator.

    Args:
        page_fetcher: Function that fetches a page
        kwargs: Arguments to pass to the page fetcher
        item_type: Type of individual items

    Returns:
        SyncPageIterator that can be iterated to get all items
    """
    return SyncPageIterator(page_fetcher, kwargs, item_type)


def create_async_page_iterator(
    page_fetcher: Callable[..., Any],  # Returns Awaitable[BaseModel]
    kwargs: Dict[str, Any],
    item_type: Optional[Type[T]] = None,
) -> AsyncPageIterator:
    """Create an asynchronous page iterator.

    Args:
        page_fetcher: Async function that fetches a page
        kwargs: Arguments to pass to the page fetcher
        item_type: Type of individual items

    Returns:
        AsyncPageIterator that can be async iterated to get all items
    """
    return AsyncPageIterator(page_fetcher, kwargs, item_type)
