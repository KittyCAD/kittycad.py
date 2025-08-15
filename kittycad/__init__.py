"""The KittyCAD Python SDK - Generated Client Classes"""

import os
from typing import Any, Optional

from .client import Client
from .exceptions import (
    KittyCADAPIError,
    KittyCADClientError,
    KittyCADConnectionError,
    KittyCADError,
    KittyCADServerError,
    KittyCADTimeoutError,
)

# Import all model types used in return type annotations


class MetaAPI:
    """API for meta endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_schema(self, *args, **kwargs) -> Any:
        """Get OpenAPI schema."""
        from .api.meta.get_schema import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_ipinfo(self, *args, **kwargs) -> Any:
        """Get ip address information."""
        from .api.meta.get_ipinfo import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def community_sso(self, *args, **kwargs) -> Any:
        """Authorize an inbound auth request from our Community page."""
        from .api.meta.community_sso import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_debug_uploads(self, *args, **kwargs) -> Any:
        """Uploads files to public blob storage for debugging purposes."""
        from .api.meta.create_debug_uploads import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_event(self, *args, **kwargs) -> Any:
        """Creates an internal telemetry event."""
        from .api.meta.create_event import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def internal_get_api_token_for_discord_user(self, *args, **kwargs) -> Any:
        """Get an API token for a user by their discord id."""
        from .api.meta.internal_get_api_token_for_discord_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def ping(self, *args, **kwargs) -> Any:
        """Return pong."""
        from .api.meta.ping import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_pricing_subscriptions(self, *args, **kwargs) -> Any:
        """Get the pricing for our subscriptions."""
        from .api.meta.get_pricing_subscriptions import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)


class AsyncMetaAPI:
    """Async API for meta endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def get_schema(self, *args, **kwargs) -> Any:
        """Get OpenAPI schema."""
        from .api.meta.get_schema import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_ipinfo(self, *args, **kwargs) -> Any:
        """Get ip address information."""
        from .api.meta.get_ipinfo import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def community_sso(self, *args, **kwargs) -> Any:
        """Authorize an inbound auth request from our Community page."""
        from .api.meta.community_sso import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_debug_uploads(self, *args, **kwargs) -> Any:
        """Uploads files to public blob storage for debugging purposes."""
        from .api.meta.create_debug_uploads import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_event(self, *args, **kwargs) -> Any:
        """Creates an internal telemetry event."""
        from .api.meta.create_event import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def internal_get_api_token_for_discord_user(self, *args, **kwargs) -> Any:
        """Get an API token for a user by their discord id."""
        from .api.meta.internal_get_api_token_for_discord_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def ping(self, *args, **kwargs) -> Any:
        """Return pong."""
        from .api.meta.ping import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_pricing_subscriptions(self, *args, **kwargs) -> Any:
        """Get the pricing for our subscriptions."""
        from .api.meta.get_pricing_subscriptions import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)


class MlAPI:
    """API for ml endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def create_text_to_cad(self, *args, **kwargs) -> Any:
        """Generate a CAD model from text."""
        from .api.ml.create_text_to_cad import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def list_ml_prompts(self, *args, **kwargs) -> Any:
        """List all ML prompts."""
        from .api.ml.list_ml_prompts import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_ml_prompt(self, *args, **kwargs) -> Any:
        """Get a ML prompt."""
        from .api.ml.get_ml_prompt import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def list_conversations_for_user(self, *args, **kwargs) -> Any:
        """List conversations"""
        from .api.ml.list_conversations_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_proprietary_to_kcl(self, *args, **kwargs) -> Any:
        """Converts a proprietary CAD format to KCL."""
        from .api.ml.create_proprietary_to_kcl import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_kcl_code_completions(self, *args, **kwargs) -> Any:
        """Generate code completions for KCL."""
        from .api.ml.create_kcl_code_completions import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_text_to_cad_iteration(self, *args, **kwargs) -> Any:
        """Iterate on a CAD model with a prompt."""
        from .api.ml.create_text_to_cad_iteration import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_text_to_cad_multi_file_iteration(self, *args, **kwargs) -> Any:
        """Iterate on a multi-file CAD model with a prompt."""
        from .api.ml.create_text_to_cad_multi_file_iteration import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def list_text_to_cad_models_for_user(self, *args, **kwargs) -> Any:
        """List text-to-CAD models you've generated."""
        from .api.ml.list_text_to_cad_models_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_text_to_cad_model_for_user(self, *args, **kwargs) -> Any:
        """Get a text-to-CAD response."""
        from .api.ml.get_text_to_cad_model_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_text_to_cad_model_feedback(self, *args, **kwargs) -> Any:
        """Give feedback to a specific ML response."""
        from .api.ml.create_text_to_cad_model_feedback import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def ml_copilot_ws(self, *args, **kwargs):
        """WebSocket connection for ml_copilot_ws

        Open a websocket to prompt the ML copilot.
        """

        # Import WebSocket wrapper class
        from .api.ml.ml_copilot_ws import WebSocket

        # Pass client directly to WebSocket constructor
        kwargs["client"] = self.client
        return WebSocket(*args, **kwargs)

    def ml_reasoning_ws(self, *args, **kwargs):
        """WebSocket connection for ml_reasoning_ws

        Open a websocket to prompt the ML copilot.
        """

        # Import WebSocket wrapper class
        from .api.ml.ml_reasoning_ws import WebSocket

        # Pass client directly to WebSocket constructor
        kwargs["client"] = self.client
        return WebSocket(*args, **kwargs)


class AsyncMlAPI:
    """Async API for ml endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def create_text_to_cad(self, *args, **kwargs) -> Any:
        """Generate a CAD model from text."""
        from .api.ml.create_text_to_cad import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def list_ml_prompts(self, *args, **kwargs) -> Any:
        """List all ML prompts."""
        from .api.ml.list_ml_prompts import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_ml_prompt(self, *args, **kwargs) -> Any:
        """Get a ML prompt."""
        from .api.ml.get_ml_prompt import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def list_conversations_for_user(self, *args, **kwargs) -> Any:
        """List conversations"""
        from .api.ml.list_conversations_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_proprietary_to_kcl(self, *args, **kwargs) -> Any:
        """Converts a proprietary CAD format to KCL."""
        from .api.ml.create_proprietary_to_kcl import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_kcl_code_completions(self, *args, **kwargs) -> Any:
        """Generate code completions for KCL."""
        from .api.ml.create_kcl_code_completions import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_text_to_cad_iteration(self, *args, **kwargs) -> Any:
        """Iterate on a CAD model with a prompt."""
        from .api.ml.create_text_to_cad_iteration import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_text_to_cad_multi_file_iteration(self, *args, **kwargs) -> Any:
        """Iterate on a multi-file CAD model with a prompt."""
        from .api.ml.create_text_to_cad_multi_file_iteration import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def list_text_to_cad_models_for_user(self, *args, **kwargs) -> Any:
        """List text-to-CAD models you've generated."""
        from .api.ml.list_text_to_cad_models_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_text_to_cad_model_for_user(self, *args, **kwargs) -> Any:
        """Get a text-to-CAD response."""
        from .api.ml.get_text_to_cad_model_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_text_to_cad_model_feedback(self, *args, **kwargs) -> Any:
        """Give feedback to a specific ML response."""
        from .api.ml.create_text_to_cad_model_feedback import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    def ml_copilot_ws(self, *args, **kwargs):
        """WebSocket connection for ml_copilot_ws (sync wrapper for async client)

        Open a websocket to prompt the ML copilot.

        Note: WebSocket connections are synchronous even in AsyncKittyCAD
        """

        # Import WebSocket wrapper class
        from .api.ml.ml_copilot_ws import WebSocket

        # Pass client directly to WebSocket constructor
        kwargs["client"] = self.client
        return WebSocket(*args, **kwargs)

    def ml_reasoning_ws(self, *args, **kwargs):
        """WebSocket connection for ml_reasoning_ws (sync wrapper for async client)

        Open a websocket to prompt the ML copilot.

        Note: WebSocket connections are synchronous even in AsyncKittyCAD
        """

        # Import WebSocket wrapper class
        from .api.ml.ml_reasoning_ws import WebSocket

        # Pass client directly to WebSocket constructor
        kwargs["client"] = self.client
        return WebSocket(*args, **kwargs)


class ApiCallsAPI:
    """API for api_calls endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_api_call_metrics(self, *args, **kwargs) -> Any:
        """Get API call metrics."""
        from .api.api_calls.get_api_call_metrics import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def list_api_calls(self, *args, **kwargs) -> Any:
        """List API calls."""
        from .api.api_calls.list_api_calls import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_api_call(self, *args, **kwargs) -> Any:
        """Get details of an API call."""
        from .api.api_calls.get_api_call import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def list_async_operations(self, *args, **kwargs) -> Any:
        """List async operations."""
        from .api.api_calls.list_async_operations import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_async_operation(self, *args, **kwargs) -> Any:
        """Get an async operation."""
        from .api.api_calls.get_async_operation import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def org_list_api_calls(self, *args, **kwargs) -> Any:
        """List API calls for your org."""
        from .api.api_calls.org_list_api_calls import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_api_call_for_org(self, *args, **kwargs) -> Any:
        """Get an API call for an org."""
        from .api.api_calls.get_api_call_for_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def user_list_api_calls(self, *args, **kwargs) -> Any:
        """List API calls for your user."""
        from .api.api_calls.user_list_api_calls import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_api_call_for_user(self, *args, **kwargs) -> Any:
        """Get an API call for a user."""
        from .api.api_calls.get_api_call_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def list_api_calls_for_user(self, *args, **kwargs) -> Any:
        """List API calls for a user."""
        from .api.api_calls.list_api_calls_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)


class AsyncApiCallsAPI:
    """Async API for api_calls endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def get_api_call_metrics(self, *args, **kwargs) -> Any:
        """Get API call metrics."""
        from .api.api_calls.get_api_call_metrics import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def list_api_calls(self, *args, **kwargs) -> Any:
        """List API calls."""
        from .api.api_calls.list_api_calls import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_api_call(self, *args, **kwargs) -> Any:
        """Get details of an API call."""
        from .api.api_calls.get_api_call import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def list_async_operations(self, *args, **kwargs) -> Any:
        """List async operations."""
        from .api.api_calls.list_async_operations import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_async_operation(self, *args, **kwargs) -> Any:
        """Get an async operation."""
        from .api.api_calls.get_async_operation import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def org_list_api_calls(self, *args, **kwargs) -> Any:
        """List API calls for your org."""
        from .api.api_calls.org_list_api_calls import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_api_call_for_org(self, *args, **kwargs) -> Any:
        """Get an API call for an org."""
        from .api.api_calls.get_api_call_for_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def user_list_api_calls(self, *args, **kwargs) -> Any:
        """List API calls for your user."""
        from .api.api_calls.user_list_api_calls import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_api_call_for_user(self, *args, **kwargs) -> Any:
        """Get an API call for a user."""
        from .api.api_calls.get_api_call_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def list_api_calls_for_user(self, *args, **kwargs) -> Any:
        """List API calls for a user."""
        from .api.api_calls.list_api_calls_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)


class AppsAPI:
    """API for apps endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def apps_github_callback(self, *args, **kwargs) -> Any:
        """Listen for callbacks to GitHub app authentication."""
        from .api.apps.apps_github_callback import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def apps_github_consent(self, *args, **kwargs) -> Any:
        """Get the consent URL for GitHub app authentication."""
        from .api.apps.apps_github_consent import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def apps_github_webhook(self, *args, **kwargs) -> Any:
        """Listen for GitHub webhooks."""
        from .api.apps.apps_github_webhook import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)


class AsyncAppsAPI:
    """Async API for apps endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def apps_github_callback(self, *args, **kwargs) -> Any:
        """Listen for callbacks to GitHub app authentication."""
        from .api.apps.apps_github_callback import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def apps_github_consent(self, *args, **kwargs) -> Any:
        """Get the consent URL for GitHub app authentication."""
        from .api.apps.apps_github_consent import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def apps_github_webhook(self, *args, **kwargs) -> Any:
        """Listen for GitHub webhooks."""
        from .api.apps.apps_github_webhook import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)


class HiddenAPI:
    """API for hidden endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def auth_api_key(self, *args, **kwargs) -> Any:
        """Authenticate using an api-key. This is disabled on production but can be used in dev to login without email magic."""
        from .api.hidden.auth_api_key import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def auth_email(self, *args, **kwargs) -> Any:
        """Create an email verification request for a user."""
        from .api.hidden.auth_email import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def auth_email_callback(self, *args, **kwargs) -> Any:
        """Listen for callbacks for email authentication for users."""
        from .api.hidden.auth_email_callback import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_auth_saml_by_org(self, *args, **kwargs) -> Any:
        """GET /auth/saml/{org_id}"""
        from .api.hidden.get_auth_saml_by_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_auth_saml(self, *args, **kwargs) -> Any:
        """Get a redirect straight to the SAML IdP."""
        from .api.hidden.get_auth_saml import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def post_auth_saml(self, *args, **kwargs) -> Any:
        """Authenticate a user via SAML"""
        from .api.hidden.post_auth_saml import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def logout(self, *args, **kwargs) -> Any:
        """This endpoint removes the session cookie for a user."""
        from .api.hidden.logout import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def redirect_user_shortlink(self, *args, **kwargs) -> Any:
        """Redirect the user to the URL for the shortlink."""
        from .api.hidden.redirect_user_shortlink import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)


class AsyncHiddenAPI:
    """Async API for hidden endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def auth_api_key(self, *args, **kwargs) -> Any:
        """Authenticate using an api-key. This is disabled on production but can be used in dev to login without email magic."""
        from .api.hidden.auth_api_key import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def auth_email(self, *args, **kwargs) -> Any:
        """Create an email verification request for a user."""
        from .api.hidden.auth_email import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def auth_email_callback(self, *args, **kwargs) -> Any:
        """Listen for callbacks for email authentication for users."""
        from .api.hidden.auth_email_callback import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_auth_saml_by_org(self, *args, **kwargs) -> Any:
        """GET /auth/saml/{org_id}"""
        from .api.hidden.get_auth_saml_by_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_auth_saml(self, *args, **kwargs) -> Any:
        """Get a redirect straight to the SAML IdP."""
        from .api.hidden.get_auth_saml import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def post_auth_saml(self, *args, **kwargs) -> Any:
        """Authenticate a user via SAML"""
        from .api.hidden.post_auth_saml import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def logout(self, *args, **kwargs) -> Any:
        """This endpoint removes the session cookie for a user."""
        from .api.hidden.logout import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def redirect_user_shortlink(self, *args, **kwargs) -> Any:
        """Redirect the user to the URL for the shortlink."""
        from .api.hidden.redirect_user_shortlink import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)


class FileAPI:
    """API for file endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def create_file_center_of_mass(self, *args, **kwargs) -> Any:
        """Get CAD file center of mass."""
        from .api.file.create_file_center_of_mass import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_file_conversion_options(self, *args, **kwargs) -> Any:
        """Convert CAD file from one format to another."""
        from .api.file.create_file_conversion_options import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_file_conversion(self, *args, **kwargs) -> Any:
        """Convert CAD file with defaults."""
        from .api.file.create_file_conversion import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_file_density(self, *args, **kwargs) -> Any:
        """Get CAD file density."""
        from .api.file.create_file_density import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_file_mass(self, *args, **kwargs) -> Any:
        """Get CAD file mass."""
        from .api.file.create_file_mass import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_file_surface_area(self, *args, **kwargs) -> Any:
        """Get CAD file surface area."""
        from .api.file.create_file_surface_area import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_file_volume(self, *args, **kwargs) -> Any:
        """Get CAD file volume."""
        from .api.file.create_file_volume import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)


class AsyncFileAPI:
    """Async API for file endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def create_file_center_of_mass(self, *args, **kwargs) -> Any:
        """Get CAD file center of mass."""
        from .api.file.create_file_center_of_mass import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_file_conversion_options(self, *args, **kwargs) -> Any:
        """Convert CAD file from one format to another."""
        from .api.file.create_file_conversion_options import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_file_conversion(self, *args, **kwargs) -> Any:
        """Convert CAD file with defaults."""
        from .api.file.create_file_conversion import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_file_density(self, *args, **kwargs) -> Any:
        """Get CAD file density."""
        from .api.file.create_file_density import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_file_mass(self, *args, **kwargs) -> Any:
        """Get CAD file mass."""
        from .api.file.create_file_mass import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_file_surface_area(self, *args, **kwargs) -> Any:
        """Get CAD file surface area."""
        from .api.file.create_file_surface_area import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_file_volume(self, *args, **kwargs) -> Any:
        """Get CAD file volume."""
        from .api.file.create_file_volume import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)


class ExecutorAPI:
    """API for executor endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def create_file_execution(self, *args, **kwargs) -> Any:
        """Execute a Zoo program in a specific language."""
        from .api.executor.create_file_execution import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_executor_term(self, *args, **kwargs):
        """WebSocket connection for create_executor_term

        Create a terminal.
        """

        # Use sync function for WebSocket endpoints without wrapper class
        from .api.executor.create_executor_term import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)


class AsyncExecutorAPI:
    """Async API for executor endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def create_file_execution(self, *args, **kwargs) -> Any:
        """Execute a Zoo program in a specific language."""
        from .api.executor.create_file_execution import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    def create_executor_term(self, *args, **kwargs):
        """WebSocket connection for create_executor_term (sync wrapper for async client)

        Create a terminal.

        Note: WebSocket connections are synchronous even in AsyncKittyCAD
        """

        # Use sync function for WebSocket endpoints without wrapper class
        from .api.executor.create_executor_term import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)


class Oauth2API:
    """API for oauth2 endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def device_auth_request(self, *args, **kwargs) -> Any:
        """Start an OAuth 2.0 Device Authorization Grant."""
        from .api.oauth2.device_auth_request import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def device_auth_confirm(self, *args, **kwargs) -> Any:
        """Confirm an OAuth 2.0 Device Authorization Grant."""
        from .api.oauth2.device_auth_confirm import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def device_access_token(self, *args, **kwargs) -> Any:
        """Request a device access token."""
        from .api.oauth2.device_access_token import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def device_auth_verify(self, *args, **kwargs) -> Any:
        """Verify an OAuth 2.0 Device Authorization Grant."""
        from .api.oauth2.device_auth_verify import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def oauth2_provider_callback(self, *args, **kwargs) -> Any:
        """Listen for callbacks for the OAuth 2.0 provider."""
        from .api.oauth2.oauth2_provider_callback import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def oauth2_provider_callback_post(self, *args, **kwargs) -> Any:
        """Listen for callbacks for the OAuth 2.0 provider."""
        from .api.oauth2.oauth2_provider_callback_post import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def oauth2_provider_consent(self, *args, **kwargs) -> Any:
        """Get the consent URL and other information for the OAuth 2.0 provider."""
        from .api.oauth2.oauth2_provider_consent import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def oauth2_token_revoke(self, *args, **kwargs) -> Any:
        """Revoke an OAuth2 token."""
        from .api.oauth2.oauth2_token_revoke import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)


class AsyncOauth2API:
    """Async API for oauth2 endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def device_auth_request(self, *args, **kwargs) -> Any:
        """Start an OAuth 2.0 Device Authorization Grant."""
        from .api.oauth2.device_auth_request import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def device_auth_confirm(self, *args, **kwargs) -> Any:
        """Confirm an OAuth 2.0 Device Authorization Grant."""
        from .api.oauth2.device_auth_confirm import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def device_access_token(self, *args, **kwargs) -> Any:
        """Request a device access token."""
        from .api.oauth2.device_access_token import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def device_auth_verify(self, *args, **kwargs) -> Any:
        """Verify an OAuth 2.0 Device Authorization Grant."""
        from .api.oauth2.device_auth_verify import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def oauth2_provider_callback(self, *args, **kwargs) -> Any:
        """Listen for callbacks for the OAuth 2.0 provider."""
        from .api.oauth2.oauth2_provider_callback import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def oauth2_provider_callback_post(self, *args, **kwargs) -> Any:
        """Listen for callbacks for the OAuth 2.0 provider."""
        from .api.oauth2.oauth2_provider_callback_post import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def oauth2_provider_consent(self, *args, **kwargs) -> Any:
        """Get the consent URL and other information for the OAuth 2.0 provider."""
        from .api.oauth2.oauth2_provider_consent import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def oauth2_token_revoke(self, *args, **kwargs) -> Any:
        """Revoke an OAuth2 token."""
        from .api.oauth2.oauth2_token_revoke import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)


class OrgsAPI:
    """API for orgs endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_org(self, *args, **kwargs) -> Any:
        """Get an org."""
        from .api.orgs.get_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def update_org(self, *args, **kwargs) -> Any:
        """Update an org."""
        from .api.orgs.update_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_org(self, *args, **kwargs) -> Any:
        """Create an org."""
        from .api.orgs.create_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def delete_org(self, *args, **kwargs) -> Any:
        """Delete an org."""
        from .api.orgs.delete_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def list_org_members(self, *args, **kwargs) -> Any:
        """List members of your org."""
        from .api.orgs.list_org_members import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_org_member(self, *args, **kwargs) -> Any:
        """Add a member to your org."""
        from .api.orgs.create_org_member import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_org_member(self, *args, **kwargs) -> Any:
        """Get a member of your org."""
        from .api.orgs.get_org_member import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def update_org_member(self, *args, **kwargs) -> Any:
        """Update a member of your org."""
        from .api.orgs.update_org_member import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def delete_org_member(self, *args, **kwargs) -> Any:
        """Remove a member from your org."""
        from .api.orgs.delete_org_member import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_org_privacy_settings(self, *args, **kwargs) -> Any:
        """Get the privacy settings for an org."""
        from .api.orgs.get_org_privacy_settings import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def update_org_privacy_settings(self, *args, **kwargs) -> Any:
        """Update the privacy settings for an org."""
        from .api.orgs.update_org_privacy_settings import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_org_saml_idp(self, *args, **kwargs) -> Any:
        """Get the SAML identity provider."""
        from .api.orgs.get_org_saml_idp import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def update_org_saml_idp(self, *args, **kwargs) -> Any:
        """Update the SAML identity provider."""
        from .api.orgs.update_org_saml_idp import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_org_saml_idp(self, *args, **kwargs) -> Any:
        """Create a SAML identity provider."""
        from .api.orgs.create_org_saml_idp import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def delete_org_saml_idp(self, *args, **kwargs) -> Any:
        """Delete an SAML identity provider."""
        from .api.orgs.delete_org_saml_idp import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_org_shortlinks(self, *args, **kwargs) -> Any:
        """Get the shortlinks for an org."""
        from .api.orgs.get_org_shortlinks import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def list_orgs(self, *args, **kwargs) -> Any:
        """List orgs."""
        from .api.orgs.list_orgs import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_any_org(self, *args, **kwargs) -> Any:
        """Get an org."""
        from .api.orgs.get_any_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def update_enterprise_pricing_for_org(self, *args, **kwargs) -> Any:
        """Set the enterprise price for an organization."""
        from .api.orgs.update_enterprise_pricing_for_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_user_org(self, *args, **kwargs) -> Any:
        """Get a user's org."""
        from .api.orgs.get_user_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)


class AsyncOrgsAPI:
    """Async API for orgs endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def get_org(self, *args, **kwargs) -> Any:
        """Get an org."""
        from .api.orgs.get_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def update_org(self, *args, **kwargs) -> Any:
        """Update an org."""
        from .api.orgs.update_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_org(self, *args, **kwargs) -> Any:
        """Create an org."""
        from .api.orgs.create_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def delete_org(self, *args, **kwargs) -> Any:
        """Delete an org."""
        from .api.orgs.delete_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def list_org_members(self, *args, **kwargs) -> Any:
        """List members of your org."""
        from .api.orgs.list_org_members import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_org_member(self, *args, **kwargs) -> Any:
        """Add a member to your org."""
        from .api.orgs.create_org_member import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_org_member(self, *args, **kwargs) -> Any:
        """Get a member of your org."""
        from .api.orgs.get_org_member import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def update_org_member(self, *args, **kwargs) -> Any:
        """Update a member of your org."""
        from .api.orgs.update_org_member import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def delete_org_member(self, *args, **kwargs) -> Any:
        """Remove a member from your org."""
        from .api.orgs.delete_org_member import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_org_privacy_settings(self, *args, **kwargs) -> Any:
        """Get the privacy settings for an org."""
        from .api.orgs.get_org_privacy_settings import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def update_org_privacy_settings(self, *args, **kwargs) -> Any:
        """Update the privacy settings for an org."""
        from .api.orgs.update_org_privacy_settings import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_org_saml_idp(self, *args, **kwargs) -> Any:
        """Get the SAML identity provider."""
        from .api.orgs.get_org_saml_idp import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def update_org_saml_idp(self, *args, **kwargs) -> Any:
        """Update the SAML identity provider."""
        from .api.orgs.update_org_saml_idp import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_org_saml_idp(self, *args, **kwargs) -> Any:
        """Create a SAML identity provider."""
        from .api.orgs.create_org_saml_idp import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def delete_org_saml_idp(self, *args, **kwargs) -> Any:
        """Delete an SAML identity provider."""
        from .api.orgs.delete_org_saml_idp import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_org_shortlinks(self, *args, **kwargs) -> Any:
        """Get the shortlinks for an org."""
        from .api.orgs.get_org_shortlinks import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def list_orgs(self, *args, **kwargs) -> Any:
        """List orgs."""
        from .api.orgs.list_orgs import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_any_org(self, *args, **kwargs) -> Any:
        """Get an org."""
        from .api.orgs.get_any_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def update_enterprise_pricing_for_org(self, *args, **kwargs) -> Any:
        """Set the enterprise price for an organization."""
        from .api.orgs.update_enterprise_pricing_for_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_user_org(self, *args, **kwargs) -> Any:
        """Get a user's org."""
        from .api.orgs.get_user_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)


class PaymentsAPI:
    """API for payments endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_payment_information_for_org(self, *args, **kwargs) -> Any:
        """Get payment info about your org."""
        from .api.payments.get_payment_information_for_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def update_payment_information_for_org(self, *args, **kwargs) -> Any:
        """Update payment info for your org."""
        from .api.payments.update_payment_information_for_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_payment_information_for_org(self, *args, **kwargs) -> Any:
        """Create payment info for your org."""
        from .api.payments.create_payment_information_for_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def delete_payment_information_for_org(self, *args, **kwargs) -> Any:
        """Delete payment info for your org."""
        from .api.payments.delete_payment_information_for_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_payment_balance_for_org(self, *args, **kwargs) -> Any:
        """Get balance for your org."""
        from .api.payments.get_payment_balance_for_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_payment_intent_for_org(self, *args, **kwargs) -> Any:
        """Create a payment intent for your org."""
        from .api.payments.create_payment_intent_for_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def list_invoices_for_org(self, *args, **kwargs) -> Any:
        """List invoices for your org."""
        from .api.payments.list_invoices_for_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def list_payment_methods_for_org(self, *args, **kwargs) -> Any:
        """List payment methods for your org."""
        from .api.payments.list_payment_methods_for_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def delete_payment_method_for_org(self, *args, **kwargs) -> Any:
        """Delete a payment method for your org."""
        from .api.payments.delete_payment_method_for_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_org_subscription(self, *args, **kwargs) -> Any:
        """Get the subscription for an org."""
        from .api.payments.get_org_subscription import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def update_org_subscription(self, *args, **kwargs) -> Any:
        """Update the subscription for an org."""
        from .api.payments.update_org_subscription import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_org_subscription(self, *args, **kwargs) -> Any:
        """Create the subscription for an org."""
        from .api.payments.create_org_subscription import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def validate_customer_tax_information_for_org(self, *args, **kwargs) -> Any:
        """Validate an orgs's information is correct and valid for automatic tax."""
        from .api.payments.validate_customer_tax_information_for_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_payment_balance_for_any_org(self, *args, **kwargs) -> Any:
        """Get balance for an org."""
        from .api.payments.get_payment_balance_for_any_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def update_payment_balance_for_any_org(self, *args, **kwargs) -> Any:
        """Update balance for an org."""
        from .api.payments.update_payment_balance_for_any_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_payment_information_for_user(self, *args, **kwargs) -> Any:
        """Get payment info about your user."""
        from .api.payments.get_payment_information_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def update_payment_information_for_user(self, *args, **kwargs) -> Any:
        """Update payment info for your user."""
        from .api.payments.update_payment_information_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_payment_information_for_user(self, *args, **kwargs) -> Any:
        """Create payment info for your user."""
        from .api.payments.create_payment_information_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def delete_payment_information_for_user(self, *args, **kwargs) -> Any:
        """Delete payment info for your user."""
        from .api.payments.delete_payment_information_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_payment_balance_for_user(self, *args, **kwargs) -> Any:
        """Get balance for your user."""
        from .api.payments.get_payment_balance_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_payment_intent_for_user(self, *args, **kwargs) -> Any:
        """Create a payment intent for your user."""
        from .api.payments.create_payment_intent_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def list_invoices_for_user(self, *args, **kwargs) -> Any:
        """List invoices for your user."""
        from .api.payments.list_invoices_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def list_payment_methods_for_user(self, *args, **kwargs) -> Any:
        """List payment methods for your user."""
        from .api.payments.list_payment_methods_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def delete_payment_method_for_user(self, *args, **kwargs) -> Any:
        """Delete a payment method for your user."""
        from .api.payments.delete_payment_method_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_user_subscription(self, *args, **kwargs) -> Any:
        """Get the subscription for a user."""
        from .api.payments.get_user_subscription import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def update_user_subscription(self, *args, **kwargs) -> Any:
        """Update the user's subscription."""
        from .api.payments.update_user_subscription import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_user_subscription(self, *args, **kwargs) -> Any:
        """Create the subscription for a user."""
        from .api.payments.create_user_subscription import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def validate_customer_tax_information_for_user(self, *args, **kwargs) -> Any:
        """Validate a user's information is correct and valid for automatic tax."""
        from .api.payments.validate_customer_tax_information_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_payment_balance_for_any_user(self, *args, **kwargs) -> Any:
        """Get balance for an user."""
        from .api.payments.get_payment_balance_for_any_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def update_payment_balance_for_any_user(self, *args, **kwargs) -> Any:
        """Update balance for an user."""
        from .api.payments.update_payment_balance_for_any_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)


class AsyncPaymentsAPI:
    """Async API for payments endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def get_payment_information_for_org(self, *args, **kwargs) -> Any:
        """Get payment info about your org."""
        from .api.payments.get_payment_information_for_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def update_payment_information_for_org(self, *args, **kwargs) -> Any:
        """Update payment info for your org."""
        from .api.payments.update_payment_information_for_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_payment_information_for_org(self, *args, **kwargs) -> Any:
        """Create payment info for your org."""
        from .api.payments.create_payment_information_for_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def delete_payment_information_for_org(self, *args, **kwargs) -> Any:
        """Delete payment info for your org."""
        from .api.payments.delete_payment_information_for_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_payment_balance_for_org(self, *args, **kwargs) -> Any:
        """Get balance for your org."""
        from .api.payments.get_payment_balance_for_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_payment_intent_for_org(self, *args, **kwargs) -> Any:
        """Create a payment intent for your org."""
        from .api.payments.create_payment_intent_for_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def list_invoices_for_org(self, *args, **kwargs) -> Any:
        """List invoices for your org."""
        from .api.payments.list_invoices_for_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def list_payment_methods_for_org(self, *args, **kwargs) -> Any:
        """List payment methods for your org."""
        from .api.payments.list_payment_methods_for_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def delete_payment_method_for_org(self, *args, **kwargs) -> Any:
        """Delete a payment method for your org."""
        from .api.payments.delete_payment_method_for_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_org_subscription(self, *args, **kwargs) -> Any:
        """Get the subscription for an org."""
        from .api.payments.get_org_subscription import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def update_org_subscription(self, *args, **kwargs) -> Any:
        """Update the subscription for an org."""
        from .api.payments.update_org_subscription import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_org_subscription(self, *args, **kwargs) -> Any:
        """Create the subscription for an org."""
        from .api.payments.create_org_subscription import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def validate_customer_tax_information_for_org(self, *args, **kwargs) -> Any:
        """Validate an orgs's information is correct and valid for automatic tax."""
        from .api.payments.validate_customer_tax_information_for_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_payment_balance_for_any_org(self, *args, **kwargs) -> Any:
        """Get balance for an org."""
        from .api.payments.get_payment_balance_for_any_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def update_payment_balance_for_any_org(self, *args, **kwargs) -> Any:
        """Update balance for an org."""
        from .api.payments.update_payment_balance_for_any_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_payment_information_for_user(self, *args, **kwargs) -> Any:
        """Get payment info about your user."""
        from .api.payments.get_payment_information_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def update_payment_information_for_user(self, *args, **kwargs) -> Any:
        """Update payment info for your user."""
        from .api.payments.update_payment_information_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_payment_information_for_user(self, *args, **kwargs) -> Any:
        """Create payment info for your user."""
        from .api.payments.create_payment_information_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def delete_payment_information_for_user(self, *args, **kwargs) -> Any:
        """Delete payment info for your user."""
        from .api.payments.delete_payment_information_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_payment_balance_for_user(self, *args, **kwargs) -> Any:
        """Get balance for your user."""
        from .api.payments.get_payment_balance_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_payment_intent_for_user(self, *args, **kwargs) -> Any:
        """Create a payment intent for your user."""
        from .api.payments.create_payment_intent_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def list_invoices_for_user(self, *args, **kwargs) -> Any:
        """List invoices for your user."""
        from .api.payments.list_invoices_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def list_payment_methods_for_user(self, *args, **kwargs) -> Any:
        """List payment methods for your user."""
        from .api.payments.list_payment_methods_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def delete_payment_method_for_user(self, *args, **kwargs) -> Any:
        """Delete a payment method for your user."""
        from .api.payments.delete_payment_method_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_user_subscription(self, *args, **kwargs) -> Any:
        """Get the subscription for a user."""
        from .api.payments.get_user_subscription import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def update_user_subscription(self, *args, **kwargs) -> Any:
        """Update the user's subscription."""
        from .api.payments.update_user_subscription import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_user_subscription(self, *args, **kwargs) -> Any:
        """Create the subscription for a user."""
        from .api.payments.create_user_subscription import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def validate_customer_tax_information_for_user(self, *args, **kwargs) -> Any:
        """Validate a user's information is correct and valid for automatic tax."""
        from .api.payments.validate_customer_tax_information_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_payment_balance_for_any_user(self, *args, **kwargs) -> Any:
        """Get balance for an user."""
        from .api.payments.get_payment_balance_for_any_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def update_payment_balance_for_any_user(self, *args, **kwargs) -> Any:
        """Update balance for an user."""
        from .api.payments.update_payment_balance_for_any_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)


class ServiceAccountsAPI:
    """API for service_accounts endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def list_service_accounts_for_org(self, *args, **kwargs) -> Any:
        """List service accounts for your org."""
        from .api.service_accounts.list_service_accounts_for_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_service_account_for_org(self, *args, **kwargs) -> Any:
        """Create a new service account for your org."""
        from .api.service_accounts.create_service_account_for_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_service_account_for_org(self, *args, **kwargs) -> Any:
        """Get an service account for your org."""
        from .api.service_accounts.get_service_account_for_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def delete_service_account_for_org(self, *args, **kwargs) -> Any:
        """Delete an service account for your org."""
        from .api.service_accounts.delete_service_account_for_org import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)


class AsyncServiceAccountsAPI:
    """Async API for service_accounts endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def list_service_accounts_for_org(self, *args, **kwargs) -> Any:
        """List service accounts for your org."""
        from .api.service_accounts.list_service_accounts_for_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_service_account_for_org(self, *args, **kwargs) -> Any:
        """Create a new service account for your org."""
        from .api.service_accounts.create_service_account_for_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_service_account_for_org(self, *args, **kwargs) -> Any:
        """Get an service account for your org."""
        from .api.service_accounts.get_service_account_for_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def delete_service_account_for_org(self, *args, **kwargs) -> Any:
        """Delete an service account for your org."""
        from .api.service_accounts.delete_service_account_for_org import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)


class StoreAPI:
    """API for store endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def create_store_coupon(self, *args, **kwargs) -> Any:
        """Create a new store coupon."""
        from .api.store.create_store_coupon import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)


class AsyncStoreAPI:
    """Async API for store endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def create_store_coupon(self, *args, **kwargs) -> Any:
        """Create a new store coupon."""
        from .api.store.create_store_coupon import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)


class UnitAPI:
    """API for unit endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_angle_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert angle units."""
        from .api.unit.get_angle_unit_conversion import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_area_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert area units."""
        from .api.unit.get_area_unit_conversion import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_current_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert current units."""
        from .api.unit.get_current_unit_conversion import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_energy_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert energy units."""
        from .api.unit.get_energy_unit_conversion import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_force_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert force units."""
        from .api.unit.get_force_unit_conversion import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_frequency_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert frequency units."""
        from .api.unit.get_frequency_unit_conversion import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_length_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert length units."""
        from .api.unit.get_length_unit_conversion import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_mass_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert mass units."""
        from .api.unit.get_mass_unit_conversion import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_power_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert power units."""
        from .api.unit.get_power_unit_conversion import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_pressure_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert pressure units."""
        from .api.unit.get_pressure_unit_conversion import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_temperature_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert temperature units."""
        from .api.unit.get_temperature_unit_conversion import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_torque_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert torque units."""
        from .api.unit.get_torque_unit_conversion import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_volume_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert volume units."""
        from .api.unit.get_volume_unit_conversion import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)


class AsyncUnitAPI:
    """Async API for unit endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def get_angle_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert angle units."""
        from .api.unit.get_angle_unit_conversion import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_area_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert area units."""
        from .api.unit.get_area_unit_conversion import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_current_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert current units."""
        from .api.unit.get_current_unit_conversion import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_energy_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert energy units."""
        from .api.unit.get_energy_unit_conversion import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_force_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert force units."""
        from .api.unit.get_force_unit_conversion import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_frequency_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert frequency units."""
        from .api.unit.get_frequency_unit_conversion import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_length_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert length units."""
        from .api.unit.get_length_unit_conversion import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_mass_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert mass units."""
        from .api.unit.get_mass_unit_conversion import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_power_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert power units."""
        from .api.unit.get_power_unit_conversion import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_pressure_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert pressure units."""
        from .api.unit.get_pressure_unit_conversion import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_temperature_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert temperature units."""
        from .api.unit.get_temperature_unit_conversion import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_torque_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert torque units."""
        from .api.unit.get_torque_unit_conversion import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_volume_unit_conversion(self, *args, **kwargs) -> Any:
        """Convert volume units."""
        from .api.unit.get_volume_unit_conversion import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)


class UsersAPI:
    """API for users endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_user_self(self, *args, **kwargs) -> Any:
        """Get your user."""
        from .api.users.get_user_self import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def update_user_self(self, *args, **kwargs) -> Any:
        """Update your user."""
        from .api.users.update_user_self import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def delete_user_self(self, *args, **kwargs) -> Any:
        """Delete your user."""
        from .api.users.delete_user_self import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def patch_user_crm(self, *args, **kwargs) -> Any:
        """Update properties in the CRM"""
        from .api.users.patch_user_crm import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_user_self_extended(self, *args, **kwargs) -> Any:
        """Get extended information about your user."""
        from .api.users.get_user_self_extended import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def put_user_form_self(self, *args, **kwargs) -> Any:
        """Create a new support/sales ticket from the website contact form. This endpoint is authenticated."""
        from .api.users.put_user_form_self import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_oauth2_providers_for_user(self, *args, **kwargs) -> Any:
        """Get the OAuth2 providers for your user."""
        from .api.users.get_oauth2_providers_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_user_privacy_settings(self, *args, **kwargs) -> Any:
        """Get the privacy settings for a user."""
        from .api.users.get_user_privacy_settings import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def update_user_privacy_settings(self, *args, **kwargs) -> Any:
        """Update the user's privacy settings."""
        from .api.users.update_user_privacy_settings import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_session_for_user(self, *args, **kwargs) -> Any:
        """Get a session for your user."""
        from .api.users.get_session_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_user_shortlinks(self, *args, **kwargs) -> Any:
        """Get the shortlinks for a user."""
        from .api.users.get_user_shortlinks import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_user_shortlink(self, *args, **kwargs) -> Any:
        """Create a shortlink for a user."""
        from .api.users.create_user_shortlink import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def update_user_shortlink(self, *args, **kwargs) -> Any:
        """Update a shortlink for a user."""
        from .api.users.update_user_shortlink import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def delete_user_shortlink(self, *args, **kwargs) -> Any:
        """Delete a shortlink for a user."""
        from .api.users.delete_user_shortlink import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def list_users(self, *args, **kwargs) -> Any:
        """List users."""
        from .api.users.list_users import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def list_users_extended(self, *args, **kwargs) -> Any:
        """List users with extended information."""
        from .api.users.list_users_extended import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_user_extended(self, *args, **kwargs) -> Any:
        """Get extended information about a user."""
        from .api.users.get_user_extended import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_user(self, *args, **kwargs) -> Any:
        """Get a user."""
        from .api.users.get_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def update_subscription_for_user(self, *args, **kwargs) -> Any:
        """Update a subscription for a user."""
        from .api.users.update_subscription_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def put_public_form(self, *args, **kwargs) -> Any:
        """Creates a new support/sales ticket from the website contact form. This endpoint is for untrusted"""
        from .api.users.put_public_form import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def put_public_subscribe(self, *args, **kwargs) -> Any:
        """Subscribes a user to the newsletter."""
        from .api.users.put_public_subscribe import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)


class AsyncUsersAPI:
    """Async API for users endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def get_user_self(self, *args, **kwargs) -> Any:
        """Get your user."""
        from .api.users.get_user_self import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def update_user_self(self, *args, **kwargs) -> Any:
        """Update your user."""
        from .api.users.update_user_self import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def delete_user_self(self, *args, **kwargs) -> Any:
        """Delete your user."""
        from .api.users.delete_user_self import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def patch_user_crm(self, *args, **kwargs) -> Any:
        """Update properties in the CRM"""
        from .api.users.patch_user_crm import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_user_self_extended(self, *args, **kwargs) -> Any:
        """Get extended information about your user."""
        from .api.users.get_user_self_extended import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def put_user_form_self(self, *args, **kwargs) -> Any:
        """Create a new support/sales ticket from the website contact form. This endpoint is authenticated."""
        from .api.users.put_user_form_self import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_oauth2_providers_for_user(self, *args, **kwargs) -> Any:
        """Get the OAuth2 providers for your user."""
        from .api.users.get_oauth2_providers_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_user_privacy_settings(self, *args, **kwargs) -> Any:
        """Get the privacy settings for a user."""
        from .api.users.get_user_privacy_settings import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def update_user_privacy_settings(self, *args, **kwargs) -> Any:
        """Update the user's privacy settings."""
        from .api.users.update_user_privacy_settings import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_session_for_user(self, *args, **kwargs) -> Any:
        """Get a session for your user."""
        from .api.users.get_session_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_user_shortlinks(self, *args, **kwargs) -> Any:
        """Get the shortlinks for a user."""
        from .api.users.get_user_shortlinks import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_user_shortlink(self, *args, **kwargs) -> Any:
        """Create a shortlink for a user."""
        from .api.users.create_user_shortlink import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def update_user_shortlink(self, *args, **kwargs) -> Any:
        """Update a shortlink for a user."""
        from .api.users.update_user_shortlink import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def delete_user_shortlink(self, *args, **kwargs) -> Any:
        """Delete a shortlink for a user."""
        from .api.users.delete_user_shortlink import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def list_users(self, *args, **kwargs) -> Any:
        """List users."""
        from .api.users.list_users import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def list_users_extended(self, *args, **kwargs) -> Any:
        """List users with extended information."""
        from .api.users.list_users_extended import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_user_extended(self, *args, **kwargs) -> Any:
        """Get extended information about a user."""
        from .api.users.get_user_extended import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_user(self, *args, **kwargs) -> Any:
        """Get a user."""
        from .api.users.get_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def update_subscription_for_user(self, *args, **kwargs) -> Any:
        """Update a subscription for a user."""
        from .api.users.update_subscription_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def put_public_form(self, *args, **kwargs) -> Any:
        """Creates a new support/sales ticket from the website contact form. This endpoint is for untrusted"""
        from .api.users.put_public_form import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def put_public_subscribe(self, *args, **kwargs) -> Any:
        """Subscribes a user to the newsletter."""
        from .api.users.put_public_subscribe import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)


class ApiTokensAPI:
    """API for api_tokens endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def list_api_tokens_for_user(self, *args, **kwargs) -> Any:
        """List API tokens for your user."""
        from .api.api_tokens.list_api_tokens_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def create_api_token_for_user(self, *args, **kwargs) -> Any:
        """Create a new API token for your user."""
        from .api.api_tokens.create_api_token_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def get_api_token_for_user(self, *args, **kwargs) -> Any:
        """Get an API token for your user."""
        from .api.api_tokens.get_api_token_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)

    def delete_api_token_for_user(self, *args, **kwargs) -> Any:
        """Delete an API token for your user."""
        from .api.api_tokens.delete_api_token_for_user import sync

        kwargs["client"] = self.client
        return sync(*args, **kwargs)


class AsyncApiTokensAPI:
    """Async API for api_tokens endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def list_api_tokens_for_user(self, *args, **kwargs) -> Any:
        """List API tokens for your user."""
        from .api.api_tokens.list_api_tokens_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def create_api_token_for_user(self, *args, **kwargs) -> Any:
        """Create a new API token for your user."""
        from .api.api_tokens.create_api_token_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def get_api_token_for_user(self, *args, **kwargs) -> Any:
        """Get an API token for your user."""
        from .api.api_tokens.get_api_token_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)

    async def delete_api_token_for_user(self, *args, **kwargs) -> Any:
        """Delete an API token for your user."""
        from .api.api_tokens.delete_api_token_for_user import asyncio

        kwargs["client"] = self.client
        return await asyncio(*args, **kwargs)


class ModelingAPI:
    """API for modeling endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def modeling_commands_ws(self, *args, **kwargs):
        """WebSocket connection for modeling_commands_ws

        Open a websocket which accepts modeling commands.
        """

        # Import WebSocket wrapper class
        from .api.modeling.modeling_commands_ws import WebSocket

        # Pass client directly to WebSocket constructor
        kwargs["client"] = self.client
        return WebSocket(*args, **kwargs)


class AsyncModelingAPI:
    """Async API for modeling endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def modeling_commands_ws(self, *args, **kwargs):
        """WebSocket connection for modeling_commands_ws (sync wrapper for async client)

        Open a websocket which accepts modeling commands.

        Note: WebSocket connections are synchronous even in AsyncKittyCAD
        """

        # Import WebSocket wrapper class
        from .api.modeling.modeling_commands_ws import WebSocket

        # Pass client directly to WebSocket constructor
        kwargs["client"] = self.client
        return WebSocket(*args, **kwargs)


class KittyCAD(Client):
    """Main KittyCAD client class with sync API interface.

    Usage:
        client = KittyCAD(token="your-api-token")
        user = client.users.get_user_self()

    Or with environment variable:
        client = KittyCAD()  # Uses KITTYCAD_API_TOKEN or ZOO_API_TOKEN
    """

    def __init__(self, token: Optional[str] = None, **kwargs) -> None:
        if token is None:
            token = os.getenv("KITTYCAD_API_TOKEN") or os.getenv("ZOO_API_TOKEN")
            if token is None:
                raise ValueError(
                    "No API token provided. Either pass token parameter or set "
                    "KITTYCAD_API_TOKEN or ZOO_API_TOKEN environment variable."
                )
        super().__init__(token=token, **kwargs)
        # Add API modules directly to client

        self.meta: MetaAPI = MetaAPI(self)

        self.ml: MlAPI = MlAPI(self)

        self.api_calls: ApiCallsAPI = ApiCallsAPI(self)

        self.apps: AppsAPI = AppsAPI(self)

        self.hidden: HiddenAPI = HiddenAPI(self)

        self.file: FileAPI = FileAPI(self)

        self.executor: ExecutorAPI = ExecutorAPI(self)

        self.oauth2: Oauth2API = Oauth2API(self)

        self.orgs: OrgsAPI = OrgsAPI(self)

        self.payments: PaymentsAPI = PaymentsAPI(self)

        self.service_accounts: ServiceAccountsAPI = ServiceAccountsAPI(self)

        self.store: StoreAPI = StoreAPI(self)

        self.unit: UnitAPI = UnitAPI(self)

        self.users: UsersAPI = UsersAPI(self)

        self.api_tokens: ApiTokensAPI = ApiTokensAPI(self)

        self.modeling: ModelingAPI = ModelingAPI(self)


class AsyncKittyCAD(Client):
    """Async KittyCAD client class with async API interface.

    Usage:
        import asyncio
        from kittycad import AsyncKittyCAD

        async def main():
            client = AsyncKittyCAD(token="your-api-token")
            user = await client.users.get_user_self()

        asyncio.run(main())

    Or with environment variable:
        client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN or ZOO_API_TOKEN
    """

    def __init__(self, token: Optional[str] = None, **kwargs) -> None:
        if token is None:
            token = os.getenv("KITTYCAD_API_TOKEN") or os.getenv("ZOO_API_TOKEN")
            if token is None:
                raise ValueError(
                    "No API token provided. Either pass token parameter or set "
                    "KITTYCAD_API_TOKEN or ZOO_API_TOKEN environment variable."
                )
        super().__init__(token=token, **kwargs)
        # Add async API modules directly to client

        self.meta: AsyncMetaAPI = AsyncMetaAPI(self)

        self.ml: AsyncMlAPI = AsyncMlAPI(self)

        self.api_calls: AsyncApiCallsAPI = AsyncApiCallsAPI(self)

        self.apps: AsyncAppsAPI = AsyncAppsAPI(self)

        self.hidden: AsyncHiddenAPI = AsyncHiddenAPI(self)

        self.file: AsyncFileAPI = AsyncFileAPI(self)

        self.executor: AsyncExecutorAPI = AsyncExecutorAPI(self)

        self.oauth2: AsyncOauth2API = AsyncOauth2API(self)

        self.orgs: AsyncOrgsAPI = AsyncOrgsAPI(self)

        self.payments: AsyncPaymentsAPI = AsyncPaymentsAPI(self)

        self.service_accounts: AsyncServiceAccountsAPI = AsyncServiceAccountsAPI(self)

        self.store: AsyncStoreAPI = AsyncStoreAPI(self)

        self.unit: AsyncUnitAPI = AsyncUnitAPI(self)

        self.users: AsyncUsersAPI = AsyncUsersAPI(self)

        self.api_tokens: AsyncApiTokensAPI = AsyncApiTokensAPI(self)

        self.modeling: AsyncModelingAPI = AsyncModelingAPI(self)


__all__ = [
    "KittyCAD",
    "AsyncKittyCAD",
    "KittyCADError",
    "KittyCADAPIError",
    "KittyCADClientError",
    "KittyCADServerError",
    "KittyCADConnectionError",
    "KittyCADTimeoutError",
]
