import datetime
from typing import Dict, List, Optional, Union

import pytest

from kittycad.api.api_calls import (
    get_api_call,
    get_api_call_for_org,
    get_api_call_for_user,
    get_api_call_metrics,
    get_async_operation,
    list_api_calls,
    list_api_calls_for_user,
    list_async_operations,
    org_list_api_calls,
    user_list_api_calls,
)
from kittycad.api.api_tokens import (
    create_api_token_for_user,
    delete_api_token_for_user,
    get_api_token_for_user,
    list_api_tokens_for_user,
)
from kittycad.api.apps import (
    apps_github_callback,
    apps_github_consent,
    apps_github_webhook,
)
from kittycad.api.executor import create_executor_term, create_file_execution
from kittycad.api.file import (
    create_file_center_of_mass,
    create_file_conversion,
    create_file_conversion_options,
    create_file_density,
    create_file_mass,
    create_file_surface_area,
    create_file_volume,
)
from kittycad.api.hidden import (
    auth_api_key,
    auth_email,
    auth_email_callback,
    get_auth_saml,
    get_auth_saml_by_org,
    logout,
    post_auth_saml,
    redirect_user_shortlink,
)
from kittycad.api.meta import (
    community_sso,
    create_debug_uploads,
    create_event,
    get_ipinfo,
    get_pricing_subscriptions,
    get_schema,
    internal_get_api_token_for_discord_user,
    ping,
)
from kittycad.api.ml import (
    create_kcl_code_completions,
    create_proprietary_to_kcl,
    create_text_to_cad,
    create_text_to_cad_iteration,
    create_text_to_cad_model_feedback,
    create_text_to_cad_multi_file_iteration,
    get_ml_prompt,
    get_text_to_cad_model_for_user,
    list_conversations_for_user,
    list_ml_prompts,
    list_text_to_cad_models_for_user,
    ml_copilot_ws,
    ml_reasoning_ws,
)
from kittycad.api.modeling import modeling_commands_ws
from kittycad.api.orgs import (
    create_org,
    create_org_member,
    create_org_saml_idp,
    delete_org,
    delete_org_member,
    delete_org_saml_idp,
    get_any_org,
    get_org,
    get_org_member,
    get_org_privacy_settings,
    get_org_saml_idp,
    get_org_shortlinks,
    get_user_org,
    list_org_members,
    list_orgs,
    update_enterprise_pricing_for_org,
    update_org,
    update_org_member,
    update_org_privacy_settings,
    update_org_saml_idp,
)
from kittycad.api.payments import (
    create_org_subscription,
    create_payment_information_for_org,
    create_payment_information_for_user,
    create_payment_intent_for_org,
    create_payment_intent_for_user,
    create_user_subscription,
    delete_payment_information_for_org,
    delete_payment_information_for_user,
    delete_payment_method_for_org,
    delete_payment_method_for_user,
    get_org_subscription,
    get_payment_balance_for_any_org,
    get_payment_balance_for_any_user,
    get_payment_balance_for_org,
    get_payment_balance_for_user,
    get_payment_information_for_org,
    get_payment_information_for_user,
    get_user_subscription,
    list_invoices_for_org,
    list_invoices_for_user,
    list_payment_methods_for_org,
    list_payment_methods_for_user,
    update_org_subscription,
    update_payment_balance_for_any_org,
    update_payment_balance_for_any_user,
    update_payment_information_for_org,
    update_payment_information_for_user,
    update_user_subscription,
    validate_customer_tax_information_for_org,
    validate_customer_tax_information_for_user,
)
from kittycad.api.service_accounts import (
    create_service_account_for_org,
    delete_service_account_for_org,
    get_service_account_for_org,
    list_service_accounts_for_org,
)
from kittycad.api.store import create_store_coupon
from kittycad.api.unit import (
    get_angle_unit_conversion,
    get_area_unit_conversion,
    get_current_unit_conversion,
    get_energy_unit_conversion,
    get_force_unit_conversion,
    get_frequency_unit_conversion,
    get_length_unit_conversion,
    get_mass_unit_conversion,
    get_power_unit_conversion,
    get_pressure_unit_conversion,
    get_temperature_unit_conversion,
    get_torque_unit_conversion,
    get_volume_unit_conversion,
)
from kittycad.api.users import (
    create_user_shortlink,
    delete_user_self,
    delete_user_shortlink,
    get_oauth2_providers_for_user,
    get_session_for_user,
    get_user,
    get_user_extended,
    get_user_privacy_settings,
    get_user_self,
    get_user_self_extended,
    get_user_shortlinks,
    list_users,
    list_users_extended,
    patch_user_crm,
    put_public_form,
    put_public_subscribe,
    put_user_form_self,
    update_subscription_for_user,
    update_user_privacy_settings,
    update_user_self,
    update_user_shortlink,
)
from kittycad.client import ClientFromEnv
from kittycad.models import (
    AccountProvider,
    ApiCallQueryGroup,
    ApiCallWithPrice,
    ApiCallWithPriceResultsPage,
    ApiToken,
    ApiTokenResultsPage,
    AppClientInfo,
    AsyncApiCallResultsPage,
    AuthApiKeyResponse,
    CodeOutput,
    ConversationResultsPage,
    CreateShortlinkResponse,
    Customer,
    CustomerBalance,
    DiscountCode,
    ExtendedUser,
    ExtendedUserResultsPage,
    FileCenterOfMass,
    FileConversion,
    FileDensity,
    FileMass,
    FileSurfaceArea,
    FileVolume,
    Invoice,
    IpAddrInfo,
    KclCodeCompletionResponse,
    KclModel,
    MlCopilotClientMessage,
    MlPrompt,
    MlPromptResultsPage,
    Org,
    OrgMember,
    OrgMemberResultsPage,
    OrgResultsPage,
    PaymentIntent,
    PaymentMethod,
    Pong,
    SamlIdentityProvider,
    ServiceAccount,
    ServiceAccountResultsPage,
    Session,
    ShortlinkResultsPage,
    TextToCad,
    TextToCadIteration,
    TextToCadMultiFileIteration,
    TextToCadResponse,
    TextToCadResponseResultsPage,
    UnitAngleConversion,
    UnitAreaConversion,
    UnitCurrentConversion,
    UnitEnergyConversion,
    UnitForceConversion,
    UnitFrequencyConversion,
    UnitLengthConversion,
    UnitMassConversion,
    UnitPowerConversion,
    UnitPressureConversion,
    UnitTemperatureConversion,
    UnitTorqueConversion,
    UnitVolumeConversion,
    User,
    UserOrgInfo,
    UserResultsPage,
    VerificationTokenResponse,
    WebSocketRequest,
    ZooProductSubscriptions,
)
from kittycad.models.add_org_member import AddOrgMember
from kittycad.models.api_call_query_group_by import ApiCallQueryGroupBy
from kittycad.models.api_call_status import ApiCallStatus
from kittycad.models.api_token_uuid import ApiTokenUuid
from kittycad.models.axis import Axis
from kittycad.models.axis_direction_pair import AxisDirectionPair
from kittycad.models.base64data import Base64Data
from kittycad.models.billing_info import BillingInfo
from kittycad.models.code_language import CodeLanguage
from kittycad.models.code_option import CodeOption
from kittycad.models.conversion_params import ConversionParams
from kittycad.models.create_shortlink_request import CreateShortlinkRequest
from kittycad.models.created_at_sort_mode import CreatedAtSortMode
from kittycad.models.crm_data import CrmData
from kittycad.models.direction import Direction
from kittycad.models.email_authentication_form import EmailAuthenticationForm
from kittycad.models.enterprise_subscription_tier_price import (
    EnterpriseSubscriptionTierPrice,
    OptionFlat,
)
from kittycad.models.event import Event, OptionModelingAppEvent
from kittycad.models.file_export_format import FileExportFormat
from kittycad.models.file_import_format import FileImportFormat
from kittycad.models.idp_metadata_source import (
    IdpMetadataSource,
    OptionBase64EncodedXml,
)
from kittycad.models.input_format3d import InputFormat3d, OptionStep
from kittycad.models.inquiry_form import InquiryForm
from kittycad.models.inquiry_type import InquiryType
from kittycad.models.kcl_code_completion_params import KclCodeCompletionParams
from kittycad.models.kcl_code_completion_request import KclCodeCompletionRequest
from kittycad.models.ml_copilot_client_message import OptionHeaders, OptionUser
from kittycad.models.ml_feedback import MlFeedback
from kittycad.models.modeling_app_event_type import ModelingAppEventType
from kittycad.models.modeling_app_individual_subscription_tier import (
    ModelingAppIndividualSubscriptionTier,
)
from kittycad.models.modeling_app_organization_subscription_tier import (
    ModelingAppOrganizationSubscriptionTier,
)
from kittycad.models.org_details import OrgDetails
from kittycad.models.output_format3d import OptionPly, OutputFormat3d
from kittycad.models.plan_interval import PlanInterval
from kittycad.models.ply_storage import PlyStorage
from kittycad.models.post_effect_type import PostEffectType
from kittycad.models.privacy_settings import PrivacySettings
from kittycad.models.saml_identity_provider_create import SamlIdentityProviderCreate
from kittycad.models.selection import OptionSceneByName, Selection
from kittycad.models.service_account_uuid import ServiceAccountUuid
from kittycad.models.session_uuid import SessionUuid
from kittycad.models.source_position import SourcePosition
from kittycad.models.source_range import SourceRange
from kittycad.models.source_range_prompt import SourceRangePrompt
from kittycad.models.store_coupon_params import StoreCouponParams
from kittycad.models.subscribe import Subscribe
from kittycad.models.system import System
from kittycad.models.text_to_cad_create_body import TextToCadCreateBody
from kittycad.models.text_to_cad_iteration_body import TextToCadIterationBody
from kittycad.models.text_to_cad_multi_file_iteration_body import (
    TextToCadMultiFileIterationBody,
)
from kittycad.models.unit_angle import UnitAngle
from kittycad.models.unit_area import UnitArea
from kittycad.models.unit_current import UnitCurrent
from kittycad.models.unit_density import UnitDensity
from kittycad.models.unit_energy import UnitEnergy
from kittycad.models.unit_force import UnitForce
from kittycad.models.unit_frequency import UnitFrequency
from kittycad.models.unit_length import UnitLength
from kittycad.models.unit_mass import UnitMass
from kittycad.models.unit_power import UnitPower
from kittycad.models.unit_pressure import UnitPressure
from kittycad.models.unit_temperature import UnitTemperature
from kittycad.models.unit_torque import UnitTorque
from kittycad.models.unit_volume import UnitVolume
from kittycad.models.update_member_to_org_body import UpdateMemberToOrgBody
from kittycad.models.update_payment_balance import UpdatePaymentBalance
from kittycad.models.update_shortlink_request import UpdateShortlinkRequest
from kittycad.models.update_user import UpdateUser
from kittycad.models.user_identifier import UserIdentifier
from kittycad.models.user_org_role import UserOrgRole
from kittycad.models.uuid import Uuid
from kittycad.models.web_socket_request import OptionDebug
from kittycad.models.zoo_product_subscriptions_org_request import (
    ZooProductSubscriptionsOrgRequest,
)
from kittycad.models.zoo_product_subscriptions_user_request import (
    ZooProductSubscriptionsUserRequest,
)
from kittycad.types import Response


@pytest.mark.skip
def test_get_schema():
    # Create our client.
    client = ClientFromEnv()

    result = get_schema.sync(
        client=client,
    )

    body: Dict = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response = get_schema.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_schema_async():
    # Create our client.
    client = ClientFromEnv()

    result = await get_schema.asyncio(
        client=client,
    )

    # OR run async with more info
    response = await get_schema.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_ipinfo():
    # Create our client.
    client = ClientFromEnv()

    result: IpAddrInfo = get_ipinfo.sync(
        client=client,
    )

    body: IpAddrInfo = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[IpAddrInfo] = get_ipinfo.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_ipinfo_async():
    # Create our client.
    client = ClientFromEnv()

    result: IpAddrInfo = await get_ipinfo.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[IpAddrInfo] = await get_ipinfo.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_create_text_to_cad():
    # Create our client.
    client = ClientFromEnv()

    result: TextToCad = create_text_to_cad.sync(
        client=client,
        output_format=FileExportFormat.FBX,
        kcl=None,  # Optional[bool]
        body=TextToCadCreateBody(
            prompt="<string>",
        ),
    )

    body: TextToCad = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[TextToCad] = create_text_to_cad.sync_detailed(
        client=client,
        output_format=FileExportFormat.FBX,
        kcl=None,  # Optional[bool]
        body=TextToCadCreateBody(
            prompt="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_text_to_cad_async():
    # Create our client.
    client = ClientFromEnv()

    result: TextToCad = await create_text_to_cad.asyncio(
        client=client,
        output_format=FileExportFormat.FBX,
        kcl=None,  # Optional[bool]
        body=TextToCadCreateBody(
            prompt="<string>",
        ),
    )

    # OR run async with more info
    response: Response[TextToCad] = await create_text_to_cad.asyncio_detailed(
        client=client,
        output_format=FileExportFormat.FBX,
        kcl=None,  # Optional[bool]
        body=TextToCadCreateBody(
            prompt="<string>",
        ),
    )


@pytest.mark.skip
def test_get_api_call_metrics():
    # Create our client.
    client = ClientFromEnv()

    result: List[ApiCallQueryGroup] = get_api_call_metrics.sync(
        client=client,
        group_by=ApiCallQueryGroupBy.EMAIL,
    )

    body: List[ApiCallQueryGroup] = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[List[ApiCallQueryGroup]] = get_api_call_metrics.sync_detailed(
        client=client,
        group_by=ApiCallQueryGroupBy.EMAIL,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_metrics_async():
    # Create our client.
    client = ClientFromEnv()

    result: List[ApiCallQueryGroup] = await get_api_call_metrics.asyncio(
        client=client,
        group_by=ApiCallQueryGroupBy.EMAIL,
    )

    # OR run async with more info
    response: Response[
        List[ApiCallQueryGroup]
    ] = await get_api_call_metrics.asyncio_detailed(
        client=client,
        group_by=ApiCallQueryGroupBy.EMAIL,
    )


@pytest.mark.skip
def test_list_api_calls():
    # Create our client.
    client = ClientFromEnv()

    result: ApiCallWithPriceResultsPage = list_api_calls.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    body: ApiCallWithPriceResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ApiCallWithPriceResultsPage] = list_api_calls.sync_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_api_calls_async():
    # Create our client.
    client = ClientFromEnv()

    result: ApiCallWithPriceResultsPage = await list_api_calls.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        ApiCallWithPriceResultsPage
    ] = await list_api_calls.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_api_call():
    # Create our client.
    client = ClientFromEnv()

    result: ApiCallWithPrice = get_api_call.sync(
        client=client,
        id="<string>",
    )

    body: ApiCallWithPrice = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ApiCallWithPrice] = get_api_call.sync_detailed(
        client=client,
        id="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_async():
    # Create our client.
    client = ClientFromEnv()

    result: ApiCallWithPrice = await get_api_call.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[ApiCallWithPrice] = await get_api_call.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_apps_github_callback():
    # Create our client.
    client = ClientFromEnv()

    apps_github_callback.sync(
        client=client,
    )

    # OR if you need more info (e.g. status_code)
    apps_github_callback.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_apps_github_callback_async():
    # Create our client.
    client = ClientFromEnv()

    await apps_github_callback.asyncio(
        client=client,
    )

    # OR run async with more info
    await apps_github_callback.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_apps_github_consent():
    # Create our client.
    client = ClientFromEnv()

    result: AppClientInfo = apps_github_consent.sync(
        client=client,
    )

    body: AppClientInfo = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[AppClientInfo] = apps_github_consent.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_apps_github_consent_async():
    # Create our client.
    client = ClientFromEnv()

    result: AppClientInfo = await apps_github_consent.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[AppClientInfo] = await apps_github_consent.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_apps_github_webhook():
    # Create our client.
    client = ClientFromEnv()

    apps_github_webhook.sync(
        client=client,
        body=bytes("some bytes", "utf-8"),
    )

    # OR if you need more info (e.g. status_code)
    apps_github_webhook.sync_detailed(
        client=client,
        body=bytes("some bytes", "utf-8"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_apps_github_webhook_async():
    # Create our client.
    client = ClientFromEnv()

    await apps_github_webhook.asyncio(
        client=client,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    await apps_github_webhook.asyncio_detailed(
        client=client,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_list_async_operations():
    # Create our client.
    client = ClientFromEnv()

    result: AsyncApiCallResultsPage = list_async_operations.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        status=ApiCallStatus.QUEUED,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    body: AsyncApiCallResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[AsyncApiCallResultsPage] = list_async_operations.sync_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        status=ApiCallStatus.QUEUED,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_async_operations_async():
    # Create our client.
    client = ClientFromEnv()

    result: AsyncApiCallResultsPage = await list_async_operations.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        status=ApiCallStatus.QUEUED,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        AsyncApiCallResultsPage
    ] = await list_async_operations.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        status=ApiCallStatus.QUEUED,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_async_operation():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[
            FileConversion,
            FileCenterOfMass,
            FileMass,
            FileVolume,
            FileDensity,
            FileSurfaceArea,
            TextToCad,
            TextToCadIteration,
            TextToCadMultiFileIteration,
        ]
    ] = get_async_operation.sync(
        client=client,
        id="<string>",
    )

    body: Union[
        FileConversion,
        FileCenterOfMass,
        FileMass,
        FileVolume,
        FileDensity,
        FileSurfaceArea,
        TextToCad,
        TextToCadIteration,
        TextToCadMultiFileIteration,
    ] = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[
        Optional[
            Union[
                FileConversion,
                FileCenterOfMass,
                FileMass,
                FileVolume,
                FileDensity,
                FileSurfaceArea,
                TextToCad,
                TextToCadIteration,
                TextToCadMultiFileIteration,
            ]
        ]
    ] = get_async_operation.sync_detailed(
        client=client,
        id="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_async_operation_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[
            FileConversion,
            FileCenterOfMass,
            FileMass,
            FileVolume,
            FileDensity,
            FileSurfaceArea,
            TextToCad,
            TextToCadIteration,
            TextToCadMultiFileIteration,
        ]
    ] = await get_async_operation.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[
        Optional[
            Union[
                FileConversion,
                FileCenterOfMass,
                FileMass,
                FileVolume,
                FileDensity,
                FileSurfaceArea,
                TextToCad,
                TextToCadIteration,
                TextToCadMultiFileIteration,
            ]
        ]
    ] = await get_async_operation.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_auth_api_key():
    # Create our client.
    client = ClientFromEnv()

    result: AuthApiKeyResponse = auth_api_key.sync(
        client=client,
    )

    body: AuthApiKeyResponse = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[AuthApiKeyResponse] = auth_api_key.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_auth_api_key_async():
    # Create our client.
    client = ClientFromEnv()

    result: AuthApiKeyResponse = await auth_api_key.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[AuthApiKeyResponse] = await auth_api_key.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_auth_email():
    # Create our client.
    client = ClientFromEnv()

    result: VerificationTokenResponse = auth_email.sync(
        client=client,
        body=EmailAuthenticationForm(
            email="<string>",
        ),
    )

    body: VerificationTokenResponse = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[VerificationTokenResponse] = auth_email.sync_detailed(
        client=client,
        body=EmailAuthenticationForm(
            email="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_auth_email_async():
    # Create our client.
    client = ClientFromEnv()

    result: VerificationTokenResponse = await auth_email.asyncio(
        client=client,
        body=EmailAuthenticationForm(
            email="<string>",
        ),
    )

    # OR run async with more info
    response: Response[VerificationTokenResponse] = await auth_email.asyncio_detailed(
        client=client,
        body=EmailAuthenticationForm(
            email="<string>",
        ),
    )


@pytest.mark.skip
def test_auth_email_callback():
    # Create our client.
    client = ClientFromEnv()

    auth_email_callback.sync(
        client=client,
        email="<string>",
        token="<string>",
        callback_url=None,  # Optional[str]
    )

    # OR if you need more info (e.g. status_code)
    auth_email_callback.sync_detailed(
        client=client,
        email="<string>",
        token="<string>",
        callback_url=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_auth_email_callback_async():
    # Create our client.
    client = ClientFromEnv()

    await auth_email_callback.asyncio(
        client=client,
        email="<string>",
        token="<string>",
        callback_url=None,  # Optional[str]
    )

    # OR run async with more info
    await auth_email_callback.asyncio_detailed(
        client=client,
        email="<string>",
        token="<string>",
        callback_url=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_auth_saml_by_org():
    # Create our client.
    client = ClientFromEnv()

    get_auth_saml_by_org.sync(
        client=client,
        org_id=Uuid("<string>"),
        callback_url=None,  # Optional[str]
    )

    # OR if you need more info (e.g. status_code)
    get_auth_saml_by_org.sync_detailed(
        client=client,
        org_id=Uuid("<string>"),
        callback_url=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_auth_saml_by_org_async():
    # Create our client.
    client = ClientFromEnv()

    await get_auth_saml_by_org.asyncio(
        client=client,
        org_id=Uuid("<string>"),
        callback_url=None,  # Optional[str]
    )

    # OR run async with more info
    await get_auth_saml_by_org.asyncio_detailed(
        client=client,
        org_id=Uuid("<string>"),
        callback_url=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_auth_saml():
    # Create our client.
    client = ClientFromEnv()

    get_auth_saml.sync(
        client=client,
        provider_id=Uuid("<string>"),
        callback_url=None,  # Optional[str]
    )

    # OR if you need more info (e.g. status_code)
    get_auth_saml.sync_detailed(
        client=client,
        provider_id=Uuid("<string>"),
        callback_url=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_auth_saml_async():
    # Create our client.
    client = ClientFromEnv()

    await get_auth_saml.asyncio(
        client=client,
        provider_id=Uuid("<string>"),
        callback_url=None,  # Optional[str]
    )

    # OR run async with more info
    await get_auth_saml.asyncio_detailed(
        client=client,
        provider_id=Uuid("<string>"),
        callback_url=None,  # Optional[str]
    )


@pytest.mark.skip
def test_post_auth_saml():
    # Create our client.
    client = ClientFromEnv()

    post_auth_saml.sync(
        client=client,
        provider_id=Uuid("<string>"),
        body=bytes("some bytes", "utf-8"),
    )

    # OR if you need more info (e.g. status_code)
    post_auth_saml.sync_detailed(
        client=client,
        provider_id=Uuid("<string>"),
        body=bytes("some bytes", "utf-8"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_post_auth_saml_async():
    # Create our client.
    client = ClientFromEnv()

    await post_auth_saml.asyncio(
        client=client,
        provider_id=Uuid("<string>"),
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    await post_auth_saml.asyncio_detailed(
        client=client,
        provider_id=Uuid("<string>"),
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_community_sso():
    # Create our client.
    client = ClientFromEnv()

    community_sso.sync(
        client=client,
        sig="<string>",
        sso="<string>",
    )

    # OR if you need more info (e.g. status_code)
    community_sso.sync_detailed(
        client=client,
        sig="<string>",
        sso="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_community_sso_async():
    # Create our client.
    client = ClientFromEnv()

    await community_sso.asyncio(
        client=client,
        sig="<string>",
        sso="<string>",
    )

    # OR run async with more info
    await community_sso.asyncio_detailed(
        client=client,
        sig="<string>",
        sso="<string>",
    )


@pytest.mark.skip
def test_create_debug_uploads():
    # Create our client.
    client = ClientFromEnv()

    result: List[str] = create_debug_uploads.sync(
        client=client,
    )

    body: List[str] = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[List[str]] = create_debug_uploads.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_debug_uploads_async():
    # Create our client.
    client = ClientFromEnv()

    result: List[str] = await create_debug_uploads.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[List[str]] = await create_debug_uploads.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_create_event():
    # Create our client.
    client = ClientFromEnv()

    create_event.sync(
        client=client,
        body=Event(
            OptionModelingAppEvent(
                created_at=datetime.datetime.now(),
                event_type=ModelingAppEventType.SUCCESSFUL_COMPILE_BEFORE_CLOSE,
                project_name="<string>",
                source_id="<string>",
                user_id="<string>",
            )
        ),
    )

    # OR if you need more info (e.g. status_code)
    create_event.sync_detailed(
        client=client,
        body=Event(
            OptionModelingAppEvent(
                created_at=datetime.datetime.now(),
                event_type=ModelingAppEventType.SUCCESSFUL_COMPILE_BEFORE_CLOSE,
                project_name="<string>",
                source_id="<string>",
                user_id="<string>",
            )
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_event_async():
    # Create our client.
    client = ClientFromEnv()

    await create_event.asyncio(
        client=client,
        body=Event(
            OptionModelingAppEvent(
                created_at=datetime.datetime.now(),
                event_type=ModelingAppEventType.SUCCESSFUL_COMPILE_BEFORE_CLOSE,
                project_name="<string>",
                source_id="<string>",
                user_id="<string>",
            )
        ),
    )

    # OR run async with more info
    await create_event.asyncio_detailed(
        client=client,
        body=Event(
            OptionModelingAppEvent(
                created_at=datetime.datetime.now(),
                event_type=ModelingAppEventType.SUCCESSFUL_COMPILE_BEFORE_CLOSE,
                project_name="<string>",
                source_id="<string>",
                user_id="<string>",
            )
        ),
    )


@pytest.mark.skip
def test_create_file_center_of_mass():
    # Create our client.
    client = ClientFromEnv()

    result: FileCenterOfMass = create_file_center_of_mass.sync(
        client=client,
        output_unit=UnitLength.CM,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    body: FileCenterOfMass = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[FileCenterOfMass] = create_file_center_of_mass.sync_detailed(
        client=client,
        output_unit=UnitLength.CM,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_center_of_mass_async():
    # Create our client.
    client = ClientFromEnv()

    result: FileCenterOfMass = await create_file_center_of_mass.asyncio(
        client=client,
        output_unit=UnitLength.CM,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[
        FileCenterOfMass
    ] = await create_file_center_of_mass.asyncio_detailed(
        client=client,
        output_unit=UnitLength.CM,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_conversion_options():
    # Create our client.
    client = ClientFromEnv()

    result: FileConversion = create_file_conversion_options.sync(
        client=client,
        body=ConversionParams(
            output_format=OutputFormat3d(
                OptionPly(
                    coords=System(
                        forward=AxisDirectionPair(
                            axis=Axis.Y,
                            direction=Direction.POSITIVE,
                        ),
                        up=AxisDirectionPair(
                            axis=Axis.Y,
                            direction=Direction.POSITIVE,
                        ),
                    ),
                    selection=Selection(
                        OptionSceneByName(
                            name="<string>",
                        )
                    ),
                    storage=PlyStorage.ASCII,
                    units=UnitLength.CM,
                )
            ),
            src_format=InputFormat3d(
                OptionStep(
                    split_closed_faces=False,
                )
            ),
        ),
    )

    body: FileConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[FileConversion] = create_file_conversion_options.sync_detailed(
        client=client,
        body=ConversionParams(
            output_format=OutputFormat3d(
                OptionPly(
                    coords=System(
                        forward=AxisDirectionPair(
                            axis=Axis.Y,
                            direction=Direction.POSITIVE,
                        ),
                        up=AxisDirectionPair(
                            axis=Axis.Y,
                            direction=Direction.POSITIVE,
                        ),
                    ),
                    selection=Selection(
                        OptionSceneByName(
                            name="<string>",
                        )
                    ),
                    storage=PlyStorage.ASCII,
                    units=UnitLength.CM,
                )
            ),
            src_format=InputFormat3d(
                OptionStep(
                    split_closed_faces=False,
                )
            ),
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_conversion_options_async():
    # Create our client.
    client = ClientFromEnv()

    result: FileConversion = await create_file_conversion_options.asyncio(
        client=client,
        body=ConversionParams(
            output_format=OutputFormat3d(
                OptionPly(
                    coords=System(
                        forward=AxisDirectionPair(
                            axis=Axis.Y,
                            direction=Direction.POSITIVE,
                        ),
                        up=AxisDirectionPair(
                            axis=Axis.Y,
                            direction=Direction.POSITIVE,
                        ),
                    ),
                    selection=Selection(
                        OptionSceneByName(
                            name="<string>",
                        )
                    ),
                    storage=PlyStorage.ASCII,
                    units=UnitLength.CM,
                )
            ),
            src_format=InputFormat3d(
                OptionStep(
                    split_closed_faces=False,
                )
            ),
        ),
    )

    # OR run async with more info
    response: Response[
        FileConversion
    ] = await create_file_conversion_options.asyncio_detailed(
        client=client,
        body=ConversionParams(
            output_format=OutputFormat3d(
                OptionPly(
                    coords=System(
                        forward=AxisDirectionPair(
                            axis=Axis.Y,
                            direction=Direction.POSITIVE,
                        ),
                        up=AxisDirectionPair(
                            axis=Axis.Y,
                            direction=Direction.POSITIVE,
                        ),
                    ),
                    selection=Selection(
                        OptionSceneByName(
                            name="<string>",
                        )
                    ),
                    storage=PlyStorage.ASCII,
                    units=UnitLength.CM,
                )
            ),
            src_format=InputFormat3d(
                OptionStep(
                    split_closed_faces=False,
                )
            ),
        ),
    )


@pytest.mark.skip
def test_create_file_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: FileConversion = create_file_conversion.sync(
        client=client,
        output_format=FileExportFormat.FBX,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    body: FileConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[FileConversion] = create_file_conversion.sync_detailed(
        client=client,
        output_format=FileExportFormat.FBX,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: FileConversion = await create_file_conversion.asyncio(
        client=client,
        output_format=FileExportFormat.FBX,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[FileConversion] = await create_file_conversion.asyncio_detailed(
        client=client,
        output_format=FileExportFormat.FBX,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_density():
    # Create our client.
    client = ClientFromEnv()

    result: FileDensity = create_file_density.sync(
        client=client,
        material_mass=3.14,
        material_mass_unit=UnitMass.G,
        output_unit=UnitDensity.LB_FT3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    body: FileDensity = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[FileDensity] = create_file_density.sync_detailed(
        client=client,
        material_mass=3.14,
        material_mass_unit=UnitMass.G,
        output_unit=UnitDensity.LB_FT3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_density_async():
    # Create our client.
    client = ClientFromEnv()

    result: FileDensity = await create_file_density.asyncio(
        client=client,
        material_mass=3.14,
        material_mass_unit=UnitMass.G,
        output_unit=UnitDensity.LB_FT3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[FileDensity] = await create_file_density.asyncio_detailed(
        client=client,
        material_mass=3.14,
        material_mass_unit=UnitMass.G,
        output_unit=UnitDensity.LB_FT3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_execution():
    # Create our client.
    client = ClientFromEnv()

    result: CodeOutput = create_file_execution.sync(
        client=client,
        lang=CodeLanguage.GO,
        output=None,  # Optional[str]
        body=bytes("some bytes", "utf-8"),
    )

    body: CodeOutput = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[CodeOutput] = create_file_execution.sync_detailed(
        client=client,
        lang=CodeLanguage.GO,
        output=None,  # Optional[str]
        body=bytes("some bytes", "utf-8"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_execution_async():
    # Create our client.
    client = ClientFromEnv()

    result: CodeOutput = await create_file_execution.asyncio(
        client=client,
        lang=CodeLanguage.GO,
        output=None,  # Optional[str]
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[CodeOutput] = await create_file_execution.asyncio_detailed(
        client=client,
        lang=CodeLanguage.GO,
        output=None,  # Optional[str]
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_mass():
    # Create our client.
    client = ClientFromEnv()

    result: FileMass = create_file_mass.sync(
        client=client,
        material_density=3.14,
        material_density_unit=UnitDensity.LB_FT3,
        output_unit=UnitMass.G,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    body: FileMass = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[FileMass] = create_file_mass.sync_detailed(
        client=client,
        material_density=3.14,
        material_density_unit=UnitDensity.LB_FT3,
        output_unit=UnitMass.G,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_mass_async():
    # Create our client.
    client = ClientFromEnv()

    result: FileMass = await create_file_mass.asyncio(
        client=client,
        material_density=3.14,
        material_density_unit=UnitDensity.LB_FT3,
        output_unit=UnitMass.G,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[FileMass] = await create_file_mass.asyncio_detailed(
        client=client,
        material_density=3.14,
        material_density_unit=UnitDensity.LB_FT3,
        output_unit=UnitMass.G,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_surface_area():
    # Create our client.
    client = ClientFromEnv()

    result: FileSurfaceArea = create_file_surface_area.sync(
        client=client,
        output_unit=UnitArea.CM2,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    body: FileSurfaceArea = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[FileSurfaceArea] = create_file_surface_area.sync_detailed(
        client=client,
        output_unit=UnitArea.CM2,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_surface_area_async():
    # Create our client.
    client = ClientFromEnv()

    result: FileSurfaceArea = await create_file_surface_area.asyncio(
        client=client,
        output_unit=UnitArea.CM2,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[
        FileSurfaceArea
    ] = await create_file_surface_area.asyncio_detailed(
        client=client,
        output_unit=UnitArea.CM2,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_volume():
    # Create our client.
    client = ClientFromEnv()

    result: FileVolume = create_file_volume.sync(
        client=client,
        output_unit=UnitVolume.CM3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    body: FileVolume = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[FileVolume] = create_file_volume.sync_detailed(
        client=client,
        output_unit=UnitVolume.CM3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_volume_async():
    # Create our client.
    client = ClientFromEnv()

    result: FileVolume = await create_file_volume.asyncio(
        client=client,
        output_unit=UnitVolume.CM3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[FileVolume] = await create_file_volume.asyncio_detailed(
        client=client,
        output_unit=UnitVolume.CM3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_internal_get_api_token_for_discord_user():
    # Create our client.
    client = ClientFromEnv()

    result: ApiToken = internal_get_api_token_for_discord_user.sync(
        client=client,
        discord_id="<string>",
    )

    body: ApiToken = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ApiToken] = (
        internal_get_api_token_for_discord_user.sync_detailed(
            client=client,
            discord_id="<string>",
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_internal_get_api_token_for_discord_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: ApiToken = await internal_get_api_token_for_discord_user.asyncio(
        client=client,
        discord_id="<string>",
    )

    # OR run async with more info
    response: Response[
        ApiToken
    ] = await internal_get_api_token_for_discord_user.asyncio_detailed(
        client=client,
        discord_id="<string>",
    )


@pytest.mark.skip
def test_logout():
    # Create our client.
    client = ClientFromEnv()

    logout.sync(
        client=client,
    )

    # OR if you need more info (e.g. status_code)
    logout.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_logout_async():
    # Create our client.
    client = ClientFromEnv()

    await logout.asyncio(
        client=client,
    )

    # OR run async with more info
    await logout.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_list_ml_prompts():
    # Create our client.
    client = ClientFromEnv()

    result: MlPromptResultsPage = list_ml_prompts.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    body: MlPromptResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[MlPromptResultsPage] = list_ml_prompts.sync_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_ml_prompts_async():
    # Create our client.
    client = ClientFromEnv()

    result: MlPromptResultsPage = await list_ml_prompts.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[MlPromptResultsPage] = await list_ml_prompts.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_ml_prompt():
    # Create our client.
    client = ClientFromEnv()

    result: MlPrompt = get_ml_prompt.sync(
        client=client,
        id="<string>",
    )

    body: MlPrompt = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[MlPrompt] = get_ml_prompt.sync_detailed(
        client=client,
        id="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_ml_prompt_async():
    # Create our client.
    client = ClientFromEnv()

    result: MlPrompt = await get_ml_prompt.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[MlPrompt] = await get_ml_prompt.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_list_conversations_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: ConversationResultsPage = list_conversations_for_user.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    body: ConversationResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ConversationResultsPage] = (
        list_conversations_for_user.sync_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_conversations_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: ConversationResultsPage = await list_conversations_for_user.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        ConversationResultsPage
    ] = await list_conversations_for_user.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_create_proprietary_to_kcl():
    # Create our client.
    client = ClientFromEnv()

    result: KclModel = create_proprietary_to_kcl.sync(
        client=client,
        code_option=CodeOption.PARSE,
    )

    body: KclModel = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[KclModel] = create_proprietary_to_kcl.sync_detailed(
        client=client,
        code_option=CodeOption.PARSE,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_proprietary_to_kcl_async():
    # Create our client.
    client = ClientFromEnv()

    result: KclModel = await create_proprietary_to_kcl.asyncio(
        client=client,
        code_option=CodeOption.PARSE,
    )

    # OR run async with more info
    response: Response[KclModel] = await create_proprietary_to_kcl.asyncio_detailed(
        client=client,
        code_option=CodeOption.PARSE,
    )


@pytest.mark.skip
def test_create_kcl_code_completions():
    # Create our client.
    client = ClientFromEnv()

    result: KclCodeCompletionResponse = create_kcl_code_completions.sync(
        client=client,
        body=KclCodeCompletionRequest(
            extra=KclCodeCompletionParams(
                language="<string>",
                trim_by_indentation=False,
            ),
            prompt="<string>",
            stop=["<string>"],
            stream=False,
            suffix="<string>",
        ),
    )

    body: KclCodeCompletionResponse = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[KclCodeCompletionResponse] = (
        create_kcl_code_completions.sync_detailed(
            client=client,
            body=KclCodeCompletionRequest(
                extra=KclCodeCompletionParams(
                    language="<string>",
                    trim_by_indentation=False,
                ),
                prompt="<string>",
                stop=["<string>"],
                stream=False,
                suffix="<string>",
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_kcl_code_completions_async():
    # Create our client.
    client = ClientFromEnv()

    result: KclCodeCompletionResponse = await create_kcl_code_completions.asyncio(
        client=client,
        body=KclCodeCompletionRequest(
            extra=KclCodeCompletionParams(
                language="<string>",
                trim_by_indentation=False,
            ),
            prompt="<string>",
            stop=["<string>"],
            stream=False,
            suffix="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        KclCodeCompletionResponse
    ] = await create_kcl_code_completions.asyncio_detailed(
        client=client,
        body=KclCodeCompletionRequest(
            extra=KclCodeCompletionParams(
                language="<string>",
                trim_by_indentation=False,
            ),
            prompt="<string>",
            stop=["<string>"],
            stream=False,
            suffix="<string>",
        ),
    )


@pytest.mark.skip
def test_create_text_to_cad_iteration():
    # Create our client.
    client = ClientFromEnv()

    result: TextToCadIteration = create_text_to_cad_iteration.sync(
        client=client,
        body=TextToCadIterationBody(
            original_source_code="<string>",
            source_ranges=[
                SourceRangePrompt(
                    prompt="<string>",
                    range=SourceRange(
                        end=SourcePosition(
                            column=10,
                            line=10,
                        ),
                        start=SourcePosition(
                            column=10,
                            line=10,
                        ),
                    ),
                )
            ],
        ),
    )

    body: TextToCadIteration = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[TextToCadIteration] = create_text_to_cad_iteration.sync_detailed(
        client=client,
        body=TextToCadIterationBody(
            original_source_code="<string>",
            source_ranges=[
                SourceRangePrompt(
                    prompt="<string>",
                    range=SourceRange(
                        end=SourcePosition(
                            column=10,
                            line=10,
                        ),
                        start=SourcePosition(
                            column=10,
                            line=10,
                        ),
                    ),
                )
            ],
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_text_to_cad_iteration_async():
    # Create our client.
    client = ClientFromEnv()

    result: TextToCadIteration = await create_text_to_cad_iteration.asyncio(
        client=client,
        body=TextToCadIterationBody(
            original_source_code="<string>",
            source_ranges=[
                SourceRangePrompt(
                    prompt="<string>",
                    range=SourceRange(
                        end=SourcePosition(
                            column=10,
                            line=10,
                        ),
                        start=SourcePosition(
                            column=10,
                            line=10,
                        ),
                    ),
                )
            ],
        ),
    )

    # OR run async with more info
    response: Response[
        TextToCadIteration
    ] = await create_text_to_cad_iteration.asyncio_detailed(
        client=client,
        body=TextToCadIterationBody(
            original_source_code="<string>",
            source_ranges=[
                SourceRangePrompt(
                    prompt="<string>",
                    range=SourceRange(
                        end=SourcePosition(
                            column=10,
                            line=10,
                        ),
                        start=SourcePosition(
                            column=10,
                            line=10,
                        ),
                    ),
                )
            ],
        ),
    )


@pytest.mark.skip
def test_create_text_to_cad_multi_file_iteration():
    # Create our client.
    client = ClientFromEnv()

    result: TextToCadMultiFileIteration = create_text_to_cad_multi_file_iteration.sync(
        client=client,
        body=TextToCadMultiFileIterationBody(
            source_ranges=[
                SourceRangePrompt(
                    prompt="<string>",
                    range=SourceRange(
                        end=SourcePosition(
                            column=10,
                            line=10,
                        ),
                        start=SourcePosition(
                            column=10,
                            line=10,
                        ),
                    ),
                )
            ],
        ),
    )

    body: TextToCadMultiFileIteration = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[TextToCadMultiFileIteration] = (
        create_text_to_cad_multi_file_iteration.sync_detailed(
            client=client,
            body=TextToCadMultiFileIterationBody(
                source_ranges=[
                    SourceRangePrompt(
                        prompt="<string>",
                        range=SourceRange(
                            end=SourcePosition(
                                column=10,
                                line=10,
                            ),
                            start=SourcePosition(
                                column=10,
                                line=10,
                            ),
                        ),
                    )
                ],
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_text_to_cad_multi_file_iteration_async():
    # Create our client.
    client = ClientFromEnv()

    result: TextToCadMultiFileIteration = (
        await create_text_to_cad_multi_file_iteration.asyncio(
            client=client,
            body=TextToCadMultiFileIterationBody(
                source_ranges=[
                    SourceRangePrompt(
                        prompt="<string>",
                        range=SourceRange(
                            end=SourcePosition(
                                column=10,
                                line=10,
                            ),
                            start=SourcePosition(
                                column=10,
                                line=10,
                            ),
                        ),
                    )
                ],
            ),
        )
    )

    # OR run async with more info
    response: Response[
        TextToCadMultiFileIteration
    ] = await create_text_to_cad_multi_file_iteration.asyncio_detailed(
        client=client,
        body=TextToCadMultiFileIterationBody(
            source_ranges=[
                SourceRangePrompt(
                    prompt="<string>",
                    range=SourceRange(
                        end=SourcePosition(
                            column=10,
                            line=10,
                        ),
                        start=SourcePosition(
                            column=10,
                            line=10,
                        ),
                    ),
                )
            ],
        ),
    )


@pytest.mark.skip
def test_delete_org():
    # Create our client.
    client = ClientFromEnv()

    delete_org.sync(
        client=client,
    )

    # OR if you need more info (e.g. status_code)
    delete_org.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_org_async():
    # Create our client.
    client = ClientFromEnv()

    await delete_org.asyncio(
        client=client,
    )

    # OR run async with more info
    await delete_org.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_org():
    # Create our client.
    client = ClientFromEnv()

    result: Org = get_org.sync(
        client=client,
    )

    body: Org = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Org] = get_org.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Org = await get_org.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[Org] = await get_org.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_create_org():
    # Create our client.
    client = ClientFromEnv()

    result: Org = create_org.sync(
        client=client,
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        ),
    )

    body: Org = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Org] = create_org.sync_detailed(
        client=client,
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Org = await create_org.asyncio(
        client=client,
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        ),
    )

    # OR run async with more info
    response: Response[Org] = await create_org.asyncio_detailed(
        client=client,
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        ),
    )


@pytest.mark.skip
def test_update_org():
    # Create our client.
    client = ClientFromEnv()

    result: Org = update_org.sync(
        client=client,
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        ),
    )

    body: Org = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Org] = update_org.sync_detailed(
        client=client,
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Org = await update_org.asyncio(
        client=client,
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        ),
    )

    # OR run async with more info
    response: Response[Org] = await update_org.asyncio_detailed(
        client=client,
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        ),
    )


@pytest.mark.skip
def test_org_list_api_calls():
    # Create our client.
    client = ClientFromEnv()

    result: ApiCallWithPriceResultsPage = org_list_api_calls.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    body: ApiCallWithPriceResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ApiCallWithPriceResultsPage] = org_list_api_calls.sync_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_org_list_api_calls_async():
    # Create our client.
    client = ClientFromEnv()

    result: ApiCallWithPriceResultsPage = await org_list_api_calls.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        ApiCallWithPriceResultsPage
    ] = await org_list_api_calls.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_api_call_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: ApiCallWithPrice = get_api_call_for_org.sync(
        client=client,
        id="<string>",
    )

    body: ApiCallWithPrice = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ApiCallWithPrice] = get_api_call_for_org.sync_detailed(
        client=client,
        id="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: ApiCallWithPrice = await get_api_call_for_org.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[ApiCallWithPrice] = await get_api_call_for_org.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_list_org_members():
    # Create our client.
    client = ClientFromEnv()

    result: OrgMemberResultsPage = list_org_members.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        role=UserOrgRole.ADMIN,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    body: OrgMemberResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[OrgMemberResultsPage] = list_org_members.sync_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        role=UserOrgRole.ADMIN,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_org_members_async():
    # Create our client.
    client = ClientFromEnv()

    result: OrgMemberResultsPage = await list_org_members.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        role=UserOrgRole.ADMIN,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[OrgMemberResultsPage] = await list_org_members.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        role=UserOrgRole.ADMIN,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_create_org_member():
    # Create our client.
    client = ClientFromEnv()

    result: OrgMember = create_org_member.sync(
        client=client,
        body=AddOrgMember(
            email="<string>",
            role=UserOrgRole.ADMIN,
        ),
    )

    body: OrgMember = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[OrgMember] = create_org_member.sync_detailed(
        client=client,
        body=AddOrgMember(
            email="<string>",
            role=UserOrgRole.ADMIN,
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_org_member_async():
    # Create our client.
    client = ClientFromEnv()

    result: OrgMember = await create_org_member.asyncio(
        client=client,
        body=AddOrgMember(
            email="<string>",
            role=UserOrgRole.ADMIN,
        ),
    )

    # OR run async with more info
    response: Response[OrgMember] = await create_org_member.asyncio_detailed(
        client=client,
        body=AddOrgMember(
            email="<string>",
            role=UserOrgRole.ADMIN,
        ),
    )


@pytest.mark.skip
def test_delete_org_member():
    # Create our client.
    client = ClientFromEnv()

    delete_org_member.sync(
        client=client,
        user_id=Uuid("<string>"),
    )

    # OR if you need more info (e.g. status_code)
    delete_org_member.sync_detailed(
        client=client,
        user_id=Uuid("<string>"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_org_member_async():
    # Create our client.
    client = ClientFromEnv()

    await delete_org_member.asyncio(
        client=client,
        user_id=Uuid("<string>"),
    )

    # OR run async with more info
    await delete_org_member.asyncio_detailed(
        client=client,
        user_id=Uuid("<string>"),
    )


@pytest.mark.skip
def test_get_org_member():
    # Create our client.
    client = ClientFromEnv()

    result: OrgMember = get_org_member.sync(
        client=client,
        user_id=Uuid("<string>"),
    )

    body: OrgMember = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[OrgMember] = get_org_member.sync_detailed(
        client=client,
        user_id=Uuid("<string>"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_member_async():
    # Create our client.
    client = ClientFromEnv()

    result: OrgMember = await get_org_member.asyncio(
        client=client,
        user_id=Uuid("<string>"),
    )

    # OR run async with more info
    response: Response[OrgMember] = await get_org_member.asyncio_detailed(
        client=client,
        user_id=Uuid("<string>"),
    )


@pytest.mark.skip
def test_update_org_member():
    # Create our client.
    client = ClientFromEnv()

    result: OrgMember = update_org_member.sync(
        client=client,
        user_id=Uuid("<string>"),
        body=UpdateMemberToOrgBody(
            role=UserOrgRole.ADMIN,
        ),
    )

    body: OrgMember = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[OrgMember] = update_org_member.sync_detailed(
        client=client,
        user_id=Uuid("<string>"),
        body=UpdateMemberToOrgBody(
            role=UserOrgRole.ADMIN,
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_member_async():
    # Create our client.
    client = ClientFromEnv()

    result: OrgMember = await update_org_member.asyncio(
        client=client,
        user_id=Uuid("<string>"),
        body=UpdateMemberToOrgBody(
            role=UserOrgRole.ADMIN,
        ),
    )

    # OR run async with more info
    response: Response[OrgMember] = await update_org_member.asyncio_detailed(
        client=client,
        user_id=Uuid("<string>"),
        body=UpdateMemberToOrgBody(
            role=UserOrgRole.ADMIN,
        ),
    )


@pytest.mark.skip
def test_delete_payment_information_for_org():
    # Create our client.
    client = ClientFromEnv()

    delete_payment_information_for_org.sync(
        client=client,
    )

    # OR if you need more info (e.g. status_code)
    delete_payment_information_for_org.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_payment_information_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    await delete_payment_information_for_org.asyncio(
        client=client,
    )

    # OR run async with more info
    await delete_payment_information_for_org.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_payment_information_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Customer = get_payment_information_for_org.sync(
        client=client,
    )

    body: Customer = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Customer] = get_payment_information_for_org.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_information_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Customer = await get_payment_information_for_org.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Customer
    ] = await get_payment_information_for_org.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_create_payment_information_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Customer = create_payment_information_for_org.sync(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    body: Customer = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Customer] = create_payment_information_for_org.sync_detailed(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_payment_information_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Customer = await create_payment_information_for_org.asyncio(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        Customer
    ] = await create_payment_information_for_org.asyncio_detailed(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )


@pytest.mark.skip
def test_update_payment_information_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Customer = update_payment_information_for_org.sync(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    body: Customer = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Customer] = update_payment_information_for_org.sync_detailed(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_payment_information_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Customer = await update_payment_information_for_org.asyncio(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        Customer
    ] = await update_payment_information_for_org.asyncio_detailed(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )


@pytest.mark.skip
def test_get_payment_balance_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: CustomerBalance = get_payment_balance_for_org.sync(
        client=client,
        include_total_due=False,
    )

    body: CustomerBalance = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[CustomerBalance] = get_payment_balance_for_org.sync_detailed(
        client=client,
        include_total_due=False,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: CustomerBalance = await get_payment_balance_for_org.asyncio(
        client=client,
        include_total_due=False,
    )

    # OR run async with more info
    response: Response[
        CustomerBalance
    ] = await get_payment_balance_for_org.asyncio_detailed(
        client=client,
        include_total_due=False,
    )


@pytest.mark.skip
def test_create_payment_intent_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: PaymentIntent = create_payment_intent_for_org.sync(
        client=client,
    )

    body: PaymentIntent = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[PaymentIntent] = create_payment_intent_for_org.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_payment_intent_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: PaymentIntent = await create_payment_intent_for_org.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        PaymentIntent
    ] = await create_payment_intent_for_org.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_list_invoices_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: List[Invoice] = list_invoices_for_org.sync(
        client=client,
    )

    body: List[Invoice] = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[List[Invoice]] = list_invoices_for_org.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_invoices_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: List[Invoice] = await list_invoices_for_org.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[List[Invoice]] = await list_invoices_for_org.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_list_payment_methods_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: List[PaymentMethod] = list_payment_methods_for_org.sync(
        client=client,
    )

    body: List[PaymentMethod] = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[List[PaymentMethod]] = (
        list_payment_methods_for_org.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_payment_methods_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: List[PaymentMethod] = await list_payment_methods_for_org.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        List[PaymentMethod]
    ] = await list_payment_methods_for_org.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_delete_payment_method_for_org():
    # Create our client.
    client = ClientFromEnv()

    delete_payment_method_for_org.sync(
        client=client,
        id="<string>",
    )

    # OR if you need more info (e.g. status_code)
    delete_payment_method_for_org.sync_detailed(
        client=client,
        id="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_payment_method_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    await delete_payment_method_for_org.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    await delete_payment_method_for_org.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_get_org_subscription():
    # Create our client.
    client = ClientFromEnv()

    result: ZooProductSubscriptions = get_org_subscription.sync(
        client=client,
    )

    body: ZooProductSubscriptions = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ZooProductSubscriptions] = get_org_subscription.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_subscription_async():
    # Create our client.
    client = ClientFromEnv()

    result: ZooProductSubscriptions = await get_org_subscription.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        ZooProductSubscriptions
    ] = await get_org_subscription.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_create_org_subscription():
    # Create our client.
    client = ClientFromEnv()

    result: ZooProductSubscriptions = create_org_subscription.sync(
        client=client,
        body=ZooProductSubscriptionsOrgRequest(
            modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
        ),
    )

    body: ZooProductSubscriptions = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ZooProductSubscriptions] = create_org_subscription.sync_detailed(
        client=client,
        body=ZooProductSubscriptionsOrgRequest(
            modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_org_subscription_async():
    # Create our client.
    client = ClientFromEnv()

    result: ZooProductSubscriptions = await create_org_subscription.asyncio(
        client=client,
        body=ZooProductSubscriptionsOrgRequest(
            modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
        ),
    )

    # OR run async with more info
    response: Response[
        ZooProductSubscriptions
    ] = await create_org_subscription.asyncio_detailed(
        client=client,
        body=ZooProductSubscriptionsOrgRequest(
            modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
        ),
    )


@pytest.mark.skip
def test_update_org_subscription():
    # Create our client.
    client = ClientFromEnv()

    result: ZooProductSubscriptions = update_org_subscription.sync(
        client=client,
        body=ZooProductSubscriptionsOrgRequest(
            modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
        ),
    )

    body: ZooProductSubscriptions = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ZooProductSubscriptions] = update_org_subscription.sync_detailed(
        client=client,
        body=ZooProductSubscriptionsOrgRequest(
            modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_subscription_async():
    # Create our client.
    client = ClientFromEnv()

    result: ZooProductSubscriptions = await update_org_subscription.asyncio(
        client=client,
        body=ZooProductSubscriptionsOrgRequest(
            modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
        ),
    )

    # OR run async with more info
    response: Response[
        ZooProductSubscriptions
    ] = await update_org_subscription.asyncio_detailed(
        client=client,
        body=ZooProductSubscriptionsOrgRequest(
            modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
        ),
    )


@pytest.mark.skip
def test_validate_customer_tax_information_for_org():
    # Create our client.
    client = ClientFromEnv()

    validate_customer_tax_information_for_org.sync(
        client=client,
    )

    # OR if you need more info (e.g. status_code)
    validate_customer_tax_information_for_org.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_validate_customer_tax_information_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    await validate_customer_tax_information_for_org.asyncio(
        client=client,
    )

    # OR run async with more info
    await validate_customer_tax_information_for_org.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_org_privacy_settings():
    # Create our client.
    client = ClientFromEnv()

    result: PrivacySettings = get_org_privacy_settings.sync(
        client=client,
    )

    body: PrivacySettings = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[PrivacySettings] = get_org_privacy_settings.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_privacy_settings_async():
    # Create our client.
    client = ClientFromEnv()

    result: PrivacySettings = await get_org_privacy_settings.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        PrivacySettings
    ] = await get_org_privacy_settings.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_update_org_privacy_settings():
    # Create our client.
    client = ClientFromEnv()

    result: PrivacySettings = update_org_privacy_settings.sync(
        client=client,
        body=PrivacySettings(
            can_train_on_data=False,
        ),
    )

    body: PrivacySettings = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[PrivacySettings] = update_org_privacy_settings.sync_detailed(
        client=client,
        body=PrivacySettings(
            can_train_on_data=False,
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_privacy_settings_async():
    # Create our client.
    client = ClientFromEnv()

    result: PrivacySettings = await update_org_privacy_settings.asyncio(
        client=client,
        body=PrivacySettings(
            can_train_on_data=False,
        ),
    )

    # OR run async with more info
    response: Response[
        PrivacySettings
    ] = await update_org_privacy_settings.asyncio_detailed(
        client=client,
        body=PrivacySettings(
            can_train_on_data=False,
        ),
    )


@pytest.mark.skip
def test_delete_org_saml_idp():
    # Create our client.
    client = ClientFromEnv()

    delete_org_saml_idp.sync(
        client=client,
    )

    # OR if you need more info (e.g. status_code)
    delete_org_saml_idp.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_org_saml_idp_async():
    # Create our client.
    client = ClientFromEnv()

    await delete_org_saml_idp.asyncio(
        client=client,
    )

    # OR run async with more info
    await delete_org_saml_idp.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_org_saml_idp():
    # Create our client.
    client = ClientFromEnv()

    result: SamlIdentityProvider = get_org_saml_idp.sync(
        client=client,
    )

    body: SamlIdentityProvider = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[SamlIdentityProvider] = get_org_saml_idp.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_saml_idp_async():
    # Create our client.
    client = ClientFromEnv()

    result: SamlIdentityProvider = await get_org_saml_idp.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[SamlIdentityProvider] = await get_org_saml_idp.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_create_org_saml_idp():
    # Create our client.
    client = ClientFromEnv()

    result: SamlIdentityProvider = create_org_saml_idp.sync(
        client=client,
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=IdpMetadataSource(
                OptionBase64EncodedXml(
                    data=Base64Data(b"<bytes>"),
                )
            ),
            technical_contact_email="<string>",
        ),
    )

    body: SamlIdentityProvider = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[SamlIdentityProvider] = create_org_saml_idp.sync_detailed(
        client=client,
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=IdpMetadataSource(
                OptionBase64EncodedXml(
                    data=Base64Data(b"<bytes>"),
                )
            ),
            technical_contact_email="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_org_saml_idp_async():
    # Create our client.
    client = ClientFromEnv()

    result: SamlIdentityProvider = await create_org_saml_idp.asyncio(
        client=client,
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=IdpMetadataSource(
                OptionBase64EncodedXml(
                    data=Base64Data(b"<bytes>"),
                )
            ),
            technical_contact_email="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        SamlIdentityProvider
    ] = await create_org_saml_idp.asyncio_detailed(
        client=client,
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=IdpMetadataSource(
                OptionBase64EncodedXml(
                    data=Base64Data(b"<bytes>"),
                )
            ),
            technical_contact_email="<string>",
        ),
    )


@pytest.mark.skip
def test_update_org_saml_idp():
    # Create our client.
    client = ClientFromEnv()

    result: SamlIdentityProvider = update_org_saml_idp.sync(
        client=client,
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=IdpMetadataSource(
                OptionBase64EncodedXml(
                    data=Base64Data(b"<bytes>"),
                )
            ),
            technical_contact_email="<string>",
        ),
    )

    body: SamlIdentityProvider = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[SamlIdentityProvider] = update_org_saml_idp.sync_detailed(
        client=client,
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=IdpMetadataSource(
                OptionBase64EncodedXml(
                    data=Base64Data(b"<bytes>"),
                )
            ),
            technical_contact_email="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_saml_idp_async():
    # Create our client.
    client = ClientFromEnv()

    result: SamlIdentityProvider = await update_org_saml_idp.asyncio(
        client=client,
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=IdpMetadataSource(
                OptionBase64EncodedXml(
                    data=Base64Data(b"<bytes>"),
                )
            ),
            technical_contact_email="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        SamlIdentityProvider
    ] = await update_org_saml_idp.asyncio_detailed(
        client=client,
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=IdpMetadataSource(
                OptionBase64EncodedXml(
                    data=Base64Data(b"<bytes>"),
                )
            ),
            technical_contact_email="<string>",
        ),
    )


@pytest.mark.skip
def test_list_service_accounts_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: ServiceAccountResultsPage = list_service_accounts_for_org.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    body: ServiceAccountResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ServiceAccountResultsPage] = (
        list_service_accounts_for_org.sync_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_service_accounts_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: ServiceAccountResultsPage = await list_service_accounts_for_org.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        ServiceAccountResultsPage
    ] = await list_service_accounts_for_org.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_create_service_account_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: ServiceAccount = create_service_account_for_org.sync(
        client=client,
        label=None,  # Optional[str]
    )

    body: ServiceAccount = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ServiceAccount] = create_service_account_for_org.sync_detailed(
        client=client,
        label=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_service_account_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: ServiceAccount = await create_service_account_for_org.asyncio(
        client=client,
        label=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        ServiceAccount
    ] = await create_service_account_for_org.asyncio_detailed(
        client=client,
        label=None,  # Optional[str]
    )


@pytest.mark.skip
def test_delete_service_account_for_org():
    # Create our client.
    client = ClientFromEnv()

    delete_service_account_for_org.sync(
        client=client,
        token=ServiceAccountUuid("<string>"),
    )

    # OR if you need more info (e.g. status_code)
    delete_service_account_for_org.sync_detailed(
        client=client,
        token=ServiceAccountUuid("<string>"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_service_account_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    await delete_service_account_for_org.asyncio(
        client=client,
        token=ServiceAccountUuid("<string>"),
    )

    # OR run async with more info
    await delete_service_account_for_org.asyncio_detailed(
        client=client,
        token=ServiceAccountUuid("<string>"),
    )


@pytest.mark.skip
def test_get_service_account_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: ServiceAccount = get_service_account_for_org.sync(
        client=client,
        token=ServiceAccountUuid("<string>"),
    )

    body: ServiceAccount = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ServiceAccount] = get_service_account_for_org.sync_detailed(
        client=client,
        token=ServiceAccountUuid("<string>"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_service_account_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: ServiceAccount = await get_service_account_for_org.asyncio(
        client=client,
        token=ServiceAccountUuid("<string>"),
    )

    # OR run async with more info
    response: Response[
        ServiceAccount
    ] = await get_service_account_for_org.asyncio_detailed(
        client=client,
        token=ServiceAccountUuid("<string>"),
    )


@pytest.mark.skip
def test_get_org_shortlinks():
    # Create our client.
    client = ClientFromEnv()

    result: ShortlinkResultsPage = get_org_shortlinks.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    body: ShortlinkResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ShortlinkResultsPage] = get_org_shortlinks.sync_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_shortlinks_async():
    # Create our client.
    client = ClientFromEnv()

    result: ShortlinkResultsPage = await get_org_shortlinks.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        ShortlinkResultsPage
    ] = await get_org_shortlinks.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_list_orgs():
    # Create our client.
    client = ClientFromEnv()

    result: OrgResultsPage = list_orgs.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    body: OrgResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[OrgResultsPage] = list_orgs.sync_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_orgs_async():
    # Create our client.
    client = ClientFromEnv()

    result: OrgResultsPage = await list_orgs.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[OrgResultsPage] = await list_orgs.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_any_org():
    # Create our client.
    client = ClientFromEnv()

    result: Org = get_any_org.sync(
        client=client,
        id=Uuid("<string>"),
    )

    body: Org = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Org] = get_any_org.sync_detailed(
        client=client,
        id=Uuid("<string>"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_any_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Org = await get_any_org.asyncio(
        client=client,
        id=Uuid("<string>"),
    )

    # OR run async with more info
    response: Response[Org] = await get_any_org.asyncio_detailed(
        client=client,
        id=Uuid("<string>"),
    )


@pytest.mark.skip
def test_update_enterprise_pricing_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: ZooProductSubscriptions = update_enterprise_pricing_for_org.sync(
        client=client,
        id=Uuid("<string>"),
        body=EnterpriseSubscriptionTierPrice(
            OptionFlat(
                interval=PlanInterval.DAY,
                price=3.14,
            )
        ),
    )

    body: ZooProductSubscriptions = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ZooProductSubscriptions] = (
        update_enterprise_pricing_for_org.sync_detailed(
            client=client,
            id=Uuid("<string>"),
            body=EnterpriseSubscriptionTierPrice(
                OptionFlat(
                    interval=PlanInterval.DAY,
                    price=3.14,
                )
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_enterprise_pricing_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: ZooProductSubscriptions = await update_enterprise_pricing_for_org.asyncio(
        client=client,
        id=Uuid("<string>"),
        body=EnterpriseSubscriptionTierPrice(
            OptionFlat(
                interval=PlanInterval.DAY,
                price=3.14,
            )
        ),
    )

    # OR run async with more info
    response: Response[
        ZooProductSubscriptions
    ] = await update_enterprise_pricing_for_org.asyncio_detailed(
        client=client,
        id=Uuid("<string>"),
        body=EnterpriseSubscriptionTierPrice(
            OptionFlat(
                interval=PlanInterval.DAY,
                price=3.14,
            )
        ),
    )


@pytest.mark.skip
def test_get_payment_balance_for_any_org():
    # Create our client.
    client = ClientFromEnv()

    result: CustomerBalance = get_payment_balance_for_any_org.sync(
        client=client,
        include_total_due=False,
        id=Uuid("<string>"),
    )

    body: CustomerBalance = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[CustomerBalance] = get_payment_balance_for_any_org.sync_detailed(
        client=client,
        include_total_due=False,
        id=Uuid("<string>"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_any_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: CustomerBalance = await get_payment_balance_for_any_org.asyncio(
        client=client,
        include_total_due=False,
        id=Uuid("<string>"),
    )

    # OR run async with more info
    response: Response[
        CustomerBalance
    ] = await get_payment_balance_for_any_org.asyncio_detailed(
        client=client,
        include_total_due=False,
        id=Uuid("<string>"),
    )


@pytest.mark.skip
def test_update_payment_balance_for_any_org():
    # Create our client.
    client = ClientFromEnv()

    result: CustomerBalance = update_payment_balance_for_any_org.sync(
        client=client,
        id=Uuid("<string>"),
        include_total_due=False,
        body=UpdatePaymentBalance(),
    )

    body: CustomerBalance = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[CustomerBalance] = (
        update_payment_balance_for_any_org.sync_detailed(
            client=client,
            id=Uuid("<string>"),
            include_total_due=False,
            body=UpdatePaymentBalance(),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_payment_balance_for_any_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: CustomerBalance = await update_payment_balance_for_any_org.asyncio(
        client=client,
        id=Uuid("<string>"),
        include_total_due=False,
        body=UpdatePaymentBalance(),
    )

    # OR run async with more info
    response: Response[
        CustomerBalance
    ] = await update_payment_balance_for_any_org.asyncio_detailed(
        client=client,
        id=Uuid("<string>"),
        include_total_due=False,
        body=UpdatePaymentBalance(),
    )


@pytest.mark.skip
def test_ping():
    # Create our client.
    client = ClientFromEnv()

    result: Pong = ping.sync(
        client=client,
    )

    body: Pong = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Pong] = ping.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_ping_async():
    # Create our client.
    client = ClientFromEnv()

    result: Pong = await ping.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[Pong] = await ping.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_pricing_subscriptions():
    # Create our client.
    client = ClientFromEnv()

    result: Dict = get_pricing_subscriptions.sync(
        client=client,
    )

    body: Dict = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Dict] = get_pricing_subscriptions.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_pricing_subscriptions_async():
    # Create our client.
    client = ClientFromEnv()

    result: Dict = await get_pricing_subscriptions.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[Dict] = await get_pricing_subscriptions.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_create_store_coupon():
    # Create our client.
    client = ClientFromEnv()

    result: DiscountCode = create_store_coupon.sync(
        client=client,
        body=StoreCouponParams(
            percent_off=10,
        ),
    )

    body: DiscountCode = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[DiscountCode] = create_store_coupon.sync_detailed(
        client=client,
        body=StoreCouponParams(
            percent_off=10,
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_store_coupon_async():
    # Create our client.
    client = ClientFromEnv()

    result: DiscountCode = await create_store_coupon.asyncio(
        client=client,
        body=StoreCouponParams(
            percent_off=10,
        ),
    )

    # OR run async with more info
    response: Response[DiscountCode] = await create_store_coupon.asyncio_detailed(
        client=client,
        body=StoreCouponParams(
            percent_off=10,
        ),
    )


@pytest.mark.skip
def test_get_angle_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: UnitAngleConversion = get_angle_unit_conversion.sync(
        client=client,
        input_unit=UnitAngle.DEGREES,
        output_unit=UnitAngle.DEGREES,
        value=3.14,
    )

    body: UnitAngleConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[UnitAngleConversion] = get_angle_unit_conversion.sync_detailed(
        client=client,
        input_unit=UnitAngle.DEGREES,
        output_unit=UnitAngle.DEGREES,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_angle_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: UnitAngleConversion = await get_angle_unit_conversion.asyncio(
        client=client,
        input_unit=UnitAngle.DEGREES,
        output_unit=UnitAngle.DEGREES,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        UnitAngleConversion
    ] = await get_angle_unit_conversion.asyncio_detailed(
        client=client,
        input_unit=UnitAngle.DEGREES,
        output_unit=UnitAngle.DEGREES,
        value=3.14,
    )


@pytest.mark.skip
def test_get_area_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: UnitAreaConversion = get_area_unit_conversion.sync(
        client=client,
        input_unit=UnitArea.CM2,
        output_unit=UnitArea.CM2,
        value=3.14,
    )

    body: UnitAreaConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[UnitAreaConversion] = get_area_unit_conversion.sync_detailed(
        client=client,
        input_unit=UnitArea.CM2,
        output_unit=UnitArea.CM2,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_area_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: UnitAreaConversion = await get_area_unit_conversion.asyncio(
        client=client,
        input_unit=UnitArea.CM2,
        output_unit=UnitArea.CM2,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        UnitAreaConversion
    ] = await get_area_unit_conversion.asyncio_detailed(
        client=client,
        input_unit=UnitArea.CM2,
        output_unit=UnitArea.CM2,
        value=3.14,
    )


@pytest.mark.skip
def test_get_current_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: UnitCurrentConversion = get_current_unit_conversion.sync(
        client=client,
        input_unit=UnitCurrent.AMPERES,
        output_unit=UnitCurrent.AMPERES,
        value=3.14,
    )

    body: UnitCurrentConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[UnitCurrentConversion] = (
        get_current_unit_conversion.sync_detailed(
            client=client,
            input_unit=UnitCurrent.AMPERES,
            output_unit=UnitCurrent.AMPERES,
            value=3.14,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_current_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: UnitCurrentConversion = await get_current_unit_conversion.asyncio(
        client=client,
        input_unit=UnitCurrent.AMPERES,
        output_unit=UnitCurrent.AMPERES,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        UnitCurrentConversion
    ] = await get_current_unit_conversion.asyncio_detailed(
        client=client,
        input_unit=UnitCurrent.AMPERES,
        output_unit=UnitCurrent.AMPERES,
        value=3.14,
    )


@pytest.mark.skip
def test_get_energy_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: UnitEnergyConversion = get_energy_unit_conversion.sync(
        client=client,
        input_unit=UnitEnergy.BTU,
        output_unit=UnitEnergy.BTU,
        value=3.14,
    )

    body: UnitEnergyConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[UnitEnergyConversion] = get_energy_unit_conversion.sync_detailed(
        client=client,
        input_unit=UnitEnergy.BTU,
        output_unit=UnitEnergy.BTU,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_energy_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: UnitEnergyConversion = await get_energy_unit_conversion.asyncio(
        client=client,
        input_unit=UnitEnergy.BTU,
        output_unit=UnitEnergy.BTU,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        UnitEnergyConversion
    ] = await get_energy_unit_conversion.asyncio_detailed(
        client=client,
        input_unit=UnitEnergy.BTU,
        output_unit=UnitEnergy.BTU,
        value=3.14,
    )


@pytest.mark.skip
def test_get_force_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: UnitForceConversion = get_force_unit_conversion.sync(
        client=client,
        input_unit=UnitForce.DYNES,
        output_unit=UnitForce.DYNES,
        value=3.14,
    )

    body: UnitForceConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[UnitForceConversion] = get_force_unit_conversion.sync_detailed(
        client=client,
        input_unit=UnitForce.DYNES,
        output_unit=UnitForce.DYNES,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_force_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: UnitForceConversion = await get_force_unit_conversion.asyncio(
        client=client,
        input_unit=UnitForce.DYNES,
        output_unit=UnitForce.DYNES,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        UnitForceConversion
    ] = await get_force_unit_conversion.asyncio_detailed(
        client=client,
        input_unit=UnitForce.DYNES,
        output_unit=UnitForce.DYNES,
        value=3.14,
    )


@pytest.mark.skip
def test_get_frequency_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: UnitFrequencyConversion = get_frequency_unit_conversion.sync(
        client=client,
        input_unit=UnitFrequency.GIGAHERTZ,
        output_unit=UnitFrequency.GIGAHERTZ,
        value=3.14,
    )

    body: UnitFrequencyConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[UnitFrequencyConversion] = (
        get_frequency_unit_conversion.sync_detailed(
            client=client,
            input_unit=UnitFrequency.GIGAHERTZ,
            output_unit=UnitFrequency.GIGAHERTZ,
            value=3.14,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_frequency_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: UnitFrequencyConversion = await get_frequency_unit_conversion.asyncio(
        client=client,
        input_unit=UnitFrequency.GIGAHERTZ,
        output_unit=UnitFrequency.GIGAHERTZ,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        UnitFrequencyConversion
    ] = await get_frequency_unit_conversion.asyncio_detailed(
        client=client,
        input_unit=UnitFrequency.GIGAHERTZ,
        output_unit=UnitFrequency.GIGAHERTZ,
        value=3.14,
    )


@pytest.mark.skip
def test_get_length_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: UnitLengthConversion = get_length_unit_conversion.sync(
        client=client,
        input_unit=UnitLength.CM,
        output_unit=UnitLength.CM,
        value=3.14,
    )

    body: UnitLengthConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[UnitLengthConversion] = get_length_unit_conversion.sync_detailed(
        client=client,
        input_unit=UnitLength.CM,
        output_unit=UnitLength.CM,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_length_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: UnitLengthConversion = await get_length_unit_conversion.asyncio(
        client=client,
        input_unit=UnitLength.CM,
        output_unit=UnitLength.CM,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        UnitLengthConversion
    ] = await get_length_unit_conversion.asyncio_detailed(
        client=client,
        input_unit=UnitLength.CM,
        output_unit=UnitLength.CM,
        value=3.14,
    )


@pytest.mark.skip
def test_get_mass_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: UnitMassConversion = get_mass_unit_conversion.sync(
        client=client,
        input_unit=UnitMass.G,
        output_unit=UnitMass.G,
        value=3.14,
    )

    body: UnitMassConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[UnitMassConversion] = get_mass_unit_conversion.sync_detailed(
        client=client,
        input_unit=UnitMass.G,
        output_unit=UnitMass.G,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_mass_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: UnitMassConversion = await get_mass_unit_conversion.asyncio(
        client=client,
        input_unit=UnitMass.G,
        output_unit=UnitMass.G,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        UnitMassConversion
    ] = await get_mass_unit_conversion.asyncio_detailed(
        client=client,
        input_unit=UnitMass.G,
        output_unit=UnitMass.G,
        value=3.14,
    )


@pytest.mark.skip
def test_get_power_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: UnitPowerConversion = get_power_unit_conversion.sync(
        client=client,
        input_unit=UnitPower.BTU_PER_MINUTE,
        output_unit=UnitPower.BTU_PER_MINUTE,
        value=3.14,
    )

    body: UnitPowerConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[UnitPowerConversion] = get_power_unit_conversion.sync_detailed(
        client=client,
        input_unit=UnitPower.BTU_PER_MINUTE,
        output_unit=UnitPower.BTU_PER_MINUTE,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_power_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: UnitPowerConversion = await get_power_unit_conversion.asyncio(
        client=client,
        input_unit=UnitPower.BTU_PER_MINUTE,
        output_unit=UnitPower.BTU_PER_MINUTE,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        UnitPowerConversion
    ] = await get_power_unit_conversion.asyncio_detailed(
        client=client,
        input_unit=UnitPower.BTU_PER_MINUTE,
        output_unit=UnitPower.BTU_PER_MINUTE,
        value=3.14,
    )


@pytest.mark.skip
def test_get_pressure_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: UnitPressureConversion = get_pressure_unit_conversion.sync(
        client=client,
        input_unit=UnitPressure.ATMOSPHERES,
        output_unit=UnitPressure.ATMOSPHERES,
        value=3.14,
    )

    body: UnitPressureConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[UnitPressureConversion] = (
        get_pressure_unit_conversion.sync_detailed(
            client=client,
            input_unit=UnitPressure.ATMOSPHERES,
            output_unit=UnitPressure.ATMOSPHERES,
            value=3.14,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_pressure_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: UnitPressureConversion = await get_pressure_unit_conversion.asyncio(
        client=client,
        input_unit=UnitPressure.ATMOSPHERES,
        output_unit=UnitPressure.ATMOSPHERES,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        UnitPressureConversion
    ] = await get_pressure_unit_conversion.asyncio_detailed(
        client=client,
        input_unit=UnitPressure.ATMOSPHERES,
        output_unit=UnitPressure.ATMOSPHERES,
        value=3.14,
    )


@pytest.mark.skip
def test_get_temperature_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: UnitTemperatureConversion = get_temperature_unit_conversion.sync(
        client=client,
        input_unit=UnitTemperature.CELSIUS,
        output_unit=UnitTemperature.CELSIUS,
        value=3.14,
    )

    body: UnitTemperatureConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[UnitTemperatureConversion] = (
        get_temperature_unit_conversion.sync_detailed(
            client=client,
            input_unit=UnitTemperature.CELSIUS,
            output_unit=UnitTemperature.CELSIUS,
            value=3.14,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_temperature_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: UnitTemperatureConversion = await get_temperature_unit_conversion.asyncio(
        client=client,
        input_unit=UnitTemperature.CELSIUS,
        output_unit=UnitTemperature.CELSIUS,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        UnitTemperatureConversion
    ] = await get_temperature_unit_conversion.asyncio_detailed(
        client=client,
        input_unit=UnitTemperature.CELSIUS,
        output_unit=UnitTemperature.CELSIUS,
        value=3.14,
    )


@pytest.mark.skip
def test_get_torque_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: UnitTorqueConversion = get_torque_unit_conversion.sync(
        client=client,
        input_unit=UnitTorque.NEWTON_METRES,
        output_unit=UnitTorque.NEWTON_METRES,
        value=3.14,
    )

    body: UnitTorqueConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[UnitTorqueConversion] = get_torque_unit_conversion.sync_detailed(
        client=client,
        input_unit=UnitTorque.NEWTON_METRES,
        output_unit=UnitTorque.NEWTON_METRES,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_torque_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: UnitTorqueConversion = await get_torque_unit_conversion.asyncio(
        client=client,
        input_unit=UnitTorque.NEWTON_METRES,
        output_unit=UnitTorque.NEWTON_METRES,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        UnitTorqueConversion
    ] = await get_torque_unit_conversion.asyncio_detailed(
        client=client,
        input_unit=UnitTorque.NEWTON_METRES,
        output_unit=UnitTorque.NEWTON_METRES,
        value=3.14,
    )


@pytest.mark.skip
def test_get_volume_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: UnitVolumeConversion = get_volume_unit_conversion.sync(
        client=client,
        input_unit=UnitVolume.CM3,
        output_unit=UnitVolume.CM3,
        value=3.14,
    )

    body: UnitVolumeConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[UnitVolumeConversion] = get_volume_unit_conversion.sync_detailed(
        client=client,
        input_unit=UnitVolume.CM3,
        output_unit=UnitVolume.CM3,
        value=3.14,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_volume_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: UnitVolumeConversion = await get_volume_unit_conversion.asyncio(
        client=client,
        input_unit=UnitVolume.CM3,
        output_unit=UnitVolume.CM3,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        UnitVolumeConversion
    ] = await get_volume_unit_conversion.asyncio_detailed(
        client=client,
        input_unit=UnitVolume.CM3,
        output_unit=UnitVolume.CM3,
        value=3.14,
    )


@pytest.mark.skip
def test_delete_user_self():
    # Create our client.
    client = ClientFromEnv()

    delete_user_self.sync(
        client=client,
    )

    # OR if you need more info (e.g. status_code)
    delete_user_self.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_user_self_async():
    # Create our client.
    client = ClientFromEnv()

    await delete_user_self.asyncio(
        client=client,
    )

    # OR run async with more info
    await delete_user_self.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_user_self():
    # Create our client.
    client = ClientFromEnv()

    result: User = get_user_self.sync(
        client=client,
    )

    body: User = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[User] = get_user_self.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_self_async():
    # Create our client.
    client = ClientFromEnv()

    result: User = await get_user_self.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[User] = await get_user_self.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_update_user_self():
    # Create our client.
    client = ClientFromEnv()

    result: User = update_user_self.sync(
        client=client,
        body=UpdateUser(
            company="<string>",
            discord="<string>",
            first_name="<string>",
            github="<string>",
            image="<string>",
            last_name="<string>",
            phone="<string>",
        ),
    )

    body: User = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[User] = update_user_self.sync_detailed(
        client=client,
        body=UpdateUser(
            company="<string>",
            discord="<string>",
            first_name="<string>",
            github="<string>",
            image="<string>",
            last_name="<string>",
            phone="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_user_self_async():
    # Create our client.
    client = ClientFromEnv()

    result: User = await update_user_self.asyncio(
        client=client,
        body=UpdateUser(
            company="<string>",
            discord="<string>",
            first_name="<string>",
            github="<string>",
            image="<string>",
            last_name="<string>",
            phone="<string>",
        ),
    )

    # OR run async with more info
    response: Response[User] = await update_user_self.asyncio_detailed(
        client=client,
        body=UpdateUser(
            company="<string>",
            discord="<string>",
            first_name="<string>",
            github="<string>",
            image="<string>",
            last_name="<string>",
            phone="<string>",
        ),
    )


@pytest.mark.skip
def test_user_list_api_calls():
    # Create our client.
    client = ClientFromEnv()

    result: ApiCallWithPriceResultsPage = user_list_api_calls.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    body: ApiCallWithPriceResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ApiCallWithPriceResultsPage] = user_list_api_calls.sync_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_user_list_api_calls_async():
    # Create our client.
    client = ClientFromEnv()

    result: ApiCallWithPriceResultsPage = await user_list_api_calls.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        ApiCallWithPriceResultsPage
    ] = await user_list_api_calls.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_api_call_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: ApiCallWithPrice = get_api_call_for_user.sync(
        client=client,
        id="<string>",
    )

    body: ApiCallWithPrice = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ApiCallWithPrice] = get_api_call_for_user.sync_detailed(
        client=client,
        id="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: ApiCallWithPrice = await get_api_call_for_user.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[ApiCallWithPrice] = await get_api_call_for_user.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_list_api_tokens_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: ApiTokenResultsPage = list_api_tokens_for_user.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    body: ApiTokenResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ApiTokenResultsPage] = list_api_tokens_for_user.sync_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_api_tokens_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: ApiTokenResultsPage = await list_api_tokens_for_user.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        ApiTokenResultsPage
    ] = await list_api_tokens_for_user.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_create_api_token_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: ApiToken = create_api_token_for_user.sync(
        client=client,
        label=None,  # Optional[str]
    )

    body: ApiToken = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ApiToken] = create_api_token_for_user.sync_detailed(
        client=client,
        label=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_api_token_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: ApiToken = await create_api_token_for_user.asyncio(
        client=client,
        label=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[ApiToken] = await create_api_token_for_user.asyncio_detailed(
        client=client,
        label=None,  # Optional[str]
    )


@pytest.mark.skip
def test_delete_api_token_for_user():
    # Create our client.
    client = ClientFromEnv()

    delete_api_token_for_user.sync(
        client=client,
        token=ApiTokenUuid("<string>"),
    )

    # OR if you need more info (e.g. status_code)
    delete_api_token_for_user.sync_detailed(
        client=client,
        token=ApiTokenUuid("<string>"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_api_token_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    await delete_api_token_for_user.asyncio(
        client=client,
        token=ApiTokenUuid("<string>"),
    )

    # OR run async with more info
    await delete_api_token_for_user.asyncio_detailed(
        client=client,
        token=ApiTokenUuid("<string>"),
    )


@pytest.mark.skip
def test_get_api_token_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: ApiToken = get_api_token_for_user.sync(
        client=client,
        token=ApiTokenUuid("<string>"),
    )

    body: ApiToken = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ApiToken] = get_api_token_for_user.sync_detailed(
        client=client,
        token=ApiTokenUuid("<string>"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_token_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: ApiToken = await get_api_token_for_user.asyncio(
        client=client,
        token=ApiTokenUuid("<string>"),
    )

    # OR run async with more info
    response: Response[ApiToken] = await get_api_token_for_user.asyncio_detailed(
        client=client,
        token=ApiTokenUuid("<string>"),
    )


@pytest.mark.skip
def test_patch_user_crm():
    # Create our client.
    client = ClientFromEnv()

    patch_user_crm.sync(
        client=client,
        body=CrmData(),
    )

    # OR if you need more info (e.g. status_code)
    patch_user_crm.sync_detailed(
        client=client,
        body=CrmData(),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_patch_user_crm_async():
    # Create our client.
    client = ClientFromEnv()

    await patch_user_crm.asyncio(
        client=client,
        body=CrmData(),
    )

    # OR run async with more info
    await patch_user_crm.asyncio_detailed(
        client=client,
        body=CrmData(),
    )


@pytest.mark.skip
def test_get_user_self_extended():
    # Create our client.
    client = ClientFromEnv()

    result: ExtendedUser = get_user_self_extended.sync(
        client=client,
    )

    body: ExtendedUser = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ExtendedUser] = get_user_self_extended.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_self_extended_async():
    # Create our client.
    client = ClientFromEnv()

    result: ExtendedUser = await get_user_self_extended.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[ExtendedUser] = await get_user_self_extended.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_put_user_form_self():
    # Create our client.
    client = ClientFromEnv()

    put_user_form_self.sync(
        client=client,
        body=InquiryForm(
            email="<string>",
            first_name="<string>",
            inquiry_type=InquiryType.GENERAL_INQUIRY,
            last_name="<string>",
            message="<string>",
        ),
    )

    # OR if you need more info (e.g. status_code)
    put_user_form_self.sync_detailed(
        client=client,
        body=InquiryForm(
            email="<string>",
            first_name="<string>",
            inquiry_type=InquiryType.GENERAL_INQUIRY,
            last_name="<string>",
            message="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_put_user_form_self_async():
    # Create our client.
    client = ClientFromEnv()

    await put_user_form_self.asyncio(
        client=client,
        body=InquiryForm(
            email="<string>",
            first_name="<string>",
            inquiry_type=InquiryType.GENERAL_INQUIRY,
            last_name="<string>",
            message="<string>",
        ),
    )

    # OR run async with more info
    await put_user_form_self.asyncio_detailed(
        client=client,
        body=InquiryForm(
            email="<string>",
            first_name="<string>",
            inquiry_type=InquiryType.GENERAL_INQUIRY,
            last_name="<string>",
            message="<string>",
        ),
    )


@pytest.mark.skip
def test_get_oauth2_providers_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: List[AccountProvider] = get_oauth2_providers_for_user.sync(
        client=client,
    )

    body: List[AccountProvider] = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[List[AccountProvider]] = (
        get_oauth2_providers_for_user.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_oauth2_providers_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: List[AccountProvider] = await get_oauth2_providers_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        List[AccountProvider]
    ] = await get_oauth2_providers_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_user_org():
    # Create our client.
    client = ClientFromEnv()

    result: UserOrgInfo = get_user_org.sync(
        client=client,
    )

    body: UserOrgInfo = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[UserOrgInfo] = get_user_org.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: UserOrgInfo = await get_user_org.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[UserOrgInfo] = await get_user_org.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_delete_payment_information_for_user():
    # Create our client.
    client = ClientFromEnv()

    delete_payment_information_for_user.sync(
        client=client,
    )

    # OR if you need more info (e.g. status_code)
    delete_payment_information_for_user.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_payment_information_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    await delete_payment_information_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    await delete_payment_information_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_payment_information_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Customer = get_payment_information_for_user.sync(
        client=client,
    )

    body: Customer = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Customer] = get_payment_information_for_user.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_information_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Customer = await get_payment_information_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Customer
    ] = await get_payment_information_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_create_payment_information_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Customer = create_payment_information_for_user.sync(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    body: Customer = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Customer] = create_payment_information_for_user.sync_detailed(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_payment_information_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Customer = await create_payment_information_for_user.asyncio(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        Customer
    ] = await create_payment_information_for_user.asyncio_detailed(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )


@pytest.mark.skip
def test_update_payment_information_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Customer = update_payment_information_for_user.sync(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    body: Customer = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Customer] = update_payment_information_for_user.sync_detailed(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_payment_information_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Customer = await update_payment_information_for_user.asyncio(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        Customer
    ] = await update_payment_information_for_user.asyncio_detailed(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )


@pytest.mark.skip
def test_get_payment_balance_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: CustomerBalance = get_payment_balance_for_user.sync(
        client=client,
        include_total_due=False,
    )

    body: CustomerBalance = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[CustomerBalance] = get_payment_balance_for_user.sync_detailed(
        client=client,
        include_total_due=False,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: CustomerBalance = await get_payment_balance_for_user.asyncio(
        client=client,
        include_total_due=False,
    )

    # OR run async with more info
    response: Response[
        CustomerBalance
    ] = await get_payment_balance_for_user.asyncio_detailed(
        client=client,
        include_total_due=False,
    )


@pytest.mark.skip
def test_create_payment_intent_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: PaymentIntent = create_payment_intent_for_user.sync(
        client=client,
    )

    body: PaymentIntent = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[PaymentIntent] = create_payment_intent_for_user.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_payment_intent_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: PaymentIntent = await create_payment_intent_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        PaymentIntent
    ] = await create_payment_intent_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_list_invoices_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: List[Invoice] = list_invoices_for_user.sync(
        client=client,
    )

    body: List[Invoice] = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[List[Invoice]] = list_invoices_for_user.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_invoices_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: List[Invoice] = await list_invoices_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[List[Invoice]] = await list_invoices_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_list_payment_methods_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: List[PaymentMethod] = list_payment_methods_for_user.sync(
        client=client,
    )

    body: List[PaymentMethod] = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[List[PaymentMethod]] = (
        list_payment_methods_for_user.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_payment_methods_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: List[PaymentMethod] = await list_payment_methods_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        List[PaymentMethod]
    ] = await list_payment_methods_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_delete_payment_method_for_user():
    # Create our client.
    client = ClientFromEnv()

    delete_payment_method_for_user.sync(
        client=client,
        id="<string>",
    )

    # OR if you need more info (e.g. status_code)
    delete_payment_method_for_user.sync_detailed(
        client=client,
        id="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_payment_method_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    await delete_payment_method_for_user.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    await delete_payment_method_for_user.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_get_user_subscription():
    # Create our client.
    client = ClientFromEnv()

    result: ZooProductSubscriptions = get_user_subscription.sync(
        client=client,
    )

    body: ZooProductSubscriptions = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ZooProductSubscriptions] = get_user_subscription.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_subscription_async():
    # Create our client.
    client = ClientFromEnv()

    result: ZooProductSubscriptions = await get_user_subscription.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        ZooProductSubscriptions
    ] = await get_user_subscription.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_create_user_subscription():
    # Create our client.
    client = ClientFromEnv()

    result: ZooProductSubscriptions = create_user_subscription.sync(
        client=client,
        body=ZooProductSubscriptionsUserRequest(
            modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
        ),
    )

    body: ZooProductSubscriptions = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ZooProductSubscriptions] = (
        create_user_subscription.sync_detailed(
            client=client,
            body=ZooProductSubscriptionsUserRequest(
                modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_user_subscription_async():
    # Create our client.
    client = ClientFromEnv()

    result: ZooProductSubscriptions = await create_user_subscription.asyncio(
        client=client,
        body=ZooProductSubscriptionsUserRequest(
            modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
        ),
    )

    # OR run async with more info
    response: Response[
        ZooProductSubscriptions
    ] = await create_user_subscription.asyncio_detailed(
        client=client,
        body=ZooProductSubscriptionsUserRequest(
            modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
        ),
    )


@pytest.mark.skip
def test_update_user_subscription():
    # Create our client.
    client = ClientFromEnv()

    result: ZooProductSubscriptions = update_user_subscription.sync(
        client=client,
        body=ZooProductSubscriptionsUserRequest(
            modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
        ),
    )

    body: ZooProductSubscriptions = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ZooProductSubscriptions] = (
        update_user_subscription.sync_detailed(
            client=client,
            body=ZooProductSubscriptionsUserRequest(
                modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_user_subscription_async():
    # Create our client.
    client = ClientFromEnv()

    result: ZooProductSubscriptions = await update_user_subscription.asyncio(
        client=client,
        body=ZooProductSubscriptionsUserRequest(
            modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
        ),
    )

    # OR run async with more info
    response: Response[
        ZooProductSubscriptions
    ] = await update_user_subscription.asyncio_detailed(
        client=client,
        body=ZooProductSubscriptionsUserRequest(
            modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
        ),
    )


@pytest.mark.skip
def test_validate_customer_tax_information_for_user():
    # Create our client.
    client = ClientFromEnv()

    validate_customer_tax_information_for_user.sync(
        client=client,
    )

    # OR if you need more info (e.g. status_code)
    validate_customer_tax_information_for_user.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_validate_customer_tax_information_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    await validate_customer_tax_information_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    await validate_customer_tax_information_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_user_privacy_settings():
    # Create our client.
    client = ClientFromEnv()

    result: PrivacySettings = get_user_privacy_settings.sync(
        client=client,
    )

    body: PrivacySettings = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[PrivacySettings] = get_user_privacy_settings.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_privacy_settings_async():
    # Create our client.
    client = ClientFromEnv()

    result: PrivacySettings = await get_user_privacy_settings.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        PrivacySettings
    ] = await get_user_privacy_settings.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_update_user_privacy_settings():
    # Create our client.
    client = ClientFromEnv()

    result: PrivacySettings = update_user_privacy_settings.sync(
        client=client,
        body=PrivacySettings(
            can_train_on_data=False,
        ),
    )

    body: PrivacySettings = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[PrivacySettings] = update_user_privacy_settings.sync_detailed(
        client=client,
        body=PrivacySettings(
            can_train_on_data=False,
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_user_privacy_settings_async():
    # Create our client.
    client = ClientFromEnv()

    result: PrivacySettings = await update_user_privacy_settings.asyncio(
        client=client,
        body=PrivacySettings(
            can_train_on_data=False,
        ),
    )

    # OR run async with more info
    response: Response[
        PrivacySettings
    ] = await update_user_privacy_settings.asyncio_detailed(
        client=client,
        body=PrivacySettings(
            can_train_on_data=False,
        ),
    )


@pytest.mark.skip
def test_get_session_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Session = get_session_for_user.sync(
        client=client,
        token=SessionUuid("<string>"),
    )

    body: Session = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Session] = get_session_for_user.sync_detailed(
        client=client,
        token=SessionUuid("<string>"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_session_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Session = await get_session_for_user.asyncio(
        client=client,
        token=SessionUuid("<string>"),
    )

    # OR run async with more info
    response: Response[Session] = await get_session_for_user.asyncio_detailed(
        client=client,
        token=SessionUuid("<string>"),
    )


@pytest.mark.skip
def test_get_user_shortlinks():
    # Create our client.
    client = ClientFromEnv()

    result: ShortlinkResultsPage = get_user_shortlinks.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    body: ShortlinkResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ShortlinkResultsPage] = get_user_shortlinks.sync_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_shortlinks_async():
    # Create our client.
    client = ClientFromEnv()

    result: ShortlinkResultsPage = await get_user_shortlinks.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        ShortlinkResultsPage
    ] = await get_user_shortlinks.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_create_user_shortlink():
    # Create our client.
    client = ClientFromEnv()

    result: CreateShortlinkResponse = create_user_shortlink.sync(
        client=client,
        body=CreateShortlinkRequest(
            restrict_to_org=False,
            url="<string>",
        ),
    )

    body: CreateShortlinkResponse = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[CreateShortlinkResponse] = create_user_shortlink.sync_detailed(
        client=client,
        body=CreateShortlinkRequest(
            restrict_to_org=False,
            url="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_user_shortlink_async():
    # Create our client.
    client = ClientFromEnv()

    result: CreateShortlinkResponse = await create_user_shortlink.asyncio(
        client=client,
        body=CreateShortlinkRequest(
            restrict_to_org=False,
            url="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        CreateShortlinkResponse
    ] = await create_user_shortlink.asyncio_detailed(
        client=client,
        body=CreateShortlinkRequest(
            restrict_to_org=False,
            url="<string>",
        ),
    )


@pytest.mark.skip
def test_delete_user_shortlink():
    # Create our client.
    client = ClientFromEnv()

    delete_user_shortlink.sync(
        client=client,
        key="<string>",
    )

    # OR if you need more info (e.g. status_code)
    delete_user_shortlink.sync_detailed(
        client=client,
        key="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_user_shortlink_async():
    # Create our client.
    client = ClientFromEnv()

    await delete_user_shortlink.asyncio(
        client=client,
        key="<string>",
    )

    # OR run async with more info
    await delete_user_shortlink.asyncio_detailed(
        client=client,
        key="<string>",
    )


@pytest.mark.skip
def test_redirect_user_shortlink():
    # Create our client.
    client = ClientFromEnv()

    redirect_user_shortlink.sync(
        client=client,
        key="<string>",
    )

    # OR if you need more info (e.g. status_code)
    redirect_user_shortlink.sync_detailed(
        client=client,
        key="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_redirect_user_shortlink_async():
    # Create our client.
    client = ClientFromEnv()

    await redirect_user_shortlink.asyncio(
        client=client,
        key="<string>",
    )

    # OR run async with more info
    await redirect_user_shortlink.asyncio_detailed(
        client=client,
        key="<string>",
    )


@pytest.mark.skip
def test_update_user_shortlink():
    # Create our client.
    client = ClientFromEnv()

    update_user_shortlink.sync(
        client=client,
        key="<string>",
        body=UpdateShortlinkRequest(
            restrict_to_org=False,
        ),
    )

    # OR if you need more info (e.g. status_code)
    update_user_shortlink.sync_detailed(
        client=client,
        key="<string>",
        body=UpdateShortlinkRequest(
            restrict_to_org=False,
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_user_shortlink_async():
    # Create our client.
    client = ClientFromEnv()

    await update_user_shortlink.asyncio(
        client=client,
        key="<string>",
        body=UpdateShortlinkRequest(
            restrict_to_org=False,
        ),
    )

    # OR run async with more info
    await update_user_shortlink.asyncio_detailed(
        client=client,
        key="<string>",
        body=UpdateShortlinkRequest(
            restrict_to_org=False,
        ),
    )


@pytest.mark.skip
def test_list_text_to_cad_models_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: TextToCadResponseResultsPage = list_text_to_cad_models_for_user.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        conversation_id=Uuid("<string>"),
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
        no_models=None,  # Optional[bool]
    )

    body: TextToCadResponseResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[TextToCadResponseResultsPage] = (
        list_text_to_cad_models_for_user.sync_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            conversation_id=Uuid("<string>"),
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
            no_models=None,  # Optional[bool]
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_text_to_cad_models_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: TextToCadResponseResultsPage = (
        await list_text_to_cad_models_for_user.asyncio(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            conversation_id=Uuid("<string>"),
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
            no_models=None,  # Optional[bool]
        )
    )

    # OR run async with more info
    response: Response[
        TextToCadResponseResultsPage
    ] = await list_text_to_cad_models_for_user.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        conversation_id=Uuid("<string>"),
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
        no_models=None,  # Optional[bool]
    )


@pytest.mark.skip
def test_get_text_to_cad_model_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: TextToCadResponse = get_text_to_cad_model_for_user.sync(
        client=client,
        id="<string>",
    )

    body: TextToCadResponse = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[TextToCadResponse] = (
        get_text_to_cad_model_for_user.sync_detailed(
            client=client,
            id="<string>",
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_text_to_cad_model_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: TextToCadResponse = await get_text_to_cad_model_for_user.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[
        TextToCadResponse
    ] = await get_text_to_cad_model_for_user.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_create_text_to_cad_model_feedback():
    # Create our client.
    client = ClientFromEnv()

    create_text_to_cad_model_feedback.sync(
        client=client,
        id="<string>",
        feedback=MlFeedback.THUMBS_UP,
    )

    # OR if you need more info (e.g. status_code)
    create_text_to_cad_model_feedback.sync_detailed(
        client=client,
        id="<string>",
        feedback=MlFeedback.THUMBS_UP,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_text_to_cad_model_feedback_async():
    # Create our client.
    client = ClientFromEnv()

    await create_text_to_cad_model_feedback.asyncio(
        client=client,
        id="<string>",
        feedback=MlFeedback.THUMBS_UP,
    )

    # OR run async with more info
    await create_text_to_cad_model_feedback.asyncio_detailed(
        client=client,
        id="<string>",
        feedback=MlFeedback.THUMBS_UP,
    )


@pytest.mark.skip
def test_list_users():
    # Create our client.
    client = ClientFromEnv()

    result: UserResultsPage = list_users.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    body: UserResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[UserResultsPage] = list_users.sync_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_users_async():
    # Create our client.
    client = ClientFromEnv()

    result: UserResultsPage = await list_users.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[UserResultsPage] = await list_users.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_list_users_extended():
    # Create our client.
    client = ClientFromEnv()

    result: ExtendedUserResultsPage = list_users_extended.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    body: ExtendedUserResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ExtendedUserResultsPage] = list_users_extended.sync_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_users_extended_async():
    # Create our client.
    client = ClientFromEnv()

    result: ExtendedUserResultsPage = await list_users_extended.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        ExtendedUserResultsPage
    ] = await list_users_extended.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_user_extended():
    # Create our client.
    client = ClientFromEnv()

    result: ExtendedUser = get_user_extended.sync(
        client=client,
        id=UserIdentifier("<string>"),
    )

    body: ExtendedUser = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ExtendedUser] = get_user_extended.sync_detailed(
        client=client,
        id=UserIdentifier("<string>"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_extended_async():
    # Create our client.
    client = ClientFromEnv()

    result: ExtendedUser = await get_user_extended.asyncio(
        client=client,
        id=UserIdentifier("<string>"),
    )

    # OR run async with more info
    response: Response[ExtendedUser] = await get_user_extended.asyncio_detailed(
        client=client,
        id=UserIdentifier("<string>"),
    )


@pytest.mark.skip
def test_get_user():
    # Create our client.
    client = ClientFromEnv()

    result: User = get_user.sync(
        client=client,
        id=UserIdentifier("<string>"),
    )

    body: User = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[User] = get_user.sync_detailed(
        client=client,
        id=UserIdentifier("<string>"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: User = await get_user.asyncio(
        client=client,
        id=UserIdentifier("<string>"),
    )

    # OR run async with more info
    response: Response[User] = await get_user.asyncio_detailed(
        client=client,
        id=UserIdentifier("<string>"),
    )


@pytest.mark.skip
def test_list_api_calls_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: ApiCallWithPriceResultsPage = list_api_calls_for_user.sync(
        client=client,
        id=UserIdentifier("<string>"),
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    body: ApiCallWithPriceResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ApiCallWithPriceResultsPage] = (
        list_api_calls_for_user.sync_detailed(
            client=client,
            id=UserIdentifier("<string>"),
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_api_calls_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: ApiCallWithPriceResultsPage = await list_api_calls_for_user.asyncio(
        client=client,
        id=UserIdentifier("<string>"),
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        ApiCallWithPriceResultsPage
    ] = await list_api_calls_for_user.asyncio_detailed(
        client=client,
        id=UserIdentifier("<string>"),
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_payment_balance_for_any_user():
    # Create our client.
    client = ClientFromEnv()

    result: CustomerBalance = get_payment_balance_for_any_user.sync(
        client=client,
        id=UserIdentifier("<string>"),
        include_total_due=False,
    )

    body: CustomerBalance = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[CustomerBalance] = (
        get_payment_balance_for_any_user.sync_detailed(
            client=client,
            id=UserIdentifier("<string>"),
            include_total_due=False,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_any_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: CustomerBalance = await get_payment_balance_for_any_user.asyncio(
        client=client,
        id=UserIdentifier("<string>"),
        include_total_due=False,
    )

    # OR run async with more info
    response: Response[
        CustomerBalance
    ] = await get_payment_balance_for_any_user.asyncio_detailed(
        client=client,
        id=UserIdentifier("<string>"),
        include_total_due=False,
    )


@pytest.mark.skip
def test_update_payment_balance_for_any_user():
    # Create our client.
    client = ClientFromEnv()

    result: CustomerBalance = update_payment_balance_for_any_user.sync(
        client=client,
        id=UserIdentifier("<string>"),
        include_total_due=False,
        body=UpdatePaymentBalance(),
    )

    body: CustomerBalance = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[CustomerBalance] = (
        update_payment_balance_for_any_user.sync_detailed(
            client=client,
            id=UserIdentifier("<string>"),
            include_total_due=False,
            body=UpdatePaymentBalance(),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_payment_balance_for_any_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: CustomerBalance = await update_payment_balance_for_any_user.asyncio(
        client=client,
        id=UserIdentifier("<string>"),
        include_total_due=False,
        body=UpdatePaymentBalance(),
    )

    # OR run async with more info
    response: Response[
        CustomerBalance
    ] = await update_payment_balance_for_any_user.asyncio_detailed(
        client=client,
        id=UserIdentifier("<string>"),
        include_total_due=False,
        body=UpdatePaymentBalance(),
    )


@pytest.mark.skip
def test_update_subscription_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: ZooProductSubscriptions = update_subscription_for_user.sync(
        client=client,
        id=UserIdentifier("<string>"),
        body=ZooProductSubscriptionsUserRequest(
            modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
        ),
    )

    body: ZooProductSubscriptions = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[ZooProductSubscriptions] = (
        update_subscription_for_user.sync_detailed(
            client=client,
            id=UserIdentifier("<string>"),
            body=ZooProductSubscriptionsUserRequest(
                modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_subscription_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: ZooProductSubscriptions = await update_subscription_for_user.asyncio(
        client=client,
        id=UserIdentifier("<string>"),
        body=ZooProductSubscriptionsUserRequest(
            modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
        ),
    )

    # OR run async with more info
    response: Response[
        ZooProductSubscriptions
    ] = await update_subscription_for_user.asyncio_detailed(
        client=client,
        id=UserIdentifier("<string>"),
        body=ZooProductSubscriptionsUserRequest(
            modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
        ),
    )


@pytest.mark.skip
def test_put_public_form():
    # Create our client.
    client = ClientFromEnv()

    put_public_form.sync(
        client=client,
        body=InquiryForm(
            email="<string>",
            first_name="<string>",
            inquiry_type=InquiryType.GENERAL_INQUIRY,
            last_name="<string>",
            message="<string>",
        ),
    )

    # OR if you need more info (e.g. status_code)
    put_public_form.sync_detailed(
        client=client,
        body=InquiryForm(
            email="<string>",
            first_name="<string>",
            inquiry_type=InquiryType.GENERAL_INQUIRY,
            last_name="<string>",
            message="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_put_public_form_async():
    # Create our client.
    client = ClientFromEnv()

    await put_public_form.asyncio(
        client=client,
        body=InquiryForm(
            email="<string>",
            first_name="<string>",
            inquiry_type=InquiryType.GENERAL_INQUIRY,
            last_name="<string>",
            message="<string>",
        ),
    )

    # OR run async with more info
    await put_public_form.asyncio_detailed(
        client=client,
        body=InquiryForm(
            email="<string>",
            first_name="<string>",
            inquiry_type=InquiryType.GENERAL_INQUIRY,
            last_name="<string>",
            message="<string>",
        ),
    )


@pytest.mark.skip
def test_put_public_subscribe():
    # Create our client.
    client = ClientFromEnv()

    put_public_subscribe.sync(
        client=client,
        body=Subscribe(
            email="<string>",
        ),
    )

    # OR if you need more info (e.g. status_code)
    put_public_subscribe.sync_detailed(
        client=client,
        body=Subscribe(
            email="<string>",
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_put_public_subscribe_async():
    # Create our client.
    client = ClientFromEnv()

    await put_public_subscribe.asyncio(
        client=client,
        body=Subscribe(
            email="<string>",
        ),
    )

    # OR run async with more info
    await put_public_subscribe.asyncio_detailed(
        client=client,
        body=Subscribe(
            email="<string>",
        ),
    )


@pytest.mark.skip
def test_create_executor_term():
    # Create our client.
    client = ClientFromEnv()

    # Connect to the websocket.
    with create_executor_term.sync(
        client=client,
    ) as websocket:
        # Send a message.
        websocket.send("{}")

        # Get the messages.
        for message in websocket:
            print(message)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_executor_term_async():
    # Create our client.
    client = ClientFromEnv()

    # Connect to the websocket.
    websocket = await create_executor_term.asyncio(
        client=client,
    )

    # Send a message.
    await websocket.send("{}")

    # Get the messages.
    async for message in websocket:
        print(message)


@pytest.mark.skip
def test_ml_copilot_ws():
    # Create our client.
    client = ClientFromEnv()

    # Connect to the websocket.
    with ml_copilot_ws.WebSocket(
        client=client,
    ) as websocket:
        # Send a message.
        websocket.send(
            MlCopilotClientMessage(
                OptionUser(
                    content="<string>",
                    current_files={"<string>": b"<bytes>"},
                    source_ranges=[
                        SourceRangePrompt(
                            prompt="<string>",
                            range=SourceRange(
                                end=SourcePosition(
                                    column=10,
                                    line=10,
                                ),
                                start=SourcePosition(
                                    column=10,
                                    line=10,
                                ),
                            ),
                        )
                    ],
                )
            )
        )

        # Get a message.
        message = websocket.recv()
        print(message)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_ml_copilot_ws_async():
    # Create our client.
    client = ClientFromEnv()

    # Connect to the websocket.
    websocket = await ml_copilot_ws.asyncio(
        client=client,
    )

    # Send a message.
    await websocket.send("{}")

    # Get the messages.
    async for message in websocket:
        print(message)


@pytest.mark.skip
def test_ml_reasoning_ws():
    # Create our client.
    client = ClientFromEnv()

    # Connect to the websocket.
    with ml_reasoning_ws.WebSocket(
        client=client,
        id="<string>",
    ) as websocket:
        # Send a message.
        websocket.send(
            MlCopilotClientMessage(
                OptionHeaders(
                    headers={"<string>": "<string>"},
                )
            )
        )

        # Get a message.
        message = websocket.recv()
        print(message)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_ml_reasoning_ws_async():
    # Create our client.
    client = ClientFromEnv()

    # Connect to the websocket.
    websocket = await ml_reasoning_ws.asyncio(
        client=client,
        id="<string>",
    )

    # Send a message.
    await websocket.send("{}")

    # Get the messages.
    async for message in websocket:
        print(message)


@pytest.mark.skip
def test_modeling_commands_ws():
    # Create our client.
    client = ClientFromEnv()

    # Connect to the websocket.
    with modeling_commands_ws.WebSocket(
        client=client,
        fps=10,
        post_effect=PostEffectType.PHOSPHOR,
        show_grid=False,
        unlocked_framerate=False,
        video_res_height=10,
        video_res_width=10,
        webrtc=False,
        api_call_id=None,  # Optional[str]
        pool=None,  # Optional[str]
        replay=None,  # Optional[str]
    ) as websocket:
        # Send a message.
        websocket.send(WebSocketRequest(OptionDebug()))

        # Get a message.
        message = websocket.recv()
        print(message)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_modeling_commands_ws_async():
    # Create our client.
    client = ClientFromEnv()

    # Connect to the websocket.
    websocket = await modeling_commands_ws.asyncio(
        client=client,
        fps=10,
        post_effect=PostEffectType.PHOSPHOR,
        show_grid=False,
        unlocked_framerate=False,
        video_res_height=10,
        video_res_width=10,
        webrtc=False,
        api_call_id=None,  # Optional[str]
        pool=None,  # Optional[str]
        replay=None,  # Optional[str]
    )

    # Send a message.
    await websocket.send("{}")

    # Get the messages.
    async for message in websocket:
        print(message)
