import datetime
from typing import List, Optional, Union

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
    list_ml_prompts,
    list_text_to_cad_models_for_user,
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
    CreateShortlinkResponse,
    Customer,
    CustomerBalance,
    DiscountCode,
    Error,
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
    TextToCadResultsPage,
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
from kittycad.models.client_metrics import ClientMetrics
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
    OptionUrl,
)
from kittycad.models.input_format3d import InputFormat3d, OptionSldprt
from kittycad.models.inquiry_form import InquiryForm
from kittycad.models.inquiry_type import InquiryType
from kittycad.models.kcl_code_completion_params import KclCodeCompletionParams
from kittycad.models.kcl_code_completion_request import KclCodeCompletionRequest
from kittycad.models.ml_feedback import MlFeedback
from kittycad.models.modeling_app_event_type import ModelingAppEventType
from kittycad.models.modeling_app_individual_subscription_tier import (
    ModelingAppIndividualSubscriptionTier,
)
from kittycad.models.modeling_app_organization_subscription_tier import (
    ModelingAppOrganizationSubscriptionTier,
)
from kittycad.models.org_details import OrgDetails
from kittycad.models.output_format3d import OptionStl, OutputFormat3d
from kittycad.models.plan_interval import PlanInterval
from kittycad.models.post_effect_type import PostEffectType
from kittycad.models.privacy_settings import PrivacySettings
from kittycad.models.saml_identity_provider_create import SamlIdentityProviderCreate
from kittycad.models.selection import OptionMeshByIndex, Selection
from kittycad.models.service_account_uuid import ServiceAccountUuid
from kittycad.models.session_uuid import SessionUuid
from kittycad.models.source_position import SourcePosition
from kittycad.models.source_range import SourceRange
from kittycad.models.source_range_prompt import SourceRangePrompt
from kittycad.models.stl_storage import StlStorage
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
from kittycad.models.web_socket_request import OptionMetricsResponse
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

    get_schema.sync(
        client=client,
    )

    # OR if you need more info (e.g. status_code)
    get_schema.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_schema_async():
    # Create our client.
    client = ClientFromEnv()

    await get_schema.asyncio(
        client=client,
    )

    # OR run async with more info
    await get_schema.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_ipinfo():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[IpAddrInfo, Error]] = get_ipinfo.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: IpAddrInfo = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[IpAddrInfo, Error]]] = get_ipinfo.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_ipinfo_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[IpAddrInfo, Error]] = await get_ipinfo.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[IpAddrInfo, Error]]
    ] = await get_ipinfo.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_create_text_to_cad():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[TextToCad, Error]] = create_text_to_cad.sync(
        client=client,
        output_format=FileExportFormat.FBX,
        kcl=None,  # Optional[bool]
        body=TextToCadCreateBody(
            prompt="<string>",
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: TextToCad = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[TextToCad, Error]]] = (
        create_text_to_cad.sync_detailed(
            client=client,
            output_format=FileExportFormat.FBX,
            kcl=None,  # Optional[bool]
            body=TextToCadCreateBody(
                prompt="<string>",
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_text_to_cad_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[TextToCad, Error]] = await create_text_to_cad.asyncio(
        client=client,
        output_format=FileExportFormat.FBX,
        kcl=None,  # Optional[bool]
        body=TextToCadCreateBody(
            prompt="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[TextToCad, Error]]
    ] = await create_text_to_cad.asyncio_detailed(
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

    result: Optional[Union[List[ApiCallQueryGroup], Error]] = get_api_call_metrics.sync(
        client=client,
        group_by=ApiCallQueryGroupBy.EMAIL,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: List[ApiCallQueryGroup] = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[List[ApiCallQueryGroup], Error]]] = (
        get_api_call_metrics.sync_detailed(
            client=client,
            group_by=ApiCallQueryGroupBy.EMAIL,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_metrics_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[List[ApiCallQueryGroup], Error]
    ] = await get_api_call_metrics.asyncio(
        client=client,
        group_by=ApiCallQueryGroupBy.EMAIL,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[List[ApiCallQueryGroup], Error]]
    ] = await get_api_call_metrics.asyncio_detailed(
        client=client,
        group_by=ApiCallQueryGroupBy.EMAIL,
    )


@pytest.mark.skip
def test_list_api_calls():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiCallWithPriceResultsPage, Error]] = list_api_calls.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ApiCallWithPriceResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ApiCallWithPriceResultsPage, Error]]] = (
        list_api_calls.sync_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_api_calls_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ApiCallWithPriceResultsPage, Error]
    ] = await list_api_calls.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ApiCallWithPriceResultsPage, Error]]
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

    result: Optional[Union[ApiCallWithPrice, Error]] = get_api_call.sync(
        client=client,
        id="<string>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ApiCallWithPrice = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ApiCallWithPrice, Error]]] = (
        get_api_call.sync_detailed(
            client=client,
            id="<string>",
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiCallWithPrice, Error]] = await get_api_call.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ApiCallWithPrice, Error]]
    ] = await get_api_call.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_apps_github_callback():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = apps_github_callback.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = apps_github_callback.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_apps_github_callback_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await apps_github_callback.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await apps_github_callback.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_apps_github_consent():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[AppClientInfo, Error]] = apps_github_consent.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: AppClientInfo = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[AppClientInfo, Error]]] = (
        apps_github_consent.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_apps_github_consent_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[AppClientInfo, Error]] = await apps_github_consent.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[AppClientInfo, Error]]
    ] = await apps_github_consent.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_apps_github_webhook():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = apps_github_webhook.sync(
        client=client,
        body=bytes("some bytes", "utf-8"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = apps_github_webhook.sync_detailed(
        client=client,
        body=bytes("some bytes", "utf-8"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_apps_github_webhook_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await apps_github_webhook.asyncio(
        client=client,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await apps_github_webhook.asyncio_detailed(
        client=client,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_list_async_operations():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[AsyncApiCallResultsPage, Error]] = (
        list_async_operations.sync(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            status=ApiCallStatus.QUEUED,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: AsyncApiCallResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[AsyncApiCallResultsPage, Error]]] = (
        list_async_operations.sync_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            status=ApiCallStatus.QUEUED,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_async_operations_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[AsyncApiCallResultsPage, Error]
    ] = await list_async_operations.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        status=ApiCallStatus.QUEUED,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[AsyncApiCallResultsPage, Error]]
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
            Error,
        ]
    ] = get_async_operation.sync(
        client=client,
        id="<string>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

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
                Error,
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
            Error,
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
                Error,
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

    result: Optional[Union[AuthApiKeyResponse, Error]] = auth_api_key.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: AuthApiKeyResponse = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[AuthApiKeyResponse, Error]]] = (
        auth_api_key.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_auth_api_key_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[AuthApiKeyResponse, Error]] = await auth_api_key.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[AuthApiKeyResponse, Error]]
    ] = await auth_api_key.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_auth_email():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[VerificationTokenResponse, Error]] = auth_email.sync(
        client=client,
        body=EmailAuthenticationForm(
            email="<string>",
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: VerificationTokenResponse = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[VerificationTokenResponse, Error]]] = (
        auth_email.sync_detailed(
            client=client,
            body=EmailAuthenticationForm(
                email="<string>",
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_auth_email_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[VerificationTokenResponse, Error]
    ] = await auth_email.asyncio(
        client=client,
        body=EmailAuthenticationForm(
            email="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[VerificationTokenResponse, Error]]
    ] = await auth_email.asyncio_detailed(
        client=client,
        body=EmailAuthenticationForm(
            email="<string>",
        ),
    )


@pytest.mark.skip
def test_auth_email_callback():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = auth_email_callback.sync(
        client=client,
        email="<string>",
        token="<string>",
        callback_url=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = auth_email_callback.sync_detailed(
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

    result: Optional[Error] = await auth_email_callback.asyncio(
        client=client,
        email="<string>",
        token="<string>",
        callback_url=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await auth_email_callback.asyncio_detailed(
        client=client,
        email="<string>",
        token="<string>",
        callback_url=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_auth_saml():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = get_auth_saml.sync(
        client=client,
        provider_id=Uuid("<string>"),
        callback_url=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = get_auth_saml.sync_detailed(
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

    result: Optional[Error] = await get_auth_saml.asyncio(
        client=client,
        provider_id=Uuid("<string>"),
        callback_url=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await get_auth_saml.asyncio_detailed(
        client=client,
        provider_id=Uuid("<string>"),
        callback_url=None,  # Optional[str]
    )


@pytest.mark.skip
def test_post_auth_saml():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = post_auth_saml.sync(
        client=client,
        provider_id=Uuid("<string>"),
        body=bytes("some bytes", "utf-8"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = post_auth_saml.sync_detailed(
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

    result: Optional[Error] = await post_auth_saml.asyncio(
        client=client,
        provider_id=Uuid("<string>"),
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await post_auth_saml.asyncio_detailed(
        client=client,
        provider_id=Uuid("<string>"),
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_community_sso():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = community_sso.sync(
        client=client,
        sig="<string>",
        sso="<string>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = community_sso.sync_detailed(
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

    result: Optional[Error] = await community_sso.asyncio(
        client=client,
        sig="<string>",
        sso="<string>",
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await community_sso.asyncio_detailed(
        client=client,
        sig="<string>",
        sso="<string>",
    )


@pytest.mark.skip
def test_create_debug_uploads():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[List[str], Error]] = create_debug_uploads.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: List[str] = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[List[str], Error]]] = (
        create_debug_uploads.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_debug_uploads_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[List[str], Error]] = await create_debug_uploads.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[List[str], Error]]
    ] = await create_debug_uploads.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_create_event():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = create_event.sync(
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

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = create_event.sync_detailed(
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

    result: Optional[Error] = await create_event.asyncio(
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
    response: Response[Optional[Error]] = await create_event.asyncio_detailed(
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

    result: Optional[Union[FileCenterOfMass, Error]] = create_file_center_of_mass.sync(
        client=client,
        output_unit=UnitLength.CM,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: FileCenterOfMass = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[FileCenterOfMass, Error]]] = (
        create_file_center_of_mass.sync_detailed(
            client=client,
            output_unit=UnitLength.CM,
            src_format=FileImportFormat.FBX,
            body=bytes("some bytes", "utf-8"),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_center_of_mass_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[FileCenterOfMass, Error]
    ] = await create_file_center_of_mass.asyncio(
        client=client,
        output_unit=UnitLength.CM,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[FileCenterOfMass, Error]]
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

    result: Optional[Union[FileConversion, Error]] = (
        create_file_conversion_options.sync(
            client=client,
            body=ConversionParams(
                output_format=OutputFormat3d(
                    OptionStl(
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
                            OptionMeshByIndex(
                                index=10,
                            )
                        ),
                        storage=StlStorage.ASCII,
                        units=UnitLength.CM,
                    )
                ),
                src_format=InputFormat3d(
                    OptionSldprt(
                        split_closed_faces=False,
                    )
                ),
            ),
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: FileConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[FileConversion, Error]]] = (
        create_file_conversion_options.sync_detailed(
            client=client,
            body=ConversionParams(
                output_format=OutputFormat3d(
                    OptionStl(
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
                            OptionMeshByIndex(
                                index=10,
                            )
                        ),
                        storage=StlStorage.ASCII,
                        units=UnitLength.CM,
                    )
                ),
                src_format=InputFormat3d(
                    OptionSldprt(
                        split_closed_faces=False,
                    )
                ),
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_conversion_options_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[FileConversion, Error]
    ] = await create_file_conversion_options.asyncio(
        client=client,
        body=ConversionParams(
            output_format=OutputFormat3d(
                OptionStl(
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
                        OptionMeshByIndex(
                            index=10,
                        )
                    ),
                    storage=StlStorage.ASCII,
                    units=UnitLength.CM,
                )
            ),
            src_format=InputFormat3d(
                OptionSldprt(
                    split_closed_faces=False,
                )
            ),
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[FileConversion, Error]]
    ] = await create_file_conversion_options.asyncio_detailed(
        client=client,
        body=ConversionParams(
            output_format=OutputFormat3d(
                OptionStl(
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
                        OptionMeshByIndex(
                            index=10,
                        )
                    ),
                    storage=StlStorage.ASCII,
                    units=UnitLength.CM,
                )
            ),
            src_format=InputFormat3d(
                OptionSldprt(
                    split_closed_faces=False,
                )
            ),
        ),
    )


@pytest.mark.skip
def test_create_file_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[FileConversion, Error]] = create_file_conversion.sync(
        client=client,
        output_format=FileExportFormat.FBX,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: FileConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[FileConversion, Error]]] = (
        create_file_conversion.sync_detailed(
            client=client,
            output_format=FileExportFormat.FBX,
            src_format=FileImportFormat.FBX,
            body=bytes("some bytes", "utf-8"),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[FileConversion, Error]
    ] = await create_file_conversion.asyncio(
        client=client,
        output_format=FileExportFormat.FBX,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[FileConversion, Error]]
    ] = await create_file_conversion.asyncio_detailed(
        client=client,
        output_format=FileExportFormat.FBX,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_density():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[FileDensity, Error]] = create_file_density.sync(
        client=client,
        material_mass=3.14,
        material_mass_unit=UnitMass.G,
        output_unit=UnitDensity.LB_FT3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: FileDensity = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[FileDensity, Error]]] = (
        create_file_density.sync_detailed(
            client=client,
            material_mass=3.14,
            material_mass_unit=UnitMass.G,
            output_unit=UnitDensity.LB_FT3,
            src_format=FileImportFormat.FBX,
            body=bytes("some bytes", "utf-8"),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_density_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[FileDensity, Error]] = await create_file_density.asyncio(
        client=client,
        material_mass=3.14,
        material_mass_unit=UnitMass.G,
        output_unit=UnitDensity.LB_FT3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[FileDensity, Error]]
    ] = await create_file_density.asyncio_detailed(
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

    result: Optional[Union[CodeOutput, Error]] = create_file_execution.sync(
        client=client,
        lang=CodeLanguage.GO,
        output=None,  # Optional[str]
        body=bytes("some bytes", "utf-8"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: CodeOutput = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[CodeOutput, Error]]] = (
        create_file_execution.sync_detailed(
            client=client,
            lang=CodeLanguage.GO,
            output=None,  # Optional[str]
            body=bytes("some bytes", "utf-8"),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_execution_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CodeOutput, Error]] = await create_file_execution.asyncio(
        client=client,
        lang=CodeLanguage.GO,
        output=None,  # Optional[str]
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[CodeOutput, Error]]
    ] = await create_file_execution.asyncio_detailed(
        client=client,
        lang=CodeLanguage.GO,
        output=None,  # Optional[str]
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_mass():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[FileMass, Error]] = create_file_mass.sync(
        client=client,
        material_density=3.14,
        material_density_unit=UnitDensity.LB_FT3,
        output_unit=UnitMass.G,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: FileMass = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[FileMass, Error]]] = (
        create_file_mass.sync_detailed(
            client=client,
            material_density=3.14,
            material_density_unit=UnitDensity.LB_FT3,
            output_unit=UnitMass.G,
            src_format=FileImportFormat.FBX,
            body=bytes("some bytes", "utf-8"),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_mass_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[FileMass, Error]] = await create_file_mass.asyncio(
        client=client,
        material_density=3.14,
        material_density_unit=UnitDensity.LB_FT3,
        output_unit=UnitMass.G,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[FileMass, Error]]
    ] = await create_file_mass.asyncio_detailed(
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

    result: Optional[Union[FileSurfaceArea, Error]] = create_file_surface_area.sync(
        client=client,
        output_unit=UnitArea.CM2,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: FileSurfaceArea = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[FileSurfaceArea, Error]]] = (
        create_file_surface_area.sync_detailed(
            client=client,
            output_unit=UnitArea.CM2,
            src_format=FileImportFormat.FBX,
            body=bytes("some bytes", "utf-8"),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_surface_area_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[FileSurfaceArea, Error]
    ] = await create_file_surface_area.asyncio(
        client=client,
        output_unit=UnitArea.CM2,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[FileSurfaceArea, Error]]
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

    result: Optional[Union[FileVolume, Error]] = create_file_volume.sync(
        client=client,
        output_unit=UnitVolume.CM3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: FileVolume = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[FileVolume, Error]]] = (
        create_file_volume.sync_detailed(
            client=client,
            output_unit=UnitVolume.CM3,
            src_format=FileImportFormat.FBX,
            body=bytes("some bytes", "utf-8"),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_volume_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[FileVolume, Error]] = await create_file_volume.asyncio(
        client=client,
        output_unit=UnitVolume.CM3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[FileVolume, Error]]
    ] = await create_file_volume.asyncio_detailed(
        client=client,
        output_unit=UnitVolume.CM3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_internal_get_api_token_for_discord_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiToken, Error]] = (
        internal_get_api_token_for_discord_user.sync(
            client=client,
            discord_id="<string>",
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ApiToken = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ApiToken, Error]]] = (
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

    result: Optional[
        Union[ApiToken, Error]
    ] = await internal_get_api_token_for_discord_user.asyncio(
        client=client,
        discord_id="<string>",
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ApiToken, Error]]
    ] = await internal_get_api_token_for_discord_user.asyncio_detailed(
        client=client,
        discord_id="<string>",
    )


@pytest.mark.skip
def test_logout():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = logout.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = logout.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_logout_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await logout.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await logout.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_list_ml_prompts():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[MlPromptResultsPage, Error]] = list_ml_prompts.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: MlPromptResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[MlPromptResultsPage, Error]]] = (
        list_ml_prompts.sync_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_ml_prompts_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[MlPromptResultsPage, Error]] = await list_ml_prompts.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[MlPromptResultsPage, Error]]
    ] = await list_ml_prompts.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_ml_prompt():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[MlPrompt, Error]] = get_ml_prompt.sync(
        client=client,
        id="<string>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: MlPrompt = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[MlPrompt, Error]]] = get_ml_prompt.sync_detailed(
        client=client,
        id="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_ml_prompt_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[MlPrompt, Error]] = await get_ml_prompt.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[
        Optional[Union[MlPrompt, Error]]
    ] = await get_ml_prompt.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_create_proprietary_to_kcl():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[KclModel, Error]] = create_proprietary_to_kcl.sync(
        client=client,
        code_option=CodeOption.PARSE,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: KclModel = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[KclModel, Error]]] = (
        create_proprietary_to_kcl.sync_detailed(
            client=client,
            code_option=CodeOption.PARSE,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_proprietary_to_kcl_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[KclModel, Error]] = await create_proprietary_to_kcl.asyncio(
        client=client,
        code_option=CodeOption.PARSE,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[KclModel, Error]]
    ] = await create_proprietary_to_kcl.asyncio_detailed(
        client=client,
        code_option=CodeOption.PARSE,
    )


@pytest.mark.skip
def test_create_kcl_code_completions():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[KclCodeCompletionResponse, Error]] = (
        create_kcl_code_completions.sync(
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

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: KclCodeCompletionResponse = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[KclCodeCompletionResponse, Error]]] = (
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

    result: Optional[
        Union[KclCodeCompletionResponse, Error]
    ] = await create_kcl_code_completions.asyncio(
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
        Optional[Union[KclCodeCompletionResponse, Error]]
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

    result: Optional[Union[TextToCadIteration, Error]] = (
        create_text_to_cad_iteration.sync(
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
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: TextToCadIteration = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[TextToCadIteration, Error]]] = (
        create_text_to_cad_iteration.sync_detailed(
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
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_text_to_cad_iteration_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[TextToCadIteration, Error]
    ] = await create_text_to_cad_iteration.asyncio(
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
        Optional[Union[TextToCadIteration, Error]]
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

    result: Optional[Union[TextToCadMultiFileIteration, Error]] = (
        create_text_to_cad_multi_file_iteration.sync(
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

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: TextToCadMultiFileIteration = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[TextToCadMultiFileIteration, Error]]] = (
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

    result: Optional[
        Union[TextToCadMultiFileIteration, Error]
    ] = await create_text_to_cad_multi_file_iteration.asyncio(
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

    # OR run async with more info
    response: Response[
        Optional[Union[TextToCadMultiFileIteration, Error]]
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
def test_get_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Org, Error]] = get_org.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Org = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[Org, Error]]] = get_org.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Org, Error]] = await get_org.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[Optional[Union[Org, Error]]] = await get_org.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_update_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Org, Error]] = update_org.sync(
        client=client,
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Org = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[Org, Error]]] = update_org.sync_detailed(
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

    result: Optional[Union[Org, Error]] = await update_org.asyncio(
        client=client,
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        ),
    )

    # OR run async with more info
    response: Response[Optional[Union[Org, Error]]] = await update_org.asyncio_detailed(
        client=client,
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        ),
    )


@pytest.mark.skip
def test_create_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Org, Error]] = create_org.sync(
        client=client,
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Org = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[Org, Error]]] = create_org.sync_detailed(
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

    result: Optional[Union[Org, Error]] = await create_org.asyncio(
        client=client,
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        ),
    )

    # OR run async with more info
    response: Response[Optional[Union[Org, Error]]] = await create_org.asyncio_detailed(
        client=client,
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        ),
    )


@pytest.mark.skip
def test_delete_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = delete_org.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = delete_org.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await delete_org.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await delete_org.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_org_list_api_calls():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiCallWithPriceResultsPage, Error]] = (
        org_list_api_calls.sync(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ApiCallWithPriceResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ApiCallWithPriceResultsPage, Error]]] = (
        org_list_api_calls.sync_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_org_list_api_calls_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ApiCallWithPriceResultsPage, Error]
    ] = await org_list_api_calls.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ApiCallWithPriceResultsPage, Error]]
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

    result: Optional[Union[ApiCallWithPrice, Error]] = get_api_call_for_org.sync(
        client=client,
        id="<string>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ApiCallWithPrice = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ApiCallWithPrice, Error]]] = (
        get_api_call_for_org.sync_detailed(
            client=client,
            id="<string>",
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ApiCallWithPrice, Error]
    ] = await get_api_call_for_org.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ApiCallWithPrice, Error]]
    ] = await get_api_call_for_org.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_list_org_members():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[OrgMemberResultsPage, Error]] = list_org_members.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        role=UserOrgRole.ADMIN,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: OrgMemberResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[OrgMemberResultsPage, Error]]] = (
        list_org_members.sync_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            role=UserOrgRole.ADMIN,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_org_members_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[OrgMemberResultsPage, Error]
    ] = await list_org_members.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        role=UserOrgRole.ADMIN,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[OrgMemberResultsPage, Error]]
    ] = await list_org_members.asyncio_detailed(
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

    result: Optional[Union[OrgMember, Error]] = create_org_member.sync(
        client=client,
        body=AddOrgMember(
            email="<string>",
            role=UserOrgRole.ADMIN,
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: OrgMember = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[OrgMember, Error]]] = (
        create_org_member.sync_detailed(
            client=client,
            body=AddOrgMember(
                email="<string>",
                role=UserOrgRole.ADMIN,
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_org_member_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[OrgMember, Error]] = await create_org_member.asyncio(
        client=client,
        body=AddOrgMember(
            email="<string>",
            role=UserOrgRole.ADMIN,
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[OrgMember, Error]]
    ] = await create_org_member.asyncio_detailed(
        client=client,
        body=AddOrgMember(
            email="<string>",
            role=UserOrgRole.ADMIN,
        ),
    )


@pytest.mark.skip
def test_get_org_member():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[OrgMember, Error]] = get_org_member.sync(
        client=client,
        user_id=Uuid("<string>"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: OrgMember = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[OrgMember, Error]]] = (
        get_org_member.sync_detailed(
            client=client,
            user_id=Uuid("<string>"),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_member_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[OrgMember, Error]] = await get_org_member.asyncio(
        client=client,
        user_id=Uuid("<string>"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[OrgMember, Error]]
    ] = await get_org_member.asyncio_detailed(
        client=client,
        user_id=Uuid("<string>"),
    )


@pytest.mark.skip
def test_update_org_member():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[OrgMember, Error]] = update_org_member.sync(
        client=client,
        user_id=Uuid("<string>"),
        body=UpdateMemberToOrgBody(
            role=UserOrgRole.ADMIN,
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: OrgMember = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[OrgMember, Error]]] = (
        update_org_member.sync_detailed(
            client=client,
            user_id=Uuid("<string>"),
            body=UpdateMemberToOrgBody(
                role=UserOrgRole.ADMIN,
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_member_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[OrgMember, Error]] = await update_org_member.asyncio(
        client=client,
        user_id=Uuid("<string>"),
        body=UpdateMemberToOrgBody(
            role=UserOrgRole.ADMIN,
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[OrgMember, Error]]
    ] = await update_org_member.asyncio_detailed(
        client=client,
        user_id=Uuid("<string>"),
        body=UpdateMemberToOrgBody(
            role=UserOrgRole.ADMIN,
        ),
    )


@pytest.mark.skip
def test_delete_org_member():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = delete_org_member.sync(
        client=client,
        user_id=Uuid("<string>"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = delete_org_member.sync_detailed(
        client=client,
        user_id=Uuid("<string>"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_org_member_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await delete_org_member.asyncio(
        client=client,
        user_id=Uuid("<string>"),
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await delete_org_member.asyncio_detailed(
        client=client,
        user_id=Uuid("<string>"),
    )


@pytest.mark.skip
def test_get_payment_information_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Customer, Error]] = get_payment_information_for_org.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Customer = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[Customer, Error]]] = (
        get_payment_information_for_org.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_information_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[Customer, Error]
    ] = await get_payment_information_for_org.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[Customer, Error]]
    ] = await get_payment_information_for_org.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_update_payment_information_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Customer, Error]] = update_payment_information_for_org.sync(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Customer = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[Customer, Error]]] = (
        update_payment_information_for_org.sync_detailed(
            client=client,
            body=BillingInfo(
                name="<string>",
                phone="<string>",
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_payment_information_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[Customer, Error]
    ] = await update_payment_information_for_org.asyncio(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[Customer, Error]]
    ] = await update_payment_information_for_org.asyncio_detailed(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )


@pytest.mark.skip
def test_create_payment_information_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Customer, Error]] = create_payment_information_for_org.sync(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Customer = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[Customer, Error]]] = (
        create_payment_information_for_org.sync_detailed(
            client=client,
            body=BillingInfo(
                name="<string>",
                phone="<string>",
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_payment_information_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[Customer, Error]
    ] = await create_payment_information_for_org.asyncio(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[Customer, Error]]
    ] = await create_payment_information_for_org.asyncio_detailed(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )


@pytest.mark.skip
def test_delete_payment_information_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = delete_payment_information_for_org.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = (
        delete_payment_information_for_org.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_payment_information_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await delete_payment_information_for_org.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Error]
    ] = await delete_payment_information_for_org.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_payment_balance_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CustomerBalance, Error]] = get_payment_balance_for_org.sync(
        client=client,
        include_total_due=False,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: CustomerBalance = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[CustomerBalance, Error]]] = (
        get_payment_balance_for_org.sync_detailed(
            client=client,
            include_total_due=False,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[CustomerBalance, Error]
    ] = await get_payment_balance_for_org.asyncio(
        client=client,
        include_total_due=False,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[CustomerBalance, Error]]
    ] = await get_payment_balance_for_org.asyncio_detailed(
        client=client,
        include_total_due=False,
    )


@pytest.mark.skip
def test_create_payment_intent_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[PaymentIntent, Error]] = create_payment_intent_for_org.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: PaymentIntent = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[PaymentIntent, Error]]] = (
        create_payment_intent_for_org.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_payment_intent_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[PaymentIntent, Error]
    ] = await create_payment_intent_for_org.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[PaymentIntent, Error]]
    ] = await create_payment_intent_for_org.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_list_invoices_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[List[Invoice], Error]] = list_invoices_for_org.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: List[Invoice] = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[List[Invoice], Error]]] = (
        list_invoices_for_org.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_invoices_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[List[Invoice], Error]] = await list_invoices_for_org.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[List[Invoice], Error]]
    ] = await list_invoices_for_org.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_list_payment_methods_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[List[PaymentMethod], Error]] = (
        list_payment_methods_for_org.sync(
            client=client,
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: List[PaymentMethod] = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[List[PaymentMethod], Error]]] = (
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

    result: Optional[
        Union[List[PaymentMethod], Error]
    ] = await list_payment_methods_for_org.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[List[PaymentMethod], Error]]
    ] = await list_payment_methods_for_org.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_delete_payment_method_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = delete_payment_method_for_org.sync(
        client=client,
        id="<string>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = delete_payment_method_for_org.sync_detailed(
        client=client,
        id="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_payment_method_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await delete_payment_method_for_org.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[
        Optional[Error]
    ] = await delete_payment_method_for_org.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_get_org_subscription():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ZooProductSubscriptions, Error]] = get_org_subscription.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ZooProductSubscriptions = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ZooProductSubscriptions, Error]]] = (
        get_org_subscription.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_subscription_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ZooProductSubscriptions, Error]
    ] = await get_org_subscription.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ZooProductSubscriptions, Error]]
    ] = await get_org_subscription.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_update_org_subscription():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ZooProductSubscriptions, Error]] = (
        update_org_subscription.sync(
            client=client,
            body=ZooProductSubscriptionsOrgRequest(
                modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
            ),
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ZooProductSubscriptions = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ZooProductSubscriptions, Error]]] = (
        update_org_subscription.sync_detailed(
            client=client,
            body=ZooProductSubscriptionsOrgRequest(
                modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_subscription_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ZooProductSubscriptions, Error]
    ] = await update_org_subscription.asyncio(
        client=client,
        body=ZooProductSubscriptionsOrgRequest(
            modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ZooProductSubscriptions, Error]]
    ] = await update_org_subscription.asyncio_detailed(
        client=client,
        body=ZooProductSubscriptionsOrgRequest(
            modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
        ),
    )


@pytest.mark.skip
def test_create_org_subscription():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ZooProductSubscriptions, Error]] = (
        create_org_subscription.sync(
            client=client,
            body=ZooProductSubscriptionsOrgRequest(
                modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
            ),
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ZooProductSubscriptions = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ZooProductSubscriptions, Error]]] = (
        create_org_subscription.sync_detailed(
            client=client,
            body=ZooProductSubscriptionsOrgRequest(
                modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_org_subscription_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ZooProductSubscriptions, Error]
    ] = await create_org_subscription.asyncio(
        client=client,
        body=ZooProductSubscriptionsOrgRequest(
            modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ZooProductSubscriptions, Error]]
    ] = await create_org_subscription.asyncio_detailed(
        client=client,
        body=ZooProductSubscriptionsOrgRequest(
            modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
        ),
    )


@pytest.mark.skip
def test_validate_customer_tax_information_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = validate_customer_tax_information_for_org.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = (
        validate_customer_tax_information_for_org.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_validate_customer_tax_information_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await validate_customer_tax_information_for_org.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Error]
    ] = await validate_customer_tax_information_for_org.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_org_privacy_settings():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[PrivacySettings, Error]] = get_org_privacy_settings.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: PrivacySettings = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[PrivacySettings, Error]]] = (
        get_org_privacy_settings.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_privacy_settings_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[PrivacySettings, Error]
    ] = await get_org_privacy_settings.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[PrivacySettings, Error]]
    ] = await get_org_privacy_settings.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_update_org_privacy_settings():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[PrivacySettings, Error]] = update_org_privacy_settings.sync(
        client=client,
        body=PrivacySettings(
            can_train_on_data=False,
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: PrivacySettings = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[PrivacySettings, Error]]] = (
        update_org_privacy_settings.sync_detailed(
            client=client,
            body=PrivacySettings(
                can_train_on_data=False,
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_privacy_settings_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[PrivacySettings, Error]
    ] = await update_org_privacy_settings.asyncio(
        client=client,
        body=PrivacySettings(
            can_train_on_data=False,
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[PrivacySettings, Error]]
    ] = await update_org_privacy_settings.asyncio_detailed(
        client=client,
        body=PrivacySettings(
            can_train_on_data=False,
        ),
    )


@pytest.mark.skip
def test_get_org_saml_idp():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[SamlIdentityProvider, Error]] = get_org_saml_idp.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: SamlIdentityProvider = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[SamlIdentityProvider, Error]]] = (
        get_org_saml_idp.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_saml_idp_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[SamlIdentityProvider, Error]
    ] = await get_org_saml_idp.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[SamlIdentityProvider, Error]]
    ] = await get_org_saml_idp.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_update_org_saml_idp():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[SamlIdentityProvider, Error]] = update_org_saml_idp.sync(
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

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: SamlIdentityProvider = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[SamlIdentityProvider, Error]]] = (
        update_org_saml_idp.sync_detailed(
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
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_saml_idp_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[SamlIdentityProvider, Error]
    ] = await update_org_saml_idp.asyncio(
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
        Optional[Union[SamlIdentityProvider, Error]]
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
def test_create_org_saml_idp():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[SamlIdentityProvider, Error]] = create_org_saml_idp.sync(
        client=client,
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=IdpMetadataSource(
                OptionUrl(
                    url="<string>",
                )
            ),
            technical_contact_email="<string>",
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: SamlIdentityProvider = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[SamlIdentityProvider, Error]]] = (
        create_org_saml_idp.sync_detailed(
            client=client,
            body=SamlIdentityProviderCreate(
                idp_entity_id="<string>",
                idp_metadata_source=IdpMetadataSource(
                    OptionUrl(
                        url="<string>",
                    )
                ),
                technical_contact_email="<string>",
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_org_saml_idp_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[SamlIdentityProvider, Error]
    ] = await create_org_saml_idp.asyncio(
        client=client,
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=IdpMetadataSource(
                OptionUrl(
                    url="<string>",
                )
            ),
            technical_contact_email="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[SamlIdentityProvider, Error]]
    ] = await create_org_saml_idp.asyncio_detailed(
        client=client,
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=IdpMetadataSource(
                OptionUrl(
                    url="<string>",
                )
            ),
            technical_contact_email="<string>",
        ),
    )


@pytest.mark.skip
def test_delete_org_saml_idp():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = delete_org_saml_idp.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = delete_org_saml_idp.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_org_saml_idp_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await delete_org_saml_idp.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await delete_org_saml_idp.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_list_service_accounts_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ServiceAccountResultsPage, Error]] = (
        list_service_accounts_for_org.sync(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ServiceAccountResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ServiceAccountResultsPage, Error]]] = (
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

    result: Optional[
        Union[ServiceAccountResultsPage, Error]
    ] = await list_service_accounts_for_org.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ServiceAccountResultsPage, Error]]
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

    result: Optional[Union[ServiceAccount, Error]] = (
        create_service_account_for_org.sync(
            client=client,
            label=None,  # Optional[str]
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ServiceAccount = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ServiceAccount, Error]]] = (
        create_service_account_for_org.sync_detailed(
            client=client,
            label=None,  # Optional[str]
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_service_account_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ServiceAccount, Error]
    ] = await create_service_account_for_org.asyncio(
        client=client,
        label=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ServiceAccount, Error]]
    ] = await create_service_account_for_org.asyncio_detailed(
        client=client,
        label=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_service_account_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ServiceAccount, Error]] = get_service_account_for_org.sync(
        client=client,
        token=ServiceAccountUuid("<string>"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ServiceAccount = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ServiceAccount, Error]]] = (
        get_service_account_for_org.sync_detailed(
            client=client,
            token=ServiceAccountUuid("<string>"),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_service_account_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ServiceAccount, Error]
    ] = await get_service_account_for_org.asyncio(
        client=client,
        token=ServiceAccountUuid("<string>"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ServiceAccount, Error]]
    ] = await get_service_account_for_org.asyncio_detailed(
        client=client,
        token=ServiceAccountUuid("<string>"),
    )


@pytest.mark.skip
def test_delete_service_account_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = delete_service_account_for_org.sync(
        client=client,
        token=ServiceAccountUuid("<string>"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = delete_service_account_for_org.sync_detailed(
        client=client,
        token=ServiceAccountUuid("<string>"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_service_account_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await delete_service_account_for_org.asyncio(
        client=client,
        token=ServiceAccountUuid("<string>"),
    )

    # OR run async with more info
    response: Response[
        Optional[Error]
    ] = await delete_service_account_for_org.asyncio_detailed(
        client=client,
        token=ServiceAccountUuid("<string>"),
    )


@pytest.mark.skip
def test_get_org_shortlinks():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ShortlinkResultsPage, Error]] = get_org_shortlinks.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ShortlinkResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ShortlinkResultsPage, Error]]] = (
        get_org_shortlinks.sync_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_shortlinks_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ShortlinkResultsPage, Error]
    ] = await get_org_shortlinks.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ShortlinkResultsPage, Error]]
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

    result: Optional[Union[OrgResultsPage, Error]] = list_orgs.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: OrgResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[OrgResultsPage, Error]]] = (
        list_orgs.sync_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_orgs_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[OrgResultsPage, Error]] = await list_orgs.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[OrgResultsPage, Error]]
    ] = await list_orgs.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_any_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Org, Error]] = get_any_org.sync(
        client=client,
        id=Uuid("<string>"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Org = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[Org, Error]]] = get_any_org.sync_detailed(
        client=client,
        id=Uuid("<string>"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_any_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Org, Error]] = await get_any_org.asyncio(
        client=client,
        id=Uuid("<string>"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[Org, Error]]
    ] = await get_any_org.asyncio_detailed(
        client=client,
        id=Uuid("<string>"),
    )


@pytest.mark.skip
def test_update_enterprise_pricing_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ZooProductSubscriptions, Error]] = (
        update_enterprise_pricing_for_org.sync(
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

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ZooProductSubscriptions = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ZooProductSubscriptions, Error]]] = (
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

    result: Optional[
        Union[ZooProductSubscriptions, Error]
    ] = await update_enterprise_pricing_for_org.asyncio(
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
        Optional[Union[ZooProductSubscriptions, Error]]
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

    result: Optional[Union[CustomerBalance, Error]] = (
        get_payment_balance_for_any_org.sync(
            client=client,
            include_total_due=False,
            id=Uuid("<string>"),
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: CustomerBalance = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[CustomerBalance, Error]]] = (
        get_payment_balance_for_any_org.sync_detailed(
            client=client,
            include_total_due=False,
            id=Uuid("<string>"),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_any_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[CustomerBalance, Error]
    ] = await get_payment_balance_for_any_org.asyncio(
        client=client,
        include_total_due=False,
        id=Uuid("<string>"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[CustomerBalance, Error]]
    ] = await get_payment_balance_for_any_org.asyncio_detailed(
        client=client,
        include_total_due=False,
        id=Uuid("<string>"),
    )


@pytest.mark.skip
def test_update_payment_balance_for_any_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CustomerBalance, Error]] = (
        update_payment_balance_for_any_org.sync(
            client=client,
            id=Uuid("<string>"),
            include_total_due=False,
            body=UpdatePaymentBalance(),
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: CustomerBalance = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[CustomerBalance, Error]]] = (
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

    result: Optional[
        Union[CustomerBalance, Error]
    ] = await update_payment_balance_for_any_org.asyncio(
        client=client,
        id=Uuid("<string>"),
        include_total_due=False,
        body=UpdatePaymentBalance(),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[CustomerBalance, Error]]
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

    result: Optional[Union[Pong, Error]] = ping.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Pong = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[Pong, Error]]] = ping.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_ping_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Pong, Error]] = await ping.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[Optional[Union[Pong, Error]]] = await ping.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_pricing_subscriptions():
    # Create our client.
    client = ClientFromEnv()

    get_pricing_subscriptions.sync(
        client=client,
    )

    # OR if you need more info (e.g. status_code)
    get_pricing_subscriptions.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_pricing_subscriptions_async():
    # Create our client.
    client = ClientFromEnv()

    await get_pricing_subscriptions.asyncio(
        client=client,
    )

    # OR run async with more info
    await get_pricing_subscriptions.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_create_store_coupon():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[DiscountCode, Error]] = create_store_coupon.sync(
        client=client,
        body=StoreCouponParams(
            percent_off=10,
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: DiscountCode = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[DiscountCode, Error]]] = (
        create_store_coupon.sync_detailed(
            client=client,
            body=StoreCouponParams(
                percent_off=10,
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_store_coupon_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[DiscountCode, Error]] = await create_store_coupon.asyncio(
        client=client,
        body=StoreCouponParams(
            percent_off=10,
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[DiscountCode, Error]]
    ] = await create_store_coupon.asyncio_detailed(
        client=client,
        body=StoreCouponParams(
            percent_off=10,
        ),
    )


@pytest.mark.skip
def test_get_angle_unit_conversion():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[UnitAngleConversion, Error]] = (
        get_angle_unit_conversion.sync(
            client=client,
            input_unit=UnitAngle.DEGREES,
            output_unit=UnitAngle.DEGREES,
            value=3.14,
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitAngleConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[UnitAngleConversion, Error]]] = (
        get_angle_unit_conversion.sync_detailed(
            client=client,
            input_unit=UnitAngle.DEGREES,
            output_unit=UnitAngle.DEGREES,
            value=3.14,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_angle_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitAngleConversion, Error]
    ] = await get_angle_unit_conversion.asyncio(
        client=client,
        input_unit=UnitAngle.DEGREES,
        output_unit=UnitAngle.DEGREES,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitAngleConversion, Error]]
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

    result: Optional[Union[UnitAreaConversion, Error]] = get_area_unit_conversion.sync(
        client=client,
        input_unit=UnitArea.CM2,
        output_unit=UnitArea.CM2,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitAreaConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[UnitAreaConversion, Error]]] = (
        get_area_unit_conversion.sync_detailed(
            client=client,
            input_unit=UnitArea.CM2,
            output_unit=UnitArea.CM2,
            value=3.14,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_area_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitAreaConversion, Error]
    ] = await get_area_unit_conversion.asyncio(
        client=client,
        input_unit=UnitArea.CM2,
        output_unit=UnitArea.CM2,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitAreaConversion, Error]]
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

    result: Optional[Union[UnitCurrentConversion, Error]] = (
        get_current_unit_conversion.sync(
            client=client,
            input_unit=UnitCurrent.AMPERES,
            output_unit=UnitCurrent.AMPERES,
            value=3.14,
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitCurrentConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[UnitCurrentConversion, Error]]] = (
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

    result: Optional[
        Union[UnitCurrentConversion, Error]
    ] = await get_current_unit_conversion.asyncio(
        client=client,
        input_unit=UnitCurrent.AMPERES,
        output_unit=UnitCurrent.AMPERES,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitCurrentConversion, Error]]
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

    result: Optional[Union[UnitEnergyConversion, Error]] = (
        get_energy_unit_conversion.sync(
            client=client,
            input_unit=UnitEnergy.BTU,
            output_unit=UnitEnergy.BTU,
            value=3.14,
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitEnergyConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[UnitEnergyConversion, Error]]] = (
        get_energy_unit_conversion.sync_detailed(
            client=client,
            input_unit=UnitEnergy.BTU,
            output_unit=UnitEnergy.BTU,
            value=3.14,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_energy_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitEnergyConversion, Error]
    ] = await get_energy_unit_conversion.asyncio(
        client=client,
        input_unit=UnitEnergy.BTU,
        output_unit=UnitEnergy.BTU,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitEnergyConversion, Error]]
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

    result: Optional[Union[UnitForceConversion, Error]] = (
        get_force_unit_conversion.sync(
            client=client,
            input_unit=UnitForce.DYNES,
            output_unit=UnitForce.DYNES,
            value=3.14,
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitForceConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[UnitForceConversion, Error]]] = (
        get_force_unit_conversion.sync_detailed(
            client=client,
            input_unit=UnitForce.DYNES,
            output_unit=UnitForce.DYNES,
            value=3.14,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_force_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitForceConversion, Error]
    ] = await get_force_unit_conversion.asyncio(
        client=client,
        input_unit=UnitForce.DYNES,
        output_unit=UnitForce.DYNES,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitForceConversion, Error]]
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

    result: Optional[Union[UnitFrequencyConversion, Error]] = (
        get_frequency_unit_conversion.sync(
            client=client,
            input_unit=UnitFrequency.GIGAHERTZ,
            output_unit=UnitFrequency.GIGAHERTZ,
            value=3.14,
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitFrequencyConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[UnitFrequencyConversion, Error]]] = (
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

    result: Optional[
        Union[UnitFrequencyConversion, Error]
    ] = await get_frequency_unit_conversion.asyncio(
        client=client,
        input_unit=UnitFrequency.GIGAHERTZ,
        output_unit=UnitFrequency.GIGAHERTZ,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitFrequencyConversion, Error]]
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

    result: Optional[Union[UnitLengthConversion, Error]] = (
        get_length_unit_conversion.sync(
            client=client,
            input_unit=UnitLength.CM,
            output_unit=UnitLength.CM,
            value=3.14,
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitLengthConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[UnitLengthConversion, Error]]] = (
        get_length_unit_conversion.sync_detailed(
            client=client,
            input_unit=UnitLength.CM,
            output_unit=UnitLength.CM,
            value=3.14,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_length_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitLengthConversion, Error]
    ] = await get_length_unit_conversion.asyncio(
        client=client,
        input_unit=UnitLength.CM,
        output_unit=UnitLength.CM,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitLengthConversion, Error]]
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

    result: Optional[Union[UnitMassConversion, Error]] = get_mass_unit_conversion.sync(
        client=client,
        input_unit=UnitMass.G,
        output_unit=UnitMass.G,
        value=3.14,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitMassConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[UnitMassConversion, Error]]] = (
        get_mass_unit_conversion.sync_detailed(
            client=client,
            input_unit=UnitMass.G,
            output_unit=UnitMass.G,
            value=3.14,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_mass_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitMassConversion, Error]
    ] = await get_mass_unit_conversion.asyncio(
        client=client,
        input_unit=UnitMass.G,
        output_unit=UnitMass.G,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitMassConversion, Error]]
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

    result: Optional[Union[UnitPowerConversion, Error]] = (
        get_power_unit_conversion.sync(
            client=client,
            input_unit=UnitPower.BTU_PER_MINUTE,
            output_unit=UnitPower.BTU_PER_MINUTE,
            value=3.14,
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitPowerConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[UnitPowerConversion, Error]]] = (
        get_power_unit_conversion.sync_detailed(
            client=client,
            input_unit=UnitPower.BTU_PER_MINUTE,
            output_unit=UnitPower.BTU_PER_MINUTE,
            value=3.14,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_power_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitPowerConversion, Error]
    ] = await get_power_unit_conversion.asyncio(
        client=client,
        input_unit=UnitPower.BTU_PER_MINUTE,
        output_unit=UnitPower.BTU_PER_MINUTE,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitPowerConversion, Error]]
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

    result: Optional[Union[UnitPressureConversion, Error]] = (
        get_pressure_unit_conversion.sync(
            client=client,
            input_unit=UnitPressure.ATMOSPHERES,
            output_unit=UnitPressure.ATMOSPHERES,
            value=3.14,
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitPressureConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[UnitPressureConversion, Error]]] = (
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

    result: Optional[
        Union[UnitPressureConversion, Error]
    ] = await get_pressure_unit_conversion.asyncio(
        client=client,
        input_unit=UnitPressure.ATMOSPHERES,
        output_unit=UnitPressure.ATMOSPHERES,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitPressureConversion, Error]]
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

    result: Optional[Union[UnitTemperatureConversion, Error]] = (
        get_temperature_unit_conversion.sync(
            client=client,
            input_unit=UnitTemperature.CELSIUS,
            output_unit=UnitTemperature.CELSIUS,
            value=3.14,
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitTemperatureConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[UnitTemperatureConversion, Error]]] = (
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

    result: Optional[
        Union[UnitTemperatureConversion, Error]
    ] = await get_temperature_unit_conversion.asyncio(
        client=client,
        input_unit=UnitTemperature.CELSIUS,
        output_unit=UnitTemperature.CELSIUS,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitTemperatureConversion, Error]]
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

    result: Optional[Union[UnitTorqueConversion, Error]] = (
        get_torque_unit_conversion.sync(
            client=client,
            input_unit=UnitTorque.NEWTON_METRES,
            output_unit=UnitTorque.NEWTON_METRES,
            value=3.14,
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitTorqueConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[UnitTorqueConversion, Error]]] = (
        get_torque_unit_conversion.sync_detailed(
            client=client,
            input_unit=UnitTorque.NEWTON_METRES,
            output_unit=UnitTorque.NEWTON_METRES,
            value=3.14,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_torque_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitTorqueConversion, Error]
    ] = await get_torque_unit_conversion.asyncio(
        client=client,
        input_unit=UnitTorque.NEWTON_METRES,
        output_unit=UnitTorque.NEWTON_METRES,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitTorqueConversion, Error]]
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

    result: Optional[Union[UnitVolumeConversion, Error]] = (
        get_volume_unit_conversion.sync(
            client=client,
            input_unit=UnitVolume.CM3,
            output_unit=UnitVolume.CM3,
            value=3.14,
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UnitVolumeConversion = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[UnitVolumeConversion, Error]]] = (
        get_volume_unit_conversion.sync_detailed(
            client=client,
            input_unit=UnitVolume.CM3,
            output_unit=UnitVolume.CM3,
            value=3.14,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_volume_unit_conversion_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[UnitVolumeConversion, Error]
    ] = await get_volume_unit_conversion.asyncio(
        client=client,
        input_unit=UnitVolume.CM3,
        output_unit=UnitVolume.CM3,
        value=3.14,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UnitVolumeConversion, Error]]
    ] = await get_volume_unit_conversion.asyncio_detailed(
        client=client,
        input_unit=UnitVolume.CM3,
        output_unit=UnitVolume.CM3,
        value=3.14,
    )


@pytest.mark.skip
def test_get_user_self():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[User, Error]] = get_user_self.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: User = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[User, Error]]] = get_user_self.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_self_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[User, Error]] = await get_user_self.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[User, Error]]
    ] = await get_user_self.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_update_user_self():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[User, Error]] = update_user_self.sync(
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

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: User = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[User, Error]]] = update_user_self.sync_detailed(
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

    result: Optional[Union[User, Error]] = await update_user_self.asyncio(
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
    response: Response[
        Optional[Union[User, Error]]
    ] = await update_user_self.asyncio_detailed(
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
def test_delete_user_self():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = delete_user_self.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = delete_user_self.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_user_self_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await delete_user_self.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await delete_user_self.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_user_list_api_calls():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiCallWithPriceResultsPage, Error]] = (
        user_list_api_calls.sync(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ApiCallWithPriceResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ApiCallWithPriceResultsPage, Error]]] = (
        user_list_api_calls.sync_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_user_list_api_calls_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ApiCallWithPriceResultsPage, Error]
    ] = await user_list_api_calls.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ApiCallWithPriceResultsPage, Error]]
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

    result: Optional[Union[ApiCallWithPrice, Error]] = get_api_call_for_user.sync(
        client=client,
        id="<string>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ApiCallWithPrice = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ApiCallWithPrice, Error]]] = (
        get_api_call_for_user.sync_detailed(
            client=client,
            id="<string>",
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ApiCallWithPrice, Error]
    ] = await get_api_call_for_user.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ApiCallWithPrice, Error]]
    ] = await get_api_call_for_user.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_list_api_tokens_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiTokenResultsPage, Error]] = list_api_tokens_for_user.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ApiTokenResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ApiTokenResultsPage, Error]]] = (
        list_api_tokens_for_user.sync_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_api_tokens_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ApiTokenResultsPage, Error]
    ] = await list_api_tokens_for_user.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ApiTokenResultsPage, Error]]
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

    result: Optional[Union[ApiToken, Error]] = create_api_token_for_user.sync(
        client=client,
        label=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ApiToken = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ApiToken, Error]]] = (
        create_api_token_for_user.sync_detailed(
            client=client,
            label=None,  # Optional[str]
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_api_token_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiToken, Error]] = await create_api_token_for_user.asyncio(
        client=client,
        label=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ApiToken, Error]]
    ] = await create_api_token_for_user.asyncio_detailed(
        client=client,
        label=None,  # Optional[str]
    )


@pytest.mark.skip
def test_get_api_token_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiToken, Error]] = get_api_token_for_user.sync(
        client=client,
        token=ApiTokenUuid("<string>"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ApiToken = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ApiToken, Error]]] = (
        get_api_token_for_user.sync_detailed(
            client=client,
            token=ApiTokenUuid("<string>"),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_token_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiToken, Error]] = await get_api_token_for_user.asyncio(
        client=client,
        token=ApiTokenUuid("<string>"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ApiToken, Error]]
    ] = await get_api_token_for_user.asyncio_detailed(
        client=client,
        token=ApiTokenUuid("<string>"),
    )


@pytest.mark.skip
def test_delete_api_token_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = delete_api_token_for_user.sync(
        client=client,
        token=ApiTokenUuid("<string>"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = delete_api_token_for_user.sync_detailed(
        client=client,
        token=ApiTokenUuid("<string>"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_api_token_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await delete_api_token_for_user.asyncio(
        client=client,
        token=ApiTokenUuid("<string>"),
    )

    # OR run async with more info
    response: Response[
        Optional[Error]
    ] = await delete_api_token_for_user.asyncio_detailed(
        client=client,
        token=ApiTokenUuid("<string>"),
    )


@pytest.mark.skip
def test_patch_user_crm():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = patch_user_crm.sync(
        client=client,
        body=CrmData(),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = patch_user_crm.sync_detailed(
        client=client,
        body=CrmData(),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_patch_user_crm_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await patch_user_crm.asyncio(
        client=client,
        body=CrmData(),
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await patch_user_crm.asyncio_detailed(
        client=client,
        body=CrmData(),
    )


@pytest.mark.skip
def test_get_user_self_extended():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ExtendedUser, Error]] = get_user_self_extended.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ExtendedUser = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ExtendedUser, Error]]] = (
        get_user_self_extended.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_self_extended_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ExtendedUser, Error]] = await get_user_self_extended.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ExtendedUser, Error]]
    ] = await get_user_self_extended.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_put_user_form_self():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = put_user_form_self.sync(
        client=client,
        body=InquiryForm(
            email="<string>",
            first_name="<string>",
            inquiry_type=InquiryType.GENERAL_INQUIRY,
            last_name="<string>",
            message="<string>",
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = put_user_form_self.sync_detailed(
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

    result: Optional[Error] = await put_user_form_self.asyncio(
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
    response: Response[Optional[Error]] = await put_user_form_self.asyncio_detailed(
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

    result: Optional[Union[List[AccountProvider], Error]] = (
        get_oauth2_providers_for_user.sync(
            client=client,
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: List[AccountProvider] = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[List[AccountProvider], Error]]] = (
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

    result: Optional[
        Union[List[AccountProvider], Error]
    ] = await get_oauth2_providers_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[List[AccountProvider], Error]]
    ] = await get_oauth2_providers_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_user_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[UserOrgInfo, Error]] = get_user_org.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UserOrgInfo = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[UserOrgInfo, Error]]] = (
        get_user_org.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[UserOrgInfo, Error]] = await get_user_org.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UserOrgInfo, Error]]
    ] = await get_user_org.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_payment_information_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Customer, Error]] = get_payment_information_for_user.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Customer = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[Customer, Error]]] = (
        get_payment_information_for_user.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_information_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[Customer, Error]
    ] = await get_payment_information_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[Customer, Error]]
    ] = await get_payment_information_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_update_payment_information_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Customer, Error]] = update_payment_information_for_user.sync(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Customer = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[Customer, Error]]] = (
        update_payment_information_for_user.sync_detailed(
            client=client,
            body=BillingInfo(
                name="<string>",
                phone="<string>",
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_payment_information_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[Customer, Error]
    ] = await update_payment_information_for_user.asyncio(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[Customer, Error]]
    ] = await update_payment_information_for_user.asyncio_detailed(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )


@pytest.mark.skip
def test_create_payment_information_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Customer, Error]] = create_payment_information_for_user.sync(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Customer = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[Customer, Error]]] = (
        create_payment_information_for_user.sync_detailed(
            client=client,
            body=BillingInfo(
                name="<string>",
                phone="<string>",
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_payment_information_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[Customer, Error]
    ] = await create_payment_information_for_user.asyncio(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[Customer, Error]]
    ] = await create_payment_information_for_user.asyncio_detailed(
        client=client,
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        ),
    )


@pytest.mark.skip
def test_delete_payment_information_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = delete_payment_information_for_user.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = (
        delete_payment_information_for_user.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_payment_information_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await delete_payment_information_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Error]
    ] = await delete_payment_information_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_payment_balance_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CustomerBalance, Error]] = get_payment_balance_for_user.sync(
        client=client,
        include_total_due=False,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: CustomerBalance = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[CustomerBalance, Error]]] = (
        get_payment_balance_for_user.sync_detailed(
            client=client,
            include_total_due=False,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[CustomerBalance, Error]
    ] = await get_payment_balance_for_user.asyncio(
        client=client,
        include_total_due=False,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[CustomerBalance, Error]]
    ] = await get_payment_balance_for_user.asyncio_detailed(
        client=client,
        include_total_due=False,
    )


@pytest.mark.skip
def test_create_payment_intent_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[PaymentIntent, Error]] = create_payment_intent_for_user.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: PaymentIntent = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[PaymentIntent, Error]]] = (
        create_payment_intent_for_user.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_payment_intent_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[PaymentIntent, Error]
    ] = await create_payment_intent_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[PaymentIntent, Error]]
    ] = await create_payment_intent_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_list_invoices_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[List[Invoice], Error]] = list_invoices_for_user.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: List[Invoice] = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[List[Invoice], Error]]] = (
        list_invoices_for_user.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_invoices_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[List[Invoice], Error]
    ] = await list_invoices_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[List[Invoice], Error]]
    ] = await list_invoices_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_list_payment_methods_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[List[PaymentMethod], Error]] = (
        list_payment_methods_for_user.sync(
            client=client,
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: List[PaymentMethod] = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[List[PaymentMethod], Error]]] = (
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

    result: Optional[
        Union[List[PaymentMethod], Error]
    ] = await list_payment_methods_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[List[PaymentMethod], Error]]
    ] = await list_payment_methods_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_delete_payment_method_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = delete_payment_method_for_user.sync(
        client=client,
        id="<string>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = delete_payment_method_for_user.sync_detailed(
        client=client,
        id="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_payment_method_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await delete_payment_method_for_user.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[
        Optional[Error]
    ] = await delete_payment_method_for_user.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_get_user_subscription():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ZooProductSubscriptions, Error]] = (
        get_user_subscription.sync(
            client=client,
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ZooProductSubscriptions = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ZooProductSubscriptions, Error]]] = (
        get_user_subscription.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_subscription_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ZooProductSubscriptions, Error]
    ] = await get_user_subscription.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ZooProductSubscriptions, Error]]
    ] = await get_user_subscription.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_update_user_subscription():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ZooProductSubscriptions, Error]] = (
        update_user_subscription.sync(
            client=client,
            body=ZooProductSubscriptionsUserRequest(
                modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
            ),
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ZooProductSubscriptions = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ZooProductSubscriptions, Error]]] = (
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

    result: Optional[
        Union[ZooProductSubscriptions, Error]
    ] = await update_user_subscription.asyncio(
        client=client,
        body=ZooProductSubscriptionsUserRequest(
            modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ZooProductSubscriptions, Error]]
    ] = await update_user_subscription.asyncio_detailed(
        client=client,
        body=ZooProductSubscriptionsUserRequest(
            modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
        ),
    )


@pytest.mark.skip
def test_create_user_subscription():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ZooProductSubscriptions, Error]] = (
        create_user_subscription.sync(
            client=client,
            body=ZooProductSubscriptionsUserRequest(
                modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
            ),
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ZooProductSubscriptions = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ZooProductSubscriptions, Error]]] = (
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

    result: Optional[
        Union[ZooProductSubscriptions, Error]
    ] = await create_user_subscription.asyncio(
        client=client,
        body=ZooProductSubscriptionsUserRequest(
            modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ZooProductSubscriptions, Error]]
    ] = await create_user_subscription.asyncio_detailed(
        client=client,
        body=ZooProductSubscriptionsUserRequest(
            modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
        ),
    )


@pytest.mark.skip
def test_validate_customer_tax_information_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = validate_customer_tax_information_for_user.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = (
        validate_customer_tax_information_for_user.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_validate_customer_tax_information_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await validate_customer_tax_information_for_user.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Error]
    ] = await validate_customer_tax_information_for_user.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_get_user_privacy_settings():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[PrivacySettings, Error]] = get_user_privacy_settings.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: PrivacySettings = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[PrivacySettings, Error]]] = (
        get_user_privacy_settings.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_privacy_settings_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[PrivacySettings, Error]
    ] = await get_user_privacy_settings.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[PrivacySettings, Error]]
    ] = await get_user_privacy_settings.asyncio_detailed(
        client=client,
    )


@pytest.mark.skip
def test_update_user_privacy_settings():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[PrivacySettings, Error]] = update_user_privacy_settings.sync(
        client=client,
        body=PrivacySettings(
            can_train_on_data=False,
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: PrivacySettings = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[PrivacySettings, Error]]] = (
        update_user_privacy_settings.sync_detailed(
            client=client,
            body=PrivacySettings(
                can_train_on_data=False,
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_user_privacy_settings_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[PrivacySettings, Error]
    ] = await update_user_privacy_settings.asyncio(
        client=client,
        body=PrivacySettings(
            can_train_on_data=False,
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[PrivacySettings, Error]]
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

    result: Optional[Union[Session, Error]] = get_session_for_user.sync(
        client=client,
        token=SessionUuid("<string>"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Session = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[Session, Error]]] = (
        get_session_for_user.sync_detailed(
            client=client,
            token=SessionUuid("<string>"),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_session_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Session, Error]] = await get_session_for_user.asyncio(
        client=client,
        token=SessionUuid("<string>"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[Session, Error]]
    ] = await get_session_for_user.asyncio_detailed(
        client=client,
        token=SessionUuid("<string>"),
    )


@pytest.mark.skip
def test_get_user_shortlinks():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ShortlinkResultsPage, Error]] = get_user_shortlinks.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ShortlinkResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ShortlinkResultsPage, Error]]] = (
        get_user_shortlinks.sync_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_shortlinks_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ShortlinkResultsPage, Error]
    ] = await get_user_shortlinks.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ShortlinkResultsPage, Error]]
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

    result: Optional[Union[CreateShortlinkResponse, Error]] = (
        create_user_shortlink.sync(
            client=client,
            body=CreateShortlinkRequest(
                restrict_to_org=False,
                url="<string>",
            ),
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: CreateShortlinkResponse = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[CreateShortlinkResponse, Error]]] = (
        create_user_shortlink.sync_detailed(
            client=client,
            body=CreateShortlinkRequest(
                restrict_to_org=False,
                url="<string>",
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_user_shortlink_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[CreateShortlinkResponse, Error]
    ] = await create_user_shortlink.asyncio(
        client=client,
        body=CreateShortlinkRequest(
            restrict_to_org=False,
            url="<string>",
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[CreateShortlinkResponse, Error]]
    ] = await create_user_shortlink.asyncio_detailed(
        client=client,
        body=CreateShortlinkRequest(
            restrict_to_org=False,
            url="<string>",
        ),
    )


@pytest.mark.skip
def test_redirect_user_shortlink():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = redirect_user_shortlink.sync(
        client=client,
        key="<string>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = redirect_user_shortlink.sync_detailed(
        client=client,
        key="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_redirect_user_shortlink_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await redirect_user_shortlink.asyncio(
        client=client,
        key="<string>",
    )

    # OR run async with more info
    response: Response[
        Optional[Error]
    ] = await redirect_user_shortlink.asyncio_detailed(
        client=client,
        key="<string>",
    )


@pytest.mark.skip
def test_update_user_shortlink():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = update_user_shortlink.sync(
        client=client,
        key="<string>",
        body=UpdateShortlinkRequest(
            restrict_to_org=False,
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = update_user_shortlink.sync_detailed(
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

    result: Optional[Error] = await update_user_shortlink.asyncio(
        client=client,
        key="<string>",
        body=UpdateShortlinkRequest(
            restrict_to_org=False,
        ),
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await update_user_shortlink.asyncio_detailed(
        client=client,
        key="<string>",
        body=UpdateShortlinkRequest(
            restrict_to_org=False,
        ),
    )


@pytest.mark.skip
def test_delete_user_shortlink():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = delete_user_shortlink.sync(
        client=client,
        key="<string>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = delete_user_shortlink.sync_detailed(
        client=client,
        key="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_user_shortlink_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await delete_user_shortlink.asyncio(
        client=client,
        key="<string>",
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await delete_user_shortlink.asyncio_detailed(
        client=client,
        key="<string>",
    )


@pytest.mark.skip
def test_list_text_to_cad_models_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[TextToCadResultsPage, Error]] = (
        list_text_to_cad_models_for_user.sync(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
            no_models=None,  # Optional[bool]
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: TextToCadResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[TextToCadResultsPage, Error]]] = (
        list_text_to_cad_models_for_user.sync_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
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

    result: Optional[
        Union[TextToCadResultsPage, Error]
    ] = await list_text_to_cad_models_for_user.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
        no_models=None,  # Optional[bool]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[TextToCadResultsPage, Error]]
    ] = await list_text_to_cad_models_for_user.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
        no_models=None,  # Optional[bool]
    )


@pytest.mark.skip
def test_get_text_to_cad_model_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[TextToCad, Error]] = get_text_to_cad_model_for_user.sync(
        client=client,
        id="<string>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: TextToCad = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[TextToCad, Error]]] = (
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

    result: Optional[
        Union[TextToCad, Error]
    ] = await get_text_to_cad_model_for_user.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[
        Optional[Union[TextToCad, Error]]
    ] = await get_text_to_cad_model_for_user.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_create_text_to_cad_model_feedback():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = create_text_to_cad_model_feedback.sync(
        client=client,
        id="<string>",
        feedback=MlFeedback.THUMBS_UP,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = (
        create_text_to_cad_model_feedback.sync_detailed(
            client=client,
            id="<string>",
            feedback=MlFeedback.THUMBS_UP,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_text_to_cad_model_feedback_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await create_text_to_cad_model_feedback.asyncio(
        client=client,
        id="<string>",
        feedback=MlFeedback.THUMBS_UP,
    )

    # OR run async with more info
    response: Response[
        Optional[Error]
    ] = await create_text_to_cad_model_feedback.asyncio_detailed(
        client=client,
        id="<string>",
        feedback=MlFeedback.THUMBS_UP,
    )


@pytest.mark.skip
def test_list_users():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[UserResultsPage, Error]] = list_users.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: UserResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[UserResultsPage, Error]]] = (
        list_users.sync_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_users_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[UserResultsPage, Error]] = await list_users.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[UserResultsPage, Error]]
    ] = await list_users.asyncio_detailed(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )


@pytest.mark.skip
def test_list_users_extended():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ExtendedUserResultsPage, Error]] = list_users_extended.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ExtendedUserResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ExtendedUserResultsPage, Error]]] = (
        list_users_extended.sync_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_users_extended_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[
        Union[ExtendedUserResultsPage, Error]
    ] = await list_users_extended.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ExtendedUserResultsPage, Error]]
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

    result: Optional[Union[ExtendedUser, Error]] = get_user_extended.sync(
        client=client,
        id=UserIdentifier("<string>"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ExtendedUser = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ExtendedUser, Error]]] = (
        get_user_extended.sync_detailed(
            client=client,
            id=UserIdentifier("<string>"),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_extended_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ExtendedUser, Error]] = await get_user_extended.asyncio(
        client=client,
        id=UserIdentifier("<string>"),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ExtendedUser, Error]]
    ] = await get_user_extended.asyncio_detailed(
        client=client,
        id=UserIdentifier("<string>"),
    )


@pytest.mark.skip
def test_get_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[User, Error]] = get_user.sync(
        client=client,
        id=UserIdentifier("<string>"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: User = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[User, Error]]] = get_user.sync_detailed(
        client=client,
        id=UserIdentifier("<string>"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[User, Error]] = await get_user.asyncio(
        client=client,
        id=UserIdentifier("<string>"),
    )

    # OR run async with more info
    response: Response[Optional[Union[User, Error]]] = await get_user.asyncio_detailed(
        client=client,
        id=UserIdentifier("<string>"),
    )


@pytest.mark.skip
def test_list_api_calls_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiCallWithPriceResultsPage, Error]] = (
        list_api_calls_for_user.sync(
            client=client,
            id=UserIdentifier("<string>"),
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ApiCallWithPriceResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ApiCallWithPriceResultsPage, Error]]] = (
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

    result: Optional[
        Union[ApiCallWithPriceResultsPage, Error]
    ] = await list_api_calls_for_user.asyncio(
        client=client,
        id=UserIdentifier("<string>"),
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ApiCallWithPriceResultsPage, Error]]
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

    result: Optional[Union[CustomerBalance, Error]] = (
        get_payment_balance_for_any_user.sync(
            client=client,
            id=UserIdentifier("<string>"),
            include_total_due=False,
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: CustomerBalance = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[CustomerBalance, Error]]] = (
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

    result: Optional[
        Union[CustomerBalance, Error]
    ] = await get_payment_balance_for_any_user.asyncio(
        client=client,
        id=UserIdentifier("<string>"),
        include_total_due=False,
    )

    # OR run async with more info
    response: Response[
        Optional[Union[CustomerBalance, Error]]
    ] = await get_payment_balance_for_any_user.asyncio_detailed(
        client=client,
        id=UserIdentifier("<string>"),
        include_total_due=False,
    )


@pytest.mark.skip
def test_update_payment_balance_for_any_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CustomerBalance, Error]] = (
        update_payment_balance_for_any_user.sync(
            client=client,
            id=UserIdentifier("<string>"),
            include_total_due=False,
            body=UpdatePaymentBalance(),
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: CustomerBalance = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[CustomerBalance, Error]]] = (
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

    result: Optional[
        Union[CustomerBalance, Error]
    ] = await update_payment_balance_for_any_user.asyncio(
        client=client,
        id=UserIdentifier("<string>"),
        include_total_due=False,
        body=UpdatePaymentBalance(),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[CustomerBalance, Error]]
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

    result: Optional[Union[ZooProductSubscriptions, Error]] = (
        update_subscription_for_user.sync(
            client=client,
            id=UserIdentifier("<string>"),
            body=ZooProductSubscriptionsUserRequest(
                modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
            ),
        )
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: ZooProductSubscriptions = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[ZooProductSubscriptions, Error]]] = (
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

    result: Optional[
        Union[ZooProductSubscriptions, Error]
    ] = await update_subscription_for_user.asyncio(
        client=client,
        id=UserIdentifier("<string>"),
        body=ZooProductSubscriptionsUserRequest(
            modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
        ),
    )

    # OR run async with more info
    response: Response[
        Optional[Union[ZooProductSubscriptions, Error]]
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

    result: Optional[Error] = put_public_form.sync(
        client=client,
        body=InquiryForm(
            email="<string>",
            first_name="<string>",
            inquiry_type=InquiryType.GENERAL_INQUIRY,
            last_name="<string>",
            message="<string>",
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = put_public_form.sync_detailed(
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

    result: Optional[Error] = await put_public_form.asyncio(
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
    response: Response[Optional[Error]] = await put_public_form.asyncio_detailed(
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

    result: Optional[Error] = put_public_subscribe.sync(
        client=client,
        body=Subscribe(
            email="<string>",
        ),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = put_public_subscribe.sync_detailed(
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

    result: Optional[Error] = await put_public_subscribe.asyncio(
        client=client,
        body=Subscribe(
            email="<string>",
        ),
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await put_public_subscribe.asyncio_detailed(
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
        websocket.send(
            WebSocketRequest(
                OptionMetricsResponse(
                    metrics=ClientMetrics(),
                )
            )
        )

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
