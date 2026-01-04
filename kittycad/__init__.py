"""The KittyCAD Python SDK"""

import json
import os
from typing import Any, Callable, Dict, List, Optional, Union

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

from kittycad._binary import upload_file_binary, upload_file_binary_async
from kittycad._downloads import stream_download, stream_download_async
from kittycad._io_types import ProgressCallback, SyncDownload, SyncUpload
from kittycad._multipart import (
    upload_file_multipart,
    upload_file_multipart_async,
    upload_json_multipart,
    upload_json_multipart_async,
)

from .client import AsyncClient, Client
from .exceptions import (
    KittyCADAPIError,
    KittyCADClientError,
    KittyCADConnectionError,
    KittyCADError,
    KittyCADServerError,
    KittyCADTimeoutError,
)
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
from .models.async_api_call_output import AsyncApiCallOutput
from .models.async_api_call_results_page import AsyncApiCallResultsPage
from .models.auth_api_key_response import AuthApiKeyResponse
from .models.auth_callback import AuthCallback
from .models.billing_info import BillingInfo
from .models.code_language import CodeLanguage
from .models.code_option import CodeOption
from .models.code_output import CodeOutput
from .models.conversation_results_page import ConversationResultsPage
from .models.conversion_params import ConversionParams
from .models.conversion_sort_mode import ConversionSortMode
from .models.create_custom_model import CreateCustomModel
from .models.create_org_dataset import CreateOrgDataset
from .models.create_shortlink_request import CreateShortlinkRequest
from .models.create_shortlink_response import CreateShortlinkResponse
from .models.created_at_sort_mode import CreatedAtSortMode
from .models.crm_data import CrmData
from .models.custom_model import CustomModel
from .models.customer import Customer
from .models.customer_balance import CustomerBalance
from .models.dataset_s3_policies import DatasetS3Policies
from .models.device_access_token_request_form import DeviceAccessTokenRequestForm
from .models.device_auth_confirm_params import DeviceAuthConfirmParams
from .models.device_auth_request_form import DeviceAuthRequestForm
from .models.discount_code import DiscountCode
from .models.email_authentication_form import EmailAuthenticationForm
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
from .models.oauth2_client_info import OAuth2ClientInfo
from .models.org import Org
from .models.org_admin_details import OrgAdminDetails
from .models.org_dataset import OrgDataset
from .models.org_dataset_conversion_stats_response import (
    OrgDatasetConversionStatsResponse,
)
from .models.org_dataset_file_conversion import OrgDatasetFileConversion
from .models.org_dataset_file_conversion_details import OrgDatasetFileConversionDetails
from .models.org_dataset_file_conversion_summary_results_page import (
    OrgDatasetFileConversionSummaryResultsPage,
)
from .models.org_dataset_results_page import OrgDatasetResultsPage
from .models.org_details import OrgDetails
from .models.org_member import OrgMember
from .models.org_member_results_page import OrgMemberResultsPage
from .models.org_results_page import OrgResultsPage
from .models.payment_intent import PaymentIntent
from .models.payment_method import PaymentMethod
from .models.pong import Pong
from .models.post_effect_type import PostEffectType
from .models.price_upsert_request import PriceUpsertRequest
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
from .models.subscription_plan_price_record import SubscriptionPlanPriceRecord
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
from .models.token_revoke_request_form import TokenRevokeRequestForm
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
from .models.update_custom_model import UpdateCustomModel
from .models.update_member_to_org_body import UpdateMemberToOrgBody
from .models.update_org_dataset import UpdateOrgDataset
from .models.update_payment_balance import UpdatePaymentBalance
from .models.update_shortlink_request import UpdateShortlinkRequest
from .models.update_user import UpdateUser
from .models.user import User
from .models.user_admin_details import UserAdminDetails
from .models.user_feature_list import UserFeatureList
from .models.user_identifier import UserIdentifier
from .models.user_org_info import UserOrgInfo
from .models.user_org_role import UserOrgRole
from .models.user_results_page import UserResultsPage
from .models.uuid import Uuid
from .models.verification_token_response import VerificationTokenResponse

# Import WebSocket-related models that may be referenced by endpoints
from .models.web_socket_request import WebSocketRequest
from .models.web_socket_response import WebSocketResponse
from .models.zoo_product_subscriptions import ZooProductSubscriptions
from .models.zoo_product_subscriptions_org_request import (
    ZooProductSubscriptionsOrgRequest,
)
from .models.zoo_product_subscriptions_user_request import (
    ZooProductSubscriptionsUserRequest,
)
from .pagination import AsyncPageIterator, SyncPageIterator
from .response_helpers import raise_for_status


class MetaAPI:
    """API for meta endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_schema(
        self,
    ) -> Dict:
        """Get OpenAPI schema."""

        url = "{}/".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(Dict).validate_python(json_data)

    def get_ipinfo(
        self,
    ) -> IpAddrInfo:
        """Get ip address information."""

        url = "{}/_meta/ipinfo".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return IpAddrInfo.model_validate(json_data)

    def community_sso(
        self,
        sig: str,
        sso: str,
    ):
        """Authorize an inbound auth request from our Community page."""

        url = "{}/community/sso".format(self.client.base_url)

        if sig is not None:
            if "?" in url:
                url = url + "&sig=" + str(sig)
            else:
                url = url + "?sig=" + str(sig)

        if sso is not None:
            if "?" in url:
                url = url + "&sso=" + str(sso)
            else:
                url = url + "?sso=" + str(sso)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def create_debug_uploads(
        self,
    ) -> List[str]:
        """Do NOT send files here that you don't want to be public."""

        url = "{}/debug/uploads".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(List[str]).validate_python(json_data)

    def create_event(
        self,
        body: Event,
    ):
        """We collect anonymous telemetry data for improving our product."""

        url = "{}/events".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def internal_get_api_token_for_discord_user(
        self,
        discord_id: str,
    ) -> ApiToken:
        """This endpoint allows us to run API calls from our discord bot on behalf of a user. The user must have a discord account linked to their Zoo Account via oauth2 for this to work.

        You must be a Zoo admin to use this endpoint."""

        url = "{}/internal/discord/api-token/{discord_id}".format(
            self.client.base_url, discord_id=discord_id
        )

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ApiToken.model_validate(json_data)

    def ping(
        self,
    ) -> Pong:
        """Return pong."""

        url = "{}/ping".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Pong.model_validate(json_data)

    def get_pricing_subscriptions(
        self,
    ) -> Dict:
        """This is the ultimate source of truth for the pricing of our subscriptions."""

        url = "{}/pricing/subscriptions".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(Dict).validate_python(json_data)


class AsyncMetaAPI:
    """Async API for meta endpoints"""

    def __init__(self, client: AsyncClient) -> None:
        self.client = client

    async def get_schema(
        self,
    ) -> Dict:
        """Get OpenAPI schema."""

        url = "{}/".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(Dict).validate_python(json_data)

    async def get_ipinfo(
        self,
    ) -> IpAddrInfo:
        """Get ip address information."""

        url = "{}/_meta/ipinfo".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return IpAddrInfo.model_validate(json_data)

    async def community_sso(
        self,
        sig: str,
        sso: str,
    ):
        """Authorize an inbound auth request from our Community page."""

        url = "{}/community/sso".format(self.client.base_url)

        if sig is not None:
            if "?" in url:
                url = url + "&sig=" + str(sig)
            else:
                url = url + "?sig=" + str(sig)

        if sso is not None:
            if "?" in url:
                url = url + "&sso=" + str(sso)
            else:
                url = url + "?sso=" + str(sso)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def create_debug_uploads(
        self,
    ) -> List[str]:
        """Do NOT send files here that you don't want to be public."""

        url = "{}/debug/uploads".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(List[str]).validate_python(json_data)

    async def create_event(
        self,
        body: Event,
    ):
        """We collect anonymous telemetry data for improving our product."""

        url = "{}/events".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def internal_get_api_token_for_discord_user(
        self,
        discord_id: str,
    ) -> ApiToken:
        """This endpoint allows us to run API calls from our discord bot on behalf of a user. The user must have a discord account linked to their Zoo Account via oauth2 for this to work.

        You must be a Zoo admin to use this endpoint."""

        url = "{}/internal/discord/api-token/{discord_id}".format(
            self.client.base_url, discord_id=discord_id
        )

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ApiToken.model_validate(json_data)

    async def ping(
        self,
    ) -> Pong:
        """Return pong."""

        url = "{}/ping".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Pong.model_validate(json_data)

    async def get_pricing_subscriptions(
        self,
    ) -> Dict:
        """This is the ultimate source of truth for the pricing of our subscriptions."""

        url = "{}/pricing/subscriptions".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(Dict).validate_python(json_data)


class MlAPI:
    """API for ml endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def create_text_to_cad(
        self,
        output_format: FileExportFormat,
        body: TextToCadCreateBody,
        *,
        kcl: Optional[bool] = None,
    ) -> TextToCad:
        """Because our source of truth for the resulting model is a STEP file, you will always have STEP file contents when you list your generated parts. Any other formats you request here will also be returned when you list your generated parts.

        This operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint.

        One thing to note, if you hit the cache, this endpoint will return right away. So you only have to wait if the status is not `Completed` or `Failed`."""

        url = "{}/ai/text-to-cad/{output_format}".format(
            self.client.base_url, output_format=output_format
        )

        if kcl is not None:
            if "?" in url:
                url = url + "&kcl=" + str(kcl).lower()
            else:
                url = url + "?kcl=" + str(kcl).lower()

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return TextToCad.model_validate(json_data)

    def list_ml_prompts(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "SyncPageIterator":
        """For text-to-cad prompts, this will always return the STEP file contents as well as the format the user originally requested.

        This endpoint requires authentication by a Zoo employee.

        The ML prompts are returned in order of creation, with the most recently created ML prompts first.

                Returns an iterator that automatically handles pagination.
                Iterate over all items across all pages:

                    for item in client.ml-prompts.list_ml_prompts():
                        print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import SyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        def fetch_page(**kw):
            return self._fetch_page_list_ml_prompts(**kw)

        # Create the page iterator
        return SyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    def _fetch_page_list_ml_prompts(self, **kwargs) -> MlPromptResultsPage:
        """Internal method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/ml-prompts".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return MlPromptResultsPage.model_validate(json_data)

    def get_ml_prompt(
        self,
        id: str,
    ) -> MlPrompt:
        """This endpoint requires authentication by a Zoo employee."""

        url = "{}/ml-prompts/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return MlPrompt.model_validate(json_data)

    def list_conversations_for_user(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "SyncPageIterator":
        """This endpoint requires authentication by any Zoo user. It returns the conversations for the authenticated user.

        The conversations are returned in order of creation, with the most recently created conversations first.

                Returns an iterator that automatically handles pagination.
                Iterate over all items across all pages:

                    for item in client.ml.list_conversations_for_user():
                        print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import SyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        def fetch_page(**kw):
            return self._fetch_page_list_conversations_for_user(**kw)

        # Create the page iterator
        return SyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    def _fetch_page_list_conversations_for_user(
        self, **kwargs
    ) -> ConversationResultsPage:
        """Internal method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/ml/conversations".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ConversationResultsPage.model_validate(json_data)

    def create_proprietary_to_kcl(
        self,
        *,
        code_option: Optional[CodeOption] = None,
    ) -> KclModel:
        """This endpoint is used to convert a proprietary CAD format to KCL. The file passed MUST have feature tree data.

        A STEP file does not have feature tree data, so it will not work. A sldprt file does have feature tree data, so it will work.

        This endpoint is designed to work with any native proprietary CAD format, for example: - SolidWorks (.sldprt) - Creo (.prt) - Catia (.catpart) - NX (.prt) - Fusion 360 (.f3d)

        This endpoint is deterministic, it preserves the original design intent by using the feature tree data. This endpoint does not use any machine learning or AI.

        This endpoint is currently in beta, and is only available to users with access to the feature. Please contact support if you are interested in getting access.

        This endpoint might have limitations and bugs, please report any issues you encounter. It will be improved over time.

        Input filepaths will be normalized and re-canonicalized to be under the current working directory -- so returned paths may differ from provided paths, and care must be taken when handling user provided paths."""

        url = "{}/ml/convert/proprietary-to-kcl".format(self.client.base_url)

        if code_option is not None:
            if "?" in url:
                url = url + "&code_option=" + str(code_option)
            else:
                url = url + "?code_option=" + str(code_option)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return KclModel.model_validate(json_data)

    def create_custom_model(
        self,
        body: CreateCustomModel,
    ) -> CustomModel:
        """Dataset readiness is enforced via `OrgDatasetFileConversion::status_counts_for_datasets`: - At least one conversion must have status `success`. - No conversions may remain in `queued`. If even a single file is still queued the dataset is treated as “not ready for training.” - A dataset consisting only of `canceled` or `error_*` entries is rejected because there’s nothing usable."""

        url = "{}/ml/custom/models".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CustomModel.model_validate(json_data)

    def get_custom_model(
        self,
        id: Uuid,
    ) -> CustomModel:
        """Retrieve the details of a single custom ML model so long as it belongs to the caller’s organization."""

        url = "{}/ml/custom/models/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CustomModel.model_validate(json_data)

    def update_custom_model(
        self,
        id: Uuid,
        body: UpdateCustomModel,
    ) -> CustomModel:
        """Update mutable metadata (name, system prompt) for a custom ML model owned by the caller's organization."""

        url = "{}/ml/custom/models/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CustomModel.model_validate(json_data)

    def list_org_datasets_for_model(
        self,
        id: Uuid,
    ) -> List[OrgDataset]:
        """List the org datasets that are currently attached to a custom ML model owned by the caller’s organization."""

        url = "{}/ml/custom/models/{id}/datasets".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(List[OrgDataset]).validate_python(json_data)

    def create_kcl_code_completions(
        self,
        body: KclCodeCompletionRequest,
    ) -> KclCodeCompletionResponse:
        """Generate code completions for KCL."""

        url = "{}/ml/kcl/completions".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return KclCodeCompletionResponse.model_validate(json_data)

    def create_text_to_cad_iteration(
        self,
        body: TextToCadIterationBody,
    ) -> TextToCadIteration:
        """Even if you give specific ranges to edit, the model might change more than just those in order to make the changes you requested without breaking the code.

        You always get the whole code back, even if you only changed a small part of it.

        This operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint.

        This endpoint will soon be deprecated in favor of the `/ml/text-to-cad/multi-file/iteration` endpoint. In that the endpoint path will remain but it will have the same behavior as `ml/text-to-cad/multi-file/iteration`."""

        url = "{}/ml/text-to-cad/iteration".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return TextToCadIteration.model_validate(json_data)

    def create_text_to_cad_multi_file_iteration(
        self,
        body: TextToCadMultiFileIterationBody,
        file_attachments: Dict[str, SyncUpload],
    ) -> TextToCadMultiFileIteration:
        """This endpoint can iterate on multi-file projects.

        Even if you give specific ranges to edit, the model might change more than just those in order to make the changes you requested without breaking the code.

        You always get the whole code back, even if you only changed a small part of it. This endpoint will always return all the code back, including files that were not changed. If your original source code imported a stl/gltf/step/etc file, the output will not include that file since the model will never change non-kcl files. The endpoint will only return the kcl files that were changed.

        This operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint.

        Input filepaths will be normalized and re-canonicalized to be under the current working directory -- so returned paths may differ from provided paths, and care must be taken when handling user provided paths.

        Examples:
            Basic usage with file attachments:

            ```python
            from pathlib import Path
            from kittycad.models.text_to_cad_multi_file_iteration_body import TextToCadMultiFileIterationBody

            # Create the request body
            body = TextToCadMultiFileIterationBody(
                # Add your parameters here
            )

            # Prepare file attachments
            file_attachments = {
                "main.kcl": Path("path/to/main.kcl"),
                "helper.kcl": Path("path/to/helper.kcl"),
            }

            # Make the request
            result = client.create_text_to_cad_multi_file_iteration(
                body=body,
                file_attachments=file_attachments,
            )
            ```

            Using different file types:

            ```python
            from io import BytesIO

            # Mix of file paths and file-like objects
            file_attachments = {
                "main.kcl": Path("main.kcl"),
                "config.kcl": BytesIO(b"// KCL configuration"),
                "data.json": "path/to/data.json",
            }

            result = client.create_text_to_cad_multi_file_iteration(
                body=body,
                file_attachments=file_attachments,
            )
            ```
        """

        url = "{}/ml/text-to-cad/multi-file/iteration".format(self.client.base_url)

        _client = self.client.get_http_client()

        # JSON + multipart endpoint
        response = upload_json_multipart(
            client=_client,
            url=url,
            json_body=body,
            file_attachments=file_attachments,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return TextToCadMultiFileIteration.model_validate(json_data)

    def list_text_to_cad_parts_for_user(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
        conversation_id: Optional[Uuid] = None,
        no_models: Optional[bool] = None,
        no_parts: Optional[bool] = None,
    ) -> "SyncPageIterator":
        """This will always return the STEP file contents as well as the format the user originally requested.

        This endpoint requires authentication by any Zoo user. It returns the text-to-CAD parts for the authenticated user.

        The text-to-CAD parts are returned in order of creation, with the most recently created text-to-CAD parts first.

                Returns an iterator that automatically handles pagination.
                Iterate over all items across all pages:

                    for item in client.user.list_text_to_cad_parts_for_user():
                        print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import SyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        if conversation_id is not None:
            kwargs["conversation_id"] = conversation_id

        if no_models is not None:
            kwargs["no_models"] = no_models

        if no_parts is not None:
            kwargs["no_parts"] = no_parts

        def fetch_page(**kw):
            return self._fetch_page_list_text_to_cad_parts_for_user(**kw)

        # Create the page iterator
        return SyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    def _fetch_page_list_text_to_cad_parts_for_user(
        self, **kwargs
    ) -> TextToCadResponseResultsPage:
        """Internal method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/user/text-to-cad".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        if "conversation_id" in kwargs and kwargs["conversation_id"] is not None:
            if "?" in url:
                url = url + "&conversation_id=" + str(kwargs["conversation_id"])
            else:
                url = url + "?conversation_id=" + str(kwargs["conversation_id"])

        if "no_models" in kwargs and kwargs["no_models"] is not None:
            if "?" in url:
                url = url + "&no_models=" + str(kwargs["no_models"]).lower()
            else:
                url = url + "?no_models=" + str(kwargs["no_models"]).lower()

        if "no_parts" in kwargs and kwargs["no_parts"] is not None:
            if "?" in url:
                url = url + "&no_parts=" + str(kwargs["no_parts"]).lower()
            else:
                url = url + "?no_parts=" + str(kwargs["no_parts"]).lower()

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return TextToCadResponseResultsPage.model_validate(json_data)

    def get_text_to_cad_part_for_user(
        self,
        id: str,
    ) -> TextToCadResponse:
        """This endpoint requires authentication by any Zoo user. The user must be the owner of the text-to-CAD model."""

        url = "{}/user/text-to-cad/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return TextToCadResponse.model_validate(json_data)

    def create_text_to_cad_part_feedback(
        self,
        id: str,
        feedback: MlFeedback,
    ):
        """This can be a text-to-CAD creation or iteration.

        This endpoint requires authentication by any Zoo user. The user must be the owner of the ML response, in order to give feedback."""

        url = "{}/user/text-to-cad/{id}".format(self.client.base_url, id=id)

        if feedback is not None:
            if "?" in url:
                url = url + "&feedback=" + str(feedback)
            else:
                url = url + "?feedback=" + str(feedback)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def ml_copilot_ws(
        self,
        conversation_id: Optional[str] = None,
        replay: Optional[bool] = None,
        pr: Optional[int] = None,
        recv_timeout: Optional[float] = None,
        ws_factory: Optional[Callable[..., ClientConnectionSync]] = None,
    ) -> "WebSocketMlCopilotWs":
        """Open a websocket to prompt the ML copilot.

        Returns a WebSocket wrapper with methods for sending/receiving data.
        """
        return WebSocketMlCopilotWs(
            conversation_id=conversation_id,
            replay=replay,
            pr=pr,
            recv_timeout=recv_timeout,
            ws_factory=ws_factory,
            client=self.client,
        )

    def ml_reasoning_ws(
        self,
        id: str,
        recv_timeout: Optional[float] = None,
        ws_factory: Optional[Callable[..., ClientConnectionSync]] = None,
    ) -> "WebSocketMlReasoningWs":
        """Open a websocket to prompt the ML copilot.

        Returns a WebSocket wrapper with methods for sending/receiving data.
        """
        return WebSocketMlReasoningWs(
            id=id, recv_timeout=recv_timeout, ws_factory=ws_factory, client=self.client
        )


class AsyncMlAPI:
    """Async API for ml endpoints"""

    def __init__(self, client: AsyncClient) -> None:
        self.client = client

    async def create_text_to_cad(
        self,
        output_format: FileExportFormat,
        body: TextToCadCreateBody,
        *,
        kcl: Optional[bool] = None,
    ) -> TextToCad:
        """Because our source of truth for the resulting model is a STEP file, you will always have STEP file contents when you list your generated parts. Any other formats you request here will also be returned when you list your generated parts.

        This operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint.

        One thing to note, if you hit the cache, this endpoint will return right away. So you only have to wait if the status is not `Completed` or `Failed`."""

        url = "{}/ai/text-to-cad/{output_format}".format(
            self.client.base_url, output_format=output_format
        )

        if kcl is not None:
            if "?" in url:
                url = url + "&kcl=" + str(kcl).lower()
            else:
                url = url + "?kcl=" + str(kcl).lower()

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return TextToCad.model_validate(json_data)

    def list_ml_prompts(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "AsyncPageIterator":
        """For text-to-cad prompts, this will always return the STEP file contents as well as the format the user originally requested.

        This endpoint requires authentication by a Zoo employee.

        The ML prompts are returned in order of creation, with the most recently created ML prompts first.

                Returns an async iterator that automatically handles pagination.
                Iterate over all items across all pages:

                    async for item in client.ml-prompts.list_ml_prompts():
                        print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import AsyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        async def fetch_page(**kw):
            return await self._fetch_page_list_ml_prompts(**kw)

        # Create the async page iterator
        return AsyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    async def _fetch_page_list_ml_prompts(self, **kwargs) -> MlPromptResultsPage:
        """Internal async method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/ml-prompts".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return MlPromptResultsPage.model_validate(json_data)

    async def get_ml_prompt(
        self,
        id: str,
    ) -> MlPrompt:
        """This endpoint requires authentication by a Zoo employee."""

        url = "{}/ml-prompts/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return MlPrompt.model_validate(json_data)

    def list_conversations_for_user(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "AsyncPageIterator":
        """This endpoint requires authentication by any Zoo user. It returns the conversations for the authenticated user.

        The conversations are returned in order of creation, with the most recently created conversations first.

                Returns an async iterator that automatically handles pagination.
                Iterate over all items across all pages:

                    async for item in client.ml.list_conversations_for_user():
                        print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import AsyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        async def fetch_page(**kw):
            return await self._fetch_page_list_conversations_for_user(**kw)

        # Create the async page iterator
        return AsyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    async def _fetch_page_list_conversations_for_user(
        self, **kwargs
    ) -> ConversationResultsPage:
        """Internal async method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/ml/conversations".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ConversationResultsPage.model_validate(json_data)

    async def create_proprietary_to_kcl(
        self,
        *,
        code_option: Optional[CodeOption] = None,
    ) -> KclModel:
        """This endpoint is used to convert a proprietary CAD format to KCL. The file passed MUST have feature tree data.

        A STEP file does not have feature tree data, so it will not work. A sldprt file does have feature tree data, so it will work.

        This endpoint is designed to work with any native proprietary CAD format, for example: - SolidWorks (.sldprt) - Creo (.prt) - Catia (.catpart) - NX (.prt) - Fusion 360 (.f3d)

        This endpoint is deterministic, it preserves the original design intent by using the feature tree data. This endpoint does not use any machine learning or AI.

        This endpoint is currently in beta, and is only available to users with access to the feature. Please contact support if you are interested in getting access.

        This endpoint might have limitations and bugs, please report any issues you encounter. It will be improved over time.

        Input filepaths will be normalized and re-canonicalized to be under the current working directory -- so returned paths may differ from provided paths, and care must be taken when handling user provided paths."""

        url = "{}/ml/convert/proprietary-to-kcl".format(self.client.base_url)

        if code_option is not None:
            if "?" in url:
                url = url + "&code_option=" + str(code_option)
            else:
                url = url + "?code_option=" + str(code_option)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return KclModel.model_validate(json_data)

    async def create_custom_model(
        self,
        body: CreateCustomModel,
    ) -> CustomModel:
        """Dataset readiness is enforced via `OrgDatasetFileConversion::status_counts_for_datasets`: - At least one conversion must have status `success`. - No conversions may remain in `queued`. If even a single file is still queued the dataset is treated as “not ready for training.” - A dataset consisting only of `canceled` or `error_*` entries is rejected because there’s nothing usable."""

        url = "{}/ml/custom/models".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CustomModel.model_validate(json_data)

    async def get_custom_model(
        self,
        id: Uuid,
    ) -> CustomModel:
        """Retrieve the details of a single custom ML model so long as it belongs to the caller’s organization."""

        url = "{}/ml/custom/models/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CustomModel.model_validate(json_data)

    async def update_custom_model(
        self,
        id: Uuid,
        body: UpdateCustomModel,
    ) -> CustomModel:
        """Update mutable metadata (name, system prompt) for a custom ML model owned by the caller's organization."""

        url = "{}/ml/custom/models/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CustomModel.model_validate(json_data)

    async def list_org_datasets_for_model(
        self,
        id: Uuid,
    ) -> List[OrgDataset]:
        """List the org datasets that are currently attached to a custom ML model owned by the caller’s organization."""

        url = "{}/ml/custom/models/{id}/datasets".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(List[OrgDataset]).validate_python(json_data)

    async def create_kcl_code_completions(
        self,
        body: KclCodeCompletionRequest,
    ) -> KclCodeCompletionResponse:
        """Generate code completions for KCL."""

        url = "{}/ml/kcl/completions".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return KclCodeCompletionResponse.model_validate(json_data)

    async def create_text_to_cad_iteration(
        self,
        body: TextToCadIterationBody,
    ) -> TextToCadIteration:
        """Even if you give specific ranges to edit, the model might change more than just those in order to make the changes you requested without breaking the code.

        You always get the whole code back, even if you only changed a small part of it.

        This operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint.

        This endpoint will soon be deprecated in favor of the `/ml/text-to-cad/multi-file/iteration` endpoint. In that the endpoint path will remain but it will have the same behavior as `ml/text-to-cad/multi-file/iteration`."""

        url = "{}/ml/text-to-cad/iteration".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return TextToCadIteration.model_validate(json_data)

    async def create_text_to_cad_multi_file_iteration(
        self,
        body: TextToCadMultiFileIterationBody,
        file_attachments: Dict[str, SyncUpload],
    ) -> TextToCadMultiFileIteration:
        """This endpoint can iterate on multi-file projects.

        Even if you give specific ranges to edit, the model might change more than just those in order to make the changes you requested without breaking the code.

        You always get the whole code back, even if you only changed a small part of it. This endpoint will always return all the code back, including files that were not changed. If your original source code imported a stl/gltf/step/etc file, the output will not include that file since the model will never change non-kcl files. The endpoint will only return the kcl files that were changed.

        This operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint.

        Input filepaths will be normalized and re-canonicalized to be under the current working directory -- so returned paths may differ from provided paths, and care must be taken when handling user provided paths.

        Examples:
            Basic usage with file attachments:

            ```python
            from pathlib import Path
            from kittycad.models.text_to_cad_multi_file_iteration_body import TextToCadMultiFileIterationBody

            # Create the request body
            body = TextToCadMultiFileIterationBody(
                # Add your parameters here
            )

            # Prepare file attachments
            file_attachments = {
                "main.kcl": Path("path/to/main.kcl"),
                "helper.kcl": Path("path/to/helper.kcl"),
            }

            # Make the request
            result = client.create_text_to_cad_multi_file_iteration(
                body=body,
                file_attachments=file_attachments,
            )
            ```

            Using different file types:

            ```python
            from io import BytesIO

            # Mix of file paths and file-like objects
            file_attachments = {
                "main.kcl": Path("main.kcl"),
                "config.kcl": BytesIO(b"// KCL configuration"),
                "data.json": "path/to/data.json",
            }

            result = client.create_text_to_cad_multi_file_iteration(
                body=body,
                file_attachments=file_attachments,
            )
            ```
        """

        url = "{}/ml/text-to-cad/multi-file/iteration".format(self.client.base_url)

        _client = self.client.get_http_client()

        # JSON + multipart endpoint
        response = await upload_json_multipart_async(
            client=_client,
            url=url,
            json_body=body,
            file_attachments=file_attachments,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return TextToCadMultiFileIteration.model_validate(json_data)

    def list_text_to_cad_parts_for_user(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
        conversation_id: Optional[Uuid] = None,
        no_models: Optional[bool] = None,
        no_parts: Optional[bool] = None,
    ) -> "AsyncPageIterator":
        """This will always return the STEP file contents as well as the format the user originally requested.

        This endpoint requires authentication by any Zoo user. It returns the text-to-CAD parts for the authenticated user.

        The text-to-CAD parts are returned in order of creation, with the most recently created text-to-CAD parts first.

                Returns an async iterator that automatically handles pagination.
                Iterate over all items across all pages:

                    async for item in client.user.list_text_to_cad_parts_for_user():
                        print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import AsyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        if conversation_id is not None:
            kwargs["conversation_id"] = conversation_id

        if no_models is not None:
            kwargs["no_models"] = no_models

        if no_parts is not None:
            kwargs["no_parts"] = no_parts

        async def fetch_page(**kw):
            return await self._fetch_page_list_text_to_cad_parts_for_user(**kw)

        # Create the async page iterator
        return AsyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    async def _fetch_page_list_text_to_cad_parts_for_user(
        self, **kwargs
    ) -> TextToCadResponseResultsPage:
        """Internal async method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/user/text-to-cad".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        if "conversation_id" in kwargs and kwargs["conversation_id"] is not None:
            if "?" in url:
                url = url + "&conversation_id=" + str(kwargs["conversation_id"])
            else:
                url = url + "?conversation_id=" + str(kwargs["conversation_id"])

        if "no_models" in kwargs and kwargs["no_models"] is not None:
            if "?" in url:
                url = url + "&no_models=" + str(kwargs["no_models"]).lower()
            else:
                url = url + "?no_models=" + str(kwargs["no_models"]).lower()

        if "no_parts" in kwargs and kwargs["no_parts"] is not None:
            if "?" in url:
                url = url + "&no_parts=" + str(kwargs["no_parts"]).lower()
            else:
                url = url + "?no_parts=" + str(kwargs["no_parts"]).lower()

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return TextToCadResponseResultsPage.model_validate(json_data)

    async def get_text_to_cad_part_for_user(
        self,
        id: str,
    ) -> TextToCadResponse:
        """This endpoint requires authentication by any Zoo user. The user must be the owner of the text-to-CAD model."""

        url = "{}/user/text-to-cad/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return TextToCadResponse.model_validate(json_data)

    async def create_text_to_cad_part_feedback(
        self,
        id: str,
        feedback: MlFeedback,
    ):
        """This can be a text-to-CAD creation or iteration.

        This endpoint requires authentication by any Zoo user. The user must be the owner of the ML response, in order to give feedback."""

        url = "{}/user/text-to-cad/{id}".format(self.client.base_url, id=id)

        if feedback is not None:
            if "?" in url:
                url = url + "&feedback=" + str(feedback)
            else:
                url = url + "?feedback=" + str(feedback)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def ml_copilot_ws(
        self,
        conversation_id: Optional[str] = None,
        replay: Optional[bool] = None,
        pr: Optional[int] = None,
    ):
        """Open a websocket to prompt the ML copilot.

        Returns an async WebSocket connection for sending/receiving data.
        """

        # For async clients, return the raw async WebSocket connection
        # This supports await websocket.send() and async for message in websocket
        async def ml_copilot_ws(
            self,
            *,
            conversation_id: Optional[str] = None,
            replay: Optional[bool] = None,
            pr: Optional[int] = None,
        ) -> ClientConnectionAsync:
            """Open a websocket to prompt the ML copilot."""

            url = "/ws/ml/copilot"

            if conversation_id is not None:
                if "?" in url:
                    url = url + "&conversation_id=" + str(conversation_id)
                else:
                    url = url + "?conversation_id=" + str(conversation_id)

            if replay is not None:
                if "?" in url:
                    url = url + "&replay=" + str(replay).lower()
                else:
                    url = url + "?replay=" + str(replay).lower()

            if pr is not None:
                if "?" in url:
                    url = url + "&pr=" + str(pr)
                else:
                    url = url + "?pr=" + str(pr)

            return await ws_connect_async(
                url.replace("http", "ws"),
                extra_headers=self.client.get_headers(),
                close_timeout=120,
                max_size=None,
            )

    async def ml_reasoning_ws(self, id: str):
        """Open a websocket to prompt the ML copilot.

        Returns an async WebSocket connection for sending/receiving data.
        """

        # For async clients, return the raw async WebSocket connection
        # This supports await websocket.send() and async for message in websocket
        async def ml_reasoning_ws(
            self,
            id: str,
        ) -> ClientConnectionAsync:
            """Open a websocket to prompt the ML copilot."""

            url = "/ws/ml/reasoning/{id}".format(id=id)

            return await ws_connect_async(
                url.replace("http", "ws"),
                extra_headers=self.client.get_headers(),
                close_timeout=120,
                max_size=None,
            )


class ApiCallsAPI:
    """API for api_calls endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_api_call_metrics(
        self,
        group_by: ApiCallQueryGroupBy,
    ) -> List[ApiCallQueryGroup]:
        """This endpoint requires authentication by a Zoo employee. The API calls are grouped by the parameter passed."""

        url = "{}/api-call-metrics".format(self.client.base_url)

        if group_by is not None:
            if "?" in url:
                url = url + "&group_by=" + str(group_by)
            else:
                url = url + "?group_by=" + str(group_by)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(List[ApiCallQueryGroup]).validate_python(json_data)

    def list_api_calls(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "SyncPageIterator":
        """This endpoint requires authentication by a Zoo employee. The API calls are returned in order of creation, with the most recently created API calls first.

        Returns an iterator that automatically handles pagination.
        Iterate over all items across all pages:

            for item in client.api-calls.list_api_calls():
                print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import SyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        def fetch_page(**kw):
            return self._fetch_page_list_api_calls(**kw)

        # Create the page iterator
        return SyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    def _fetch_page_list_api_calls(self, **kwargs) -> ApiCallWithPriceResultsPage:
        """Internal method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/api-calls".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ApiCallWithPriceResultsPage.model_validate(json_data)

    def get_api_call(
        self,
        id: str,
    ) -> ApiCallWithPrice:
        """This endpoint requires authentication by any Zoo user. It returns details of the requested API call for the user.

        If the user is not authenticated to view the specified API call, then it is not returned.

        Only Zoo employees can view API calls for other users."""

        url = "{}/api-calls/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ApiCallWithPrice.model_validate(json_data)

    def list_async_operations(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
        status: Optional[ApiCallStatus] = None,
    ) -> "SyncPageIterator":
        """For async file conversion operations, this endpoint does not return the contents of converted files (`output`). To get the contents use the `/async/operations/{id}` endpoint.

        This endpoint requires authentication by a Zoo employee.

                Returns an iterator that automatically handles pagination.
                Iterate over all items across all pages:

                    for item in client.async.list_async_operations():
                        print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import SyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        if status is not None:
            kwargs["status"] = status

        def fetch_page(**kw):
            return self._fetch_page_list_async_operations(**kw)

        # Create the page iterator
        return SyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    def _fetch_page_list_async_operations(self, **kwargs) -> AsyncApiCallResultsPage:
        """Internal method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/async/operations".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        if "status" in kwargs and kwargs["status"] is not None:
            if "?" in url:
                url = url + "&status=" + str(kwargs["status"])
            else:
                url = url + "?status=" + str(kwargs["status"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return AsyncApiCallResultsPage.model_validate(json_data)

    def get_async_operation(
        self,
        id: str,
    ) -> AsyncApiCallOutput:
        """Get the status and output of an async operation.

        This endpoint requires authentication by any Zoo user. It returns details of the requested async operation for the user.

        If the user is not authenticated to view the specified async operation, then it is not returned.

        Only Zoo employees with the proper access can view async operations for other users."""

        url = "{}/async/operations/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return AsyncApiCallOutput.model_validate(json_data)

    def org_list_api_calls(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "SyncPageIterator":
        """This includes all API calls that were made by users in the org.

        This endpoint requires authentication by an org admin. It returns the API calls for the authenticated user's org.

        The API calls are returned in order of creation, with the most recently created API calls first.

                Returns an iterator that automatically handles pagination.
                Iterate over all items across all pages:

                    for item in client.org.org_list_api_calls():
                        print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import SyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        def fetch_page(**kw):
            return self._fetch_page_org_list_api_calls(**kw)

        # Create the page iterator
        return SyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    def _fetch_page_org_list_api_calls(self, **kwargs) -> ApiCallWithPriceResultsPage:
        """Internal method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/org/api-calls".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ApiCallWithPriceResultsPage.model_validate(json_data)

    def get_api_call_for_org(
        self,
        id: str,
    ) -> ApiCallWithPrice:
        """This endpoint requires authentication by an org admin. It returns details of the requested API call for the user's org."""

        url = "{}/org/api-calls/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ApiCallWithPrice.model_validate(json_data)

    def user_list_api_calls(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "SyncPageIterator":
        """This endpoint requires authentication by any Zoo user. It returns the API calls for the authenticated user.

        The API calls are returned in order of creation, with the most recently created API calls first.

                Returns an iterator that automatically handles pagination.
                Iterate over all items across all pages:

                    for item in client.user.user_list_api_calls():
                        print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import SyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        def fetch_page(**kw):
            return self._fetch_page_user_list_api_calls(**kw)

        # Create the page iterator
        return SyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    def _fetch_page_user_list_api_calls(self, **kwargs) -> ApiCallWithPriceResultsPage:
        """Internal method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/user/api-calls".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ApiCallWithPriceResultsPage.model_validate(json_data)

    def get_api_call_for_user(
        self,
        id: str,
    ) -> ApiCallWithPrice:
        """This endpoint requires authentication by any Zoo user. It returns details of the requested API call for the user."""

        url = "{}/user/api-calls/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ApiCallWithPrice.model_validate(json_data)

    def list_api_calls_for_user(
        self,
        id: UserIdentifier,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "SyncPageIterator":
        """This endpoint requires authentication by any Zoo user. It returns the API calls for the authenticated user if "me" is passed as the user id.

        Alternatively, you can use the `/user/api-calls` endpoint to get the API calls for your user.

        If the authenticated user is a Zoo employee, then the API calls are returned for the user specified by the user id.

        The API calls are returned in order of creation, with the most recently created API calls first.

                Returns an iterator that automatically handles pagination.
                Iterate over all items across all pages:

                    for item in client.users.list_api_calls_for_user():
                        print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import SyncPageIterator

        # Store path parameters in closure for later use

        _id = id

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        def fetch_page(**kw):
            return self._fetch_page_list_api_calls_for_user(id=_id, **kw)

        # Create the page iterator
        return SyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    def _fetch_page_list_api_calls_for_user(
        self, id: UserIdentifier, **kwargs
    ) -> ApiCallWithPriceResultsPage:
        """Internal method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/users/{id}/api-calls".format(self.client.base_url, id=id)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ApiCallWithPriceResultsPage.model_validate(json_data)


class AsyncApiCallsAPI:
    """Async API for api_calls endpoints"""

    def __init__(self, client: AsyncClient) -> None:
        self.client = client

    async def get_api_call_metrics(
        self,
        group_by: ApiCallQueryGroupBy,
    ) -> List[ApiCallQueryGroup]:
        """This endpoint requires authentication by a Zoo employee. The API calls are grouped by the parameter passed."""

        url = "{}/api-call-metrics".format(self.client.base_url)

        if group_by is not None:
            if "?" in url:
                url = url + "&group_by=" + str(group_by)
            else:
                url = url + "?group_by=" + str(group_by)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(List[ApiCallQueryGroup]).validate_python(json_data)

    def list_api_calls(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "AsyncPageIterator":
        """This endpoint requires authentication by a Zoo employee. The API calls are returned in order of creation, with the most recently created API calls first.

        Returns an async iterator that automatically handles pagination.
        Iterate over all items across all pages:

            async for item in client.api-calls.list_api_calls():
                print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import AsyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        async def fetch_page(**kw):
            return await self._fetch_page_list_api_calls(**kw)

        # Create the async page iterator
        return AsyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    async def _fetch_page_list_api_calls(self, **kwargs) -> ApiCallWithPriceResultsPage:
        """Internal async method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/api-calls".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ApiCallWithPriceResultsPage.model_validate(json_data)

    async def get_api_call(
        self,
        id: str,
    ) -> ApiCallWithPrice:
        """This endpoint requires authentication by any Zoo user. It returns details of the requested API call for the user.

        If the user is not authenticated to view the specified API call, then it is not returned.

        Only Zoo employees can view API calls for other users."""

        url = "{}/api-calls/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ApiCallWithPrice.model_validate(json_data)

    def list_async_operations(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
        status: Optional[ApiCallStatus] = None,
    ) -> "AsyncPageIterator":
        """For async file conversion operations, this endpoint does not return the contents of converted files (`output`). To get the contents use the `/async/operations/{id}` endpoint.

        This endpoint requires authentication by a Zoo employee.

                Returns an async iterator that automatically handles pagination.
                Iterate over all items across all pages:

                    async for item in client.async.list_async_operations():
                        print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import AsyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        if status is not None:
            kwargs["status"] = status

        async def fetch_page(**kw):
            return await self._fetch_page_list_async_operations(**kw)

        # Create the async page iterator
        return AsyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    async def _fetch_page_list_async_operations(
        self, **kwargs
    ) -> AsyncApiCallResultsPage:
        """Internal async method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/async/operations".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        if "status" in kwargs and kwargs["status"] is not None:
            if "?" in url:
                url = url + "&status=" + str(kwargs["status"])
            else:
                url = url + "?status=" + str(kwargs["status"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return AsyncApiCallResultsPage.model_validate(json_data)

    async def get_async_operation(
        self,
        id: str,
    ) -> AsyncApiCallOutput:
        """Get the status and output of an async operation.

        This endpoint requires authentication by any Zoo user. It returns details of the requested async operation for the user.

        If the user is not authenticated to view the specified async operation, then it is not returned.

        Only Zoo employees with the proper access can view async operations for other users."""

        url = "{}/async/operations/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return AsyncApiCallOutput.model_validate(json_data)

    def org_list_api_calls(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "AsyncPageIterator":
        """This includes all API calls that were made by users in the org.

        This endpoint requires authentication by an org admin. It returns the API calls for the authenticated user's org.

        The API calls are returned in order of creation, with the most recently created API calls first.

                Returns an async iterator that automatically handles pagination.
                Iterate over all items across all pages:

                    async for item in client.org.org_list_api_calls():
                        print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import AsyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        async def fetch_page(**kw):
            return await self._fetch_page_org_list_api_calls(**kw)

        # Create the async page iterator
        return AsyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    async def _fetch_page_org_list_api_calls(
        self, **kwargs
    ) -> ApiCallWithPriceResultsPage:
        """Internal async method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/org/api-calls".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ApiCallWithPriceResultsPage.model_validate(json_data)

    async def get_api_call_for_org(
        self,
        id: str,
    ) -> ApiCallWithPrice:
        """This endpoint requires authentication by an org admin. It returns details of the requested API call for the user's org."""

        url = "{}/org/api-calls/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ApiCallWithPrice.model_validate(json_data)

    def user_list_api_calls(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "AsyncPageIterator":
        """This endpoint requires authentication by any Zoo user. It returns the API calls for the authenticated user.

        The API calls are returned in order of creation, with the most recently created API calls first.

                Returns an async iterator that automatically handles pagination.
                Iterate over all items across all pages:

                    async for item in client.user.user_list_api_calls():
                        print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import AsyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        async def fetch_page(**kw):
            return await self._fetch_page_user_list_api_calls(**kw)

        # Create the async page iterator
        return AsyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    async def _fetch_page_user_list_api_calls(
        self, **kwargs
    ) -> ApiCallWithPriceResultsPage:
        """Internal async method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/user/api-calls".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ApiCallWithPriceResultsPage.model_validate(json_data)

    async def get_api_call_for_user(
        self,
        id: str,
    ) -> ApiCallWithPrice:
        """This endpoint requires authentication by any Zoo user. It returns details of the requested API call for the user."""

        url = "{}/user/api-calls/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ApiCallWithPrice.model_validate(json_data)

    def list_api_calls_for_user(
        self,
        id: UserIdentifier,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "AsyncPageIterator":
        """This endpoint requires authentication by any Zoo user. It returns the API calls for the authenticated user if "me" is passed as the user id.

        Alternatively, you can use the `/user/api-calls` endpoint to get the API calls for your user.

        If the authenticated user is a Zoo employee, then the API calls are returned for the user specified by the user id.

        The API calls are returned in order of creation, with the most recently created API calls first.

                Returns an async iterator that automatically handles pagination.
                Iterate over all items across all pages:

                    async for item in client.users.list_api_calls_for_user():
                        print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import AsyncPageIterator

        # Store path parameters in closure for later use

        _id = id

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        async def fetch_page(**kw):
            return await self._fetch_page_list_api_calls_for_user(id=_id, **kw)

        # Create the async page iterator
        return AsyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    async def _fetch_page_list_api_calls_for_user(
        self, id: UserIdentifier, **kwargs
    ) -> ApiCallWithPriceResultsPage:
        """Internal async method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/users/{id}/api-calls".format(self.client.base_url, id=id)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ApiCallWithPriceResultsPage.model_validate(json_data)


class AppsAPI:
    """API for apps endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def apps_github_callback(
        self,
    ):
        """This is different than OAuth 2.0 authentication for users. This endpoint grants access for Zoo to access user's repos.

        The user doesn't need Zoo OAuth authorization for this endpoint, this is purely for the GitHub permissions to access repos."""

        url = "{}/apps/github/callback".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def apps_github_consent(
        self,
    ) -> AppClientInfo:
        """This is different than OAuth 2.0 authentication for users. This endpoint grants access for Zoo to access user's repos.

        The user doesn't need Zoo OAuth authorization for this endpoint, this is purely for the GitHub permissions to access repos."""

        url = "{}/apps/github/consent".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return AppClientInfo.model_validate(json_data)

    def apps_github_webhook(
        self,
        body: bytes,
    ):
        """These come from the GitHub app."""

        url = "{}/apps/github/webhook".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body,
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None


class AsyncAppsAPI:
    """Async API for apps endpoints"""

    def __init__(self, client: AsyncClient) -> None:
        self.client = client

    async def apps_github_callback(
        self,
    ):
        """This is different than OAuth 2.0 authentication for users. This endpoint grants access for Zoo to access user's repos.

        The user doesn't need Zoo OAuth authorization for this endpoint, this is purely for the GitHub permissions to access repos."""

        url = "{}/apps/github/callback".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def apps_github_consent(
        self,
    ) -> AppClientInfo:
        """This is different than OAuth 2.0 authentication for users. This endpoint grants access for Zoo to access user's repos.

        The user doesn't need Zoo OAuth authorization for this endpoint, this is purely for the GitHub permissions to access repos."""

        url = "{}/apps/github/consent".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return AppClientInfo.model_validate(json_data)

    async def apps_github_webhook(
        self,
        body: bytes,
    ):
        """These come from the GitHub app."""

        url = "{}/apps/github/webhook".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body,
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None


class HiddenAPI:
    """API for hidden endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def auth_api_key(
        self,
    ) -> AuthApiKeyResponse:
        """This returns a session token."""

        url = "{}/auth/api-key".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return AuthApiKeyResponse.model_validate(json_data)

    def auth_email(
        self,
        body: EmailAuthenticationForm,
    ) -> VerificationTokenResponse:
        """Create an email verification request for a user."""

        url = "{}/auth/email".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return VerificationTokenResponse.model_validate(json_data)

    def auth_email_callback(
        self,
        email: str,
        token: str,
        *,
        callback_url: Optional[str] = None,
    ):
        """Listen for callbacks for email authentication for users."""

        url = "{}/auth/email/callback".format(self.client.base_url)

        if callback_url is not None:
            if "?" in url:
                url = url + "&callback_url=" + str(callback_url)
            else:
                url = url + "?callback_url=" + str(callback_url)

        if email is not None:
            if "?" in url:
                url = url + "&email=" + str(email)
            else:
                url = url + "?email=" + str(email)

        if token is not None:
            if "?" in url:
                url = url + "&token=" + str(token)
            else:
                url = url + "?token=" + str(token)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def get_auth_saml_by_org(
        self,
        org_id: Uuid,
        *,
        callback_url: Optional[str] = None,
    ):
        """Redirects the browser straight to the org’s SAML IdP."""

        url = "{}/auth/saml/org/{org_id}/login".format(
            self.client.base_url, org_id=org_id
        )

        if callback_url is not None:
            if "?" in url:
                url = url + "&callback_url=" + str(callback_url)
            else:
                url = url + "?callback_url=" + str(callback_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def get_auth_saml(
        self,
        provider_id: Uuid,
        *,
        callback_url: Optional[str] = None,
    ):
        """The UI uses this to avoid having to ask the API anything about the IdP. It already knows the SAML IdP ID from the path, so it can just link to this path and rely on the API to redirect to the actual IdP."""

        url = "{}/auth/saml/provider/{provider_id}/login".format(
            self.client.base_url, provider_id=provider_id
        )

        if callback_url is not None:
            if "?" in url:
                url = url + "&callback_url=" + str(callback_url)
            else:
                url = url + "?callback_url=" + str(callback_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def post_auth_saml(
        self,
        provider_id: Uuid,
        body: bytes,
    ):
        """Authenticate a user via SAML"""

        url = "{}/auth/saml/provider/{provider_id}/login".format(
            self.client.base_url, provider_id=provider_id
        )

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body,
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def logout(
        self,
    ):
        """This is used in logout scenarios."""

        url = "{}/logout".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def redirect_user_shortlink(
        self,
        key: str,
    ):
        """This endpoint might require authentication by a Zoo user. It gets the shortlink for the user and redirects them to the URL. If the shortlink is owned by an org, the user must be a member of the org."""

        url = "{}/user/shortlinks/{key}".format(self.client.base_url, key=key)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None


class AsyncHiddenAPI:
    """Async API for hidden endpoints"""

    def __init__(self, client: AsyncClient) -> None:
        self.client = client

    async def auth_api_key(
        self,
    ) -> AuthApiKeyResponse:
        """This returns a session token."""

        url = "{}/auth/api-key".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return AuthApiKeyResponse.model_validate(json_data)

    async def auth_email(
        self,
        body: EmailAuthenticationForm,
    ) -> VerificationTokenResponse:
        """Create an email verification request for a user."""

        url = "{}/auth/email".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return VerificationTokenResponse.model_validate(json_data)

    async def auth_email_callback(
        self,
        email: str,
        token: str,
        *,
        callback_url: Optional[str] = None,
    ):
        """Listen for callbacks for email authentication for users."""

        url = "{}/auth/email/callback".format(self.client.base_url)

        if callback_url is not None:
            if "?" in url:
                url = url + "&callback_url=" + str(callback_url)
            else:
                url = url + "?callback_url=" + str(callback_url)

        if email is not None:
            if "?" in url:
                url = url + "&email=" + str(email)
            else:
                url = url + "?email=" + str(email)

        if token is not None:
            if "?" in url:
                url = url + "&token=" + str(token)
            else:
                url = url + "?token=" + str(token)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def get_auth_saml_by_org(
        self,
        org_id: Uuid,
        *,
        callback_url: Optional[str] = None,
    ):
        """Redirects the browser straight to the org’s SAML IdP."""

        url = "{}/auth/saml/org/{org_id}/login".format(
            self.client.base_url, org_id=org_id
        )

        if callback_url is not None:
            if "?" in url:
                url = url + "&callback_url=" + str(callback_url)
            else:
                url = url + "?callback_url=" + str(callback_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def get_auth_saml(
        self,
        provider_id: Uuid,
        *,
        callback_url: Optional[str] = None,
    ):
        """The UI uses this to avoid having to ask the API anything about the IdP. It already knows the SAML IdP ID from the path, so it can just link to this path and rely on the API to redirect to the actual IdP."""

        url = "{}/auth/saml/provider/{provider_id}/login".format(
            self.client.base_url, provider_id=provider_id
        )

        if callback_url is not None:
            if "?" in url:
                url = url + "&callback_url=" + str(callback_url)
            else:
                url = url + "?callback_url=" + str(callback_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def post_auth_saml(
        self,
        provider_id: Uuid,
        body: bytes,
    ):
        """Authenticate a user via SAML"""

        url = "{}/auth/saml/provider/{provider_id}/login".format(
            self.client.base_url, provider_id=provider_id
        )

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body,
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def logout(
        self,
    ):
        """This is used in logout scenarios."""

        url = "{}/logout".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def redirect_user_shortlink(
        self,
        key: str,
    ):
        """This endpoint might require authentication by a Zoo user. It gets the shortlink for the user and redirects them to the URL. If the shortlink is owned by an org, the user must be a member of the org."""

        url = "{}/user/shortlinks/{key}".format(self.client.base_url, key=key)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None


class FileAPI:
    """API for file endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def create_file_center_of_mass(
        self,
        src_format: FileImportFormat,
        body: bytes,
        *,
        output_unit: Optional[UnitLength] = None,
    ) -> FileCenterOfMass:
        """We assume any file given to us has one consistent unit throughout. We also assume the file is at the proper scale.

        This endpoint returns the cartesian coordinate in world space measure units.

        In the future, we will use the units inside the file if they are given and do any conversions if necessary for the calculation. But currently, that is not supported.

        Get the center of mass of an object in a CAD file. If the file is larger than 25MB, it will be performed asynchronously.

        If the operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint."""

        url = "{}/file/center-of-mass".format(self.client.base_url)

        if output_unit is not None:
            if "?" in url:
                url = url + "&output_unit=" + str(output_unit)
            else:
                url = url + "?output_unit=" + str(output_unit)

        if src_format is not None:
            if "?" in url:
                url = url + "&src_format=" + str(src_format)
            else:
                url = url + "?src_format=" + str(src_format)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body,
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return FileCenterOfMass.model_validate(json_data)

    def create_file_conversion_options(
        self,
        body: ConversionParams,
        file_attachments: Dict[str, SyncUpload],
    ) -> FileConversion:
        """This takes a HTTP multipart body with these fields in any order:

         - The input and output format options (as JSON), name is 'body'.  - The files to convert, in raw binary. Must supply filenames.

        This starts a conversion job and returns the `id` of the operation. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint.

        Examples:
            Basic usage with file attachments:

            ```python
            from pathlib import Path
            from kittycad.models.conversion_params import ConversionParams

            # Create the request body
            body = ConversionParams(
                # Add your parameters here
            )

            # Prepare file attachments
            file_attachments = {
                "main.kcl": Path("path/to/main.kcl"),
                "helper.kcl": Path("path/to/helper.kcl"),
            }

            # Make the request
            result = client.create_file_conversion_options(
                body=body,
                file_attachments=file_attachments,
            )
            ```

            Using different file types:

            ```python
            from io import BytesIO

            # Mix of file paths and file-like objects
            file_attachments = {
                "main.kcl": Path("main.kcl"),
                "config.kcl": BytesIO(b"// KCL configuration"),
                "data.json": "path/to/data.json",
            }

            result = client.create_file_conversion_options(
                body=body,
                file_attachments=file_attachments,
            )
            ```
        """

        url = "{}/file/conversion".format(self.client.base_url)

        _client = self.client.get_http_client()

        # JSON + multipart endpoint
        response = upload_json_multipart(
            client=_client,
            url=url,
            json_body=body,
            file_attachments=file_attachments,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return FileConversion.model_validate(json_data)

    def create_file_conversion(
        self,
        output_format: FileExportFormat,
        src_format: FileImportFormat,
        body: bytes,
    ) -> FileConversion:
        """If you wish to specify the conversion options, use the `/file/conversion` endpoint instead.

        Convert a CAD file from one format to another. If the file being converted is larger than 25MB, it will be performed asynchronously.

        If the conversion is performed synchronously, the contents of the converted file (`output`) will be returned as a base64 encoded string.

        If the operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint."""

        url = "{}/file/conversion/{src_format}/{output_format}".format(
            self.client.base_url, output_format=output_format, src_format=src_format
        )

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body,
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return FileConversion.model_validate(json_data)

    def create_file_density(
        self,
        material_mass: float,
        src_format: FileImportFormat,
        body: bytes,
        *,
        material_mass_unit: Optional[UnitMass] = None,
        output_unit: Optional[UnitDensity] = None,
    ) -> FileDensity:
        """We assume any file given to us has one consistent unit throughout. We also assume the file is at the proper scale.

        This endpoint assumes if you are giving a material mass in a specific mass units, we return a density in mass unit per cubic measure unit.

        In the future, we will use the units inside the file if they are given and do any conversions if necessary for the calculation. But currently, that is not supported.

        Get the density of an object in a CAD file. If the file is larger than 25MB, it will be performed asynchronously.

        If the operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint."""

        url = "{}/file/density".format(self.client.base_url)

        if material_mass is not None:
            if "?" in url:
                url = url + "&material_mass=" + str(material_mass)
            else:
                url = url + "?material_mass=" + str(material_mass)

        if material_mass_unit is not None:
            if "?" in url:
                url = url + "&material_mass_unit=" + str(material_mass_unit)
            else:
                url = url + "?material_mass_unit=" + str(material_mass_unit)

        if output_unit is not None:
            if "?" in url:
                url = url + "&output_unit=" + str(output_unit)
            else:
                url = url + "?output_unit=" + str(output_unit)

        if src_format is not None:
            if "?" in url:
                url = url + "&src_format=" + str(src_format)
            else:
                url = url + "?src_format=" + str(src_format)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body,
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return FileDensity.model_validate(json_data)

    def create_file_mass(
        self,
        material_density: float,
        src_format: FileImportFormat,
        body: bytes,
        *,
        material_density_unit: Optional[UnitDensity] = None,
        output_unit: Optional[UnitMass] = None,
    ) -> FileMass:
        """We assume any file given to us has one consistent unit throughout. We also assume the file is at the proper scale.

        This endpoint assumes if you are giving a material density in a specific mass unit per cubic measure unit, we return a mass in mass units. The same mass units as passed in the material density.

        In the future, we will use the units inside the file if they are given and do any conversions if necessary for the calculation. But currently, that is not supported.

        Get the mass of an object in a CAD file. If the file is larger than 25MB, it will be performed asynchronously.

        If the operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint."""

        url = "{}/file/mass".format(self.client.base_url)

        if material_density is not None:
            if "?" in url:
                url = url + "&material_density=" + str(material_density)
            else:
                url = url + "?material_density=" + str(material_density)

        if material_density_unit is not None:
            if "?" in url:
                url = url + "&material_density_unit=" + str(material_density_unit)
            else:
                url = url + "?material_density_unit=" + str(material_density_unit)

        if output_unit is not None:
            if "?" in url:
                url = url + "&output_unit=" + str(output_unit)
            else:
                url = url + "?output_unit=" + str(output_unit)

        if src_format is not None:
            if "?" in url:
                url = url + "&src_format=" + str(src_format)
            else:
                url = url + "?src_format=" + str(src_format)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body,
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return FileMass.model_validate(json_data)

    def create_file_surface_area(
        self,
        src_format: FileImportFormat,
        body: bytes,
        *,
        output_unit: Optional[UnitArea] = None,
    ) -> FileSurfaceArea:
        """We assume any file given to us has one consistent unit throughout. We also assume the file is at the proper scale.

        This endpoint returns the square measure units.

        In the future, we will use the units inside the file if they are given and do any conversions if necessary for the calculation. But currently, that is not supported.

        Get the surface area of an object in a CAD file. If the file is larger than 25MB, it will be performed asynchronously.

        If the operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint."""

        url = "{}/file/surface-area".format(self.client.base_url)

        if output_unit is not None:
            if "?" in url:
                url = url + "&output_unit=" + str(output_unit)
            else:
                url = url + "?output_unit=" + str(output_unit)

        if src_format is not None:
            if "?" in url:
                url = url + "&src_format=" + str(src_format)
            else:
                url = url + "?src_format=" + str(src_format)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body,
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return FileSurfaceArea.model_validate(json_data)

    def create_file_volume(
        self,
        src_format: FileImportFormat,
        body: bytes,
        *,
        output_unit: Optional[UnitVolume] = None,
    ) -> FileVolume:
        """We assume any file given to us has one consistent unit throughout. We also assume the file is at the proper scale.

        This endpoint returns the cubic measure units.

        In the future, we will use the units inside the file if they are given and do any conversions if necessary for the calculation. But currently, that is not supported.

        Get the volume of an object in a CAD file. If the file is larger than 25MB, it will be performed asynchronously.

        If the operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint."""

        url = "{}/file/volume".format(self.client.base_url)

        if output_unit is not None:
            if "?" in url:
                url = url + "&output_unit=" + str(output_unit)
            else:
                url = url + "?output_unit=" + str(output_unit)

        if src_format is not None:
            if "?" in url:
                url = url + "&src_format=" + str(src_format)
            else:
                url = url + "?src_format=" + str(src_format)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body,
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return FileVolume.model_validate(json_data)


class AsyncFileAPI:
    """Async API for file endpoints"""

    def __init__(self, client: AsyncClient) -> None:
        self.client = client

    async def create_file_center_of_mass(
        self,
        src_format: FileImportFormat,
        body: bytes,
        *,
        output_unit: Optional[UnitLength] = None,
    ) -> FileCenterOfMass:
        """We assume any file given to us has one consistent unit throughout. We also assume the file is at the proper scale.

        This endpoint returns the cartesian coordinate in world space measure units.

        In the future, we will use the units inside the file if they are given and do any conversions if necessary for the calculation. But currently, that is not supported.

        Get the center of mass of an object in a CAD file. If the file is larger than 25MB, it will be performed asynchronously.

        If the operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint."""

        url = "{}/file/center-of-mass".format(self.client.base_url)

        if output_unit is not None:
            if "?" in url:
                url = url + "&output_unit=" + str(output_unit)
            else:
                url = url + "?output_unit=" + str(output_unit)

        if src_format is not None:
            if "?" in url:
                url = url + "&src_format=" + str(src_format)
            else:
                url = url + "?src_format=" + str(src_format)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body,
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return FileCenterOfMass.model_validate(json_data)

    async def create_file_conversion_options(
        self,
        body: ConversionParams,
        file_attachments: Dict[str, SyncUpload],
    ) -> FileConversion:
        """This takes a HTTP multipart body with these fields in any order:

         - The input and output format options (as JSON), name is 'body'.  - The files to convert, in raw binary. Must supply filenames.

        This starts a conversion job and returns the `id` of the operation. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint.

        Examples:
            Basic usage with file attachments:

            ```python
            from pathlib import Path
            from kittycad.models.conversion_params import ConversionParams

            # Create the request body
            body = ConversionParams(
                # Add your parameters here
            )

            # Prepare file attachments
            file_attachments = {
                "main.kcl": Path("path/to/main.kcl"),
                "helper.kcl": Path("path/to/helper.kcl"),
            }

            # Make the request
            result = client.create_file_conversion_options(
                body=body,
                file_attachments=file_attachments,
            )
            ```

            Using different file types:

            ```python
            from io import BytesIO

            # Mix of file paths and file-like objects
            file_attachments = {
                "main.kcl": Path("main.kcl"),
                "config.kcl": BytesIO(b"// KCL configuration"),
                "data.json": "path/to/data.json",
            }

            result = client.create_file_conversion_options(
                body=body,
                file_attachments=file_attachments,
            )
            ```
        """

        url = "{}/file/conversion".format(self.client.base_url)

        _client = self.client.get_http_client()

        # JSON + multipart endpoint
        response = await upload_json_multipart_async(
            client=_client,
            url=url,
            json_body=body,
            file_attachments=file_attachments,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return FileConversion.model_validate(json_data)

    async def create_file_conversion(
        self,
        output_format: FileExportFormat,
        src_format: FileImportFormat,
        body: bytes,
    ) -> FileConversion:
        """If you wish to specify the conversion options, use the `/file/conversion` endpoint instead.

        Convert a CAD file from one format to another. If the file being converted is larger than 25MB, it will be performed asynchronously.

        If the conversion is performed synchronously, the contents of the converted file (`output`) will be returned as a base64 encoded string.

        If the operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint."""

        url = "{}/file/conversion/{src_format}/{output_format}".format(
            self.client.base_url, output_format=output_format, src_format=src_format
        )

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body,
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return FileConversion.model_validate(json_data)

    async def create_file_density(
        self,
        material_mass: float,
        src_format: FileImportFormat,
        body: bytes,
        *,
        material_mass_unit: Optional[UnitMass] = None,
        output_unit: Optional[UnitDensity] = None,
    ) -> FileDensity:
        """We assume any file given to us has one consistent unit throughout. We also assume the file is at the proper scale.

        This endpoint assumes if you are giving a material mass in a specific mass units, we return a density in mass unit per cubic measure unit.

        In the future, we will use the units inside the file if they are given and do any conversions if necessary for the calculation. But currently, that is not supported.

        Get the density of an object in a CAD file. If the file is larger than 25MB, it will be performed asynchronously.

        If the operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint."""

        url = "{}/file/density".format(self.client.base_url)

        if material_mass is not None:
            if "?" in url:
                url = url + "&material_mass=" + str(material_mass)
            else:
                url = url + "?material_mass=" + str(material_mass)

        if material_mass_unit is not None:
            if "?" in url:
                url = url + "&material_mass_unit=" + str(material_mass_unit)
            else:
                url = url + "?material_mass_unit=" + str(material_mass_unit)

        if output_unit is not None:
            if "?" in url:
                url = url + "&output_unit=" + str(output_unit)
            else:
                url = url + "?output_unit=" + str(output_unit)

        if src_format is not None:
            if "?" in url:
                url = url + "&src_format=" + str(src_format)
            else:
                url = url + "?src_format=" + str(src_format)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body,
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return FileDensity.model_validate(json_data)

    async def create_file_mass(
        self,
        material_density: float,
        src_format: FileImportFormat,
        body: bytes,
        *,
        material_density_unit: Optional[UnitDensity] = None,
        output_unit: Optional[UnitMass] = None,
    ) -> FileMass:
        """We assume any file given to us has one consistent unit throughout. We also assume the file is at the proper scale.

        This endpoint assumes if you are giving a material density in a specific mass unit per cubic measure unit, we return a mass in mass units. The same mass units as passed in the material density.

        In the future, we will use the units inside the file if they are given and do any conversions if necessary for the calculation. But currently, that is not supported.

        Get the mass of an object in a CAD file. If the file is larger than 25MB, it will be performed asynchronously.

        If the operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint."""

        url = "{}/file/mass".format(self.client.base_url)

        if material_density is not None:
            if "?" in url:
                url = url + "&material_density=" + str(material_density)
            else:
                url = url + "?material_density=" + str(material_density)

        if material_density_unit is not None:
            if "?" in url:
                url = url + "&material_density_unit=" + str(material_density_unit)
            else:
                url = url + "?material_density_unit=" + str(material_density_unit)

        if output_unit is not None:
            if "?" in url:
                url = url + "&output_unit=" + str(output_unit)
            else:
                url = url + "?output_unit=" + str(output_unit)

        if src_format is not None:
            if "?" in url:
                url = url + "&src_format=" + str(src_format)
            else:
                url = url + "?src_format=" + str(src_format)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body,
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return FileMass.model_validate(json_data)

    async def create_file_surface_area(
        self,
        src_format: FileImportFormat,
        body: bytes,
        *,
        output_unit: Optional[UnitArea] = None,
    ) -> FileSurfaceArea:
        """We assume any file given to us has one consistent unit throughout. We also assume the file is at the proper scale.

        This endpoint returns the square measure units.

        In the future, we will use the units inside the file if they are given and do any conversions if necessary for the calculation. But currently, that is not supported.

        Get the surface area of an object in a CAD file. If the file is larger than 25MB, it will be performed asynchronously.

        If the operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint."""

        url = "{}/file/surface-area".format(self.client.base_url)

        if output_unit is not None:
            if "?" in url:
                url = url + "&output_unit=" + str(output_unit)
            else:
                url = url + "?output_unit=" + str(output_unit)

        if src_format is not None:
            if "?" in url:
                url = url + "&src_format=" + str(src_format)
            else:
                url = url + "?src_format=" + str(src_format)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body,
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return FileSurfaceArea.model_validate(json_data)

    async def create_file_volume(
        self,
        src_format: FileImportFormat,
        body: bytes,
        *,
        output_unit: Optional[UnitVolume] = None,
    ) -> FileVolume:
        """We assume any file given to us has one consistent unit throughout. We also assume the file is at the proper scale.

        This endpoint returns the cubic measure units.

        In the future, we will use the units inside the file if they are given and do any conversions if necessary for the calculation. But currently, that is not supported.

        Get the volume of an object in a CAD file. If the file is larger than 25MB, it will be performed asynchronously.

        If the operation is performed asynchronously, the `id` of the operation will be returned. You can use the `id` returned from the request to get status information about the async operation from the `/async/operations/{id}` endpoint."""

        url = "{}/file/volume".format(self.client.base_url)

        if output_unit is not None:
            if "?" in url:
                url = url + "&output_unit=" + str(output_unit)
            else:
                url = url + "?output_unit=" + str(output_unit)

        if src_format is not None:
            if "?" in url:
                url = url + "&src_format=" + str(src_format)
            else:
                url = url + "?src_format=" + str(src_format)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body,
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return FileVolume.model_validate(json_data)


class ExecutorAPI:
    """API for executor endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def create_file_execution(
        self,
        lang: CodeLanguage,
        body: bytes,
        *,
        output: Optional[str] = None,
    ) -> CodeOutput:
        """Execute a Zoo program in a specific language."""

        url = "{}/file/execute/{lang}".format(self.client.base_url, lang=lang)

        if output is not None:
            if "?" in url:
                url = url + "&output=" + str(output)
            else:
                url = url + "?output=" + str(output)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body,
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CodeOutput.model_validate(json_data)

    def create_executor_term(
        self,
        recv_timeout: Optional[float] = None,
        ws_factory: Optional[Callable[..., ClientConnectionSync]] = None,
    ) -> "WebSocketCreateExecutorTerm":
        """Create a terminal.

        Returns a WebSocket wrapper with methods for sending/receiving data.
        """
        return WebSocketCreateExecutorTerm(
            recv_timeout=recv_timeout, ws_factory=ws_factory, client=self.client
        )


class AsyncExecutorAPI:
    """Async API for executor endpoints"""

    def __init__(self, client: AsyncClient) -> None:
        self.client = client

    async def create_file_execution(
        self,
        lang: CodeLanguage,
        body: bytes,
        *,
        output: Optional[str] = None,
    ) -> CodeOutput:
        """Execute a Zoo program in a specific language."""

        url = "{}/file/execute/{lang}".format(self.client.base_url, lang=lang)

        if output is not None:
            if "?" in url:
                url = url + "&output=" + str(output)
            else:
                url = url + "?output=" + str(output)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body,
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CodeOutput.model_validate(json_data)

    async def create_executor_term(self):
        """Create a terminal.

        Returns an async WebSocket connection for sending/receiving data.
        """

        # For async clients, return the raw async WebSocket connection
        # This supports await websocket.send() and async for message in websocket
        async def create_executor_term(
            self,
        ) -> ClientConnectionAsync:
            """Create a terminal."""

            url = "/ws/executor/term"

            return await ws_connect_async(
                url.replace("http", "ws"),
                extra_headers=self.client.get_headers(),
                close_timeout=120,
                max_size=None,
            )


class Oauth2API:
    """API for oauth2 endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def device_auth_request(
        self,
        body: DeviceAuthRequestForm,
    ):
        """This endpoint is designed to be accessed from an *unauthenticated* API client. It generates and records a `device_code` and `user_code` which must be verified and confirmed prior to a token being granted."""

        url = "{}/oauth2/device/auth".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def device_auth_confirm(
        self,
        body: DeviceAuthConfirmParams,
    ):
        """This endpoint is designed to be accessed by the user agent (browser), not the client requesting the token. So we do not actually return the token here; it will be returned in response to the poll on `/oauth2/device/token`."""

        url = "{}/oauth2/device/confirm".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def device_access_token(
        self,
        body: DeviceAccessTokenRequestForm,
    ):
        """This endpoint should be polled by the client until the user code is verified and the grant is confirmed."""

        url = "{}/oauth2/device/token".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def device_auth_verify(
        self,
        user_code: str,
        *,
        app_name: Optional[str] = None,
    ):
        """This endpoint should be accessed in a full user agent (e.g., a browser). If the user is not logged in, we redirect them to the login page and use the `callback_url` parameter to get them to the UI verification form upon logging in. If they are logged in, we redirect them to the UI verification form on the website."""

        url = "{}/oauth2/device/verify".format(self.client.base_url)

        if app_name is not None:
            if "?" in url:
                url = url + "&app_name=" + str(app_name)
            else:
                url = url + "?app_name=" + str(app_name)

        if user_code is not None:
            if "?" in url:
                url = url + "&user_code=" + str(user_code)
            else:
                url = url + "?user_code=" + str(user_code)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def oauth2_provider_callback(
        self,
        provider: AccountProvider,
        *,
        code: Optional[str] = None,
        id_token: Optional[str] = None,
        state: Optional[str] = None,
        user: Optional[str] = None,
    ):
        """Listen for callbacks for the OAuth 2.0 provider."""

        url = "{}/oauth2/provider/{provider}/callback".format(
            self.client.base_url, provider=provider
        )

        if code is not None:
            if "?" in url:
                url = url + "&code=" + str(code)
            else:
                url = url + "?code=" + str(code)

        if id_token is not None:
            if "?" in url:
                url = url + "&id_token=" + str(id_token)
            else:
                url = url + "?id_token=" + str(id_token)

        if state is not None:
            if "?" in url:
                url = url + "&state=" + str(state)
            else:
                url = url + "?state=" + str(state)

        if user is not None:
            if "?" in url:
                url = url + "&user=" + str(user)
            else:
                url = url + "?user=" + str(user)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def oauth2_provider_callback_post(
        self,
        provider: AccountProvider,
        body: AuthCallback,
    ):
        """This specific endpoint listens for posts of form data."""

        url = "{}/oauth2/provider/{provider}/callback".format(
            self.client.base_url, provider=provider
        )

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def oauth2_provider_consent(
        self,
        provider: AccountProvider,
        *,
        callback_url: Optional[str] = None,
    ) -> OAuth2ClientInfo:
        """Get the consent URL and other information for the OAuth 2.0 provider."""

        url = "{}/oauth2/provider/{provider}/consent".format(
            self.client.base_url, provider=provider
        )

        if callback_url is not None:
            if "?" in url:
                url = url + "&callback_url=" + str(callback_url)
            else:
                url = url + "?callback_url=" + str(callback_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OAuth2ClientInfo.model_validate(json_data)

    def oauth2_token_revoke(
        self,
        body: TokenRevokeRequestForm,
    ):
        """This endpoint is designed to be accessed from an *unauthenticated* API client."""

        url = "{}/oauth2/token/revoke".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None


class AsyncOauth2API:
    """Async API for oauth2 endpoints"""

    def __init__(self, client: AsyncClient) -> None:
        self.client = client

    async def device_auth_request(
        self,
        body: DeviceAuthRequestForm,
    ):
        """This endpoint is designed to be accessed from an *unauthenticated* API client. It generates and records a `device_code` and `user_code` which must be verified and confirmed prior to a token being granted."""

        url = "{}/oauth2/device/auth".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def device_auth_confirm(
        self,
        body: DeviceAuthConfirmParams,
    ):
        """This endpoint is designed to be accessed by the user agent (browser), not the client requesting the token. So we do not actually return the token here; it will be returned in response to the poll on `/oauth2/device/token`."""

        url = "{}/oauth2/device/confirm".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def device_access_token(
        self,
        body: DeviceAccessTokenRequestForm,
    ):
        """This endpoint should be polled by the client until the user code is verified and the grant is confirmed."""

        url = "{}/oauth2/device/token".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def device_auth_verify(
        self,
        user_code: str,
        *,
        app_name: Optional[str] = None,
    ):
        """This endpoint should be accessed in a full user agent (e.g., a browser). If the user is not logged in, we redirect them to the login page and use the `callback_url` parameter to get them to the UI verification form upon logging in. If they are logged in, we redirect them to the UI verification form on the website."""

        url = "{}/oauth2/device/verify".format(self.client.base_url)

        if app_name is not None:
            if "?" in url:
                url = url + "&app_name=" + str(app_name)
            else:
                url = url + "?app_name=" + str(app_name)

        if user_code is not None:
            if "?" in url:
                url = url + "&user_code=" + str(user_code)
            else:
                url = url + "?user_code=" + str(user_code)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def oauth2_provider_callback(
        self,
        provider: AccountProvider,
        *,
        code: Optional[str] = None,
        id_token: Optional[str] = None,
        state: Optional[str] = None,
        user: Optional[str] = None,
    ):
        """Listen for callbacks for the OAuth 2.0 provider."""

        url = "{}/oauth2/provider/{provider}/callback".format(
            self.client.base_url, provider=provider
        )

        if code is not None:
            if "?" in url:
                url = url + "&code=" + str(code)
            else:
                url = url + "?code=" + str(code)

        if id_token is not None:
            if "?" in url:
                url = url + "&id_token=" + str(id_token)
            else:
                url = url + "?id_token=" + str(id_token)

        if state is not None:
            if "?" in url:
                url = url + "&state=" + str(state)
            else:
                url = url + "?state=" + str(state)

        if user is not None:
            if "?" in url:
                url = url + "&user=" + str(user)
            else:
                url = url + "?user=" + str(user)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def oauth2_provider_callback_post(
        self,
        provider: AccountProvider,
        body: AuthCallback,
    ):
        """This specific endpoint listens for posts of form data."""

        url = "{}/oauth2/provider/{provider}/callback".format(
            self.client.base_url, provider=provider
        )

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def oauth2_provider_consent(
        self,
        provider: AccountProvider,
        *,
        callback_url: Optional[str] = None,
    ) -> OAuth2ClientInfo:
        """Get the consent URL and other information for the OAuth 2.0 provider."""

        url = "{}/oauth2/provider/{provider}/consent".format(
            self.client.base_url, provider=provider
        )

        if callback_url is not None:
            if "?" in url:
                url = url + "&callback_url=" + str(callback_url)
            else:
                url = url + "?callback_url=" + str(callback_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OAuth2ClientInfo.model_validate(json_data)

    async def oauth2_token_revoke(
        self,
        body: TokenRevokeRequestForm,
    ):
        """This endpoint is designed to be accessed from an *unauthenticated* API client."""

        url = "{}/oauth2/token/revoke".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None


class OrgsAPI:
    """API for orgs endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_org(
        self,
    ) -> Org:
        """This endpoint requires authentication by an org admin. It gets the authenticated user's org."""

        url = "{}/org".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Org.model_validate(json_data)

    def update_org(
        self,
        body: OrgDetails,
    ) -> Org:
        """This endpoint requires authentication by an org admin. It updates the authenticated user's org."""

        url = "{}/org".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Org.model_validate(json_data)

    def create_org(
        self,
        body: OrgDetails,
    ) -> Org:
        """This endpoint requires authentication by a Zoo user that is not already in an org. It creates a new org for the authenticated user and makes them an admin."""

        url = "{}/org".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Org.model_validate(json_data)

    def delete_org(
        self,
    ):
        """In order to delete an org, you must first delete all of its members, except yourself.

        You must also have no outstanding invoices or unpaid balances.

        This endpoint requires authentication by an org admin. It deletes the authenticated user's org."""

        url = "{}/org".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def org_dataset_s3_policies(
        self,
        role_arn: str,
        uri: str,
    ) -> DatasetS3Policies:
        """Return the IAM policies customers should apply when onboarding an S3 dataset."""

        url = "{}/org/dataset/s3/policies".format(self.client.base_url)

        if role_arn is not None:
            if "?" in url:
                url = url + "&role_arn=" + str(role_arn)
            else:
                url = url + "?role_arn=" + str(role_arn)

        if uri is not None:
            if "?" in url:
                url = url + "&uri=" + str(uri)
            else:
                url = url + "?uri=" + str(uri)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return DatasetS3Policies.model_validate(json_data)

    def list_org_datasets(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "SyncPageIterator":
        """List every dataset that belongs to the caller's organization.

        Returns an iterator that automatically handles pagination.
        Iterate over all items across all pages:

            for item in client.org.list_org_datasets():
                print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import SyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        def fetch_page(**kw):
            return self._fetch_page_list_org_datasets(**kw)

        # Create the page iterator
        return SyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    def _fetch_page_list_org_datasets(self, **kwargs) -> OrgDatasetResultsPage:
        """Internal method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/org/datasets".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return OrgDatasetResultsPage.model_validate(json_data)

    def create_org_dataset(
        self,
        body: CreateOrgDataset,
    ) -> OrgDataset:
        """If the dataset lives in S3, call `/org/dataset/s3/policies` first so you can generate the trust, permission, and bucket policies scoped to your dataset before invoking this endpoint."""

        url = "{}/org/datasets".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgDataset.model_validate(json_data)

    def get_org_dataset(
        self,
        id: Uuid,
    ) -> OrgDataset:
        """Fetch a single dataset by id so long as it belongs to the authenticated org."""

        url = "{}/org/datasets/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgDataset.model_validate(json_data)

    def update_org_dataset(
        self,
        id: Uuid,
        body: UpdateOrgDataset,
    ) -> OrgDataset:
        """IMPORTANT: Use this endpoint to fix connectivity to the same underlying storage location (e.g. rotating credentials or correcting a typo). Do not repoint an existing dataset at a completely different bucket or provider—create a new dataset instead so conversions in flight keep their original source. This warning applies to every storage backend, not just S3."""

        url = "{}/org/datasets/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgDataset.model_validate(json_data)

    def delete_org_dataset(
        self,
        id: Uuid,
    ):
        """This is a destructive operation that: - requires org admin authentication and the dataset must belong to the caller's org. - fails with a 409 Conflict if the dataset is still attached to any custom model. - deletes Zoo-managed artifacts for this dataset (converted outputs and embeddings). - does **not** delete or modify the customer's source bucket/prefix.

        All internal artifact deletions are strict; if any cleanup fails, the request fails."""

        url = "{}/org/datasets/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def list_org_dataset_conversions(
        self,
        id: Uuid,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[ConversionSortMode] = None,
    ) -> "SyncPageIterator":
        """List the file conversions that have been processed for a given dataset owned by the caller's org.

        Returns an iterator that automatically handles pagination.
        Iterate over all items across all pages:

            for item in client.org.list_org_dataset_conversions():
                print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import SyncPageIterator

        # Store path parameters in closure for later use

        _id = id

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        def fetch_page(**kw):
            return self._fetch_page_list_org_dataset_conversions(id=_id, **kw)

        # Create the page iterator
        return SyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    def _fetch_page_list_org_dataset_conversions(
        self, id: Uuid, **kwargs
    ) -> OrgDatasetFileConversionSummaryResultsPage:
        """Internal method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/org/datasets/{id}/conversions".format(self.client.base_url, id=id)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return OrgDatasetFileConversionSummaryResultsPage.model_validate(json_data)

    def get_org_dataset_conversion(
        self,
        conversion_id: Uuid,
        id: Uuid,
    ) -> OrgDatasetFileConversionDetails:
        """Fetch the metadata and converted output for a single dataset conversion."""

        url = "{}/org/datasets/{id}/conversions/{conversion_id}".format(
            self.client.base_url, conversion_id=conversion_id, id=id
        )

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgDatasetFileConversionDetails.model_validate(json_data)

    def retry_org_dataset_conversion(
        self,
        conversion_id: Uuid,
        id: Uuid,
    ) -> OrgDatasetFileConversion:
        """Retry a specific dataset conversion that failed previously for the caller's org."""

        url = "{}/org/datasets/{id}/conversions/{conversion_id}/retry".format(
            self.client.base_url, conversion_id=conversion_id, id=id
        )

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgDatasetFileConversion.model_validate(json_data)

    def rescan_org_dataset(
        self,
        id: Uuid,
    ) -> OrgDataset:
        """Request a rescan of a dataset that belongs to the caller's org."""

        url = "{}/org/datasets/{id}/rescan".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgDataset.model_validate(json_data)

    def get_org_dataset_conversion_stats(
        self,
        id: Uuid,
    ) -> OrgDatasetConversionStatsResponse:
        """Return aggregate conversion stats for a dataset owned by the caller's org."""

        url = "{}/org/datasets/{id}/stats".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgDatasetConversionStatsResponse.model_validate(json_data)

    def list_org_members(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
        role: Optional[UserOrgRole] = None,
    ) -> "SyncPageIterator":
        """This endpoint requires authentication by an org admin. It lists the members of the authenticated user's org.

        Returns an iterator that automatically handles pagination.
        Iterate over all items across all pages:

            for item in client.org.list_org_members():
                print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import SyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        if role is not None:
            kwargs["role"] = role

        def fetch_page(**kw):
            return self._fetch_page_list_org_members(**kw)

        # Create the page iterator
        return SyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    def _fetch_page_list_org_members(self, **kwargs) -> OrgMemberResultsPage:
        """Internal method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/org/members".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        if "role" in kwargs and kwargs["role"] is not None:
            if "?" in url:
                url = url + "&role=" + str(kwargs["role"])
            else:
                url = url + "?role=" + str(kwargs["role"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return OrgMemberResultsPage.model_validate(json_data)

    def create_org_member(
        self,
        body: AddOrgMember,
    ) -> OrgMember:
        """If the user exists, this will add them to your org. If they do not exist, this will create a new user and add them to your org.

        In both cases the user gets an email that they have been added to the org.

        If the user is already in your org, this will return a 400 and a message.

        If the user is already in a different org, this will return a 400 and a message.

        This endpoint requires authentication by an org admin. It adds the specified member to the authenticated user's org."""

        url = "{}/org/members".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgMember.model_validate(json_data)

    def get_org_member(
        self,
        user_id: Uuid,
    ) -> OrgMember:
        """This endpoint requires authentication by an org admin. It gets the specified member of the authenticated user's org."""

        url = "{}/org/members/{user_id}".format(self.client.base_url, user_id=user_id)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgMember.model_validate(json_data)

    def update_org_member(
        self,
        user_id: Uuid,
        body: UpdateMemberToOrgBody,
    ) -> OrgMember:
        """This endpoint requires authentication by an org admin. It updates the specified member of the authenticated user's org."""

        url = "{}/org/members/{user_id}".format(self.client.base_url, user_id=user_id)

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgMember.model_validate(json_data)

    def delete_org_member(
        self,
        user_id: Uuid,
    ):
        """This endpoint requires authentication by an org admin. It removes the specified member from the authenticated user's org."""

        url = "{}/org/members/{user_id}".format(self.client.base_url, user_id=user_id)

        _client = self.client.get_http_client()

        response = _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def get_org_privacy_settings(
        self,
    ) -> PrivacySettings:
        """This endpoint requires authentication by an org admin. It gets the privacy settings for the authenticated user's org."""

        url = "{}/org/privacy".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return PrivacySettings.model_validate(json_data)

    def update_org_privacy_settings(
        self,
        body: PrivacySettings,
    ) -> PrivacySettings:
        """This endpoint requires authentication by an org admin. It updates the privacy settings for the authenticated user's org."""

        url = "{}/org/privacy".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return PrivacySettings.model_validate(json_data)

    def get_org_saml_idp(
        self,
    ) -> SamlIdentityProvider:
        """This endpoint requires authentication by an org admin."""

        url = "{}/org/saml/idp".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return SamlIdentityProvider.model_validate(json_data)

    def update_org_saml_idp(
        self,
        body: SamlIdentityProviderCreate,
    ) -> SamlIdentityProvider:
        """This endpoint requires authentication by an org admin."""

        url = "{}/org/saml/idp".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return SamlIdentityProvider.model_validate(json_data)

    def create_org_saml_idp(
        self,
        body: SamlIdentityProviderCreate,
    ) -> SamlIdentityProvider:
        """This endpoint requires authentication by an org admin."""

        url = "{}/org/saml/idp".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return SamlIdentityProvider.model_validate(json_data)

    def delete_org_saml_idp(
        self,
    ):
        """This endpoint requires authentication by an org admin."""

        url = "{}/org/saml/idp".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def get_org_shortlinks(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "SyncPageIterator":
        """This endpoint requires authentication by an org admin. It gets the shortlinks for the authenticated user's org.

        Returns an iterator that automatically handles pagination.
        Iterate over all items across all pages:

            for item in client.org.get_org_shortlinks():
                print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import SyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        def fetch_page(**kw):
            return self._fetch_page_get_org_shortlinks(**kw)

        # Create the page iterator
        return SyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    def _fetch_page_get_org_shortlinks(self, **kwargs) -> ShortlinkResultsPage:
        """Internal method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/org/shortlinks".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ShortlinkResultsPage.model_validate(json_data)

    def list_orgs(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "SyncPageIterator":
        """This endpoint requires authentication by a Zoo employee. The orgs are returned in order of creation, with the most recently created orgs first.

        Returns an iterator that automatically handles pagination.
        Iterate over all items across all pages:

            for item in client.orgs.list_orgs():
                print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import SyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        def fetch_page(**kw):
            return self._fetch_page_list_orgs(**kw)

        # Create the page iterator
        return SyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    def _fetch_page_list_orgs(self, **kwargs) -> OrgResultsPage:
        """Internal method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/orgs".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return OrgResultsPage.model_validate(json_data)

    def get_any_org(
        self,
        id: Uuid,
    ) -> Org:
        """This endpoint requires authentication by a Zoo employee. It gets the information for the specified org."""

        url = "{}/orgs/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Org.model_validate(json_data)

    def org_admin_details_get(
        self,
        id: Uuid,
    ) -> OrgAdminDetails:
        """Zoo admins can retrieve extended information about any organization, while non-admins receive a 404 to avoid leaking existence."""

        url = "{}/orgs/{id}/admin/details".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgAdminDetails.model_validate(json_data)

    def get_user_org(
        self,
    ) -> UserOrgInfo:
        """This endpoint requires authentication by any Zoo user. It gets the authenticated user's org.

        If the user is not a member of an org, this endpoint will return a 404."""

        url = "{}/user/org".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UserOrgInfo.model_validate(json_data)


class AsyncOrgsAPI:
    """Async API for orgs endpoints"""

    def __init__(self, client: AsyncClient) -> None:
        self.client = client

    async def get_org(
        self,
    ) -> Org:
        """This endpoint requires authentication by an org admin. It gets the authenticated user's org."""

        url = "{}/org".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Org.model_validate(json_data)

    async def update_org(
        self,
        body: OrgDetails,
    ) -> Org:
        """This endpoint requires authentication by an org admin. It updates the authenticated user's org."""

        url = "{}/org".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Org.model_validate(json_data)

    async def create_org(
        self,
        body: OrgDetails,
    ) -> Org:
        """This endpoint requires authentication by a Zoo user that is not already in an org. It creates a new org for the authenticated user and makes them an admin."""

        url = "{}/org".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Org.model_validate(json_data)

    async def delete_org(
        self,
    ):
        """In order to delete an org, you must first delete all of its members, except yourself.

        You must also have no outstanding invoices or unpaid balances.

        This endpoint requires authentication by an org admin. It deletes the authenticated user's org."""

        url = "{}/org".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def org_dataset_s3_policies(
        self,
        role_arn: str,
        uri: str,
    ) -> DatasetS3Policies:
        """Return the IAM policies customers should apply when onboarding an S3 dataset."""

        url = "{}/org/dataset/s3/policies".format(self.client.base_url)

        if role_arn is not None:
            if "?" in url:
                url = url + "&role_arn=" + str(role_arn)
            else:
                url = url + "?role_arn=" + str(role_arn)

        if uri is not None:
            if "?" in url:
                url = url + "&uri=" + str(uri)
            else:
                url = url + "?uri=" + str(uri)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return DatasetS3Policies.model_validate(json_data)

    def list_org_datasets(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "AsyncPageIterator":
        """List every dataset that belongs to the caller's organization.

        Returns an async iterator that automatically handles pagination.
        Iterate over all items across all pages:

            async for item in client.org.list_org_datasets():
                print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import AsyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        async def fetch_page(**kw):
            return await self._fetch_page_list_org_datasets(**kw)

        # Create the async page iterator
        return AsyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    async def _fetch_page_list_org_datasets(self, **kwargs) -> OrgDatasetResultsPage:
        """Internal async method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/org/datasets".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return OrgDatasetResultsPage.model_validate(json_data)

    async def create_org_dataset(
        self,
        body: CreateOrgDataset,
    ) -> OrgDataset:
        """If the dataset lives in S3, call `/org/dataset/s3/policies` first so you can generate the trust, permission, and bucket policies scoped to your dataset before invoking this endpoint."""

        url = "{}/org/datasets".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgDataset.model_validate(json_data)

    async def get_org_dataset(
        self,
        id: Uuid,
    ) -> OrgDataset:
        """Fetch a single dataset by id so long as it belongs to the authenticated org."""

        url = "{}/org/datasets/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgDataset.model_validate(json_data)

    async def update_org_dataset(
        self,
        id: Uuid,
        body: UpdateOrgDataset,
    ) -> OrgDataset:
        """IMPORTANT: Use this endpoint to fix connectivity to the same underlying storage location (e.g. rotating credentials or correcting a typo). Do not repoint an existing dataset at a completely different bucket or provider—create a new dataset instead so conversions in flight keep their original source. This warning applies to every storage backend, not just S3."""

        url = "{}/org/datasets/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgDataset.model_validate(json_data)

    async def delete_org_dataset(
        self,
        id: Uuid,
    ):
        """This is a destructive operation that: - requires org admin authentication and the dataset must belong to the caller's org. - fails with a 409 Conflict if the dataset is still attached to any custom model. - deletes Zoo-managed artifacts for this dataset (converted outputs and embeddings). - does **not** delete or modify the customer's source bucket/prefix.

        All internal artifact deletions are strict; if any cleanup fails, the request fails."""

        url = "{}/org/datasets/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def list_org_dataset_conversions(
        self,
        id: Uuid,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[ConversionSortMode] = None,
    ) -> "AsyncPageIterator":
        """List the file conversions that have been processed for a given dataset owned by the caller's org.

        Returns an async iterator that automatically handles pagination.
        Iterate over all items across all pages:

            async for item in client.org.list_org_dataset_conversions():
                print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import AsyncPageIterator

        # Store path parameters in closure for later use

        _id = id

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        async def fetch_page(**kw):
            return await self._fetch_page_list_org_dataset_conversions(id=_id, **kw)

        # Create the async page iterator
        return AsyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    async def _fetch_page_list_org_dataset_conversions(
        self, id: Uuid, **kwargs
    ) -> OrgDatasetFileConversionSummaryResultsPage:
        """Internal async method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/org/datasets/{id}/conversions".format(self.client.base_url, id=id)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return OrgDatasetFileConversionSummaryResultsPage.model_validate(json_data)

    async def get_org_dataset_conversion(
        self,
        conversion_id: Uuid,
        id: Uuid,
    ) -> OrgDatasetFileConversionDetails:
        """Fetch the metadata and converted output for a single dataset conversion."""

        url = "{}/org/datasets/{id}/conversions/{conversion_id}".format(
            self.client.base_url, conversion_id=conversion_id, id=id
        )

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgDatasetFileConversionDetails.model_validate(json_data)

    async def retry_org_dataset_conversion(
        self,
        conversion_id: Uuid,
        id: Uuid,
    ) -> OrgDatasetFileConversion:
        """Retry a specific dataset conversion that failed previously for the caller's org."""

        url = "{}/org/datasets/{id}/conversions/{conversion_id}/retry".format(
            self.client.base_url, conversion_id=conversion_id, id=id
        )

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgDatasetFileConversion.model_validate(json_data)

    async def rescan_org_dataset(
        self,
        id: Uuid,
    ) -> OrgDataset:
        """Request a rescan of a dataset that belongs to the caller's org."""

        url = "{}/org/datasets/{id}/rescan".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgDataset.model_validate(json_data)

    async def get_org_dataset_conversion_stats(
        self,
        id: Uuid,
    ) -> OrgDatasetConversionStatsResponse:
        """Return aggregate conversion stats for a dataset owned by the caller's org."""

        url = "{}/org/datasets/{id}/stats".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgDatasetConversionStatsResponse.model_validate(json_data)

    def list_org_members(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
        role: Optional[UserOrgRole] = None,
    ) -> "AsyncPageIterator":
        """This endpoint requires authentication by an org admin. It lists the members of the authenticated user's org.

        Returns an async iterator that automatically handles pagination.
        Iterate over all items across all pages:

            async for item in client.org.list_org_members():
                print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import AsyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        if role is not None:
            kwargs["role"] = role

        async def fetch_page(**kw):
            return await self._fetch_page_list_org_members(**kw)

        # Create the async page iterator
        return AsyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    async def _fetch_page_list_org_members(self, **kwargs) -> OrgMemberResultsPage:
        """Internal async method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/org/members".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        if "role" in kwargs and kwargs["role"] is not None:
            if "?" in url:
                url = url + "&role=" + str(kwargs["role"])
            else:
                url = url + "?role=" + str(kwargs["role"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return OrgMemberResultsPage.model_validate(json_data)

    async def create_org_member(
        self,
        body: AddOrgMember,
    ) -> OrgMember:
        """If the user exists, this will add them to your org. If they do not exist, this will create a new user and add them to your org.

        In both cases the user gets an email that they have been added to the org.

        If the user is already in your org, this will return a 400 and a message.

        If the user is already in a different org, this will return a 400 and a message.

        This endpoint requires authentication by an org admin. It adds the specified member to the authenticated user's org."""

        url = "{}/org/members".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgMember.model_validate(json_data)

    async def get_org_member(
        self,
        user_id: Uuid,
    ) -> OrgMember:
        """This endpoint requires authentication by an org admin. It gets the specified member of the authenticated user's org."""

        url = "{}/org/members/{user_id}".format(self.client.base_url, user_id=user_id)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgMember.model_validate(json_data)

    async def update_org_member(
        self,
        user_id: Uuid,
        body: UpdateMemberToOrgBody,
    ) -> OrgMember:
        """This endpoint requires authentication by an org admin. It updates the specified member of the authenticated user's org."""

        url = "{}/org/members/{user_id}".format(self.client.base_url, user_id=user_id)

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgMember.model_validate(json_data)

    async def delete_org_member(
        self,
        user_id: Uuid,
    ):
        """This endpoint requires authentication by an org admin. It removes the specified member from the authenticated user's org."""

        url = "{}/org/members/{user_id}".format(self.client.base_url, user_id=user_id)

        _client = self.client.get_http_client()

        response = await _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def get_org_privacy_settings(
        self,
    ) -> PrivacySettings:
        """This endpoint requires authentication by an org admin. It gets the privacy settings for the authenticated user's org."""

        url = "{}/org/privacy".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return PrivacySettings.model_validate(json_data)

    async def update_org_privacy_settings(
        self,
        body: PrivacySettings,
    ) -> PrivacySettings:
        """This endpoint requires authentication by an org admin. It updates the privacy settings for the authenticated user's org."""

        url = "{}/org/privacy".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return PrivacySettings.model_validate(json_data)

    async def get_org_saml_idp(
        self,
    ) -> SamlIdentityProvider:
        """This endpoint requires authentication by an org admin."""

        url = "{}/org/saml/idp".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return SamlIdentityProvider.model_validate(json_data)

    async def update_org_saml_idp(
        self,
        body: SamlIdentityProviderCreate,
    ) -> SamlIdentityProvider:
        """This endpoint requires authentication by an org admin."""

        url = "{}/org/saml/idp".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return SamlIdentityProvider.model_validate(json_data)

    async def create_org_saml_idp(
        self,
        body: SamlIdentityProviderCreate,
    ) -> SamlIdentityProvider:
        """This endpoint requires authentication by an org admin."""

        url = "{}/org/saml/idp".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return SamlIdentityProvider.model_validate(json_data)

    async def delete_org_saml_idp(
        self,
    ):
        """This endpoint requires authentication by an org admin."""

        url = "{}/org/saml/idp".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def get_org_shortlinks(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "AsyncPageIterator":
        """This endpoint requires authentication by an org admin. It gets the shortlinks for the authenticated user's org.

        Returns an async iterator that automatically handles pagination.
        Iterate over all items across all pages:

            async for item in client.org.get_org_shortlinks():
                print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import AsyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        async def fetch_page(**kw):
            return await self._fetch_page_get_org_shortlinks(**kw)

        # Create the async page iterator
        return AsyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    async def _fetch_page_get_org_shortlinks(self, **kwargs) -> ShortlinkResultsPage:
        """Internal async method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/org/shortlinks".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ShortlinkResultsPage.model_validate(json_data)

    def list_orgs(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "AsyncPageIterator":
        """This endpoint requires authentication by a Zoo employee. The orgs are returned in order of creation, with the most recently created orgs first.

        Returns an async iterator that automatically handles pagination.
        Iterate over all items across all pages:

            async for item in client.orgs.list_orgs():
                print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import AsyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        async def fetch_page(**kw):
            return await self._fetch_page_list_orgs(**kw)

        # Create the async page iterator
        return AsyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    async def _fetch_page_list_orgs(self, **kwargs) -> OrgResultsPage:
        """Internal async method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/orgs".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return OrgResultsPage.model_validate(json_data)

    async def get_any_org(
        self,
        id: Uuid,
    ) -> Org:
        """This endpoint requires authentication by a Zoo employee. It gets the information for the specified org."""

        url = "{}/orgs/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Org.model_validate(json_data)

    async def org_admin_details_get(
        self,
        id: Uuid,
    ) -> OrgAdminDetails:
        """Zoo admins can retrieve extended information about any organization, while non-admins receive a 404 to avoid leaking existence."""

        url = "{}/orgs/{id}/admin/details".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return OrgAdminDetails.model_validate(json_data)

    async def get_user_org(
        self,
    ) -> UserOrgInfo:
        """This endpoint requires authentication by any Zoo user. It gets the authenticated user's org.

        If the user is not a member of an org, this endpoint will return a 404."""

        url = "{}/user/org".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UserOrgInfo.model_validate(json_data)


class PaymentsAPI:
    """API for payments endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_payment_information_for_org(
        self,
    ) -> Customer:
        """This includes billing address, phone, and name.

        This endpoint requires authentication by an org admin. It gets the payment information for the authenticated user's org."""

        url = "{}/org/payment".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Customer.model_validate(json_data)

    def update_payment_information_for_org(
        self,
        body: BillingInfo,
    ) -> Customer:
        """This includes billing address, phone, and name.

        This endpoint requires authentication by an org admin. It updates the payment information for the authenticated user's org."""

        url = "{}/org/payment".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Customer.model_validate(json_data)

    def create_payment_information_for_org(
        self,
        body: BillingInfo,
    ) -> Customer:
        """This includes billing address, phone, and name.

        This endpoint requires authentication by the org admin. It creates the payment information for the authenticated user's org."""

        url = "{}/org/payment".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Customer.model_validate(json_data)

    def delete_payment_information_for_org(
        self,
    ):
        """This includes billing address, phone, and name.

        This endpoint requires authentication by an org admin. It deletes the payment information for the authenticated user's org."""

        url = "{}/org/payment".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def get_payment_balance_for_org(
        self,
        *,
        include_total_due: Optional[bool] = None,
    ) -> CustomerBalance:
        """This endpoint requires authentication by any member of an org. It gets the balance information for the authenticated user's org."""

        url = "{}/org/payment/balance".format(self.client.base_url)

        if include_total_due is not None:
            if "?" in url:
                url = url + "&include_total_due=" + str(include_total_due).lower()
            else:
                url = url + "?include_total_due=" + str(include_total_due).lower()

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CustomerBalance.model_validate(json_data)

    def create_payment_intent_for_org(
        self,
    ) -> PaymentIntent:
        """This endpoint requires authentication by the org admin. It creates a new payment intent for the authenticated user's org's org."""

        url = "{}/org/payment/intent".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return PaymentIntent.model_validate(json_data)

    def list_invoices_for_org(
        self,
    ) -> List[Invoice]:
        """This endpoint requires authentication by an org admin. It lists invoices for the authenticated user's org."""

        url = "{}/org/payment/invoices".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(List[Invoice]).validate_python(json_data)

    def list_payment_methods_for_org(
        self,
    ) -> List[PaymentMethod]:
        """This endpoint requires authentication by an org admin. It lists payment methods for the authenticated user's org."""

        url = "{}/org/payment/methods".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(List[PaymentMethod]).validate_python(json_data)

    def delete_payment_method_for_org(
        self,
        id: str,
    ):
        """This endpoint requires authentication by an org admin. It deletes the specified payment method for the authenticated user's org."""

        url = "{}/org/payment/methods/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def get_org_subscription(
        self,
    ) -> ZooProductSubscriptions:
        """This endpoint requires authentication by any member of an org. It gets the subscription for the authenticated user's org."""

        url = "{}/org/payment/subscriptions".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ZooProductSubscriptions.model_validate(json_data)

    def update_org_subscription(
        self,
        body: ZooProductSubscriptionsOrgRequest,
    ) -> ZooProductSubscriptions:
        """This endpoint requires authentication by an org admin. It updates the subscription for the authenticated user's org."""

        url = "{}/org/payment/subscriptions".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ZooProductSubscriptions.model_validate(json_data)

    def create_org_subscription(
        self,
        body: ZooProductSubscriptionsOrgRequest,
    ) -> ZooProductSubscriptions:
        """This endpoint requires authentication by an org admin. It creates the subscription for the authenticated user's org."""

        url = "{}/org/payment/subscriptions".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ZooProductSubscriptions.model_validate(json_data)

    def validate_customer_tax_information_for_org(
        self,
    ):
        """This endpoint requires authentication by an org admin. It will return an error if the org's information is not valid for automatic tax. Otherwise, it will return an empty successful response."""

        url = "{}/org/payment/tax".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def get_payment_balance_for_any_org(
        self,
        id: Uuid,
        *,
        include_total_due: Optional[bool] = None,
    ) -> CustomerBalance:
        """This endpoint requires authentication by a Zoo employee. It gets the balance information for the specified org."""

        url = "{}/orgs/{id}/payment/balance".format(self.client.base_url, id=id)

        if include_total_due is not None:
            if "?" in url:
                url = url + "&include_total_due=" + str(include_total_due).lower()
            else:
                url = url + "?include_total_due=" + str(include_total_due).lower()

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CustomerBalance.model_validate(json_data)

    def update_payment_balance_for_any_org(
        self,
        id: Uuid,
        body: UpdatePaymentBalance,
        *,
        include_total_due: Optional[bool] = None,
    ) -> CustomerBalance:
        """This endpoint requires authentication by a Zoo employee. It updates the balance information for the specified org."""

        url = "{}/orgs/{id}/payment/balance".format(self.client.base_url, id=id)

        if include_total_due is not None:
            if "?" in url:
                url = url + "&include_total_due=" + str(include_total_due).lower()
            else:
                url = url + "?include_total_due=" + str(include_total_due).lower()

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CustomerBalance.model_validate(json_data)

    def update_org_subscription_for_any_org(
        self,
        id: Uuid,
        body: ZooProductSubscriptionsOrgRequest,
    ) -> ZooProductSubscriptions:
        """This endpoint requires authentication by a Zoo admin. It updates the subscription for the specified org."""

        url = "{}/orgs/{id}/payment/subscriptions".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ZooProductSubscriptions.model_validate(json_data)

    def upsert_subscription_plan_price(
        self,
        slug: str,
        body: PriceUpsertRequest,
    ) -> SubscriptionPlanPriceRecord:
        """You must be a Zoo admin to perform this request."""

        url = "{}/subscription-plans/{slug}/prices".format(
            self.client.base_url, slug=slug
        )

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return SubscriptionPlanPriceRecord.model_validate(json_data)

    def get_payment_information_for_user(
        self,
    ) -> Customer:
        """This includes billing address, phone, and name.

        This endpoint requires authentication by any Zoo user. It gets the payment information for the authenticated user."""

        url = "{}/user/payment".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Customer.model_validate(json_data)

    def update_payment_information_for_user(
        self,
        body: BillingInfo,
    ) -> Customer:
        """This includes billing address, phone, and name.

        This endpoint requires authentication by any Zoo user. It updates the payment information for the authenticated user."""

        url = "{}/user/payment".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Customer.model_validate(json_data)

    def create_payment_information_for_user(
        self,
        body: BillingInfo,
    ) -> Customer:
        """This includes billing address, phone, and name.

        This endpoint requires authentication by any Zoo user. It creates the payment information for the authenticated user."""

        url = "{}/user/payment".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Customer.model_validate(json_data)

    def delete_payment_information_for_user(
        self,
    ):
        """This includes billing address, phone, and name.

        This endpoint requires authentication by any Zoo user. It deletes the payment information for the authenticated user."""

        url = "{}/user/payment".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def get_payment_balance_for_user(
        self,
        *,
        include_total_due: Optional[bool] = None,
    ) -> CustomerBalance:
        """This endpoint requires authentication by any Zoo user. It gets the balance information for the authenticated user."""

        url = "{}/user/payment/balance".format(self.client.base_url)

        if include_total_due is not None:
            if "?" in url:
                url = url + "&include_total_due=" + str(include_total_due).lower()
            else:
                url = url + "?include_total_due=" + str(include_total_due).lower()

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CustomerBalance.model_validate(json_data)

    def create_payment_intent_for_user(
        self,
    ) -> PaymentIntent:
        """This endpoint requires authentication by any Zoo user. It creates a new payment intent for the authenticated user."""

        url = "{}/user/payment/intent".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return PaymentIntent.model_validate(json_data)

    def list_invoices_for_user(
        self,
    ) -> List[Invoice]:
        """This endpoint requires authentication by any Zoo user. It lists invoices for the authenticated user."""

        url = "{}/user/payment/invoices".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(List[Invoice]).validate_python(json_data)

    def list_payment_methods_for_user(
        self,
    ) -> List[PaymentMethod]:
        """This endpoint requires authentication by any Zoo user. It lists payment methods for the authenticated user."""

        url = "{}/user/payment/methods".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(List[PaymentMethod]).validate_python(json_data)

    def delete_payment_method_for_user(
        self,
        id: str,
        *,
        force: Optional[bool] = None,
    ):
        """This endpoint requires authentication by any Zoo user. It deletes the specified payment method for the authenticated user."""

        url = "{}/user/payment/methods/{id}".format(self.client.base_url, id=id)

        if force is not None:
            if "?" in url:
                url = url + "&force=" + str(force).lower()
            else:
                url = url + "?force=" + str(force).lower()

        _client = self.client.get_http_client()

        response = _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def set_default_payment_method_for_user(
        self,
        id: str,
    ):
        """This endpoint requires authentication by any Zoo user. It sets the default payment method for the authenticated user."""

        url = "{}/user/payment/methods/{id}/default".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def get_user_subscription(
        self,
    ) -> ZooProductSubscriptions:
        """This endpoint requires authentication by any Zoo user. It gets the subscription for the user."""

        url = "{}/user/payment/subscriptions".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ZooProductSubscriptions.model_validate(json_data)

    def update_user_subscription(
        self,
        body: ZooProductSubscriptionsUserRequest,
    ) -> ZooProductSubscriptions:
        """This endpoint requires authentication by any Zoo user. It updates the subscription for the user."""

        url = "{}/user/payment/subscriptions".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ZooProductSubscriptions.model_validate(json_data)

    def create_user_subscription(
        self,
        body: ZooProductSubscriptionsUserRequest,
    ) -> ZooProductSubscriptions:
        """This endpoint requires authentication by any Zoo user. It creates the subscription for the user."""

        url = "{}/user/payment/subscriptions".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ZooProductSubscriptions.model_validate(json_data)

    def validate_customer_tax_information_for_user(
        self,
    ):
        """This endpoint requires authentication by any Zoo user. It will return an error if the user's information is not valid for automatic tax. Otherwise, it will return an empty successful response."""

        url = "{}/user/payment/tax".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def get_payment_balance_for_any_user(
        self,
        id: UserIdentifier,
        *,
        include_total_due: Optional[bool] = None,
    ) -> CustomerBalance:
        """This endpoint requires authentication by a Zoo employee. It gets the balance information for the specified user."""

        url = "{}/users/{id}/payment/balance".format(self.client.base_url, id=id)

        if include_total_due is not None:
            if "?" in url:
                url = url + "&include_total_due=" + str(include_total_due).lower()
            else:
                url = url + "?include_total_due=" + str(include_total_due).lower()

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CustomerBalance.model_validate(json_data)

    def update_payment_balance_for_any_user(
        self,
        id: UserIdentifier,
        body: UpdatePaymentBalance,
        *,
        include_total_due: Optional[bool] = None,
    ) -> CustomerBalance:
        """This endpoint requires authentication by a Zoo employee. It updates the balance information for the specified user."""

        url = "{}/users/{id}/payment/balance".format(self.client.base_url, id=id)

        if include_total_due is not None:
            if "?" in url:
                url = url + "&include_total_due=" + str(include_total_due).lower()
            else:
                url = url + "?include_total_due=" + str(include_total_due).lower()

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CustomerBalance.model_validate(json_data)


class AsyncPaymentsAPI:
    """Async API for payments endpoints"""

    def __init__(self, client: AsyncClient) -> None:
        self.client = client

    async def get_payment_information_for_org(
        self,
    ) -> Customer:
        """This includes billing address, phone, and name.

        This endpoint requires authentication by an org admin. It gets the payment information for the authenticated user's org."""

        url = "{}/org/payment".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Customer.model_validate(json_data)

    async def update_payment_information_for_org(
        self,
        body: BillingInfo,
    ) -> Customer:
        """This includes billing address, phone, and name.

        This endpoint requires authentication by an org admin. It updates the payment information for the authenticated user's org."""

        url = "{}/org/payment".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Customer.model_validate(json_data)

    async def create_payment_information_for_org(
        self,
        body: BillingInfo,
    ) -> Customer:
        """This includes billing address, phone, and name.

        This endpoint requires authentication by the org admin. It creates the payment information for the authenticated user's org."""

        url = "{}/org/payment".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Customer.model_validate(json_data)

    async def delete_payment_information_for_org(
        self,
    ):
        """This includes billing address, phone, and name.

        This endpoint requires authentication by an org admin. It deletes the payment information for the authenticated user's org."""

        url = "{}/org/payment".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def get_payment_balance_for_org(
        self,
        *,
        include_total_due: Optional[bool] = None,
    ) -> CustomerBalance:
        """This endpoint requires authentication by any member of an org. It gets the balance information for the authenticated user's org."""

        url = "{}/org/payment/balance".format(self.client.base_url)

        if include_total_due is not None:
            if "?" in url:
                url = url + "&include_total_due=" + str(include_total_due).lower()
            else:
                url = url + "?include_total_due=" + str(include_total_due).lower()

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CustomerBalance.model_validate(json_data)

    async def create_payment_intent_for_org(
        self,
    ) -> PaymentIntent:
        """This endpoint requires authentication by the org admin. It creates a new payment intent for the authenticated user's org's org."""

        url = "{}/org/payment/intent".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return PaymentIntent.model_validate(json_data)

    async def list_invoices_for_org(
        self,
    ) -> List[Invoice]:
        """This endpoint requires authentication by an org admin. It lists invoices for the authenticated user's org."""

        url = "{}/org/payment/invoices".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(List[Invoice]).validate_python(json_data)

    async def list_payment_methods_for_org(
        self,
    ) -> List[PaymentMethod]:
        """This endpoint requires authentication by an org admin. It lists payment methods for the authenticated user's org."""

        url = "{}/org/payment/methods".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(List[PaymentMethod]).validate_python(json_data)

    async def delete_payment_method_for_org(
        self,
        id: str,
    ):
        """This endpoint requires authentication by an org admin. It deletes the specified payment method for the authenticated user's org."""

        url = "{}/org/payment/methods/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def get_org_subscription(
        self,
    ) -> ZooProductSubscriptions:
        """This endpoint requires authentication by any member of an org. It gets the subscription for the authenticated user's org."""

        url = "{}/org/payment/subscriptions".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ZooProductSubscriptions.model_validate(json_data)

    async def update_org_subscription(
        self,
        body: ZooProductSubscriptionsOrgRequest,
    ) -> ZooProductSubscriptions:
        """This endpoint requires authentication by an org admin. It updates the subscription for the authenticated user's org."""

        url = "{}/org/payment/subscriptions".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ZooProductSubscriptions.model_validate(json_data)

    async def create_org_subscription(
        self,
        body: ZooProductSubscriptionsOrgRequest,
    ) -> ZooProductSubscriptions:
        """This endpoint requires authentication by an org admin. It creates the subscription for the authenticated user's org."""

        url = "{}/org/payment/subscriptions".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ZooProductSubscriptions.model_validate(json_data)

    async def validate_customer_tax_information_for_org(
        self,
    ):
        """This endpoint requires authentication by an org admin. It will return an error if the org's information is not valid for automatic tax. Otherwise, it will return an empty successful response."""

        url = "{}/org/payment/tax".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def get_payment_balance_for_any_org(
        self,
        id: Uuid,
        *,
        include_total_due: Optional[bool] = None,
    ) -> CustomerBalance:
        """This endpoint requires authentication by a Zoo employee. It gets the balance information for the specified org."""

        url = "{}/orgs/{id}/payment/balance".format(self.client.base_url, id=id)

        if include_total_due is not None:
            if "?" in url:
                url = url + "&include_total_due=" + str(include_total_due).lower()
            else:
                url = url + "?include_total_due=" + str(include_total_due).lower()

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CustomerBalance.model_validate(json_data)

    async def update_payment_balance_for_any_org(
        self,
        id: Uuid,
        body: UpdatePaymentBalance,
        *,
        include_total_due: Optional[bool] = None,
    ) -> CustomerBalance:
        """This endpoint requires authentication by a Zoo employee. It updates the balance information for the specified org."""

        url = "{}/orgs/{id}/payment/balance".format(self.client.base_url, id=id)

        if include_total_due is not None:
            if "?" in url:
                url = url + "&include_total_due=" + str(include_total_due).lower()
            else:
                url = url + "?include_total_due=" + str(include_total_due).lower()

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CustomerBalance.model_validate(json_data)

    async def update_org_subscription_for_any_org(
        self,
        id: Uuid,
        body: ZooProductSubscriptionsOrgRequest,
    ) -> ZooProductSubscriptions:
        """This endpoint requires authentication by a Zoo admin. It updates the subscription for the specified org."""

        url = "{}/orgs/{id}/payment/subscriptions".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ZooProductSubscriptions.model_validate(json_data)

    async def upsert_subscription_plan_price(
        self,
        slug: str,
        body: PriceUpsertRequest,
    ) -> SubscriptionPlanPriceRecord:
        """You must be a Zoo admin to perform this request."""

        url = "{}/subscription-plans/{slug}/prices".format(
            self.client.base_url, slug=slug
        )

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return SubscriptionPlanPriceRecord.model_validate(json_data)

    async def get_payment_information_for_user(
        self,
    ) -> Customer:
        """This includes billing address, phone, and name.

        This endpoint requires authentication by any Zoo user. It gets the payment information for the authenticated user."""

        url = "{}/user/payment".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Customer.model_validate(json_data)

    async def update_payment_information_for_user(
        self,
        body: BillingInfo,
    ) -> Customer:
        """This includes billing address, phone, and name.

        This endpoint requires authentication by any Zoo user. It updates the payment information for the authenticated user."""

        url = "{}/user/payment".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Customer.model_validate(json_data)

    async def create_payment_information_for_user(
        self,
        body: BillingInfo,
    ) -> Customer:
        """This includes billing address, phone, and name.

        This endpoint requires authentication by any Zoo user. It creates the payment information for the authenticated user."""

        url = "{}/user/payment".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Customer.model_validate(json_data)

    async def delete_payment_information_for_user(
        self,
    ):
        """This includes billing address, phone, and name.

        This endpoint requires authentication by any Zoo user. It deletes the payment information for the authenticated user."""

        url = "{}/user/payment".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def get_payment_balance_for_user(
        self,
        *,
        include_total_due: Optional[bool] = None,
    ) -> CustomerBalance:
        """This endpoint requires authentication by any Zoo user. It gets the balance information for the authenticated user."""

        url = "{}/user/payment/balance".format(self.client.base_url)

        if include_total_due is not None:
            if "?" in url:
                url = url + "&include_total_due=" + str(include_total_due).lower()
            else:
                url = url + "?include_total_due=" + str(include_total_due).lower()

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CustomerBalance.model_validate(json_data)

    async def create_payment_intent_for_user(
        self,
    ) -> PaymentIntent:
        """This endpoint requires authentication by any Zoo user. It creates a new payment intent for the authenticated user."""

        url = "{}/user/payment/intent".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return PaymentIntent.model_validate(json_data)

    async def list_invoices_for_user(
        self,
    ) -> List[Invoice]:
        """This endpoint requires authentication by any Zoo user. It lists invoices for the authenticated user."""

        url = "{}/user/payment/invoices".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(List[Invoice]).validate_python(json_data)

    async def list_payment_methods_for_user(
        self,
    ) -> List[PaymentMethod]:
        """This endpoint requires authentication by any Zoo user. It lists payment methods for the authenticated user."""

        url = "{}/user/payment/methods".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(List[PaymentMethod]).validate_python(json_data)

    async def delete_payment_method_for_user(
        self,
        id: str,
        *,
        force: Optional[bool] = None,
    ):
        """This endpoint requires authentication by any Zoo user. It deletes the specified payment method for the authenticated user."""

        url = "{}/user/payment/methods/{id}".format(self.client.base_url, id=id)

        if force is not None:
            if "?" in url:
                url = url + "&force=" + str(force).lower()
            else:
                url = url + "?force=" + str(force).lower()

        _client = self.client.get_http_client()

        response = await _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def set_default_payment_method_for_user(
        self,
        id: str,
    ):
        """This endpoint requires authentication by any Zoo user. It sets the default payment method for the authenticated user."""

        url = "{}/user/payment/methods/{id}/default".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def get_user_subscription(
        self,
    ) -> ZooProductSubscriptions:
        """This endpoint requires authentication by any Zoo user. It gets the subscription for the user."""

        url = "{}/user/payment/subscriptions".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ZooProductSubscriptions.model_validate(json_data)

    async def update_user_subscription(
        self,
        body: ZooProductSubscriptionsUserRequest,
    ) -> ZooProductSubscriptions:
        """This endpoint requires authentication by any Zoo user. It updates the subscription for the user."""

        url = "{}/user/payment/subscriptions".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ZooProductSubscriptions.model_validate(json_data)

    async def create_user_subscription(
        self,
        body: ZooProductSubscriptionsUserRequest,
    ) -> ZooProductSubscriptions:
        """This endpoint requires authentication by any Zoo user. It creates the subscription for the user."""

        url = "{}/user/payment/subscriptions".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ZooProductSubscriptions.model_validate(json_data)

    async def validate_customer_tax_information_for_user(
        self,
    ):
        """This endpoint requires authentication by any Zoo user. It will return an error if the user's information is not valid for automatic tax. Otherwise, it will return an empty successful response."""

        url = "{}/user/payment/tax".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def get_payment_balance_for_any_user(
        self,
        id: UserIdentifier,
        *,
        include_total_due: Optional[bool] = None,
    ) -> CustomerBalance:
        """This endpoint requires authentication by a Zoo employee. It gets the balance information for the specified user."""

        url = "{}/users/{id}/payment/balance".format(self.client.base_url, id=id)

        if include_total_due is not None:
            if "?" in url:
                url = url + "&include_total_due=" + str(include_total_due).lower()
            else:
                url = url + "?include_total_due=" + str(include_total_due).lower()

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CustomerBalance.model_validate(json_data)

    async def update_payment_balance_for_any_user(
        self,
        id: UserIdentifier,
        body: UpdatePaymentBalance,
        *,
        include_total_due: Optional[bool] = None,
    ) -> CustomerBalance:
        """This endpoint requires authentication by a Zoo employee. It updates the balance information for the specified user."""

        url = "{}/users/{id}/payment/balance".format(self.client.base_url, id=id)

        if include_total_due is not None:
            if "?" in url:
                url = url + "&include_total_due=" + str(include_total_due).lower()
            else:
                url = url + "?include_total_due=" + str(include_total_due).lower()

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CustomerBalance.model_validate(json_data)


class ServiceAccountsAPI:
    """API for service_accounts endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def list_service_accounts_for_org(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "SyncPageIterator":
        """This endpoint requires authentication by an org admin. It returns the service accounts for the organization.

        The service accounts are returned in order of creation, with the most recently created service accounts first.

                Returns an iterator that automatically handles pagination.
                Iterate over all items across all pages:

                    for item in client.org.list_service_accounts_for_org():
                        print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import SyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        def fetch_page(**kw):
            return self._fetch_page_list_service_accounts_for_org(**kw)

        # Create the page iterator
        return SyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    def _fetch_page_list_service_accounts_for_org(
        self, **kwargs
    ) -> ServiceAccountResultsPage:
        """Internal method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/org/service-accounts".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ServiceAccountResultsPage.model_validate(json_data)

    def create_service_account_for_org(
        self,
        *,
        label: Optional[str] = None,
    ) -> ServiceAccount:
        """This endpoint requires authentication by an org admin. It creates a new service account for the organization."""

        url = "{}/org/service-accounts".format(self.client.base_url)

        if label is not None:
            if "?" in url:
                url = url + "&label=" + str(label)
            else:
                url = url + "?label=" + str(label)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ServiceAccount.model_validate(json_data)

    def get_service_account_for_org(
        self,
        token: ServiceAccountUuid,
    ) -> ServiceAccount:
        """This endpoint requires authentication by an org admin. It returns details of the requested service account for the organization."""

        url = "{}/org/service-accounts/{token}".format(
            self.client.base_url, token=token
        )

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ServiceAccount.model_validate(json_data)

    def delete_service_account_for_org(
        self,
        token: ServiceAccountUuid,
    ):
        """This endpoint requires authentication by an org admin. It deletes the requested service account for the organization.

        This endpoint does not actually delete the service account from the database. It merely marks the token as invalid. We still want to keep the service account in the database for historical purposes."""

        url = "{}/org/service-accounts/{token}".format(
            self.client.base_url, token=token
        )

        _client = self.client.get_http_client()

        response = _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None


class AsyncServiceAccountsAPI:
    """Async API for service_accounts endpoints"""

    def __init__(self, client: AsyncClient) -> None:
        self.client = client

    def list_service_accounts_for_org(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "AsyncPageIterator":
        """This endpoint requires authentication by an org admin. It returns the service accounts for the organization.

        The service accounts are returned in order of creation, with the most recently created service accounts first.

                Returns an async iterator that automatically handles pagination.
                Iterate over all items across all pages:

                    async for item in client.org.list_service_accounts_for_org():
                        print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import AsyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        async def fetch_page(**kw):
            return await self._fetch_page_list_service_accounts_for_org(**kw)

        # Create the async page iterator
        return AsyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    async def _fetch_page_list_service_accounts_for_org(
        self, **kwargs
    ) -> ServiceAccountResultsPage:
        """Internal async method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/org/service-accounts".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ServiceAccountResultsPage.model_validate(json_data)

    async def create_service_account_for_org(
        self,
        *,
        label: Optional[str] = None,
    ) -> ServiceAccount:
        """This endpoint requires authentication by an org admin. It creates a new service account for the organization."""

        url = "{}/org/service-accounts".format(self.client.base_url)

        if label is not None:
            if "?" in url:
                url = url + "&label=" + str(label)
            else:
                url = url + "?label=" + str(label)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ServiceAccount.model_validate(json_data)

    async def get_service_account_for_org(
        self,
        token: ServiceAccountUuid,
    ) -> ServiceAccount:
        """This endpoint requires authentication by an org admin. It returns details of the requested service account for the organization."""

        url = "{}/org/service-accounts/{token}".format(
            self.client.base_url, token=token
        )

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ServiceAccount.model_validate(json_data)

    async def delete_service_account_for_org(
        self,
        token: ServiceAccountUuid,
    ):
        """This endpoint requires authentication by an org admin. It deletes the requested service account for the organization.

        This endpoint does not actually delete the service account from the database. It merely marks the token as invalid. We still want to keep the service account in the database for historical purposes."""

        url = "{}/org/service-accounts/{token}".format(
            self.client.base_url, token=token
        )

        _client = self.client.get_http_client()

        response = await _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None


class StoreAPI:
    """API for store endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def create_store_coupon(
        self,
        body: StoreCouponParams,
    ) -> DiscountCode:
        """This endpoint requires authentication by a Zoo employee. It creates a new store coupon."""

        url = "{}/store/coupon".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return DiscountCode.model_validate(json_data)


class AsyncStoreAPI:
    """Async API for store endpoints"""

    def __init__(self, client: AsyncClient) -> None:
        self.client = client

    async def create_store_coupon(
        self,
        body: StoreCouponParams,
    ) -> DiscountCode:
        """This endpoint requires authentication by a Zoo employee. It creates a new store coupon."""

        url = "{}/store/coupon".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return DiscountCode.model_validate(json_data)


class UnitAPI:
    """API for unit endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_angle_unit_conversion(
        self,
        input_unit: UnitAngle,
        output_unit: UnitAngle,
        value: float,
    ) -> UnitAngleConversion:
        """Convert an angle unit value to another angle unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/angle/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitAngleConversion.model_validate(json_data)

    def get_area_unit_conversion(
        self,
        input_unit: UnitArea,
        output_unit: UnitArea,
        value: float,
    ) -> UnitAreaConversion:
        """Convert an area unit value to another area unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/area/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitAreaConversion.model_validate(json_data)

    def get_current_unit_conversion(
        self,
        input_unit: UnitCurrent,
        output_unit: UnitCurrent,
        value: float,
    ) -> UnitCurrentConversion:
        """Convert a current unit value to another current unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/current/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitCurrentConversion.model_validate(json_data)

    def get_energy_unit_conversion(
        self,
        input_unit: UnitEnergy,
        output_unit: UnitEnergy,
        value: float,
    ) -> UnitEnergyConversion:
        """Convert a energy unit value to another energy unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/energy/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitEnergyConversion.model_validate(json_data)

    def get_force_unit_conversion(
        self,
        input_unit: UnitForce,
        output_unit: UnitForce,
        value: float,
    ) -> UnitForceConversion:
        """Convert a force unit value to another force unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/force/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitForceConversion.model_validate(json_data)

    def get_frequency_unit_conversion(
        self,
        input_unit: UnitFrequency,
        output_unit: UnitFrequency,
        value: float,
    ) -> UnitFrequencyConversion:
        """Convert a frequency unit value to another frequency unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/frequency/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitFrequencyConversion.model_validate(json_data)

    def get_length_unit_conversion(
        self,
        input_unit: UnitLength,
        output_unit: UnitLength,
        value: float,
    ) -> UnitLengthConversion:
        """Convert a length unit value to another length unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/length/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitLengthConversion.model_validate(json_data)

    def get_mass_unit_conversion(
        self,
        input_unit: UnitMass,
        output_unit: UnitMass,
        value: float,
    ) -> UnitMassConversion:
        """Convert a mass unit value to another mass unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/mass/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitMassConversion.model_validate(json_data)

    def get_power_unit_conversion(
        self,
        input_unit: UnitPower,
        output_unit: UnitPower,
        value: float,
    ) -> UnitPowerConversion:
        """Convert a power unit value to another power unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/power/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitPowerConversion.model_validate(json_data)

    def get_pressure_unit_conversion(
        self,
        input_unit: UnitPressure,
        output_unit: UnitPressure,
        value: float,
    ) -> UnitPressureConversion:
        """Convert a pressure unit value to another pressure unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/pressure/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitPressureConversion.model_validate(json_data)

    def get_temperature_unit_conversion(
        self,
        input_unit: UnitTemperature,
        output_unit: UnitTemperature,
        value: float,
    ) -> UnitTemperatureConversion:
        """Convert a temperature unit value to another temperature unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/temperature/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitTemperatureConversion.model_validate(json_data)

    def get_torque_unit_conversion(
        self,
        input_unit: UnitTorque,
        output_unit: UnitTorque,
        value: float,
    ) -> UnitTorqueConversion:
        """Convert a torque unit value to another torque unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/torque/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitTorqueConversion.model_validate(json_data)

    def get_volume_unit_conversion(
        self,
        input_unit: UnitVolume,
        output_unit: UnitVolume,
        value: float,
    ) -> UnitVolumeConversion:
        """Convert a volume unit value to another volume unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/volume/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitVolumeConversion.model_validate(json_data)


class AsyncUnitAPI:
    """Async API for unit endpoints"""

    def __init__(self, client: AsyncClient) -> None:
        self.client = client

    async def get_angle_unit_conversion(
        self,
        input_unit: UnitAngle,
        output_unit: UnitAngle,
        value: float,
    ) -> UnitAngleConversion:
        """Convert an angle unit value to another angle unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/angle/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitAngleConversion.model_validate(json_data)

    async def get_area_unit_conversion(
        self,
        input_unit: UnitArea,
        output_unit: UnitArea,
        value: float,
    ) -> UnitAreaConversion:
        """Convert an area unit value to another area unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/area/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitAreaConversion.model_validate(json_data)

    async def get_current_unit_conversion(
        self,
        input_unit: UnitCurrent,
        output_unit: UnitCurrent,
        value: float,
    ) -> UnitCurrentConversion:
        """Convert a current unit value to another current unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/current/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitCurrentConversion.model_validate(json_data)

    async def get_energy_unit_conversion(
        self,
        input_unit: UnitEnergy,
        output_unit: UnitEnergy,
        value: float,
    ) -> UnitEnergyConversion:
        """Convert a energy unit value to another energy unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/energy/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitEnergyConversion.model_validate(json_data)

    async def get_force_unit_conversion(
        self,
        input_unit: UnitForce,
        output_unit: UnitForce,
        value: float,
    ) -> UnitForceConversion:
        """Convert a force unit value to another force unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/force/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitForceConversion.model_validate(json_data)

    async def get_frequency_unit_conversion(
        self,
        input_unit: UnitFrequency,
        output_unit: UnitFrequency,
        value: float,
    ) -> UnitFrequencyConversion:
        """Convert a frequency unit value to another frequency unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/frequency/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitFrequencyConversion.model_validate(json_data)

    async def get_length_unit_conversion(
        self,
        input_unit: UnitLength,
        output_unit: UnitLength,
        value: float,
    ) -> UnitLengthConversion:
        """Convert a length unit value to another length unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/length/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitLengthConversion.model_validate(json_data)

    async def get_mass_unit_conversion(
        self,
        input_unit: UnitMass,
        output_unit: UnitMass,
        value: float,
    ) -> UnitMassConversion:
        """Convert a mass unit value to another mass unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/mass/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitMassConversion.model_validate(json_data)

    async def get_power_unit_conversion(
        self,
        input_unit: UnitPower,
        output_unit: UnitPower,
        value: float,
    ) -> UnitPowerConversion:
        """Convert a power unit value to another power unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/power/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitPowerConversion.model_validate(json_data)

    async def get_pressure_unit_conversion(
        self,
        input_unit: UnitPressure,
        output_unit: UnitPressure,
        value: float,
    ) -> UnitPressureConversion:
        """Convert a pressure unit value to another pressure unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/pressure/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitPressureConversion.model_validate(json_data)

    async def get_temperature_unit_conversion(
        self,
        input_unit: UnitTemperature,
        output_unit: UnitTemperature,
        value: float,
    ) -> UnitTemperatureConversion:
        """Convert a temperature unit value to another temperature unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/temperature/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitTemperatureConversion.model_validate(json_data)

    async def get_torque_unit_conversion(
        self,
        input_unit: UnitTorque,
        output_unit: UnitTorque,
        value: float,
    ) -> UnitTorqueConversion:
        """Convert a torque unit value to another torque unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/torque/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitTorqueConversion.model_validate(json_data)

    async def get_volume_unit_conversion(
        self,
        input_unit: UnitVolume,
        output_unit: UnitVolume,
        value: float,
    ) -> UnitVolumeConversion:
        """Convert a volume unit value to another volume unit value. This is a nice endpoint to use for helper functions."""

        url = "{}/unit/conversion/volume/{input_unit}/{output_unit}".format(
            self.client.base_url, input_unit=input_unit, output_unit=output_unit
        )

        if value is not None:
            if "?" in url:
                url = url + "&value=" + str(value)
            else:
                url = url + "?value=" + str(value)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UnitVolumeConversion.model_validate(json_data)


class UsersAPI:
    """API for users endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_user_self(
        self,
    ) -> User:
        """Get the user information for the authenticated user.

        Alternatively, you can also use the `/users/me` endpoint."""

        url = "{}/user".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return User.model_validate(json_data)

    def update_user_self(
        self,
        body: UpdateUser,
    ) -> User:
        """This endpoint requires authentication by any Zoo user. It updates information about the authenticated user."""

        url = "{}/user".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return User.model_validate(json_data)

    def delete_user_self(
        self,
    ):
        """This endpoint requires authentication by any Zoo user. It deletes the authenticated user from Zoo's database.

        This call will only succeed if all invoices associated with the user have been paid in full and there is no outstanding balance."""

        url = "{}/user".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def patch_user_crm(
        self,
        body: CrmData,
    ):
        """Update properties in the CRM"""

        url = "{}/user/crm".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.patch(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def get_user_self_extended(
        self,
    ) -> ExtendedUser:
        """Get the user information for the authenticated user.

        Alternatively, you can also use the `/users-extended/me` endpoint."""

        url = "{}/user/extended".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ExtendedUser.model_validate(json_data)

    def user_features_get(
        self,
    ) -> UserFeatureList:
        """Returns only features that are marked as safe for exposure to clients and currently resolved to `true` for the requesting user (including org overrides)."""

        url = "{}/user/features".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UserFeatureList.model_validate(json_data)

    def put_user_form_self(
        self,
        body: InquiryForm,
    ):
        """It gets attached to the user's account."""

        url = "{}/user/form".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def get_oauth2_providers_for_user(
        self,
    ) -> List[AccountProvider]:
        """If this returns an empty array, then the user has not connected any OAuth2 providers and uses raw email authentication.

        This endpoint requires authentication by any Zoo user. It gets the providers for the authenticated user."""

        url = "{}/user/oauth2/providers".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(List[AccountProvider]).validate_python(json_data)

    def get_user_privacy_settings(
        self,
    ) -> PrivacySettings:
        """This endpoint requires authentication by any Zoo user. It gets the privacy settings for the user."""

        url = "{}/user/privacy".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return PrivacySettings.model_validate(json_data)

    def update_user_privacy_settings(
        self,
        body: PrivacySettings,
    ) -> PrivacySettings:
        """This endpoint requires authentication by any Zoo user. It updates the privacy settings for the user."""

        url = "{}/user/privacy".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return PrivacySettings.model_validate(json_data)

    def get_session_for_user(
        self,
        token: SessionUuid,
    ) -> Session:
        """This endpoint requires authentication by any Zoo user. It returns details of the requested API token for the user."""

        url = "{}/user/session/{token}".format(self.client.base_url, token=token)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Session.model_validate(json_data)

    def get_user_shortlinks(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "SyncPageIterator":
        """This endpoint requires authentication by any Zoo user. It gets the shortlinks for the user.

        Returns an iterator that automatically handles pagination.
        Iterate over all items across all pages:

            for item in client.user.get_user_shortlinks():
                print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import SyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        def fetch_page(**kw):
            return self._fetch_page_get_user_shortlinks(**kw)

        # Create the page iterator
        return SyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    def _fetch_page_get_user_shortlinks(self, **kwargs) -> ShortlinkResultsPage:
        """Internal method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/user/shortlinks".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ShortlinkResultsPage.model_validate(json_data)

    def create_user_shortlink(
        self,
        body: CreateShortlinkRequest,
    ) -> CreateShortlinkResponse:
        """This endpoint requires authentication by any Zoo user. It creates a shortlink for the user."""

        url = "{}/user/shortlinks".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CreateShortlinkResponse.model_validate(json_data)

    def update_user_shortlink(
        self,
        key: str,
        body: UpdateShortlinkRequest,
    ):
        """This endpoint requires authentication by any Zoo user. It updates a shortlink for the user.

        This endpoint really only allows you to change the `restrict_to_org` setting of a shortlink. Thus it is only useful for folks who are part of an org. If you are not part of an org, you will not be able to change the `restrict_to_org` status."""

        url = "{}/user/shortlinks/{key}".format(self.client.base_url, key=key)

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def delete_user_shortlink(
        self,
        key: str,
    ):
        """This endpoint requires authentication by any Zoo user. It deletes a shortlink for the user."""

        url = "{}/user/shortlinks/{key}".format(self.client.base_url, key=key)

        _client = self.client.get_http_client()

        response = _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def list_users(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "SyncPageIterator":
        """This endpoint requires authentication by a Zoo employee. The users are returned in order of creation, with the most recently created users first.

        Returns an iterator that automatically handles pagination.
        Iterate over all items across all pages:

            for item in client.users.list_users():
                print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import SyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        def fetch_page(**kw):
            return self._fetch_page_list_users(**kw)

        # Create the page iterator
        return SyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    def _fetch_page_list_users(self, **kwargs) -> UserResultsPage:
        """Internal method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/users".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return UserResultsPage.model_validate(json_data)

    def list_users_extended(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "SyncPageIterator":
        """This endpoint requires authentication by a Zoo employee. The users are returned in order of creation, with the most recently created users first.

        Returns an iterator that automatically handles pagination.
        Iterate over all items across all pages:

            for item in client.users-extended.list_users_extended():
                print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import SyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        def fetch_page(**kw):
            return self._fetch_page_list_users_extended(**kw)

        # Create the page iterator
        return SyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    def _fetch_page_list_users_extended(self, **kwargs) -> ExtendedUserResultsPage:
        """Internal method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/users-extended".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ExtendedUserResultsPage.model_validate(json_data)

    def get_user_extended(
        self,
        id: UserIdentifier,
    ) -> ExtendedUser:
        """To get information about yourself, use `/users-extended/me` as the endpoint. By doing so you will get the user information for the authenticated user.

        Alternatively, to get information about the authenticated user, use `/user/extended` endpoint."""

        url = "{}/users-extended/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ExtendedUser.model_validate(json_data)

    def get_user(
        self,
        id: UserIdentifier,
    ) -> User:
        """To get information about yourself, use `/users/me` as the endpoint. By doing so you will get the user information for the authenticated user.

        Alternatively, to get information about the authenticated user, use `/user` endpoint."""

        url = "{}/users/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return User.model_validate(json_data)

    def user_admin_details_get(
        self,
        id: UserIdentifier,
    ) -> UserAdminDetails:
        """Zoo admins can retrieve extended information about any user, while non-admins receive a 404 to avoid leaking the existence of the resource."""

        url = "{}/users/{id}/admin/details".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UserAdminDetails.model_validate(json_data)

    def update_subscription_for_user(
        self,
        id: UserIdentifier,
        body: ZooProductSubscriptionsUserRequest,
    ) -> ZooProductSubscriptions:
        """You must be a Zoo admin to perform this request."""

        url = "{}/users/{id}/payment/subscriptions".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ZooProductSubscriptions.model_validate(json_data)

    def put_public_form(
        self,
        body: InquiryForm,
    ):
        """users and is not authenticated."""

        url = "{}/website/form".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def put_public_subscribe(
        self,
        body: Subscribe,
    ):
        """Subscribes a user to the newsletter."""

        url = "{}/website/subscribe".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None


class AsyncUsersAPI:
    """Async API for users endpoints"""

    def __init__(self, client: AsyncClient) -> None:
        self.client = client

    async def get_user_self(
        self,
    ) -> User:
        """Get the user information for the authenticated user.

        Alternatively, you can also use the `/users/me` endpoint."""

        url = "{}/user".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return User.model_validate(json_data)

    async def update_user_self(
        self,
        body: UpdateUser,
    ) -> User:
        """This endpoint requires authentication by any Zoo user. It updates information about the authenticated user."""

        url = "{}/user".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return User.model_validate(json_data)

    async def delete_user_self(
        self,
    ):
        """This endpoint requires authentication by any Zoo user. It deletes the authenticated user from Zoo's database.

        This call will only succeed if all invoices associated with the user have been paid in full and there is no outstanding balance."""

        url = "{}/user".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def patch_user_crm(
        self,
        body: CrmData,
    ):
        """Update properties in the CRM"""

        url = "{}/user/crm".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.patch(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def get_user_self_extended(
        self,
    ) -> ExtendedUser:
        """Get the user information for the authenticated user.

        Alternatively, you can also use the `/users-extended/me` endpoint."""

        url = "{}/user/extended".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ExtendedUser.model_validate(json_data)

    async def user_features_get(
        self,
    ) -> UserFeatureList:
        """Returns only features that are marked as safe for exposure to clients and currently resolved to `true` for the requesting user (including org overrides)."""

        url = "{}/user/features".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UserFeatureList.model_validate(json_data)

    async def put_user_form_self(
        self,
        body: InquiryForm,
    ):
        """It gets attached to the user's account."""

        url = "{}/user/form".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def get_oauth2_providers_for_user(
        self,
    ) -> List[AccountProvider]:
        """If this returns an empty array, then the user has not connected any OAuth2 providers and uses raw email authentication.

        This endpoint requires authentication by any Zoo user. It gets the providers for the authenticated user."""

        url = "{}/user/oauth2/providers".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into annotated/collection/union types using TypeAdapter
        from pydantic import TypeAdapter

        return TypeAdapter(List[AccountProvider]).validate_python(json_data)

    async def get_user_privacy_settings(
        self,
    ) -> PrivacySettings:
        """This endpoint requires authentication by any Zoo user. It gets the privacy settings for the user."""

        url = "{}/user/privacy".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return PrivacySettings.model_validate(json_data)

    async def update_user_privacy_settings(
        self,
        body: PrivacySettings,
    ) -> PrivacySettings:
        """This endpoint requires authentication by any Zoo user. It updates the privacy settings for the user."""

        url = "{}/user/privacy".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return PrivacySettings.model_validate(json_data)

    async def get_session_for_user(
        self,
        token: SessionUuid,
    ) -> Session:
        """This endpoint requires authentication by any Zoo user. It returns details of the requested API token for the user."""

        url = "{}/user/session/{token}".format(self.client.base_url, token=token)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return Session.model_validate(json_data)

    def get_user_shortlinks(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "AsyncPageIterator":
        """This endpoint requires authentication by any Zoo user. It gets the shortlinks for the user.

        Returns an async iterator that automatically handles pagination.
        Iterate over all items across all pages:

            async for item in client.user.get_user_shortlinks():
                print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import AsyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        async def fetch_page(**kw):
            return await self._fetch_page_get_user_shortlinks(**kw)

        # Create the async page iterator
        return AsyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    async def _fetch_page_get_user_shortlinks(self, **kwargs) -> ShortlinkResultsPage:
        """Internal async method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/user/shortlinks".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ShortlinkResultsPage.model_validate(json_data)

    async def create_user_shortlink(
        self,
        body: CreateShortlinkRequest,
    ) -> CreateShortlinkResponse:
        """This endpoint requires authentication by any Zoo user. It creates a shortlink for the user."""

        url = "{}/user/shortlinks".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return CreateShortlinkResponse.model_validate(json_data)

    async def update_user_shortlink(
        self,
        key: str,
        body: UpdateShortlinkRequest,
    ):
        """This endpoint requires authentication by any Zoo user. It updates a shortlink for the user.

        This endpoint really only allows you to change the `restrict_to_org` setting of a shortlink. Thus it is only useful for folks who are part of an org. If you are not part of an org, you will not be able to change the `restrict_to_org` status."""

        url = "{}/user/shortlinks/{key}".format(self.client.base_url, key=key)

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def delete_user_shortlink(
        self,
        key: str,
    ):
        """This endpoint requires authentication by any Zoo user. It deletes a shortlink for the user."""

        url = "{}/user/shortlinks/{key}".format(self.client.base_url, key=key)

        _client = self.client.get_http_client()

        response = await _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    def list_users(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "AsyncPageIterator":
        """This endpoint requires authentication by a Zoo employee. The users are returned in order of creation, with the most recently created users first.

        Returns an async iterator that automatically handles pagination.
        Iterate over all items across all pages:

            async for item in client.users.list_users():
                print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import AsyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        async def fetch_page(**kw):
            return await self._fetch_page_list_users(**kw)

        # Create the async page iterator
        return AsyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    async def _fetch_page_list_users(self, **kwargs) -> UserResultsPage:
        """Internal async method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/users".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return UserResultsPage.model_validate(json_data)

    def list_users_extended(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "AsyncPageIterator":
        """This endpoint requires authentication by a Zoo employee. The users are returned in order of creation, with the most recently created users first.

        Returns an async iterator that automatically handles pagination.
        Iterate over all items across all pages:

            async for item in client.users-extended.list_users_extended():
                print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import AsyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        async def fetch_page(**kw):
            return await self._fetch_page_list_users_extended(**kw)

        # Create the async page iterator
        return AsyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    async def _fetch_page_list_users_extended(
        self, **kwargs
    ) -> ExtendedUserResultsPage:
        """Internal async method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/users-extended".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ExtendedUserResultsPage.model_validate(json_data)

    async def get_user_extended(
        self,
        id: UserIdentifier,
    ) -> ExtendedUser:
        """To get information about yourself, use `/users-extended/me` as the endpoint. By doing so you will get the user information for the authenticated user.

        Alternatively, to get information about the authenticated user, use `/user/extended` endpoint."""

        url = "{}/users-extended/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ExtendedUser.model_validate(json_data)

    async def get_user(
        self,
        id: UserIdentifier,
    ) -> User:
        """To get information about yourself, use `/users/me` as the endpoint. By doing so you will get the user information for the authenticated user.

        Alternatively, to get information about the authenticated user, use `/user` endpoint."""

        url = "{}/users/{id}".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return User.model_validate(json_data)

    async def user_admin_details_get(
        self,
        id: UserIdentifier,
    ) -> UserAdminDetails:
        """Zoo admins can retrieve extended information about any user, while non-admins receive a 404 to avoid leaking the existence of the resource."""

        url = "{}/users/{id}/admin/details".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return UserAdminDetails.model_validate(json_data)

    async def update_subscription_for_user(
        self,
        id: UserIdentifier,
        body: ZooProductSubscriptionsUserRequest,
    ) -> ZooProductSubscriptions:
        """You must be a Zoo admin to perform this request."""

        url = "{}/users/{id}/payment/subscriptions".format(self.client.base_url, id=id)

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ZooProductSubscriptions.model_validate(json_data)

    async def put_public_form(
        self,
        body: InquiryForm,
    ):
        """users and is not authenticated."""

        url = "{}/website/form".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None

    async def put_public_subscribe(
        self,
        body: Subscribe,
    ):
        """Subscribes a user to the newsletter."""

        url = "{}/website/subscribe".format(self.client.base_url)

        _client = self.client.get_http_client()

        response = await _client.put(
            url=url,
            headers=self.client.get_headers(),
            content=body.model_dump_json(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None


class ApiTokensAPI:
    """API for api_tokens endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def list_api_tokens_for_user(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "SyncPageIterator":
        """This endpoint requires authentication by any Zoo user. It returns the API tokens for the authenticated user.

        The API tokens are returned in order of creation, with the most recently created API tokens first.

                Returns an iterator that automatically handles pagination.
                Iterate over all items across all pages:

                    for item in client.user.list_api_tokens_for_user():
                        print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import SyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        def fetch_page(**kw):
            return self._fetch_page_list_api_tokens_for_user(**kw)

        # Create the page iterator
        return SyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    def _fetch_page_list_api_tokens_for_user(self, **kwargs) -> ApiTokenResultsPage:
        """Internal method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/user/api-tokens".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ApiTokenResultsPage.model_validate(json_data)

    def create_api_token_for_user(
        self,
        *,
        label: Optional[str] = None,
    ) -> ApiToken:
        """This endpoint requires authentication by any Zoo user. It creates a new API token for the authenticated user."""

        url = "{}/user/api-tokens".format(self.client.base_url)

        if label is not None:
            if "?" in url:
                url = url + "&label=" + str(label)
            else:
                url = url + "?label=" + str(label)

        _client = self.client.get_http_client()

        response = _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ApiToken.model_validate(json_data)

    def get_api_token_for_user(
        self,
        token: ApiTokenUuid,
    ) -> ApiToken:
        """This endpoint requires authentication by any Zoo user. It returns details of the requested API token for the user."""

        url = "{}/user/api-tokens/{token}".format(self.client.base_url, token=token)

        _client = self.client.get_http_client()

        response = _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ApiToken.model_validate(json_data)

    def delete_api_token_for_user(
        self,
        token: ApiTokenUuid,
    ):
        """This endpoint requires authentication by any Zoo user. It deletes the requested API token for the user.

        This endpoint does not actually delete the API token from the database. It merely marks the token as invalid. We still want to keep the token in the database for historical purposes."""

        url = "{}/user/api-tokens/{token}".format(self.client.base_url, token=token)

        _client = self.client.get_http_client()

        response = _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None


class AsyncApiTokensAPI:
    """Async API for api_tokens endpoints"""

    def __init__(self, client: AsyncClient) -> None:
        self.client = client

    def list_api_tokens_for_user(
        self,
        *,
        limit: Optional[int] = None,
        page_token: Optional[str] = None,
        sort_by: Optional[CreatedAtSortMode] = None,
    ) -> "AsyncPageIterator":
        """This endpoint requires authentication by any Zoo user. It returns the API tokens for the authenticated user.

        The API tokens are returned in order of creation, with the most recently created API tokens first.

                Returns an async iterator that automatically handles pagination.
                Iterate over all items across all pages:

                    async for item in client.user.list_api_tokens_for_user():
                        print(item)
        """

        from typing import Any, Dict

        from kittycad.pagination import AsyncPageIterator

        # Store path parameters in closure for later use

        # Create arguments dict, filtering out None values
        kwargs: Dict[str, Any] = {}

        if limit is not None:
            kwargs["limit"] = limit

        if page_token is not None:
            kwargs["page_token"] = page_token

        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        async def fetch_page(**kw):
            return await self._fetch_page_list_api_tokens_for_user(**kw)

        # Create the async page iterator
        return AsyncPageIterator(
            page_fetcher=fetch_page,
            initial_kwargs=kwargs,
        )

    async def _fetch_page_list_api_tokens_for_user(
        self, **kwargs
    ) -> ApiTokenResultsPage:
        """Internal async method to fetch a single page."""
        # Build URL with path parameters
        url = "{}/user/api-tokens".format(self.client.base_url)

        # Add query parameters

        if "limit" in kwargs and kwargs["limit"] is not None:
            if "?" in url:
                url = url + "&limit=" + str(kwargs["limit"])
            else:
                url = url + "?limit=" + str(kwargs["limit"])

        if "page_token" in kwargs and kwargs["page_token"] is not None:
            if "?" in url:
                url = url + "&page_token=" + str(kwargs["page_token"])
            else:
                url = url + "?page_token=" + str(kwargs["page_token"])

        if "sort_by" in kwargs and kwargs["sort_by"] is not None:
            if "?" in url:
                url = url + "&sort_by=" + str(kwargs["sort_by"])
            else:
                url = url + "?sort_by=" + str(kwargs["sort_by"])

        # Pagination parameters (limit, page_token) are already handled above as regular query params

        _client = self.client.get_http_client()
        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()
        # Validate into a Pydantic model (supports BaseModel/RootModel)
        return ApiTokenResultsPage.model_validate(json_data)

    async def create_api_token_for_user(
        self,
        *,
        label: Optional[str] = None,
    ) -> ApiToken:
        """This endpoint requires authentication by any Zoo user. It creates a new API token for the authenticated user."""

        url = "{}/user/api-tokens".format(self.client.base_url)

        if label is not None:
            if "?" in url:
                url = url + "&label=" + str(label)
            else:
                url = url + "?label=" + str(label)

        _client = self.client.get_http_client()

        response = await _client.post(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ApiToken.model_validate(json_data)

    async def get_api_token_for_user(
        self,
        token: ApiTokenUuid,
    ) -> ApiToken:
        """This endpoint requires authentication by any Zoo user. It returns details of the requested API token for the user."""

        url = "{}/user/api-tokens/{token}".format(self.client.base_url, token=token)

        _client = self.client.get_http_client()

        response = await _client.get(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        if not response.content:
            return None  # type: ignore

        json_data = response.json()

        # Validate into a Pydantic model (works for BaseModel and RootModel)
        return ApiToken.model_validate(json_data)

    async def delete_api_token_for_user(
        self,
        token: ApiTokenUuid,
    ):
        """This endpoint requires authentication by any Zoo user. It deletes the requested API token for the user.

        This endpoint does not actually delete the API token from the database. It merely marks the token as invalid. We still want to keep the token in the database for historical purposes."""

        url = "{}/user/api-tokens/{token}".format(self.client.base_url, token=token)

        _client = self.client.get_http_client()

        response = await _client.delete(
            url=url,
            headers=self.client.get_headers(),
        )

        if not response.is_success:
            from kittycad.response_helpers import raise_for_status

            raise_for_status(response)

        return response.json() if response.content else None


class ModelingAPI:
    """API for modeling endpoints"""

    def __init__(self, client: Client) -> None:
        self.client = client

    def modeling_commands_ws(
        self,
        api_call_id: Optional[str] = None,
        fps: Optional[int] = None,
        order_independent_transparency: Optional[bool] = None,
        pool: Optional[str] = None,
        post_effect: Optional[PostEffectType] = None,
        replay: Optional[str] = None,
        show_grid: Optional[bool] = None,
        unlocked_framerate: Optional[bool] = None,
        video_res_height: Optional[int] = None,
        video_res_width: Optional[int] = None,
        webrtc: Optional[bool] = None,
        pr: Optional[int] = None,
        recv_timeout: Optional[float] = None,
        ws_factory: Optional[Callable[..., ClientConnectionSync]] = None,
    ) -> "WebSocketModelingCommandsWs":
        """Open a websocket which accepts modeling commands.

        Returns a WebSocket wrapper with methods for sending/receiving data.
        """
        return WebSocketModelingCommandsWs(
            api_call_id=api_call_id,
            fps=fps,
            order_independent_transparency=order_independent_transparency,
            pool=pool,
            post_effect=post_effect,
            replay=replay,
            show_grid=show_grid,
            unlocked_framerate=unlocked_framerate,
            video_res_height=video_res_height,
            video_res_width=video_res_width,
            webrtc=webrtc,
            pr=pr,
            recv_timeout=recv_timeout,
            ws_factory=ws_factory,
            client=self.client,
        )


class AsyncModelingAPI:
    """Async API for modeling endpoints"""

    def __init__(self, client: AsyncClient) -> None:
        self.client = client

    async def modeling_commands_ws(
        self,
        api_call_id: Optional[str] = None,
        fps: Optional[int] = None,
        order_independent_transparency: Optional[bool] = None,
        pool: Optional[str] = None,
        post_effect: Optional[PostEffectType] = None,
        replay: Optional[str] = None,
        show_grid: Optional[bool] = None,
        unlocked_framerate: Optional[bool] = None,
        video_res_height: Optional[int] = None,
        video_res_width: Optional[int] = None,
        webrtc: Optional[bool] = None,
        pr: Optional[int] = None,
    ):
        """Open a websocket which accepts modeling commands.

        Returns an async WebSocket connection for sending/receiving data.
        """

        # For async clients, return the raw async WebSocket connection
        # This supports await websocket.send() and async for message in websocket
        async def modeling_commands_ws(
            self,
            *,
            api_call_id: Optional[str] = None,
            fps: Optional[int] = None,
            order_independent_transparency: Optional[bool] = None,
            pool: Optional[str] = None,
            post_effect: Optional[PostEffectType] = None,
            replay: Optional[str] = None,
            show_grid: Optional[bool] = None,
            unlocked_framerate: Optional[bool] = None,
            video_res_height: Optional[int] = None,
            video_res_width: Optional[int] = None,
            webrtc: Optional[bool] = None,
            pr: Optional[int] = None,
        ) -> ClientConnectionAsync:
            """Open a websocket which accepts modeling commands."""

            url = "/ws/modeling/commands"

            if api_call_id is not None:
                if "?" in url:
                    url = url + "&api_call_id=" + str(api_call_id)
                else:
                    url = url + "?api_call_id=" + str(api_call_id)

            if fps is not None:
                if "?" in url:
                    url = url + "&fps=" + str(fps)
                else:
                    url = url + "?fps=" + str(fps)

            if order_independent_transparency is not None:
                if "?" in url:
                    url = (
                        url
                        + "&order_independent_transparency="
                        + str(order_independent_transparency).lower()
                    )
                else:
                    url = (
                        url
                        + "?order_independent_transparency="
                        + str(order_independent_transparency).lower()
                    )

            if pool is not None:
                if "?" in url:
                    url = url + "&pool=" + str(pool)
                else:
                    url = url + "?pool=" + str(pool)

            if post_effect is not None:
                if "?" in url:
                    url = url + "&post_effect=" + str(post_effect)
                else:
                    url = url + "?post_effect=" + str(post_effect)

            if replay is not None:
                if "?" in url:
                    url = url + "&replay=" + str(replay)
                else:
                    url = url + "?replay=" + str(replay)

            if show_grid is not None:
                if "?" in url:
                    url = url + "&show_grid=" + str(show_grid).lower()
                else:
                    url = url + "?show_grid=" + str(show_grid).lower()

            if unlocked_framerate is not None:
                if "?" in url:
                    url = url + "&unlocked_framerate=" + str(unlocked_framerate).lower()
                else:
                    url = url + "?unlocked_framerate=" + str(unlocked_framerate).lower()

            if video_res_height is not None:
                if "?" in url:
                    url = url + "&video_res_height=" + str(video_res_height)
                else:
                    url = url + "?video_res_height=" + str(video_res_height)

            if video_res_width is not None:
                if "?" in url:
                    url = url + "&video_res_width=" + str(video_res_width)
                else:
                    url = url + "?video_res_width=" + str(video_res_width)

            if webrtc is not None:
                if "?" in url:
                    url = url + "&webrtc=" + str(webrtc).lower()
                else:
                    url = url + "?webrtc=" + str(webrtc).lower()

            if pr is not None:
                if "?" in url:
                    url = url + "&pr=" + str(pr)
                else:
                    url = url + "?pr=" + str(pr)

            return await ws_connect_async(
                url.replace("http", "ws"),
                extra_headers=self.client.get_headers(),
                close_timeout=120,
                max_size=None,
            )


class WebSocketMlCopilotWs:
    """A websocket connection for ml_copilot_ws."""

    ws: ClientConnectionSync

    def __init__(
        self,
        conversation_id: Optional[str] = None,
        replay: Optional[bool] = None,
        pr: Optional[int] = None,
        recv_timeout: Optional[float] = None,
        ws_factory: Optional[Callable[..., ClientConnectionSync]] = None,
        *,
        client: Client,
    ):
        # Inline WebSocket connection logic

        url = ("{}" + "/ws/ml/copilot").format(client.base_url)

        if conversation_id is not None:
            if "?" in url:
                url = url + "&conversation_id=" + str(conversation_id)
            else:
                url = url + "?conversation_id=" + str(conversation_id)

        if replay is not None:
            if "?" in url:
                url = url + "&replay=" + str(replay).lower()
            else:
                url = url + "?replay=" + str(replay).lower()

        if pr is not None:
            if "?" in url:
                url = url + "&pr=" + str(pr)
            else:
                url = url + "?pr=" + str(pr)

        headers = client.get_headers()
        factory = ws_factory or ws_connect
        self.ws = factory(
            url.replace("http", "ws"),
            additional_headers=headers,
            close_timeout=120,
            max_size=None,
        )
        self._recv_timeout = (
            client.get_websocket_recv_timeout()
            if recv_timeout is None
            else recv_timeout
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
            yield MlCopilotServerMessage.model_validate_json(message)

    def send(self, data: MlCopilotClientMessage):
        """Send data to the websocket."""

        self.ws.send(json.dumps(data.model_dump(exclude_none=True)))

    def send_binary(self, data: MlCopilotClientMessage):
        """Send data as bson to the websocket."""

        self.ws.send(bson.encode(data.model_dump(exclude_none=True)))

    def recv(self) -> MlCopilotServerMessage:
        """Receive data from the websocket."""
        message = self.ws.recv(timeout=self._recv_timeout)

        return MlCopilotServerMessage.model_validate_json(message)

    def close(self):
        """Close the websocket."""
        self.ws.close()


class WebSocketMlReasoningWs:
    """A websocket connection for ml_reasoning_ws."""

    ws: ClientConnectionSync

    def __init__(
        self,
        id: str,
        recv_timeout: Optional[float] = None,
        ws_factory: Optional[Callable[..., ClientConnectionSync]] = None,
        *,
        client: Client,
    ):
        # Inline WebSocket connection logic

        url = ("{}" + "/ws/ml/reasoning/{id}").format(client.base_url, id=id)

        headers = client.get_headers()
        factory = ws_factory or ws_connect
        self.ws = factory(
            url.replace("http", "ws"),
            additional_headers=headers,
            close_timeout=120,
            max_size=None,
        )
        self._recv_timeout = (
            client.get_websocket_recv_timeout()
            if recv_timeout is None
            else recv_timeout
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
            yield MlCopilotServerMessage.model_validate_json(message)

    def send(self, data: MlCopilotClientMessage):
        """Send data to the websocket."""

        self.ws.send(json.dumps(data.model_dump(exclude_none=True)))

    def send_binary(self, data: MlCopilotClientMessage):
        """Send data as bson to the websocket."""

        self.ws.send(bson.encode(data.model_dump(exclude_none=True)))

    def recv(self) -> MlCopilotServerMessage:
        """Receive data from the websocket."""
        message = self.ws.recv(timeout=self._recv_timeout)

        return MlCopilotServerMessage.model_validate_json(message)

    def close(self):
        """Close the websocket."""
        self.ws.close()


class WebSocketCreateExecutorTerm:
    """A websocket connection for create_executor_term."""

    ws: ClientConnectionSync

    def __init__(
        self,
        recv_timeout: Optional[float] = None,
        ws_factory: Optional[Callable[..., ClientConnectionSync]] = None,
        *,
        client: Client,
    ):
        # Inline WebSocket connection logic

        url = ("{}" + "/ws/executor/term").format(client.base_url)

        headers = client.get_headers()
        factory = ws_factory or ws_connect
        self.ws = factory(
            url.replace("http", "ws"),
            additional_headers=headers,
            close_timeout=120,
            max_size=None,
        )
        self._recv_timeout = (
            client.get_websocket_recv_timeout()
            if recv_timeout is None
            else recv_timeout
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
            yield json.loads(message)

    def send(self, data: Dict[str, Any]):
        """Send data to the websocket."""

        self.ws.send(json.dumps(data))

    def send_binary(self, data: Dict[str, Any]):
        """Send data as bson to the websocket."""

        self.ws.send(bson.encode(data))

    def recv(self) -> Dict[str, Any]:
        """Receive data from the websocket."""
        message = self.ws.recv(timeout=self._recv_timeout)

        return json.loads(message)

    def close(self):
        """Close the websocket."""
        self.ws.close()


class WebSocketModelingCommandsWs:
    """A websocket connection for modeling_commands_ws."""

    ws: ClientConnectionSync

    def __init__(
        self,
        api_call_id: Optional[str] = None,
        fps: Optional[int] = None,
        order_independent_transparency: Optional[bool] = None,
        pool: Optional[str] = None,
        post_effect: Optional[PostEffectType] = None,
        replay: Optional[str] = None,
        show_grid: Optional[bool] = None,
        unlocked_framerate: Optional[bool] = None,
        video_res_height: Optional[int] = None,
        video_res_width: Optional[int] = None,
        webrtc: Optional[bool] = None,
        pr: Optional[int] = None,
        recv_timeout: Optional[float] = None,
        ws_factory: Optional[Callable[..., ClientConnectionSync]] = None,
        *,
        client: Client,
    ):
        # Inline WebSocket connection logic

        url = ("{}" + "/ws/modeling/commands").format(client.base_url)

        if api_call_id is not None:
            if "?" in url:
                url = url + "&api_call_id=" + str(api_call_id)
            else:
                url = url + "?api_call_id=" + str(api_call_id)

        if fps is not None:
            if "?" in url:
                url = url + "&fps=" + str(fps)
            else:
                url = url + "?fps=" + str(fps)

        if order_independent_transparency is not None:
            if "?" in url:
                url = (
                    url
                    + "&order_independent_transparency="
                    + str(order_independent_transparency).lower()
                )
            else:
                url = (
                    url
                    + "?order_independent_transparency="
                    + str(order_independent_transparency).lower()
                )

        if pool is not None:
            if "?" in url:
                url = url + "&pool=" + str(pool)
            else:
                url = url + "?pool=" + str(pool)

        if post_effect is not None:
            if "?" in url:
                url = url + "&post_effect=" + str(post_effect)
            else:
                url = url + "?post_effect=" + str(post_effect)

        if replay is not None:
            if "?" in url:
                url = url + "&replay=" + str(replay)
            else:
                url = url + "?replay=" + str(replay)

        if show_grid is not None:
            if "?" in url:
                url = url + "&show_grid=" + str(show_grid).lower()
            else:
                url = url + "?show_grid=" + str(show_grid).lower()

        if unlocked_framerate is not None:
            if "?" in url:
                url = url + "&unlocked_framerate=" + str(unlocked_framerate).lower()
            else:
                url = url + "?unlocked_framerate=" + str(unlocked_framerate).lower()

        if video_res_height is not None:
            if "?" in url:
                url = url + "&video_res_height=" + str(video_res_height)
            else:
                url = url + "?video_res_height=" + str(video_res_height)

        if video_res_width is not None:
            if "?" in url:
                url = url + "&video_res_width=" + str(video_res_width)
            else:
                url = url + "?video_res_width=" + str(video_res_width)

        if webrtc is not None:
            if "?" in url:
                url = url + "&webrtc=" + str(webrtc).lower()
            else:
                url = url + "?webrtc=" + str(webrtc).lower()

        if pr is not None:
            if "?" in url:
                url = url + "&pr=" + str(pr)
            else:
                url = url + "?pr=" + str(pr)

        headers = client.get_headers()
        factory = ws_factory or ws_connect
        self.ws = factory(
            url.replace("http", "ws"),
            additional_headers=headers,
            close_timeout=120,
            max_size=None,
        )
        self._recv_timeout = (
            client.get_websocket_recv_timeout()
            if recv_timeout is None
            else recv_timeout
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
            yield WebSocketResponse.model_validate_json(message)

    def send(self, data: WebSocketRequest):
        """Send data to the websocket."""

        self.ws.send(json.dumps(data.model_dump(exclude_none=True)))

    def send_binary(self, data: WebSocketRequest):
        """Send data as bson to the websocket."""

        self.ws.send(bson.encode(data.model_dump(exclude_none=True)))

    def recv(self) -> WebSocketResponse:
        """Receive data from the websocket."""
        message = self.ws.recv(timeout=self._recv_timeout)

        return WebSocketResponse.model_validate_json(message)

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

    Attributes:


        meta: MetaAPI - Access to meta endpoints


        ml: MlAPI - Access to ml endpoints


        api_calls: ApiCallsAPI - Access to api_calls endpoints


        apps: AppsAPI - Access to apps endpoints


        hidden: HiddenAPI - Access to hidden endpoints


        file: FileAPI - Access to file endpoints


        executor: ExecutorAPI - Access to executor endpoints


        oauth2: Oauth2API - Access to oauth2 endpoints


        orgs: OrgsAPI - Access to orgs endpoints


        payments: PaymentsAPI - Access to payments endpoints


        service_accounts: ServiceAccountsAPI - Access to service_accounts endpoints


        store: StoreAPI - Access to store endpoints


        unit: UnitAPI - Access to unit endpoints


        users: UsersAPI - Access to users endpoints


        api_tokens: ApiTokensAPI - Access to api_tokens endpoints


        modeling: ModelingAPI - Access to modeling endpoints

    """

    # API attribute type annotations for documentation

    meta: "MetaAPI"

    ml: "MlAPI"

    api_calls: "ApiCallsAPI"

    apps: "AppsAPI"

    hidden: "HiddenAPI"

    file: "FileAPI"

    executor: "ExecutorAPI"

    oauth2: "Oauth2API"

    orgs: "OrgsAPI"

    payments: "PaymentsAPI"

    service_accounts: "ServiceAccountsAPI"

    store: "StoreAPI"

    unit: "UnitAPI"

    users: "UsersAPI"

    api_tokens: "ApiTokensAPI"

    modeling: "ModelingAPI"

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

        # Import and initialize API classes

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


class AsyncKittyCAD(AsyncClient):
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

    Attributes:


        meta: AsyncMetaAPI - Access to meta endpoints


        ml: AsyncMlAPI - Access to ml endpoints


        api_calls: AsyncApiCallsAPI - Access to api_calls endpoints


        apps: AsyncAppsAPI - Access to apps endpoints


        hidden: AsyncHiddenAPI - Access to hidden endpoints


        file: AsyncFileAPI - Access to file endpoints


        executor: AsyncExecutorAPI - Access to executor endpoints


        oauth2: AsyncOauth2API - Access to oauth2 endpoints


        orgs: AsyncOrgsAPI - Access to orgs endpoints


        payments: AsyncPaymentsAPI - Access to payments endpoints


        service_accounts: AsyncServiceAccountsAPI - Access to service_accounts endpoints


        store: AsyncStoreAPI - Access to store endpoints


        unit: AsyncUnitAPI - Access to unit endpoints


        users: AsyncUsersAPI - Access to users endpoints


        api_tokens: AsyncApiTokensAPI - Access to api_tokens endpoints


        modeling: AsyncModelingAPI - Access to modeling endpoints

    """

    # API attribute type annotations for documentation

    meta: "AsyncMetaAPI"

    ml: "AsyncMlAPI"

    api_calls: "AsyncApiCallsAPI"

    apps: "AsyncAppsAPI"

    hidden: "AsyncHiddenAPI"

    file: "AsyncFileAPI"

    executor: "AsyncExecutorAPI"

    oauth2: "AsyncOauth2API"

    orgs: "AsyncOrgsAPI"

    payments: "AsyncPaymentsAPI"

    service_accounts: "AsyncServiceAccountsAPI"

    store: "AsyncStoreAPI"

    unit: "AsyncUnitAPI"

    users: "AsyncUsersAPI"

    api_tokens: "AsyncApiTokensAPI"

    modeling: "AsyncModelingAPI"

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

        # Import and initialize async API classes

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
