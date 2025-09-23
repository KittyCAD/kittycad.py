Pagination
==========

The KittyCAD Python SDK provides automatic pagination support for list endpoints that return large datasets. Instead of manually handling page tokens and making multiple requests, you can simply iterate over all results using Python's standard iteration patterns.

Features
--------

* **Automatic Pagination**: Seamlessly iterate through all pages of results
* **Memory Efficient**: Uses generators to yield results as they're fetched (O(1) memory usage)
* **Type Safe**: Full type annotations and IDE support
* **Both Sync & Async**: Works with both ``KittyCAD`` and ``AsyncKittyCAD`` clients
* **OpenAI-Style API**: Familiar pagination patterns inspired by the OpenAI Python SDK

Quick Start
-----------

**Sync Example:**

.. code-block:: python

    from kittycad import KittyCAD
    
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable
    
    # Iterate through all API calls automatically
    for api_call in client.api_calls.list_api_calls():
        print(f"API Call: {api_call}")
        # No manual pagination needed!

**Async Example:**

.. code-block:: python

    import asyncio
    from kittycad import AsyncKittyCAD
    
    async def main():
        client = AsyncKittyCAD()
        
        # Iterate through all results asynchronously
        async for api_call in client.api_calls.list_api_calls():
            print(f"API Call: {api_call}")
            
        await client.aclose()
    
    asyncio.run(main())

How It Works
------------

The pagination system automatically:

1. **Detects Paginated Endpoints**: Uses the ``x-dropshot-pagination`` OpenAPI extension
2. **Returns Iterators**: Instead of page objects, returns ``SyncPageIterator`` or ``AsyncPageIterator``
3. **Handles Page Tokens**: Automatically manages ``page_token`` and ``limit`` parameters
4. **Yields Individual Items**: You get the actual items, not page wrappers
5. **Preserves Parameters**: All your query parameters are maintained across pages

Available Paginated Endpoints
-----------------------------

The following endpoints support automatic pagination:


Api Calls API
-------------

**list_api_calls**
    List API calls.
    
    Returns: ``SyncPageIterator[ApiCallWithPrice]``
    
    Example:
    
    .. code-block:: python
    
        # Sync
        for item in client.api_calls.list_api_calls():
            print(item)
            
        # Async  
        async for item in client.api_calls.list_api_calls():
            print(item)

**list_async_operations**
    List async operations.
    
    Returns: ``SyncPageIterator[AsyncApiCall]``
    
    Example:
    
    .. code-block:: python
    
        # Sync
        for item in client.api_calls.list_async_operations():
            print(item)
            
        # Async  
        async for item in client.api_calls.list_async_operations():
            print(item)

**org_list_api_calls**
    List API calls for your org.
    
    Returns: ``SyncPageIterator[ApiCallWithPrice]``
    
    Example:
    
    .. code-block:: python
    
        # Sync
        for item in client.api_calls.org_list_api_calls():
            print(item)
            
        # Async  
        async for item in client.api_calls.org_list_api_calls():
            print(item)

**user_list_api_calls**
    List API calls for your user.
    
    Returns: ``SyncPageIterator[ApiCallWithPrice]``
    
    Example:
    
    .. code-block:: python
    
        # Sync
        for item in client.api_calls.user_list_api_calls():
            print(item)
            
        # Async  
        async for item in client.api_calls.user_list_api_calls():
            print(item)

**list_api_calls_for_user**
    List API calls for a user.
    
    Returns: ``SyncPageIterator[ApiCallWithPrice]``
    
    Example:
    
    .. code-block:: python
    
        # Sync
        for item in client.api_calls.list_api_calls_for_user():
            print(item)
            
        # Async  
        async for item in client.api_calls.list_api_calls_for_user():
            print(item)


Api Tokens API
--------------

**list_api_tokens_for_user**
    List API tokens for your user.
    
    Returns: ``SyncPageIterator[ApiToken]``
    
    Example:
    
    .. code-block:: python
    
        # Sync
        for item in client.api_tokens.list_api_tokens_for_user():
            print(item)
            
        # Async  
        async for item in client.api_tokens.list_api_tokens_for_user():
            print(item)


Ml API
------

**list_conversations_for_user**
    List conversations
    
    Returns: ``SyncPageIterator[Conversation]``
    
    Example:
    
    .. code-block:: python
    
        # Sync
        for item in client.ml.list_conversations_for_user():
            print(item)
            
        # Async  
        async for item in client.ml.list_conversations_for_user():
            print(item)

**list_ml_prompts**
    List all ML prompts.
    
    Returns: ``SyncPageIterator[MlPrompt]``
    
    Example:
    
    .. code-block:: python
    
        # Sync
        for item in client.ml.list_ml_prompts():
            print(item)
            
        # Async  
        async for item in client.ml.list_ml_prompts():
            print(item)

**list_text_to_cad_parts_for_user**
    List text-to-CAD parts you've generated.
    
    Returns: ``SyncPageIterator[TextToCadResponse]``
    
    Example:
    
    .. code-block:: python
    
        # Sync
        for item in client.ml.list_text_to_cad_parts_for_user():
            print(item)
            
        # Async  
        async for item in client.ml.list_text_to_cad_parts_for_user():
            print(item)


Orgs API
--------

**list_org_members**
    List members of your org.
    
    Returns: ``SyncPageIterator[OrgMember]``
    
    Example:
    
    .. code-block:: python
    
        # Sync
        for item in client.orgs.list_org_members():
            print(item)
            
        # Async  
        async for item in client.orgs.list_org_members():
            print(item)

**get_org_shortlinks**
    Get the shortlinks for an org.
    
    Returns: ``SyncPageIterator[Shortlink]``
    
    Example:
    
    .. code-block:: python
    
        # Sync
        for item in client.orgs.get_org_shortlinks():
            print(item)
            
        # Async  
        async for item in client.orgs.get_org_shortlinks():
            print(item)

**list_orgs**
    List orgs.
    
    Returns: ``SyncPageIterator[Org]``
    
    Example:
    
    .. code-block:: python
    
        # Sync
        for item in client.orgs.list_orgs():
            print(item)
            
        # Async  
        async for item in client.orgs.list_orgs():
            print(item)


Service Accounts API
--------------------

**list_service_accounts_for_org**
    List service accounts for your org.
    
    Returns: ``SyncPageIterator[ServiceAccount]``
    
    Example:
    
    .. code-block:: python
    
        # Sync
        for item in client.service_accounts.list_service_accounts_for_org():
            print(item)
            
        # Async  
        async for item in client.service_accounts.list_service_accounts_for_org():
            print(item)


Users API
---------

**get_user_shortlinks**
    Get the shortlinks for a user.
    
    Returns: ``SyncPageIterator[Shortlink]``
    
    Example:
    
    .. code-block:: python
    
        # Sync
        for item in client.users.get_user_shortlinks():
            print(item)
            
        # Async  
        async for item in client.users.get_user_shortlinks():
            print(item)

**list_users**
    List users.
    
    Returns: ``SyncPageIterator[User]``
    
    Example:
    
    .. code-block:: python
    
        # Sync
        for item in client.users.list_users():
            print(item)
            
        # Async  
        async for item in client.users.list_users():
            print(item)

**list_users_extended**
    List users with extended information.
    
    Returns: ``SyncPageIterator[ExtendedUser]``
    
    Example:
    
    .. code-block:: python
    
        # Sync
        for item in client.users.list_users_extended():
            print(item)
            
        # Async  
        async for item in client.users.list_users_extended():
            print(item)


Advanced Usage
--------------

Controlling Page Size
~~~~~~~~~~~~~~~~~~~~

You can control the page size using the ``limit`` parameter:

.. code-block:: python

    # Fetch 50 items per page instead of the default
    for item in client.api_calls.list_api_calls(limit=50):
        print(item)

Starting from a Specific Page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can start pagination from a specific page token:

.. code-block:: python

    # Start from a specific page
    for item in client.api_calls.list_api_calls(page_token="your_token_here"):
        print(item)

Early Termination
~~~~~~~~~~~~~~~~

You can break out of the iteration at any time:

.. code-block:: python

    # Only process the first 100 items
    count = 0
    for item in client.api_calls.list_api_calls():
        print(item)
        count += 1
        if count >= 100:
            break

Memory Efficiency
~~~~~~~~~~~~~~~~

The pagination system uses generators for memory efficiency:

.. code-block:: python

    # This uses O(1) memory regardless of total result count
    # Items are fetched and yielded as needed
    for item in client.api_calls.list_api_calls():
        process_large_item(item)  # Memory usage stays constant

Error Handling
~~~~~~~~~~~~~

Handle API errors during pagination:

.. code-block:: python

    try:
        for item in client.api_calls.list_api_calls():
            print(item)
    except Exception as e:
        print(f"Pagination failed: {e}")

Multiple Iterations
~~~~~~~~~~~~~~~~~~

You can iterate over the same paginator multiple times:

.. code-block:: python

    paginator = client.api_calls.list_api_calls()
    
    # First iteration
    for item in paginator:
        print(f"First pass: {item}")
        
    # Second iteration (starts fresh)
    for item in paginator:
        print(f"Second pass: {item}")

Type Safety
----------

All paginated endpoints return properly typed iterators:

.. code-block:: python

    from kittycad.models import ApiCallWithPrice
    
    # Full type safety and IDE support
    item: ApiCallWithPrice
    for item in client.api_calls.list_api_calls():
        # IDE knows 'item' is ApiCallWithPrice
        print(item.id)  # Autocomplete works!
        print(item.created_at)  # Type checking works!

Implementation Details
---------------------

The pagination system is built on top of:

* **SyncPageIterator**: For synchronous pagination
* **AsyncPageIterator**: For asynchronous pagination  
* **Dropshot Pagination**: Uses the industry-standard Dropshot pagination protocol
* **Type Inference**: Automatically extracts item types from ``*ResultsPage`` response types

The iterators implement Python's standard iteration protocols, so they work seamlessly with:

* ``for`` loops
* ``list()`` comprehensions  
* ``async for`` loops
* ``itertools`` functions
* Any code that expects iterables

Contributing
-----------

This documentation is automatically generated from the OpenAPI specification. 
To update it, run:

.. code-block:: bash

    python generate/generate_pagination_docs.py

The pagination implementation can be found in ``kittycad/pagination.py``.