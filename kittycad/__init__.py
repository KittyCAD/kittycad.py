"""The KittyCAD Python SDK - Generated Client Classes"""

import json
import os
from typing import Any, Dict, List, Optional, Union

import bson
import httpx
from websockets.asyncio.client import (
    ClientConnection as ClientConnectionAsync,
    connect as ws_connect_async,
)
from websockets.sync.client import (
    ClientConnection as ClientConnectionSync,
    connect as ws_connect,
)

from .client import Client
from .exceptions import (
    KittyCADAPIError,
    KittyCADClientError,
    KittyCADConnectionError,
    KittyCADError,
    KittyCADServerError,
    KittyCADTimeoutError,
)

# Import model types
from .models.account_provider import AccountProvider
from .models.add_org_member import AddOrgMember
from .models.api_call_query_group import ApiCallQueryGroup
from .models.api_call_query_group_by import ApiCallQueryGroupBy
from .models.api_call_status import ApiCallStatus
from .models.api_call_with_price import ApiCallWithPrice
from .models.api_call_with_price_results_page import ApiCallWithPriceResultsPage
from .models.api_token import ApiToken
from .models.api_token_results_page import ApiTokenResultsPage
from .models.api_token_uuid import ApiTokenUuid
from .models.app_client_info import AppClientInfo
from .models.async_api_call_results_page import AsyncApiCallResultsPage
from .models.auth_api_key_response import AuthApiKeyResponse
from .models.billing_info import BillingInfo
from .models.code_language import CodeLanguage
from .models.code_option import CodeOption
from .models.code_output import CodeOutput
from .models.conversation_results_page import ConversationResultsPage
from .models.conversion_params import ConversionParams
from .models.create_shortlink_request import CreateShortlinkRequest
from .models.create_shortlink_response import CreateShortlinkResponse
from .models.created_at_sort_mode import CreatedAtSortMode
from .models.crm_data import CrmData
from .models.customer import Customer
from .models.customer_balance import CustomerBalance
from .models.discount_code import DiscountCode
from .models.email_authentication_form import EmailAuthenticationForm
from .models.enterprise_subscription_tier_price import EnterpriseSubscriptionTierPrice
from .models.event import Event
from .models.extended_user import ExtendedUser
from .models.extended_user_results_page import ExtendedUserResultsPage
from .models.file_center_of_mass import FileCenterOfMass
from .models.file_conversion import FileConversion
from .models.file_density import FileDensity
from .models.file_export_format import FileExportFormat
from .models.file_import_format import FileImportFormat
from .models.file_mass import FileMass
from .models.file_surface_area import FileSurfaceArea
from .models.file_volume import FileVolume
from .models.inquiry_form import InquiryForm
from .models.invoice import Invoice
from .models.ip_addr_info import IpAddrInfo
from .models.kcl_code_completion_request import KclCodeCompletionRequest
from .models.kcl_code_completion_response import KclCodeCompletionResponse
from .models.kcl_model import KclModel
from .models.ml_copilot_client_message import MlCopilotClientMessage
from .models.ml_copilot_server_message import MlCopilotServerMessage
from .models.ml_feedback import MlFeedback
from .models.ml_prompt import MlPrompt
from .models.ml_prompt_results_page import MlPromptResultsPage
from .models.org import Org
from .models.org_details import OrgDetails
from .models.org_member import OrgMember
from .models.org_member_results_page import OrgMemberResultsPage
from .models.org_results_page import OrgResultsPage
from .models.payment_intent import PaymentIntent
from .models.payment_method import PaymentMethod
from .models.pong import Pong
from .models.post_effect_type import PostEffectType
from .models.privacy_settings import PrivacySettings
from .models.saml_identity_provider import SamlIdentityProvider
from .models.saml_identity_provider_create import SamlIdentityProviderCreate
from .models.service_account import ServiceAccount
from .models.service_account_results_page import ServiceAccountResultsPage
from .models.service_account_uuid import ServiceAccountUuid
from .models.session import Session
from .models.session_uuid import SessionUuid
from .models.shortlink_results_page import ShortlinkResultsPage
from .models.store_coupon_params import StoreCouponParams
from .models.subscribe import Subscribe
from .models.text_to_cad import TextToCad
from .models.text_to_cad_create_body import TextToCadCreateBody
from .models.text_to_cad_iteration import TextToCadIteration
from .models.text_to_cad_iteration_body import TextToCadIterationBody
from .models.text_to_cad_multi_file_iteration import TextToCadMultiFileIteration
from .models.text_to_cad_multi_file_iteration_body import (
    TextToCadMultiFileIterationBody,
)
from .models.text_to_cad_response import TextToCadResponse
from .models.text_to_cad_response_results_page import TextToCadResponseResultsPage
from .models.unit_angle import UnitAngle
from .models.unit_angle_conversion import UnitAngleConversion
from .models.unit_area import UnitArea
from .models.unit_area_conversion import UnitAreaConversion
from .models.unit_current import UnitCurrent
from .models.unit_current_conversion import UnitCurrentConversion
from .models.unit_density import UnitDensity
from .models.unit_energy import UnitEnergy
from .models.unit_energy_conversion import UnitEnergyConversion
from .models.unit_force import UnitForce
from .models.unit_force_conversion import UnitForceConversion
from .models.unit_frequency import UnitFrequency
from .models.unit_frequency_conversion import UnitFrequencyConversion
from .models.unit_length import UnitLength
from .models.unit_length_conversion import UnitLengthConversion
from .models.unit_mass import UnitMass
from .models.unit_mass_conversion import UnitMassConversion
from .models.unit_power import UnitPower
from .models.unit_power_conversion import UnitPowerConversion
from .models.unit_pressure import UnitPressure
from .models.unit_pressure_conversion import UnitPressureConversion
from .models.unit_temperature import UnitTemperature
from .models.unit_temperature_conversion import UnitTemperatureConversion
from .models.unit_torque import UnitTorque
from .models.unit_torque_conversion import UnitTorqueConversion
from .models.unit_volume import UnitVolume
from .models.unit_volume_conversion import UnitVolumeConversion
from .models.update_member_to_org_body import UpdateMemberToOrgBody
from .models.update_payment_balance import UpdatePaymentBalance
from .models.update_shortlink_request import UpdateShortlinkRequest
from .models.update_user import UpdateUser
from .models.user import User
from .models.user_identifier import UserIdentifier
from .models.user_org_info import UserOrgInfo
from .models.user_org_role import UserOrgRole
from .models.user_results_page import UserResultsPage
from .models.uuid import Uuid
from .models.verification_token_response import VerificationTokenResponse
from .models.web_socket_request import WebSocketRequest
from .models.web_socket_response import WebSocketResponse
from .models.zoo_product_subscriptions import ZooProductSubscriptions
from .models.zoo_product_subscriptions_org_request import (
    ZooProductSubscriptionsOrgRequest,
)
from .models.zoo_product_subscriptions_user_request import (
    ZooProductSubscriptionsUserRequest,
)
from .response_helpers import raise_for_status
from .types import Response

# Import WebSocket request/response models


class MetaAPI:
    """API for meta endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_schema(self) -> Any:
        """Get OpenAPI schema."""
        from .api.meta.get_schema import sync

        return sync(client=self.client)

    def get_ipinfo(self) -> Any:
        """Get ip address information."""
        from .api.meta.get_ipinfo import sync

        return sync(client=self.client)

    def community_sso(self) -> Any:
        """Authorize an inbound auth request from our Community page."""
        from .api.meta.community_sso import sync

        return sync(client=self.client)

    def create_debug_uploads(self) -> Any:
        """Uploads files to public blob storage for debugging purposes."""
        from .api.meta.create_debug_uploads import sync

        return sync(client=self.client)

    def create_event(self) -> Any:
        """Creates an internal telemetry event."""
        from .api.meta.create_event import sync

        return sync(client=self.client)

    def internal_get_api_token_for_discord_user(self) -> Any:
        """Get an API token for a user by their discord id."""
        from .api.meta.internal_get_api_token_for_discord_user import sync

        return sync(client=self.client)

    def ping(self) -> Any:
        """Return pong."""
        from .api.meta.ping import sync

        return sync(client=self.client)

    def get_pricing_subscriptions(self) -> Any:
        """Get the pricing for our subscriptions."""
        from .api.meta.get_pricing_subscriptions import sync

        return sync(client=self.client)


class AsyncMetaAPI:
    """Async API for meta endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def get_schema(self) -> Any:
        """Get OpenAPI schema."""
        from .api.meta.get_schema import asyncio

        return await asyncio(client=self.client)

    async def get_ipinfo(self) -> Any:
        """Get ip address information."""
        from .api.meta.get_ipinfo import asyncio

        return await asyncio(client=self.client)

    async def community_sso(self) -> Any:
        """Authorize an inbound auth request from our Community page."""
        from .api.meta.community_sso import asyncio

        return await asyncio(client=self.client)

    async def create_debug_uploads(self) -> Any:
        """Uploads files to public blob storage for debugging purposes."""
        from .api.meta.create_debug_uploads import asyncio

        return await asyncio(client=self.client)

    async def create_event(self) -> Any:
        """Creates an internal telemetry event."""
        from .api.meta.create_event import asyncio

        return await asyncio(client=self.client)

    async def internal_get_api_token_for_discord_user(self) -> Any:
        """Get an API token for a user by their discord id."""
        from .api.meta.internal_get_api_token_for_discord_user import asyncio

        return await asyncio(client=self.client)

    async def ping(self) -> Any:
        """Return pong."""
        from .api.meta.ping import asyncio

        return await asyncio(client=self.client)

    async def get_pricing_subscriptions(self) -> Any:
        """Get the pricing for our subscriptions."""
        from .api.meta.get_pricing_subscriptions import asyncio

        return await asyncio(client=self.client)


class MlAPI:
    """API for ml endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def create_text_to_cad(self) -> Any:
        """Generate a CAD model from text."""
        from .api.ml.create_text_to_cad import sync

        return sync(client=self.client)

    def list_ml_prompts(self) -> Any:
        """List all ML prompts."""
        from .api.ml.list_ml_prompts import sync

        return sync(client=self.client)

    def get_ml_prompt(self) -> Any:
        """Get a ML prompt."""
        from .api.ml.get_ml_prompt import sync

        return sync(client=self.client)

    def list_conversations_for_user(self) -> Any:
        """List conversations"""
        from .api.ml.list_conversations_for_user import sync

        return sync(client=self.client)

    def create_proprietary_to_kcl(self) -> Any:
        """Converts a proprietary CAD format to KCL."""
        from .api.ml.create_proprietary_to_kcl import sync

        return sync(client=self.client)

    def create_kcl_code_completions(self) -> Any:
        """Generate code completions for KCL."""
        from .api.ml.create_kcl_code_completions import sync

        return sync(client=self.client)

    def create_text_to_cad_iteration(self) -> Any:
        """Iterate on a CAD model with a prompt."""
        from .api.ml.create_text_to_cad_iteration import sync

        return sync(client=self.client)

    def create_text_to_cad_multi_file_iteration(self) -> Any:
        """Iterate on a multi-file CAD model with a prompt."""
        from .api.ml.create_text_to_cad_multi_file_iteration import sync

        return sync(client=self.client)

    def list_text_to_cad_models_for_user(self) -> Any:
        """List text-to-CAD models you've generated."""
        from .api.ml.list_text_to_cad_models_for_user import sync

        return sync(client=self.client)

    def get_text_to_cad_model_for_user(self) -> Any:
        """Get a text-to-CAD response."""
        from .api.ml.get_text_to_cad_model_for_user import sync

        return sync(client=self.client)

    def create_text_to_cad_model_feedback(self) -> Any:
        """Give feedback to a specific ML response."""
        from .api.ml.create_text_to_cad_model_feedback import sync

        return sync(client=self.client)

    def ml_copilot_ws(self) -> "WebSocketMlCopilotWs":
        """Open a websocket to prompt the ML copilot.

        Returns a WebSocket wrapper with methods for sending/receiving data.
        """
        return WebSocketMlCopilotWs(client=self.client)

    def ml_reasoning_ws(self, id: str) -> "WebSocketMlReasoningWs":
        """Open a websocket to prompt the ML copilot.

        Returns a WebSocket wrapper with methods for sending/receiving data.
        """
        return WebSocketMlReasoningWs(id, client=self.client)


class AsyncMlAPI:
    """Async API for ml endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def create_text_to_cad(self) -> Any:
        """Generate a CAD model from text."""
        from .api.ml.create_text_to_cad import asyncio

        return await asyncio(client=self.client)

    async def list_ml_prompts(self) -> Any:
        """List all ML prompts."""
        from .api.ml.list_ml_prompts import asyncio

        return await asyncio(client=self.client)

    async def get_ml_prompt(self) -> Any:
        """Get a ML prompt."""
        from .api.ml.get_ml_prompt import asyncio

        return await asyncio(client=self.client)

    async def list_conversations_for_user(self) -> Any:
        """List conversations"""
        from .api.ml.list_conversations_for_user import asyncio

        return await asyncio(client=self.client)

    async def create_proprietary_to_kcl(self) -> Any:
        """Converts a proprietary CAD format to KCL."""
        from .api.ml.create_proprietary_to_kcl import asyncio

        return await asyncio(client=self.client)

    async def create_kcl_code_completions(self) -> Any:
        """Generate code completions for KCL."""
        from .api.ml.create_kcl_code_completions import asyncio

        return await asyncio(client=self.client)

    async def create_text_to_cad_iteration(self) -> Any:
        """Iterate on a CAD model with a prompt."""
        from .api.ml.create_text_to_cad_iteration import asyncio

        return await asyncio(client=self.client)

    async def create_text_to_cad_multi_file_iteration(self) -> Any:
        """Iterate on a multi-file CAD model with a prompt."""
        from .api.ml.create_text_to_cad_multi_file_iteration import asyncio

        return await asyncio(client=self.client)

    async def list_text_to_cad_models_for_user(self) -> Any:
        """List text-to-CAD models you've generated."""
        from .api.ml.list_text_to_cad_models_for_user import asyncio

        return await asyncio(client=self.client)

    async def get_text_to_cad_model_for_user(self) -> Any:
        """Get a text-to-CAD response."""
        from .api.ml.get_text_to_cad_model_for_user import asyncio

        return await asyncio(client=self.client)

    async def create_text_to_cad_model_feedback(self) -> Any:
        """Give feedback to a specific ML response."""
        from .api.ml.create_text_to_cad_model_feedback import asyncio

        return await asyncio(client=self.client)

    def ml_copilot_ws(self) -> "WebSocketMlCopilotWs":
        """Open a websocket to prompt the ML copilot.

        Returns a WebSocket wrapper with methods for sending/receiving data.
        Note: WebSocket connections are synchronous even in AsyncKittyCAD
        """
        return WebSocketMlCopilotWs(client=self.client)

    def ml_reasoning_ws(self, id: str) -> "WebSocketMlReasoningWs":
        """Open a websocket to prompt the ML copilot.

        Returns a WebSocket wrapper with methods for sending/receiving data.
        Note: WebSocket connections are synchronous even in AsyncKittyCAD
        """
        return WebSocketMlReasoningWs(id, client=self.client)


class ApiCallsAPI:
    """API for api_calls endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_api_call_metrics(self) -> Any:
        """Get API call metrics."""
        from .api.api_calls.get_api_call_metrics import sync

        return sync(client=self.client)

    def list_api_calls(self) -> Any:
        """List API calls."""
        from .api.api_calls.list_api_calls import sync

        return sync(client=self.client)

    def get_api_call(self) -> Any:
        """Get details of an API call."""
        from .api.api_calls.get_api_call import sync

        return sync(client=self.client)

    def list_async_operations(self) -> Any:
        """List async operations."""
        from .api.api_calls.list_async_operations import sync

        return sync(client=self.client)

    def get_async_operation(self) -> Any:
        """Get an async operation."""
        from .api.api_calls.get_async_operation import sync

        return sync(client=self.client)

    def org_list_api_calls(self) -> Any:
        """List API calls for your org."""
        from .api.api_calls.org_list_api_calls import sync

        return sync(client=self.client)

    def get_api_call_for_org(self) -> Any:
        """Get an API call for an org."""
        from .api.api_calls.get_api_call_for_org import sync

        return sync(client=self.client)

    def user_list_api_calls(self) -> Any:
        """List API calls for your user."""
        from .api.api_calls.user_list_api_calls import sync

        return sync(client=self.client)

    def get_api_call_for_user(self) -> Any:
        """Get an API call for a user."""
        from .api.api_calls.get_api_call_for_user import sync

        return sync(client=self.client)

    def list_api_calls_for_user(self) -> Any:
        """List API calls for a user."""
        from .api.api_calls.list_api_calls_for_user import sync

        return sync(client=self.client)


class AsyncApiCallsAPI:
    """Async API for api_calls endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def get_api_call_metrics(self) -> Any:
        """Get API call metrics."""
        from .api.api_calls.get_api_call_metrics import asyncio

        return await asyncio(client=self.client)

    async def list_api_calls(self) -> Any:
        """List API calls."""
        from .api.api_calls.list_api_calls import asyncio

        return await asyncio(client=self.client)

    async def get_api_call(self) -> Any:
        """Get details of an API call."""
        from .api.api_calls.get_api_call import asyncio

        return await asyncio(client=self.client)

    async def list_async_operations(self) -> Any:
        """List async operations."""
        from .api.api_calls.list_async_operations import asyncio

        return await asyncio(client=self.client)

    async def get_async_operation(self) -> Any:
        """Get an async operation."""
        from .api.api_calls.get_async_operation import asyncio

        return await asyncio(client=self.client)

    async def org_list_api_calls(self) -> Any:
        """List API calls for your org."""
        from .api.api_calls.org_list_api_calls import asyncio

        return await asyncio(client=self.client)

    async def get_api_call_for_org(self) -> Any:
        """Get an API call for an org."""
        from .api.api_calls.get_api_call_for_org import asyncio

        return await asyncio(client=self.client)

    async def user_list_api_calls(self) -> Any:
        """List API calls for your user."""
        from .api.api_calls.user_list_api_calls import asyncio

        return await asyncio(client=self.client)

    async def get_api_call_for_user(self) -> Any:
        """Get an API call for a user."""
        from .api.api_calls.get_api_call_for_user import asyncio

        return await asyncio(client=self.client)

    async def list_api_calls_for_user(self) -> Any:
        """List API calls for a user."""
        from .api.api_calls.list_api_calls_for_user import asyncio

        return await asyncio(client=self.client)


class AppsAPI:
    """API for apps endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def apps_github_callback(self) -> Any:
        """Listen for callbacks to GitHub app authentication."""
        from .api.apps.apps_github_callback import sync

        return sync(client=self.client)

    def apps_github_consent(self) -> Any:
        """Get the consent URL for GitHub app authentication."""
        from .api.apps.apps_github_consent import sync

        return sync(client=self.client)

    def apps_github_webhook(self) -> Any:
        """Listen for GitHub webhooks."""
        from .api.apps.apps_github_webhook import sync

        return sync(client=self.client)


class AsyncAppsAPI:
    """Async API for apps endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def apps_github_callback(self) -> Any:
        """Listen for callbacks to GitHub app authentication."""
        from .api.apps.apps_github_callback import asyncio

        return await asyncio(client=self.client)

    async def apps_github_consent(self) -> Any:
        """Get the consent URL for GitHub app authentication."""
        from .api.apps.apps_github_consent import asyncio

        return await asyncio(client=self.client)

    async def apps_github_webhook(self) -> Any:
        """Listen for GitHub webhooks."""
        from .api.apps.apps_github_webhook import asyncio

        return await asyncio(client=self.client)


class HiddenAPI:
    """API for hidden endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def auth_api_key(self) -> Any:
        """Authenticate using an api-key. This is disabled on production but can be used in dev to login without email magic."""
        from .api.hidden.auth_api_key import sync

        return sync(client=self.client)

    def auth_email(self) -> Any:
        """Create an email verification request for a user."""
        from .api.hidden.auth_email import sync

        return sync(client=self.client)

    def auth_email_callback(self) -> Any:
        """Listen for callbacks for email authentication for users."""
        from .api.hidden.auth_email_callback import sync

        return sync(client=self.client)

    def get_auth_saml_by_org(self) -> Any:
        """GET /auth/saml/{org_id}"""
        from .api.hidden.get_auth_saml_by_org import sync

        return sync(client=self.client)

    def get_auth_saml(self) -> Any:
        """Get a redirect straight to the SAML IdP."""
        from .api.hidden.get_auth_saml import sync

        return sync(client=self.client)

    def post_auth_saml(self) -> Any:
        """Authenticate a user via SAML"""
        from .api.hidden.post_auth_saml import sync

        return sync(client=self.client)

    def logout(self) -> Any:
        """This endpoint removes the session cookie for a user."""
        from .api.hidden.logout import sync

        return sync(client=self.client)

    def redirect_user_shortlink(self) -> Any:
        """Redirect the user to the URL for the shortlink."""
        from .api.hidden.redirect_user_shortlink import sync

        return sync(client=self.client)


class AsyncHiddenAPI:
    """Async API for hidden endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def auth_api_key(self) -> Any:
        """Authenticate using an api-key. This is disabled on production but can be used in dev to login without email magic."""
        from .api.hidden.auth_api_key import asyncio

        return await asyncio(client=self.client)

    async def auth_email(self) -> Any:
        """Create an email verification request for a user."""
        from .api.hidden.auth_email import asyncio

        return await asyncio(client=self.client)

    async def auth_email_callback(self) -> Any:
        """Listen for callbacks for email authentication for users."""
        from .api.hidden.auth_email_callback import asyncio

        return await asyncio(client=self.client)

    async def get_auth_saml_by_org(self) -> Any:
        """GET /auth/saml/{org_id}"""
        from .api.hidden.get_auth_saml_by_org import asyncio

        return await asyncio(client=self.client)

    async def get_auth_saml(self) -> Any:
        """Get a redirect straight to the SAML IdP."""
        from .api.hidden.get_auth_saml import asyncio

        return await asyncio(client=self.client)

    async def post_auth_saml(self) -> Any:
        """Authenticate a user via SAML"""
        from .api.hidden.post_auth_saml import asyncio

        return await asyncio(client=self.client)

    async def logout(self) -> Any:
        """This endpoint removes the session cookie for a user."""
        from .api.hidden.logout import asyncio

        return await asyncio(client=self.client)

    async def redirect_user_shortlink(self) -> Any:
        """Redirect the user to the URL for the shortlink."""
        from .api.hidden.redirect_user_shortlink import asyncio

        return await asyncio(client=self.client)


class FileAPI:
    """API for file endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def create_file_center_of_mass(self) -> Any:
        """Get CAD file center of mass."""
        from .api.file.create_file_center_of_mass import sync

        return sync(client=self.client)

    def create_file_conversion_options(self) -> Any:
        """Convert CAD file from one format to another."""
        from .api.file.create_file_conversion_options import sync

        return sync(client=self.client)

    def create_file_conversion(self) -> Any:
        """Convert CAD file with defaults."""
        from .api.file.create_file_conversion import sync

        return sync(client=self.client)

    def create_file_density(self) -> Any:
        """Get CAD file density."""
        from .api.file.create_file_density import sync

        return sync(client=self.client)

    def create_file_mass(self) -> Any:
        """Get CAD file mass."""
        from .api.file.create_file_mass import sync

        return sync(client=self.client)

    def create_file_surface_area(self) -> Any:
        """Get CAD file surface area."""
        from .api.file.create_file_surface_area import sync

        return sync(client=self.client)

    def create_file_volume(self) -> Any:
        """Get CAD file volume."""
        from .api.file.create_file_volume import sync

        return sync(client=self.client)


class AsyncFileAPI:
    """Async API for file endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def create_file_center_of_mass(self) -> Any:
        """Get CAD file center of mass."""
        from .api.file.create_file_center_of_mass import asyncio

        return await asyncio(client=self.client)

    async def create_file_conversion_options(self) -> Any:
        """Convert CAD file from one format to another."""
        from .api.file.create_file_conversion_options import asyncio

        return await asyncio(client=self.client)

    async def create_file_conversion(self) -> Any:
        """Convert CAD file with defaults."""
        from .api.file.create_file_conversion import asyncio

        return await asyncio(client=self.client)

    async def create_file_density(self) -> Any:
        """Get CAD file density."""
        from .api.file.create_file_density import asyncio

        return await asyncio(client=self.client)

    async def create_file_mass(self) -> Any:
        """Get CAD file mass."""
        from .api.file.create_file_mass import asyncio

        return await asyncio(client=self.client)

    async def create_file_surface_area(self) -> Any:
        """Get CAD file surface area."""
        from .api.file.create_file_surface_area import asyncio

        return await asyncio(client=self.client)

    async def create_file_volume(self) -> Any:
        """Get CAD file volume."""
        from .api.file.create_file_volume import asyncio

        return await asyncio(client=self.client)


class ExecutorAPI:
    """API for executor endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def create_file_execution(self) -> Any:
        """Execute a Zoo program in a specific language."""
        from .api.executor.create_file_execution import sync

        return sync(client=self.client)

    def create_executor_term(self) -> ClientConnectionSync:
        """Create a terminal.

        Returns a raw WebSocket connection for create_executor_term.
        """
        from .api.executor.create_executor_term import sync

        return sync(client=self.client)


class AsyncExecutorAPI:
    """Async API for executor endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def create_file_execution(self) -> Any:
        """Execute a Zoo program in a specific language."""
        from .api.executor.create_file_execution import asyncio

        return await asyncio(client=self.client)

    async def create_executor_term(self) -> ClientConnectionAsync:
        """Create a terminal.

        Returns a raw async WebSocket connection for create_executor_term.
        """
        from .api.executor.create_executor_term import asyncio

        return await asyncio(client=self.client)


class Oauth2API:
    """API for oauth2 endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def device_auth_request(self) -> Any:
        """Start an OAuth 2.0 Device Authorization Grant."""
        from .api.oauth2.device_auth_request import sync

        return sync(client=self.client)

    def device_auth_confirm(self) -> Any:
        """Confirm an OAuth 2.0 Device Authorization Grant."""
        from .api.oauth2.device_auth_confirm import sync

        return sync(client=self.client)

    def device_access_token(self) -> Any:
        """Request a device access token."""
        from .api.oauth2.device_access_token import sync

        return sync(client=self.client)

    def device_auth_verify(self) -> Any:
        """Verify an OAuth 2.0 Device Authorization Grant."""
        from .api.oauth2.device_auth_verify import sync

        return sync(client=self.client)

    def oauth2_provider_callback(self) -> Any:
        """Listen for callbacks for the OAuth 2.0 provider."""
        from .api.oauth2.oauth2_provider_callback import sync

        return sync(client=self.client)

    def oauth2_provider_callback_post(self) -> Any:
        """Listen for callbacks for the OAuth 2.0 provider."""
        from .api.oauth2.oauth2_provider_callback_post import sync

        return sync(client=self.client)

    def oauth2_provider_consent(self) -> Any:
        """Get the consent URL and other information for the OAuth 2.0 provider."""
        from .api.oauth2.oauth2_provider_consent import sync

        return sync(client=self.client)

    def oauth2_token_revoke(self) -> Any:
        """Revoke an OAuth2 token."""
        from .api.oauth2.oauth2_token_revoke import sync

        return sync(client=self.client)


class AsyncOauth2API:
    """Async API for oauth2 endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def device_auth_request(self) -> Any:
        """Start an OAuth 2.0 Device Authorization Grant."""
        from .api.oauth2.device_auth_request import asyncio

        return await asyncio(client=self.client)

    async def device_auth_confirm(self) -> Any:
        """Confirm an OAuth 2.0 Device Authorization Grant."""
        from .api.oauth2.device_auth_confirm import asyncio

        return await asyncio(client=self.client)

    async def device_access_token(self) -> Any:
        """Request a device access token."""
        from .api.oauth2.device_access_token import asyncio

        return await asyncio(client=self.client)

    async def device_auth_verify(self) -> Any:
        """Verify an OAuth 2.0 Device Authorization Grant."""
        from .api.oauth2.device_auth_verify import asyncio

        return await asyncio(client=self.client)

    async def oauth2_provider_callback(self) -> Any:
        """Listen for callbacks for the OAuth 2.0 provider."""
        from .api.oauth2.oauth2_provider_callback import asyncio

        return await asyncio(client=self.client)

    async def oauth2_provider_callback_post(self) -> Any:
        """Listen for callbacks for the OAuth 2.0 provider."""
        from .api.oauth2.oauth2_provider_callback_post import asyncio

        return await asyncio(client=self.client)

    async def oauth2_provider_consent(self) -> Any:
        """Get the consent URL and other information for the OAuth 2.0 provider."""
        from .api.oauth2.oauth2_provider_consent import asyncio

        return await asyncio(client=self.client)

    async def oauth2_token_revoke(self) -> Any:
        """Revoke an OAuth2 token."""
        from .api.oauth2.oauth2_token_revoke import asyncio

        return await asyncio(client=self.client)


class OrgsAPI:
    """API for orgs endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_org(self) -> Any:
        """Get an org."""
        from .api.orgs.get_org import sync

        return sync(client=self.client)

    def update_org(self) -> Any:
        """Update an org."""
        from .api.orgs.update_org import sync

        return sync(client=self.client)

    def create_org(self) -> Any:
        """Create an org."""
        from .api.orgs.create_org import sync

        return sync(client=self.client)

    def delete_org(self) -> Any:
        """Delete an org."""
        from .api.orgs.delete_org import sync

        return sync(client=self.client)

    def list_org_members(self) -> Any:
        """List members of your org."""
        from .api.orgs.list_org_members import sync

        return sync(client=self.client)

    def create_org_member(self) -> Any:
        """Add a member to your org."""
        from .api.orgs.create_org_member import sync

        return sync(client=self.client)

    def get_org_member(self) -> Any:
        """Get a member of your org."""
        from .api.orgs.get_org_member import sync

        return sync(client=self.client)

    def update_org_member(self) -> Any:
        """Update a member of your org."""
        from .api.orgs.update_org_member import sync

        return sync(client=self.client)

    def delete_org_member(self) -> Any:
        """Remove a member from your org."""
        from .api.orgs.delete_org_member import sync

        return sync(client=self.client)

    def get_org_privacy_settings(self) -> Any:
        """Get the privacy settings for an org."""
        from .api.orgs.get_org_privacy_settings import sync

        return sync(client=self.client)

    def update_org_privacy_settings(self) -> Any:
        """Update the privacy settings for an org."""
        from .api.orgs.update_org_privacy_settings import sync

        return sync(client=self.client)

    def get_org_saml_idp(self) -> Any:
        """Get the SAML identity provider."""
        from .api.orgs.get_org_saml_idp import sync

        return sync(client=self.client)

    def update_org_saml_idp(self) -> Any:
        """Update the SAML identity provider."""
        from .api.orgs.update_org_saml_idp import sync

        return sync(client=self.client)

    def create_org_saml_idp(self) -> Any:
        """Create a SAML identity provider."""
        from .api.orgs.create_org_saml_idp import sync

        return sync(client=self.client)

    def delete_org_saml_idp(self) -> Any:
        """Delete an SAML identity provider."""
        from .api.orgs.delete_org_saml_idp import sync

        return sync(client=self.client)

    def get_org_shortlinks(self) -> Any:
        """Get the shortlinks for an org."""
        from .api.orgs.get_org_shortlinks import sync

        return sync(client=self.client)

    def list_orgs(self) -> Any:
        """List orgs."""
        from .api.orgs.list_orgs import sync

        return sync(client=self.client)

    def get_any_org(self) -> Any:
        """Get an org."""
        from .api.orgs.get_any_org import sync

        return sync(client=self.client)

    def update_enterprise_pricing_for_org(self) -> Any:
        """Set the enterprise price for an organization."""
        from .api.orgs.update_enterprise_pricing_for_org import sync

        return sync(client=self.client)

    def get_user_org(self) -> Any:
        """Get a user's org."""
        from .api.orgs.get_user_org import sync

        return sync(client=self.client)


class AsyncOrgsAPI:
    """Async API for orgs endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def get_org(self) -> Any:
        """Get an org."""
        from .api.orgs.get_org import asyncio

        return await asyncio(client=self.client)

    async def update_org(self) -> Any:
        """Update an org."""
        from .api.orgs.update_org import asyncio

        return await asyncio(client=self.client)

    async def create_org(self) -> Any:
        """Create an org."""
        from .api.orgs.create_org import asyncio

        return await asyncio(client=self.client)

    async def delete_org(self) -> Any:
        """Delete an org."""
        from .api.orgs.delete_org import asyncio

        return await asyncio(client=self.client)

    async def list_org_members(self) -> Any:
        """List members of your org."""
        from .api.orgs.list_org_members import asyncio

        return await asyncio(client=self.client)

    async def create_org_member(self) -> Any:
        """Add a member to your org."""
        from .api.orgs.create_org_member import asyncio

        return await asyncio(client=self.client)

    async def get_org_member(self) -> Any:
        """Get a member of your org."""
        from .api.orgs.get_org_member import asyncio

        return await asyncio(client=self.client)

    async def update_org_member(self) -> Any:
        """Update a member of your org."""
        from .api.orgs.update_org_member import asyncio

        return await asyncio(client=self.client)

    async def delete_org_member(self) -> Any:
        """Remove a member from your org."""
        from .api.orgs.delete_org_member import asyncio

        return await asyncio(client=self.client)

    async def get_org_privacy_settings(self) -> Any:
        """Get the privacy settings for an org."""
        from .api.orgs.get_org_privacy_settings import asyncio

        return await asyncio(client=self.client)

    async def update_org_privacy_settings(self) -> Any:
        """Update the privacy settings for an org."""
        from .api.orgs.update_org_privacy_settings import asyncio

        return await asyncio(client=self.client)

    async def get_org_saml_idp(self) -> Any:
        """Get the SAML identity provider."""
        from .api.orgs.get_org_saml_idp import asyncio

        return await asyncio(client=self.client)

    async def update_org_saml_idp(self) -> Any:
        """Update the SAML identity provider."""
        from .api.orgs.update_org_saml_idp import asyncio

        return await asyncio(client=self.client)

    async def create_org_saml_idp(self) -> Any:
        """Create a SAML identity provider."""
        from .api.orgs.create_org_saml_idp import asyncio

        return await asyncio(client=self.client)

    async def delete_org_saml_idp(self) -> Any:
        """Delete an SAML identity provider."""
        from .api.orgs.delete_org_saml_idp import asyncio

        return await asyncio(client=self.client)

    async def get_org_shortlinks(self) -> Any:
        """Get the shortlinks for an org."""
        from .api.orgs.get_org_shortlinks import asyncio

        return await asyncio(client=self.client)

    async def list_orgs(self) -> Any:
        """List orgs."""
        from .api.orgs.list_orgs import asyncio

        return await asyncio(client=self.client)

    async def get_any_org(self) -> Any:
        """Get an org."""
        from .api.orgs.get_any_org import asyncio

        return await asyncio(client=self.client)

    async def update_enterprise_pricing_for_org(self) -> Any:
        """Set the enterprise price for an organization."""
        from .api.orgs.update_enterprise_pricing_for_org import asyncio

        return await asyncio(client=self.client)

    async def get_user_org(self) -> Any:
        """Get a user's org."""
        from .api.orgs.get_user_org import asyncio

        return await asyncio(client=self.client)


class PaymentsAPI:
    """API for payments endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_payment_information_for_org(self) -> Any:
        """Get payment info about your org."""
        from .api.payments.get_payment_information_for_org import sync

        return sync(client=self.client)

    def update_payment_information_for_org(self) -> Any:
        """Update payment info for your org."""
        from .api.payments.update_payment_information_for_org import sync

        return sync(client=self.client)

    def create_payment_information_for_org(self) -> Any:
        """Create payment info for your org."""
        from .api.payments.create_payment_information_for_org import sync

        return sync(client=self.client)

    def delete_payment_information_for_org(self) -> Any:
        """Delete payment info for your org."""
        from .api.payments.delete_payment_information_for_org import sync

        return sync(client=self.client)

    def get_payment_balance_for_org(self) -> Any:
        """Get balance for your org."""
        from .api.payments.get_payment_balance_for_org import sync

        return sync(client=self.client)

    def create_payment_intent_for_org(self) -> Any:
        """Create a payment intent for your org."""
        from .api.payments.create_payment_intent_for_org import sync

        return sync(client=self.client)

    def list_invoices_for_org(self) -> Any:
        """List invoices for your org."""
        from .api.payments.list_invoices_for_org import sync

        return sync(client=self.client)

    def list_payment_methods_for_org(self) -> Any:
        """List payment methods for your org."""
        from .api.payments.list_payment_methods_for_org import sync

        return sync(client=self.client)

    def delete_payment_method_for_org(self) -> Any:
        """Delete a payment method for your org."""
        from .api.payments.delete_payment_method_for_org import sync

        return sync(client=self.client)

    def get_org_subscription(self) -> Any:
        """Get the subscription for an org."""
        from .api.payments.get_org_subscription import sync

        return sync(client=self.client)

    def update_org_subscription(self) -> Any:
        """Update the subscription for an org."""
        from .api.payments.update_org_subscription import sync

        return sync(client=self.client)

    def create_org_subscription(self) -> Any:
        """Create the subscription for an org."""
        from .api.payments.create_org_subscription import sync

        return sync(client=self.client)

    def validate_customer_tax_information_for_org(self) -> Any:
        """Validate an orgs's information is correct and valid for automatic tax."""
        from .api.payments.validate_customer_tax_information_for_org import sync

        return sync(client=self.client)

    def get_payment_balance_for_any_org(self) -> Any:
        """Get balance for an org."""
        from .api.payments.get_payment_balance_for_any_org import sync

        return sync(client=self.client)

    def update_payment_balance_for_any_org(self) -> Any:
        """Update balance for an org."""
        from .api.payments.update_payment_balance_for_any_org import sync

        return sync(client=self.client)

    def get_payment_information_for_user(self) -> Any:
        """Get payment info about your user."""
        from .api.payments.get_payment_information_for_user import sync

        return sync(client=self.client)

    def update_payment_information_for_user(self) -> Any:
        """Update payment info for your user."""
        from .api.payments.update_payment_information_for_user import sync

        return sync(client=self.client)

    def create_payment_information_for_user(self) -> Any:
        """Create payment info for your user."""
        from .api.payments.create_payment_information_for_user import sync

        return sync(client=self.client)

    def delete_payment_information_for_user(self) -> Any:
        """Delete payment info for your user."""
        from .api.payments.delete_payment_information_for_user import sync

        return sync(client=self.client)

    def get_payment_balance_for_user(self) -> Any:
        """Get balance for your user."""
        from .api.payments.get_payment_balance_for_user import sync

        return sync(client=self.client)

    def create_payment_intent_for_user(self) -> Any:
        """Create a payment intent for your user."""
        from .api.payments.create_payment_intent_for_user import sync

        return sync(client=self.client)

    def list_invoices_for_user(self) -> Any:
        """List invoices for your user."""
        from .api.payments.list_invoices_for_user import sync

        return sync(client=self.client)

    def list_payment_methods_for_user(self) -> Any:
        """List payment methods for your user."""
        from .api.payments.list_payment_methods_for_user import sync

        return sync(client=self.client)

    def delete_payment_method_for_user(self) -> Any:
        """Delete a payment method for your user."""
        from .api.payments.delete_payment_method_for_user import sync

        return sync(client=self.client)

    def get_user_subscription(self) -> Any:
        """Get the subscription for a user."""
        from .api.payments.get_user_subscription import sync

        return sync(client=self.client)

    def update_user_subscription(self) -> Any:
        """Update the user's subscription."""
        from .api.payments.update_user_subscription import sync

        return sync(client=self.client)

    def create_user_subscription(self) -> Any:
        """Create the subscription for a user."""
        from .api.payments.create_user_subscription import sync

        return sync(client=self.client)

    def validate_customer_tax_information_for_user(self) -> Any:
        """Validate a user's information is correct and valid for automatic tax."""
        from .api.payments.validate_customer_tax_information_for_user import sync

        return sync(client=self.client)

    def get_payment_balance_for_any_user(self) -> Any:
        """Get balance for an user."""
        from .api.payments.get_payment_balance_for_any_user import sync

        return sync(client=self.client)

    def update_payment_balance_for_any_user(self) -> Any:
        """Update balance for an user."""
        from .api.payments.update_payment_balance_for_any_user import sync

        return sync(client=self.client)


class AsyncPaymentsAPI:
    """Async API for payments endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def get_payment_information_for_org(self) -> Any:
        """Get payment info about your org."""
        from .api.payments.get_payment_information_for_org import asyncio

        return await asyncio(client=self.client)

    async def update_payment_information_for_org(self) -> Any:
        """Update payment info for your org."""
        from .api.payments.update_payment_information_for_org import asyncio

        return await asyncio(client=self.client)

    async def create_payment_information_for_org(self) -> Any:
        """Create payment info for your org."""
        from .api.payments.create_payment_information_for_org import asyncio

        return await asyncio(client=self.client)

    async def delete_payment_information_for_org(self) -> Any:
        """Delete payment info for your org."""
        from .api.payments.delete_payment_information_for_org import asyncio

        return await asyncio(client=self.client)

    async def get_payment_balance_for_org(self) -> Any:
        """Get balance for your org."""
        from .api.payments.get_payment_balance_for_org import asyncio

        return await asyncio(client=self.client)

    async def create_payment_intent_for_org(self) -> Any:
        """Create a payment intent for your org."""
        from .api.payments.create_payment_intent_for_org import asyncio

        return await asyncio(client=self.client)

    async def list_invoices_for_org(self) -> Any:
        """List invoices for your org."""
        from .api.payments.list_invoices_for_org import asyncio

        return await asyncio(client=self.client)

    async def list_payment_methods_for_org(self) -> Any:
        """List payment methods for your org."""
        from .api.payments.list_payment_methods_for_org import asyncio

        return await asyncio(client=self.client)

    async def delete_payment_method_for_org(self) -> Any:
        """Delete a payment method for your org."""
        from .api.payments.delete_payment_method_for_org import asyncio

        return await asyncio(client=self.client)

    async def get_org_subscription(self) -> Any:
        """Get the subscription for an org."""
        from .api.payments.get_org_subscription import asyncio

        return await asyncio(client=self.client)

    async def update_org_subscription(self) -> Any:
        """Update the subscription for an org."""
        from .api.payments.update_org_subscription import asyncio

        return await asyncio(client=self.client)

    async def create_org_subscription(self) -> Any:
        """Create the subscription for an org."""
        from .api.payments.create_org_subscription import asyncio

        return await asyncio(client=self.client)

    async def validate_customer_tax_information_for_org(self) -> Any:
        """Validate an orgs's information is correct and valid for automatic tax."""
        from .api.payments.validate_customer_tax_information_for_org import asyncio

        return await asyncio(client=self.client)

    async def get_payment_balance_for_any_org(self) -> Any:
        """Get balance for an org."""
        from .api.payments.get_payment_balance_for_any_org import asyncio

        return await asyncio(client=self.client)

    async def update_payment_balance_for_any_org(self) -> Any:
        """Update balance for an org."""
        from .api.payments.update_payment_balance_for_any_org import asyncio

        return await asyncio(client=self.client)

    async def get_payment_information_for_user(self) -> Any:
        """Get payment info about your user."""
        from .api.payments.get_payment_information_for_user import asyncio

        return await asyncio(client=self.client)

    async def update_payment_information_for_user(self) -> Any:
        """Update payment info for your user."""
        from .api.payments.update_payment_information_for_user import asyncio

        return await asyncio(client=self.client)

    async def create_payment_information_for_user(self) -> Any:
        """Create payment info for your user."""
        from .api.payments.create_payment_information_for_user import asyncio

        return await asyncio(client=self.client)

    async def delete_payment_information_for_user(self) -> Any:
        """Delete payment info for your user."""
        from .api.payments.delete_payment_information_for_user import asyncio

        return await asyncio(client=self.client)

    async def get_payment_balance_for_user(self) -> Any:
        """Get balance for your user."""
        from .api.payments.get_payment_balance_for_user import asyncio

        return await asyncio(client=self.client)

    async def create_payment_intent_for_user(self) -> Any:
        """Create a payment intent for your user."""
        from .api.payments.create_payment_intent_for_user import asyncio

        return await asyncio(client=self.client)

    async def list_invoices_for_user(self) -> Any:
        """List invoices for your user."""
        from .api.payments.list_invoices_for_user import asyncio

        return await asyncio(client=self.client)

    async def list_payment_methods_for_user(self) -> Any:
        """List payment methods for your user."""
        from .api.payments.list_payment_methods_for_user import asyncio

        return await asyncio(client=self.client)

    async def delete_payment_method_for_user(self) -> Any:
        """Delete a payment method for your user."""
        from .api.payments.delete_payment_method_for_user import asyncio

        return await asyncio(client=self.client)

    async def get_user_subscription(self) -> Any:
        """Get the subscription for a user."""
        from .api.payments.get_user_subscription import asyncio

        return await asyncio(client=self.client)

    async def update_user_subscription(self) -> Any:
        """Update the user's subscription."""
        from .api.payments.update_user_subscription import asyncio

        return await asyncio(client=self.client)

    async def create_user_subscription(self) -> Any:
        """Create the subscription for a user."""
        from .api.payments.create_user_subscription import asyncio

        return await asyncio(client=self.client)

    async def validate_customer_tax_information_for_user(self) -> Any:
        """Validate a user's information is correct and valid for automatic tax."""
        from .api.payments.validate_customer_tax_information_for_user import asyncio

        return await asyncio(client=self.client)

    async def get_payment_balance_for_any_user(self) -> Any:
        """Get balance for an user."""
        from .api.payments.get_payment_balance_for_any_user import asyncio

        return await asyncio(client=self.client)

    async def update_payment_balance_for_any_user(self) -> Any:
        """Update balance for an user."""
        from .api.payments.update_payment_balance_for_any_user import asyncio

        return await asyncio(client=self.client)


class ServiceAccountsAPI:
    """API for service_accounts endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def list_service_accounts_for_org(self) -> Any:
        """List service accounts for your org."""
        from .api.service_accounts.list_service_accounts_for_org import sync

        return sync(client=self.client)

    def create_service_account_for_org(self) -> Any:
        """Create a new service account for your org."""
        from .api.service_accounts.create_service_account_for_org import sync

        return sync(client=self.client)

    def get_service_account_for_org(self) -> Any:
        """Get an service account for your org."""
        from .api.service_accounts.get_service_account_for_org import sync

        return sync(client=self.client)

    def delete_service_account_for_org(self) -> Any:
        """Delete an service account for your org."""
        from .api.service_accounts.delete_service_account_for_org import sync

        return sync(client=self.client)


class AsyncServiceAccountsAPI:
    """Async API for service_accounts endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def list_service_accounts_for_org(self) -> Any:
        """List service accounts for your org."""
        from .api.service_accounts.list_service_accounts_for_org import asyncio

        return await asyncio(client=self.client)

    async def create_service_account_for_org(self) -> Any:
        """Create a new service account for your org."""
        from .api.service_accounts.create_service_account_for_org import asyncio

        return await asyncio(client=self.client)

    async def get_service_account_for_org(self) -> Any:
        """Get an service account for your org."""
        from .api.service_accounts.get_service_account_for_org import asyncio

        return await asyncio(client=self.client)

    async def delete_service_account_for_org(self) -> Any:
        """Delete an service account for your org."""
        from .api.service_accounts.delete_service_account_for_org import asyncio

        return await asyncio(client=self.client)


class StoreAPI:
    """API for store endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def create_store_coupon(self) -> Any:
        """Create a new store coupon."""
        from .api.store.create_store_coupon import sync

        return sync(client=self.client)


class AsyncStoreAPI:
    """Async API for store endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def create_store_coupon(self) -> Any:
        """Create a new store coupon."""
        from .api.store.create_store_coupon import asyncio

        return await asyncio(client=self.client)


class UnitAPI:
    """API for unit endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_angle_unit_conversion(self) -> Any:
        """Convert angle units."""
        from .api.unit.get_angle_unit_conversion import sync

        return sync(client=self.client)

    def get_area_unit_conversion(self) -> Any:
        """Convert area units."""
        from .api.unit.get_area_unit_conversion import sync

        return sync(client=self.client)

    def get_current_unit_conversion(self) -> Any:
        """Convert current units."""
        from .api.unit.get_current_unit_conversion import sync

        return sync(client=self.client)

    def get_energy_unit_conversion(self) -> Any:
        """Convert energy units."""
        from .api.unit.get_energy_unit_conversion import sync

        return sync(client=self.client)

    def get_force_unit_conversion(self) -> Any:
        """Convert force units."""
        from .api.unit.get_force_unit_conversion import sync

        return sync(client=self.client)

    def get_frequency_unit_conversion(self) -> Any:
        """Convert frequency units."""
        from .api.unit.get_frequency_unit_conversion import sync

        return sync(client=self.client)

    def get_length_unit_conversion(self) -> Any:
        """Convert length units."""
        from .api.unit.get_length_unit_conversion import sync

        return sync(client=self.client)

    def get_mass_unit_conversion(self) -> Any:
        """Convert mass units."""
        from .api.unit.get_mass_unit_conversion import sync

        return sync(client=self.client)

    def get_power_unit_conversion(self) -> Any:
        """Convert power units."""
        from .api.unit.get_power_unit_conversion import sync

        return sync(client=self.client)

    def get_pressure_unit_conversion(self) -> Any:
        """Convert pressure units."""
        from .api.unit.get_pressure_unit_conversion import sync

        return sync(client=self.client)

    def get_temperature_unit_conversion(self) -> Any:
        """Convert temperature units."""
        from .api.unit.get_temperature_unit_conversion import sync

        return sync(client=self.client)

    def get_torque_unit_conversion(self) -> Any:
        """Convert torque units."""
        from .api.unit.get_torque_unit_conversion import sync

        return sync(client=self.client)

    def get_volume_unit_conversion(self) -> Any:
        """Convert volume units."""
        from .api.unit.get_volume_unit_conversion import sync

        return sync(client=self.client)


class AsyncUnitAPI:
    """Async API for unit endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def get_angle_unit_conversion(self) -> Any:
        """Convert angle units."""
        from .api.unit.get_angle_unit_conversion import asyncio

        return await asyncio(client=self.client)

    async def get_area_unit_conversion(self) -> Any:
        """Convert area units."""
        from .api.unit.get_area_unit_conversion import asyncio

        return await asyncio(client=self.client)

    async def get_current_unit_conversion(self) -> Any:
        """Convert current units."""
        from .api.unit.get_current_unit_conversion import asyncio

        return await asyncio(client=self.client)

    async def get_energy_unit_conversion(self) -> Any:
        """Convert energy units."""
        from .api.unit.get_energy_unit_conversion import asyncio

        return await asyncio(client=self.client)

    async def get_force_unit_conversion(self) -> Any:
        """Convert force units."""
        from .api.unit.get_force_unit_conversion import asyncio

        return await asyncio(client=self.client)

    async def get_frequency_unit_conversion(self) -> Any:
        """Convert frequency units."""
        from .api.unit.get_frequency_unit_conversion import asyncio

        return await asyncio(client=self.client)

    async def get_length_unit_conversion(self) -> Any:
        """Convert length units."""
        from .api.unit.get_length_unit_conversion import asyncio

        return await asyncio(client=self.client)

    async def get_mass_unit_conversion(self) -> Any:
        """Convert mass units."""
        from .api.unit.get_mass_unit_conversion import asyncio

        return await asyncio(client=self.client)

    async def get_power_unit_conversion(self) -> Any:
        """Convert power units."""
        from .api.unit.get_power_unit_conversion import asyncio

        return await asyncio(client=self.client)

    async def get_pressure_unit_conversion(self) -> Any:
        """Convert pressure units."""
        from .api.unit.get_pressure_unit_conversion import asyncio

        return await asyncio(client=self.client)

    async def get_temperature_unit_conversion(self) -> Any:
        """Convert temperature units."""
        from .api.unit.get_temperature_unit_conversion import asyncio

        return await asyncio(client=self.client)

    async def get_torque_unit_conversion(self) -> Any:
        """Convert torque units."""
        from .api.unit.get_torque_unit_conversion import asyncio

        return await asyncio(client=self.client)

    async def get_volume_unit_conversion(self) -> Any:
        """Convert volume units."""
        from .api.unit.get_volume_unit_conversion import asyncio

        return await asyncio(client=self.client)


class UsersAPI:
    """API for users endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_user_self(self) -> Any:
        """Get your user."""
        from .api.users.get_user_self import sync

        return sync(client=self.client)

    def update_user_self(self) -> Any:
        """Update your user."""
        from .api.users.update_user_self import sync

        return sync(client=self.client)

    def delete_user_self(self) -> Any:
        """Delete your user."""
        from .api.users.delete_user_self import sync

        return sync(client=self.client)

    def patch_user_crm(self) -> Any:
        """Update properties in the CRM"""
        from .api.users.patch_user_crm import sync

        return sync(client=self.client)

    def get_user_self_extended(self) -> Any:
        """Get extended information about your user."""
        from .api.users.get_user_self_extended import sync

        return sync(client=self.client)

    def put_user_form_self(self) -> Any:
        """Create a new support/sales ticket from the website contact form. This endpoint is authenticated."""
        from .api.users.put_user_form_self import sync

        return sync(client=self.client)

    def get_oauth2_providers_for_user(self) -> Any:
        """Get the OAuth2 providers for your user."""
        from .api.users.get_oauth2_providers_for_user import sync

        return sync(client=self.client)

    def get_user_privacy_settings(self) -> Any:
        """Get the privacy settings for a user."""
        from .api.users.get_user_privacy_settings import sync

        return sync(client=self.client)

    def update_user_privacy_settings(self) -> Any:
        """Update the user's privacy settings."""
        from .api.users.update_user_privacy_settings import sync

        return sync(client=self.client)

    def get_session_for_user(self) -> Any:
        """Get a session for your user."""
        from .api.users.get_session_for_user import sync

        return sync(client=self.client)

    def get_user_shortlinks(self) -> Any:
        """Get the shortlinks for a user."""
        from .api.users.get_user_shortlinks import sync

        return sync(client=self.client)

    def create_user_shortlink(self) -> Any:
        """Create a shortlink for a user."""
        from .api.users.create_user_shortlink import sync

        return sync(client=self.client)

    def update_user_shortlink(self) -> Any:
        """Update a shortlink for a user."""
        from .api.users.update_user_shortlink import sync

        return sync(client=self.client)

    def delete_user_shortlink(self) -> Any:
        """Delete a shortlink for a user."""
        from .api.users.delete_user_shortlink import sync

        return sync(client=self.client)

    def list_users(self) -> Any:
        """List users."""
        from .api.users.list_users import sync

        return sync(client=self.client)

    def list_users_extended(self) -> Any:
        """List users with extended information."""
        from .api.users.list_users_extended import sync

        return sync(client=self.client)

    def get_user_extended(self) -> Any:
        """Get extended information about a user."""
        from .api.users.get_user_extended import sync

        return sync(client=self.client)

    def get_user(self) -> Any:
        """Get a user."""
        from .api.users.get_user import sync

        return sync(client=self.client)

    def update_subscription_for_user(self) -> Any:
        """Update a subscription for a user."""
        from .api.users.update_subscription_for_user import sync

        return sync(client=self.client)

    def put_public_form(self) -> Any:
        """Creates a new support/sales ticket from the website contact form. This endpoint is for untrusted"""
        from .api.users.put_public_form import sync

        return sync(client=self.client)

    def put_public_subscribe(self) -> Any:
        """Subscribes a user to the newsletter."""
        from .api.users.put_public_subscribe import sync

        return sync(client=self.client)


class AsyncUsersAPI:
    """Async API for users endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def get_user_self(self) -> Any:
        """Get your user."""
        from .api.users.get_user_self import asyncio

        return await asyncio(client=self.client)

    async def update_user_self(self) -> Any:
        """Update your user."""
        from .api.users.update_user_self import asyncio

        return await asyncio(client=self.client)

    async def delete_user_self(self) -> Any:
        """Delete your user."""
        from .api.users.delete_user_self import asyncio

        return await asyncio(client=self.client)

    async def patch_user_crm(self) -> Any:
        """Update properties in the CRM"""
        from .api.users.patch_user_crm import asyncio

        return await asyncio(client=self.client)

    async def get_user_self_extended(self) -> Any:
        """Get extended information about your user."""
        from .api.users.get_user_self_extended import asyncio

        return await asyncio(client=self.client)

    async def put_user_form_self(self) -> Any:
        """Create a new support/sales ticket from the website contact form. This endpoint is authenticated."""
        from .api.users.put_user_form_self import asyncio

        return await asyncio(client=self.client)

    async def get_oauth2_providers_for_user(self) -> Any:
        """Get the OAuth2 providers for your user."""
        from .api.users.get_oauth2_providers_for_user import asyncio

        return await asyncio(client=self.client)

    async def get_user_privacy_settings(self) -> Any:
        """Get the privacy settings for a user."""
        from .api.users.get_user_privacy_settings import asyncio

        return await asyncio(client=self.client)

    async def update_user_privacy_settings(self) -> Any:
        """Update the user's privacy settings."""
        from .api.users.update_user_privacy_settings import asyncio

        return await asyncio(client=self.client)

    async def get_session_for_user(self) -> Any:
        """Get a session for your user."""
        from .api.users.get_session_for_user import asyncio

        return await asyncio(client=self.client)

    async def get_user_shortlinks(self) -> Any:
        """Get the shortlinks for a user."""
        from .api.users.get_user_shortlinks import asyncio

        return await asyncio(client=self.client)

    async def create_user_shortlink(self) -> Any:
        """Create a shortlink for a user."""
        from .api.users.create_user_shortlink import asyncio

        return await asyncio(client=self.client)

    async def update_user_shortlink(self) -> Any:
        """Update a shortlink for a user."""
        from .api.users.update_user_shortlink import asyncio

        return await asyncio(client=self.client)

    async def delete_user_shortlink(self) -> Any:
        """Delete a shortlink for a user."""
        from .api.users.delete_user_shortlink import asyncio

        return await asyncio(client=self.client)

    async def list_users(self) -> Any:
        """List users."""
        from .api.users.list_users import asyncio

        return await asyncio(client=self.client)

    async def list_users_extended(self) -> Any:
        """List users with extended information."""
        from .api.users.list_users_extended import asyncio

        return await asyncio(client=self.client)

    async def get_user_extended(self) -> Any:
        """Get extended information about a user."""
        from .api.users.get_user_extended import asyncio

        return await asyncio(client=self.client)

    async def get_user(self) -> Any:
        """Get a user."""
        from .api.users.get_user import asyncio

        return await asyncio(client=self.client)

    async def update_subscription_for_user(self) -> Any:
        """Update a subscription for a user."""
        from .api.users.update_subscription_for_user import asyncio

        return await asyncio(client=self.client)

    async def put_public_form(self) -> Any:
        """Creates a new support/sales ticket from the website contact form. This endpoint is for untrusted"""
        from .api.users.put_public_form import asyncio

        return await asyncio(client=self.client)

    async def put_public_subscribe(self) -> Any:
        """Subscribes a user to the newsletter."""
        from .api.users.put_public_subscribe import asyncio

        return await asyncio(client=self.client)


class ApiTokensAPI:
    """API for api_tokens endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def list_api_tokens_for_user(self) -> Any:
        """List API tokens for your user."""
        from .api.api_tokens.list_api_tokens_for_user import sync

        return sync(client=self.client)

    def create_api_token_for_user(self) -> Any:
        """Create a new API token for your user."""
        from .api.api_tokens.create_api_token_for_user import sync

        return sync(client=self.client)

    def get_api_token_for_user(self) -> Any:
        """Get an API token for your user."""
        from .api.api_tokens.get_api_token_for_user import sync

        return sync(client=self.client)

    def delete_api_token_for_user(self) -> Any:
        """Delete an API token for your user."""
        from .api.api_tokens.delete_api_token_for_user import sync

        return sync(client=self.client)


class AsyncApiTokensAPI:
    """Async API for api_tokens endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    async def list_api_tokens_for_user(self) -> Any:
        """List API tokens for your user."""
        from .api.api_tokens.list_api_tokens_for_user import asyncio

        return await asyncio(client=self.client)

    async def create_api_token_for_user(self) -> Any:
        """Create a new API token for your user."""
        from .api.api_tokens.create_api_token_for_user import asyncio

        return await asyncio(client=self.client)

    async def get_api_token_for_user(self) -> Any:
        """Get an API token for your user."""
        from .api.api_tokens.get_api_token_for_user import asyncio

        return await asyncio(client=self.client)

    async def delete_api_token_for_user(self) -> Any:
        """Delete an API token for your user."""
        from .api.api_tokens.delete_api_token_for_user import asyncio

        return await asyncio(client=self.client)


class ModelingAPI:
    """API for modeling endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def modeling_commands_ws(
        self,
        fps: int,
        post_effect: PostEffectType,
        show_grid: bool,
        unlocked_framerate: bool,
        video_res_height: int,
        video_res_width: int,
        webrtc: bool,
        api_call_id: Optional[str] = None,
        pool: Optional[str] = None,
        replay: Optional[str] = None,
    ) -> "WebSocketModelingCommandsWs":
        """Open a websocket which accepts modeling commands.

        Returns a WebSocket wrapper with methods for sending/receiving data.
        """
        return WebSocketModelingCommandsWs(
            fps,
            post_effect,
            show_grid,
            unlocked_framerate,
            video_res_height,
            video_res_width,
            webrtc,
            api_call_id,
            pool,
            replay,
            client=self.client,
        )


class AsyncModelingAPI:
    """Async API for modeling endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def modeling_commands_ws(
        self,
        fps: int,
        post_effect: PostEffectType,
        show_grid: bool,
        unlocked_framerate: bool,
        video_res_height: int,
        video_res_width: int,
        webrtc: bool,
        api_call_id: Optional[str] = None,
        pool: Optional[str] = None,
        replay: Optional[str] = None,
    ) -> "WebSocketModelingCommandsWs":
        """Open a websocket which accepts modeling commands.

        Returns a WebSocket wrapper with methods for sending/receiving data.
        Note: WebSocket connections are synchronous even in AsyncKittyCAD
        """
        return WebSocketModelingCommandsWs(
            fps,
            post_effect,
            show_grid,
            unlocked_framerate,
            video_res_height,
            video_res_width,
            webrtc,
            api_call_id,
            pool,
            replay,
            client=self.client,
        )


class WebSocketMlCopilotWs:
    """A websocket connection for ml_copilot_ws."""

    ws: ClientConnectionSync

    def __init__(self, *, client: Client):
        from .api.ml.ml_copilot_ws import sync

        self.ws = sync(client=client)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __iter__(self):
        """
        Iterate on incoming messages.

        The iterator calls recv() and yields messages in an infinite loop.

        It exits when the connection is closed normally. It raises a
        ConnectionClosedError exception after a protocol error or a network failure.
        """
        for message in self.ws:
            yield WebSocketResponse(**json.loads(message))

    def send(self, data: WebSocketRequest):
        """Send data to the websocket."""
        self.ws.send(json.dumps(data.model_dump()))

    def send_binary(self, data: WebSocketRequest):
        """Send data as bson to the websocket."""
        self.ws.send(bson.encode(data.model_dump()))

    def recv(self) -> WebSocketResponse:
        """Receive data from the websocket."""
        message = self.ws.recv(timeout=60)
        return WebSocketResponse(**json.loads(message))

    def close(self):
        """Close the websocket."""
        self.ws.close()


class WebSocketMlReasoningWs:
    """A websocket connection for ml_reasoning_ws."""

    ws: ClientConnectionSync

    def __init__(self, id: str, *, client: Client):
        from .api.ml.ml_reasoning_ws import sync

        self.ws = sync(id, client=client)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __iter__(self):
        """
        Iterate on incoming messages.

        The iterator calls recv() and yields messages in an infinite loop.

        It exits when the connection is closed normally. It raises a
        ConnectionClosedError exception after a protocol error or a network failure.
        """
        for message in self.ws:
            yield WebSocketResponse(**json.loads(message))

    def send(self, data: WebSocketRequest):
        """Send data to the websocket."""
        self.ws.send(json.dumps(data.model_dump()))

    def send_binary(self, data: WebSocketRequest):
        """Send data as bson to the websocket."""
        self.ws.send(bson.encode(data.model_dump()))

    def recv(self) -> WebSocketResponse:
        """Receive data from the websocket."""
        message = self.ws.recv(timeout=60)
        return WebSocketResponse(**json.loads(message))

    def close(self):
        """Close the websocket."""
        self.ws.close()


class WebSocketModelingCommandsWs:
    """A websocket connection for modeling_commands_ws."""

    ws: ClientConnectionSync

    def __init__(
        self,
        fps: int,
        post_effect: PostEffectType,
        show_grid: bool,
        unlocked_framerate: bool,
        video_res_height: int,
        video_res_width: int,
        webrtc: bool,
        api_call_id: Optional[str] = None,
        pool: Optional[str] = None,
        replay: Optional[str] = None,
        *,
        client: Client,
    ):
        from .api.modeling.modeling_commands_ws import sync

        self.ws = sync(
            fps,
            post_effect,
            show_grid,
            unlocked_framerate,
            video_res_height,
            video_res_width,
            webrtc,
            api_call_id,
            pool,
            replay,
            client=client,
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __iter__(self):
        """
        Iterate on incoming messages.

        The iterator calls recv() and yields messages in an infinite loop.

        It exits when the connection is closed normally. It raises a
        ConnectionClosedError exception after a protocol error or a network failure.
        """
        for message in self.ws:
            yield WebSocketResponse(**json.loads(message))

    def send(self, data: WebSocketRequest):
        """Send data to the websocket."""
        self.ws.send(json.dumps(data.model_dump()))

    def send_binary(self, data: WebSocketRequest):
        """Send data as bson to the websocket."""
        self.ws.send(bson.encode(data.model_dump()))

    def recv(self) -> WebSocketResponse:
        """Receive data from the websocket."""
        message = self.ws.recv(timeout=60)
        return WebSocketResponse(**json.loads(message))

    def close(self):
        """Close the websocket."""
        self.ws.close()


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

        # Also check for ZOO_HOST environment variable if no base_url provided
        if "base_url" not in kwargs:
            zoo_host = os.getenv("ZOO_HOST")
            if zoo_host:
                kwargs["base_url"] = zoo_host

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

        # Also check for ZOO_HOST environment variable if no base_url provided
        if "base_url" not in kwargs:
            zoo_host = os.getenv("ZOO_HOST")
            if zoo_host:
                kwargs["base_url"] = zoo_host

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
