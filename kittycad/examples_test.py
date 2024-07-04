from typing import List, Optional, Union

import pytest

from kittycad.api.ai import (
    create_kcl_code_completions,
    create_text_to_cad,
    create_text_to_cad_model_feedback,
    get_ai_prompt,
    get_text_to_cad_model_for_user,
    list_ai_prompts,
    list_text_to_cad_models_for_user,
)
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
    create_file_density,
    create_file_mass,
    create_file_surface_area,
    create_file_volume,
)
from kittycad.api.hidden import (
    auth_email,
    auth_email_callback,
    get_auth_saml,
    logout,
    post_auth_saml,
)
from kittycad.api.meta import (
    create_debug_uploads,
    create_event,
    get_ipinfo,
    get_metadata,
    get_pricing_subscriptions,
    get_schema,
    internal_get_api_token_for_discord_user,
    ping,
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
    delete_user_self,
    get_oauth2_providers_for_user,
    get_session_for_user,
    get_user,
    get_user_extended,
    get_user_onboarding_self,
    get_user_privacy_settings,
    get_user_self,
    get_user_self_extended,
    list_users,
    list_users_extended,
    update_user_privacy_settings,
    update_user_self,
)
from kittycad.client import ClientFromEnv
from kittycad.models import (
    AccountProvider,
    AiPrompt,
    AiPromptResultsPage,
    ApiCallQueryGroup,
    ApiCallWithPrice,
    ApiCallWithPriceResultsPage,
    ApiToken,
    ApiTokenResultsPage,
    AppClientInfo,
    AsyncApiCallResultsPage,
    CodeOutput,
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
    Metadata,
    Onboarding,
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
    TextToCad,
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
from kittycad.models.ai_feedback import AiFeedback
from kittycad.models.api_call_query_group_by import ApiCallQueryGroupBy
from kittycad.models.api_call_status import ApiCallStatus
from kittycad.models.billing_info import BillingInfo
from kittycad.models.code_language import CodeLanguage
from kittycad.models.created_at_sort_mode import CreatedAtSortMode
from kittycad.models.email_authentication_form import EmailAuthenticationForm
from kittycad.models.event import modeling_app_event
from kittycad.models.file_export_format import FileExportFormat
from kittycad.models.file_import_format import FileImportFormat
from kittycad.models.idp_metadata_source import base64_encoded_xml
from kittycad.models.kcl_code_completion_params import KclCodeCompletionParams
from kittycad.models.kcl_code_completion_request import KclCodeCompletionRequest
from kittycad.models.modeling_app_event_type import ModelingAppEventType
from kittycad.models.modeling_app_individual_subscription_tier import (
    ModelingAppIndividualSubscriptionTier,
)
from kittycad.models.modeling_app_organization_subscription_tier import (
    ModelingAppOrganizationSubscriptionTier,
)
from kittycad.models.org_details import OrgDetails
from kittycad.models.plan_interval import PlanInterval
from kittycad.models.post_effect_type import PostEffectType
from kittycad.models.privacy_settings import PrivacySettings
from kittycad.models.rtc_sdp_type import RtcSdpType
from kittycad.models.rtc_session_description import RtcSessionDescription
from kittycad.models.saml_identity_provider_create import SamlIdentityProviderCreate
from kittycad.models.store_coupon_params import StoreCouponParams
from kittycad.models.subscription_tier_price import per_user
from kittycad.models.text_to_cad_create_body import TextToCadCreateBody
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
from kittycad.models.update_user import UpdateUser
from kittycad.models.user_org_role import UserOrgRole
from kittycad.models.uuid import Uuid
from kittycad.models.web_socket_request import sdp_offer
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
def test_get_metadata():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Metadata, Error]] = get_metadata.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Metadata = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[Metadata, Error]]] = get_metadata.sync_detailed(
        client=client,
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_metadata_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Metadata, Error]] = await get_metadata.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[Optional[Union[Metadata, Error]]] = (
        await get_metadata.asyncio_detailed(
            client=client,
        )
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
    response: Response[Optional[Union[IpAddrInfo, Error]]] = (
        await get_ipinfo.asyncio_detailed(
            client=client,
        )
    )


@pytest.mark.skip
def test_list_ai_prompts():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[AiPromptResultsPage, Error]] = list_ai_prompts.sync(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: AiPromptResultsPage = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[AiPromptResultsPage, Error]]] = (
        list_ai_prompts.sync_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_ai_prompts_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[AiPromptResultsPage, Error]] = await list_ai_prompts.asyncio(
        client=client,
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,  # Optional[int]
        page_token=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[Optional[Union[AiPromptResultsPage, Error]]] = (
        await list_ai_prompts.asyncio_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


@pytest.mark.skip
def test_get_ai_prompt():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[AiPrompt, Error]] = get_ai_prompt.sync(
        client=client,
        id="<uuid>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: AiPrompt = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[AiPrompt, Error]]] = get_ai_prompt.sync_detailed(
        client=client,
        id="<uuid>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_ai_prompt_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[AiPrompt, Error]] = await get_ai_prompt.asyncio(
        client=client,
        id="<uuid>",
    )

    # OR run async with more info
    response: Response[Optional[Union[AiPrompt, Error]]] = (
        await get_ai_prompt.asyncio_detailed(
            client=client,
            id="<uuid>",
        )
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

    result: Optional[Union[KclCodeCompletionResponse, Error]] = (
        await create_kcl_code_completions.asyncio(
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

    # OR run async with more info
    response: Response[Optional[Union[KclCodeCompletionResponse, Error]]] = (
        await create_kcl_code_completions.asyncio_detailed(
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


@pytest.mark.skip
def test_create_text_to_cad():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[TextToCad, Error]] = create_text_to_cad.sync(
        client=client,
        output_format=FileExportFormat.FBX,
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
        body=TextToCadCreateBody(
            prompt="<string>",
        ),
    )

    # OR run async with more info
    response: Response[Optional[Union[TextToCad, Error]]] = (
        await create_text_to_cad.asyncio_detailed(
            client=client,
            output_format=FileExportFormat.FBX,
            body=TextToCadCreateBody(
                prompt="<string>",
            ),
        )
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

    result: Optional[Union[List[ApiCallQueryGroup], Error]] = (
        await get_api_call_metrics.asyncio(
            client=client,
            group_by=ApiCallQueryGroupBy.EMAIL,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[List[ApiCallQueryGroup], Error]]] = (
        await get_api_call_metrics.asyncio_detailed(
            client=client,
            group_by=ApiCallQueryGroupBy.EMAIL,
        )
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

    result: Optional[Union[ApiCallWithPriceResultsPage, Error]] = (
        await list_api_calls.asyncio(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[ApiCallWithPriceResultsPage, Error]]] = (
        await list_api_calls.asyncio_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


@pytest.mark.skip
def test_get_api_call():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiCallWithPrice, Error]] = get_api_call.sync(
        client=client,
        id="<uuid>",
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
            id="<uuid>",
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
        id="<uuid>",
    )

    # OR run async with more info
    response: Response[Optional[Union[ApiCallWithPrice, Error]]] = (
        await get_api_call.asyncio_detailed(
            client=client,
            id="<uuid>",
        )
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
    response: Response[Optional[Union[AppClientInfo, Error]]] = (
        await apps_github_consent.asyncio_detailed(
            client=client,
        )
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

    result: Optional[Union[AsyncApiCallResultsPage, Error]] = (
        await list_async_operations.asyncio(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            status=ApiCallStatus.QUEUED,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[AsyncApiCallResultsPage, Error]]] = (
        await list_async_operations.asyncio_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            status=ApiCallStatus.QUEUED,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
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
                Error,
            ]
        ]
    ] = await get_async_operation.asyncio_detailed(
        client=client,
        id="<string>",
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

    result: Optional[Union[VerificationTokenResponse, Error]] = (
        await auth_email.asyncio(
            client=client,
            body=EmailAuthenticationForm(
                email="<string>",
            ),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[VerificationTokenResponse, Error]]] = (
        await auth_email.asyncio_detailed(
            client=client,
            body=EmailAuthenticationForm(
                email="<string>",
            ),
        )
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
        provider_id=Uuid("<uuid>"),
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
        provider_id=Uuid("<uuid>"),
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
        provider_id=Uuid("<uuid>"),
        callback_url=None,  # Optional[str]
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await get_auth_saml.asyncio_detailed(
        client=client,
        provider_id=Uuid("<uuid>"),
        callback_url=None,  # Optional[str]
    )


@pytest.mark.skip
def test_post_auth_saml():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = post_auth_saml.sync(
        client=client,
        provider_id=Uuid("<uuid>"),
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
        provider_id=Uuid("<uuid>"),
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
        provider_id=Uuid("<uuid>"),
        body=bytes("some bytes", "utf-8"),
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await post_auth_saml.asyncio_detailed(
        client=client,
        provider_id=Uuid("<uuid>"),
        body=bytes("some bytes", "utf-8"),
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
    response: Response[Optional[Union[List[str], Error]]] = (
        await create_debug_uploads.asyncio_detailed(
            client=client,
        )
    )


@pytest.mark.skip
def test_create_event():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = create_event.sync(
        client=client,
        body=modeling_app_event(
            created_at="<string>",
            event_type=ModelingAppEventType.SUCCESSFUL_COMPILE_BEFORE_CLOSE,
            project_name="<string>",
            source_id="<uuid>",
            user_id="<string>",
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
        body=modeling_app_event(
            created_at="<string>",
            event_type=ModelingAppEventType.SUCCESSFUL_COMPILE_BEFORE_CLOSE,
            project_name="<string>",
            source_id="<uuid>",
            user_id="<string>",
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
        body=modeling_app_event(
            created_at="<string>",
            event_type=ModelingAppEventType.SUCCESSFUL_COMPILE_BEFORE_CLOSE,
            project_name="<string>",
            source_id="<uuid>",
            user_id="<string>",
        ),
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await create_event.asyncio_detailed(
        client=client,
        body=modeling_app_event(
            created_at="<string>",
            event_type=ModelingAppEventType.SUCCESSFUL_COMPILE_BEFORE_CLOSE,
            project_name="<string>",
            source_id="<uuid>",
            user_id="<string>",
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

    result: Optional[Union[FileCenterOfMass, Error]] = (
        await create_file_center_of_mass.asyncio(
            client=client,
            output_unit=UnitLength.CM,
            src_format=FileImportFormat.FBX,
            body=bytes("some bytes", "utf-8"),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[FileCenterOfMass, Error]]] = (
        await create_file_center_of_mass.asyncio_detailed(
            client=client,
            output_unit=UnitLength.CM,
            src_format=FileImportFormat.FBX,
            body=bytes("some bytes", "utf-8"),
        )
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

    result: Optional[Union[FileConversion, Error]] = (
        await create_file_conversion.asyncio(
            client=client,
            output_format=FileExportFormat.FBX,
            src_format=FileImportFormat.FBX,
            body=bytes("some bytes", "utf-8"),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[FileConversion, Error]]] = (
        await create_file_conversion.asyncio_detailed(
            client=client,
            output_format=FileExportFormat.FBX,
            src_format=FileImportFormat.FBX,
            body=bytes("some bytes", "utf-8"),
        )
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
    response: Response[Optional[Union[FileDensity, Error]]] = (
        await create_file_density.asyncio_detailed(
            client=client,
            material_mass=3.14,
            material_mass_unit=UnitMass.G,
            output_unit=UnitDensity.LB_FT3,
            src_format=FileImportFormat.FBX,
            body=bytes("some bytes", "utf-8"),
        )
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
    response: Response[Optional[Union[CodeOutput, Error]]] = (
        await create_file_execution.asyncio_detailed(
            client=client,
            lang=CodeLanguage.GO,
            output=None,  # Optional[str]
            body=bytes("some bytes", "utf-8"),
        )
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
    response: Response[Optional[Union[FileMass, Error]]] = (
        await create_file_mass.asyncio_detailed(
            client=client,
            material_density=3.14,
            material_density_unit=UnitDensity.LB_FT3,
            output_unit=UnitMass.G,
            src_format=FileImportFormat.FBX,
            body=bytes("some bytes", "utf-8"),
        )
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

    result: Optional[Union[FileSurfaceArea, Error]] = (
        await create_file_surface_area.asyncio(
            client=client,
            output_unit=UnitArea.CM2,
            src_format=FileImportFormat.FBX,
            body=bytes("some bytes", "utf-8"),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[FileSurfaceArea, Error]]] = (
        await create_file_surface_area.asyncio_detailed(
            client=client,
            output_unit=UnitArea.CM2,
            src_format=FileImportFormat.FBX,
            body=bytes("some bytes", "utf-8"),
        )
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
    response: Response[Optional[Union[FileVolume, Error]]] = (
        await create_file_volume.asyncio_detailed(
            client=client,
            output_unit=UnitVolume.CM3,
            src_format=FileImportFormat.FBX,
            body=bytes("some bytes", "utf-8"),
        )
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

    result: Optional[Union[ApiToken, Error]] = (
        await internal_get_api_token_for_discord_user.asyncio(
            client=client,
            discord_id="<string>",
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[ApiToken, Error]]] = (
        await internal_get_api_token_for_discord_user.asyncio_detailed(
            client=client,
            discord_id="<string>",
        )
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

    result: Optional[Union[ApiCallWithPriceResultsPage, Error]] = (
        await org_list_api_calls.asyncio(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[ApiCallWithPriceResultsPage, Error]]] = (
        await org_list_api_calls.asyncio_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


@pytest.mark.skip
def test_get_api_call_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiCallWithPrice, Error]] = get_api_call_for_org.sync(
        client=client,
        id="<uuid>",
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
            id="<uuid>",
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiCallWithPrice, Error]] = (
        await get_api_call_for_org.asyncio(
            client=client,
            id="<uuid>",
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[ApiCallWithPrice, Error]]] = (
        await get_api_call_for_org.asyncio_detailed(
            client=client,
            id="<uuid>",
        )
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

    result: Optional[Union[OrgMemberResultsPage, Error]] = (
        await list_org_members.asyncio(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            role=UserOrgRole.ADMIN,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[OrgMemberResultsPage, Error]]] = (
        await list_org_members.asyncio_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            role=UserOrgRole.ADMIN,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
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
    response: Response[Optional[Union[OrgMember, Error]]] = (
        await create_org_member.asyncio_detailed(
            client=client,
            body=AddOrgMember(
                email="<string>",
                role=UserOrgRole.ADMIN,
            ),
        )
    )


@pytest.mark.skip
def test_get_org_member():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[OrgMember, Error]] = get_org_member.sync(
        client=client,
        user_id=Uuid("<uuid>"),
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
            user_id=Uuid("<uuid>"),
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
        user_id=Uuid("<uuid>"),
    )

    # OR run async with more info
    response: Response[Optional[Union[OrgMember, Error]]] = (
        await get_org_member.asyncio_detailed(
            client=client,
            user_id=Uuid("<uuid>"),
        )
    )


@pytest.mark.skip
def test_update_org_member():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[OrgMember, Error]] = update_org_member.sync(
        client=client,
        user_id=Uuid("<uuid>"),
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
            user_id=Uuid("<uuid>"),
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
        user_id=Uuid("<uuid>"),
        body=UpdateMemberToOrgBody(
            role=UserOrgRole.ADMIN,
        ),
    )

    # OR run async with more info
    response: Response[Optional[Union[OrgMember, Error]]] = (
        await update_org_member.asyncio_detailed(
            client=client,
            user_id=Uuid("<uuid>"),
            body=UpdateMemberToOrgBody(
                role=UserOrgRole.ADMIN,
            ),
        )
    )


@pytest.mark.skip
def test_delete_org_member():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = delete_org_member.sync(
        client=client,
        user_id=Uuid("<uuid>"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = delete_org_member.sync_detailed(
        client=client,
        user_id=Uuid("<uuid>"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_org_member_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await delete_org_member.asyncio(
        client=client,
        user_id=Uuid("<uuid>"),
    )

    # OR run async with more info
    response: Response[Optional[Error]] = await delete_org_member.asyncio_detailed(
        client=client,
        user_id=Uuid("<uuid>"),
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

    result: Optional[Union[Customer, Error]] = (
        await get_payment_information_for_org.asyncio(
            client=client,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[Customer, Error]]] = (
        await get_payment_information_for_org.asyncio_detailed(
            client=client,
        )
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

    result: Optional[Union[Customer, Error]] = (
        await update_payment_information_for_org.asyncio(
            client=client,
            body=BillingInfo(
                name="<string>",
                phone="<string>",
            ),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[Customer, Error]]] = (
        await update_payment_information_for_org.asyncio_detailed(
            client=client,
            body=BillingInfo(
                name="<string>",
                phone="<string>",
            ),
        )
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

    result: Optional[Union[Customer, Error]] = (
        await create_payment_information_for_org.asyncio(
            client=client,
            body=BillingInfo(
                name="<string>",
                phone="<string>",
            ),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[Customer, Error]]] = (
        await create_payment_information_for_org.asyncio_detailed(
            client=client,
            body=BillingInfo(
                name="<string>",
                phone="<string>",
            ),
        )
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
    response: Response[Optional[Error]] = (
        await delete_payment_information_for_org.asyncio_detailed(
            client=client,
        )
    )


@pytest.mark.skip
def test_get_payment_balance_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CustomerBalance, Error]] = get_payment_balance_for_org.sync(
        client=client,
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
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CustomerBalance, Error]] = (
        await get_payment_balance_for_org.asyncio(
            client=client,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[CustomerBalance, Error]]] = (
        await get_payment_balance_for_org.asyncio_detailed(
            client=client,
        )
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

    result: Optional[Union[PaymentIntent, Error]] = (
        await create_payment_intent_for_org.asyncio(
            client=client,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[PaymentIntent, Error]]] = (
        await create_payment_intent_for_org.asyncio_detailed(
            client=client,
        )
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
    response: Response[Optional[Union[List[Invoice], Error]]] = (
        await list_invoices_for_org.asyncio_detailed(
            client=client,
        )
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

    result: Optional[Union[List[PaymentMethod], Error]] = (
        await list_payment_methods_for_org.asyncio(
            client=client,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[List[PaymentMethod], Error]]] = (
        await list_payment_methods_for_org.asyncio_detailed(
            client=client,
        )
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
    response: Response[Optional[Error]] = (
        await delete_payment_method_for_org.asyncio_detailed(
            client=client,
            id="<string>",
        )
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

    result: Optional[Union[ZooProductSubscriptions, Error]] = (
        await get_org_subscription.asyncio(
            client=client,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[ZooProductSubscriptions, Error]]] = (
        await get_org_subscription.asyncio_detailed(
            client=client,
        )
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

    result: Optional[Union[ZooProductSubscriptions, Error]] = (
        await update_org_subscription.asyncio(
            client=client,
            body=ZooProductSubscriptionsOrgRequest(
                modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
            ),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[ZooProductSubscriptions, Error]]] = (
        await update_org_subscription.asyncio_detailed(
            client=client,
            body=ZooProductSubscriptionsOrgRequest(
                modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
            ),
        )
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

    result: Optional[Union[ZooProductSubscriptions, Error]] = (
        await create_org_subscription.asyncio(
            client=client,
            body=ZooProductSubscriptionsOrgRequest(
                modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
            ),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[ZooProductSubscriptions, Error]]] = (
        await create_org_subscription.asyncio_detailed(
            client=client,
            body=ZooProductSubscriptionsOrgRequest(
                modeling_app=ModelingAppOrganizationSubscriptionTier.TEAM,
            ),
        )
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
    response: Response[Optional[Error]] = (
        await validate_customer_tax_information_for_org.asyncio_detailed(
            client=client,
        )
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

    result: Optional[Union[PrivacySettings, Error]] = (
        await get_org_privacy_settings.asyncio(
            client=client,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[PrivacySettings, Error]]] = (
        await get_org_privacy_settings.asyncio_detailed(
            client=client,
        )
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

    result: Optional[Union[PrivacySettings, Error]] = (
        await update_org_privacy_settings.asyncio(
            client=client,
            body=PrivacySettings(
                can_train_on_data=False,
            ),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[PrivacySettings, Error]]] = (
        await update_org_privacy_settings.asyncio_detailed(
            client=client,
            body=PrivacySettings(
                can_train_on_data=False,
            ),
        )
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

    result: Optional[Union[SamlIdentityProvider, Error]] = (
        await get_org_saml_idp.asyncio(
            client=client,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[SamlIdentityProvider, Error]]] = (
        await get_org_saml_idp.asyncio_detailed(
            client=client,
        )
    )


@pytest.mark.skip
def test_update_org_saml_idp():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[SamlIdentityProvider, Error]] = update_org_saml_idp.sync(
        client=client,
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=base64_encoded_xml(
                data="<string>",
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
                idp_metadata_source=base64_encoded_xml(
                    data="<string>",
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

    result: Optional[Union[SamlIdentityProvider, Error]] = (
        await update_org_saml_idp.asyncio(
            client=client,
            body=SamlIdentityProviderCreate(
                idp_entity_id="<string>",
                idp_metadata_source=base64_encoded_xml(
                    data="<string>",
                ),
                technical_contact_email="<string>",
            ),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[SamlIdentityProvider, Error]]] = (
        await update_org_saml_idp.asyncio_detailed(
            client=client,
            body=SamlIdentityProviderCreate(
                idp_entity_id="<string>",
                idp_metadata_source=base64_encoded_xml(
                    data="<string>",
                ),
                technical_contact_email="<string>",
            ),
        )
    )


@pytest.mark.skip
def test_create_org_saml_idp():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[SamlIdentityProvider, Error]] = create_org_saml_idp.sync(
        client=client,
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=base64_encoded_xml(
                data="<string>",
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
                idp_metadata_source=base64_encoded_xml(
                    data="<string>",
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

    result: Optional[Union[SamlIdentityProvider, Error]] = (
        await create_org_saml_idp.asyncio(
            client=client,
            body=SamlIdentityProviderCreate(
                idp_entity_id="<string>",
                idp_metadata_source=base64_encoded_xml(
                    data="<string>",
                ),
                technical_contact_email="<string>",
            ),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[SamlIdentityProvider, Error]]] = (
        await create_org_saml_idp.asyncio_detailed(
            client=client,
            body=SamlIdentityProviderCreate(
                idp_entity_id="<string>",
                idp_metadata_source=base64_encoded_xml(
                    data="<string>",
                ),
                technical_contact_email="<string>",
            ),
        )
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

    result: Optional[Union[ServiceAccountResultsPage, Error]] = (
        await list_service_accounts_for_org.asyncio(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[ServiceAccountResultsPage, Error]]] = (
        await list_service_accounts_for_org.asyncio_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
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

    result: Optional[Union[ServiceAccount, Error]] = (
        await create_service_account_for_org.asyncio(
            client=client,
            label=None,  # Optional[str]
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[ServiceAccount, Error]]] = (
        await create_service_account_for_org.asyncio_detailed(
            client=client,
            label=None,  # Optional[str]
        )
    )


@pytest.mark.skip
def test_get_service_account_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ServiceAccount, Error]] = get_service_account_for_org.sync(
        client=client,
        token="<uuid>",
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
            token="<uuid>",
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_service_account_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ServiceAccount, Error]] = (
        await get_service_account_for_org.asyncio(
            client=client,
            token="<uuid>",
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[ServiceAccount, Error]]] = (
        await get_service_account_for_org.asyncio_detailed(
            client=client,
            token="<uuid>",
        )
    )


@pytest.mark.skip
def test_delete_service_account_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = delete_service_account_for_org.sync(
        client=client,
        token="<uuid>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = delete_service_account_for_org.sync_detailed(
        client=client,
        token="<uuid>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_service_account_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await delete_service_account_for_org.asyncio(
        client=client,
        token="<uuid>",
    )

    # OR run async with more info
    response: Response[Optional[Error]] = (
        await delete_service_account_for_org.asyncio_detailed(
            client=client,
            token="<uuid>",
        )
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
    response: Response[Optional[Union[OrgResultsPage, Error]]] = (
        await list_orgs.asyncio_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


@pytest.mark.skip
def test_get_any_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Org, Error]] = get_any_org.sync(
        client=client,
        id=Uuid("<uuid>"),
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Org = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[Org, Error]]] = get_any_org.sync_detailed(
        client=client,
        id=Uuid("<uuid>"),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_any_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Org, Error]] = await get_any_org.asyncio(
        client=client,
        id=Uuid("<uuid>"),
    )

    # OR run async with more info
    response: Response[Optional[Union[Org, Error]]] = (
        await get_any_org.asyncio_detailed(
            client=client,
            id=Uuid("<uuid>"),
        )
    )


@pytest.mark.skip
def test_update_enterprise_pricing_for_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ZooProductSubscriptions, Error]] = (
        update_enterprise_pricing_for_org.sync(
            client=client,
            id=Uuid("<uuid>"),
            body=per_user(
                interval=PlanInterval.DAY,
                price=3.14,
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
            id=Uuid("<uuid>"),
            body=per_user(
                interval=PlanInterval.DAY,
                price=3.14,
            ),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_enterprise_pricing_for_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ZooProductSubscriptions, Error]] = (
        await update_enterprise_pricing_for_org.asyncio(
            client=client,
            id=Uuid("<uuid>"),
            body=per_user(
                interval=PlanInterval.DAY,
                price=3.14,
            ),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[ZooProductSubscriptions, Error]]] = (
        await update_enterprise_pricing_for_org.asyncio_detailed(
            client=client,
            id=Uuid("<uuid>"),
            body=per_user(
                interval=PlanInterval.DAY,
                price=3.14,
            ),
        )
    )


@pytest.mark.skip
def test_get_payment_balance_for_any_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CustomerBalance, Error]] = (
        get_payment_balance_for_any_org.sync(
            client=client,
            id=Uuid("<uuid>"),
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
            id=Uuid("<uuid>"),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_any_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CustomerBalance, Error]] = (
        await get_payment_balance_for_any_org.asyncio(
            client=client,
            id=Uuid("<uuid>"),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[CustomerBalance, Error]]] = (
        await get_payment_balance_for_any_org.asyncio_detailed(
            client=client,
            id=Uuid("<uuid>"),
        )
    )


@pytest.mark.skip
def test_update_payment_balance_for_any_org():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CustomerBalance, Error]] = (
        update_payment_balance_for_any_org.sync(
            client=client,
            id=Uuid("<uuid>"),
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
            id=Uuid("<uuid>"),
            body=UpdatePaymentBalance(),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_payment_balance_for_any_org_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CustomerBalance, Error]] = (
        await update_payment_balance_for_any_org.asyncio(
            client=client,
            id=Uuid("<uuid>"),
            body=UpdatePaymentBalance(),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[CustomerBalance, Error]]] = (
        await update_payment_balance_for_any_org.asyncio_detailed(
            client=client,
            id=Uuid("<uuid>"),
            body=UpdatePaymentBalance(),
        )
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
    response: Response[Optional[Union[DiscountCode, Error]]] = (
        await create_store_coupon.asyncio_detailed(
            client=client,
            body=StoreCouponParams(
                percent_off=10,
            ),
        )
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

    result: Optional[Union[UnitAngleConversion, Error]] = (
        await get_angle_unit_conversion.asyncio(
            client=client,
            input_unit=UnitAngle.DEGREES,
            output_unit=UnitAngle.DEGREES,
            value=3.14,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[UnitAngleConversion, Error]]] = (
        await get_angle_unit_conversion.asyncio_detailed(
            client=client,
            input_unit=UnitAngle.DEGREES,
            output_unit=UnitAngle.DEGREES,
            value=3.14,
        )
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

    result: Optional[Union[UnitAreaConversion, Error]] = (
        await get_area_unit_conversion.asyncio(
            client=client,
            input_unit=UnitArea.CM2,
            output_unit=UnitArea.CM2,
            value=3.14,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[UnitAreaConversion, Error]]] = (
        await get_area_unit_conversion.asyncio_detailed(
            client=client,
            input_unit=UnitArea.CM2,
            output_unit=UnitArea.CM2,
            value=3.14,
        )
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

    result: Optional[Union[UnitCurrentConversion, Error]] = (
        await get_current_unit_conversion.asyncio(
            client=client,
            input_unit=UnitCurrent.AMPERES,
            output_unit=UnitCurrent.AMPERES,
            value=3.14,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[UnitCurrentConversion, Error]]] = (
        await get_current_unit_conversion.asyncio_detailed(
            client=client,
            input_unit=UnitCurrent.AMPERES,
            output_unit=UnitCurrent.AMPERES,
            value=3.14,
        )
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

    result: Optional[Union[UnitEnergyConversion, Error]] = (
        await get_energy_unit_conversion.asyncio(
            client=client,
            input_unit=UnitEnergy.BTU,
            output_unit=UnitEnergy.BTU,
            value=3.14,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[UnitEnergyConversion, Error]]] = (
        await get_energy_unit_conversion.asyncio_detailed(
            client=client,
            input_unit=UnitEnergy.BTU,
            output_unit=UnitEnergy.BTU,
            value=3.14,
        )
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

    result: Optional[Union[UnitForceConversion, Error]] = (
        await get_force_unit_conversion.asyncio(
            client=client,
            input_unit=UnitForce.DYNES,
            output_unit=UnitForce.DYNES,
            value=3.14,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[UnitForceConversion, Error]]] = (
        await get_force_unit_conversion.asyncio_detailed(
            client=client,
            input_unit=UnitForce.DYNES,
            output_unit=UnitForce.DYNES,
            value=3.14,
        )
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

    result: Optional[Union[UnitFrequencyConversion, Error]] = (
        await get_frequency_unit_conversion.asyncio(
            client=client,
            input_unit=UnitFrequency.GIGAHERTZ,
            output_unit=UnitFrequency.GIGAHERTZ,
            value=3.14,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[UnitFrequencyConversion, Error]]] = (
        await get_frequency_unit_conversion.asyncio_detailed(
            client=client,
            input_unit=UnitFrequency.GIGAHERTZ,
            output_unit=UnitFrequency.GIGAHERTZ,
            value=3.14,
        )
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

    result: Optional[Union[UnitLengthConversion, Error]] = (
        await get_length_unit_conversion.asyncio(
            client=client,
            input_unit=UnitLength.CM,
            output_unit=UnitLength.CM,
            value=3.14,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[UnitLengthConversion, Error]]] = (
        await get_length_unit_conversion.asyncio_detailed(
            client=client,
            input_unit=UnitLength.CM,
            output_unit=UnitLength.CM,
            value=3.14,
        )
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

    result: Optional[Union[UnitMassConversion, Error]] = (
        await get_mass_unit_conversion.asyncio(
            client=client,
            input_unit=UnitMass.G,
            output_unit=UnitMass.G,
            value=3.14,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[UnitMassConversion, Error]]] = (
        await get_mass_unit_conversion.asyncio_detailed(
            client=client,
            input_unit=UnitMass.G,
            output_unit=UnitMass.G,
            value=3.14,
        )
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

    result: Optional[Union[UnitPowerConversion, Error]] = (
        await get_power_unit_conversion.asyncio(
            client=client,
            input_unit=UnitPower.BTU_PER_MINUTE,
            output_unit=UnitPower.BTU_PER_MINUTE,
            value=3.14,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[UnitPowerConversion, Error]]] = (
        await get_power_unit_conversion.asyncio_detailed(
            client=client,
            input_unit=UnitPower.BTU_PER_MINUTE,
            output_unit=UnitPower.BTU_PER_MINUTE,
            value=3.14,
        )
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

    result: Optional[Union[UnitPressureConversion, Error]] = (
        await get_pressure_unit_conversion.asyncio(
            client=client,
            input_unit=UnitPressure.ATMOSPHERES,
            output_unit=UnitPressure.ATMOSPHERES,
            value=3.14,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[UnitPressureConversion, Error]]] = (
        await get_pressure_unit_conversion.asyncio_detailed(
            client=client,
            input_unit=UnitPressure.ATMOSPHERES,
            output_unit=UnitPressure.ATMOSPHERES,
            value=3.14,
        )
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

    result: Optional[Union[UnitTemperatureConversion, Error]] = (
        await get_temperature_unit_conversion.asyncio(
            client=client,
            input_unit=UnitTemperature.CELSIUS,
            output_unit=UnitTemperature.CELSIUS,
            value=3.14,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[UnitTemperatureConversion, Error]]] = (
        await get_temperature_unit_conversion.asyncio_detailed(
            client=client,
            input_unit=UnitTemperature.CELSIUS,
            output_unit=UnitTemperature.CELSIUS,
            value=3.14,
        )
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

    result: Optional[Union[UnitTorqueConversion, Error]] = (
        await get_torque_unit_conversion.asyncio(
            client=client,
            input_unit=UnitTorque.NEWTON_METRES,
            output_unit=UnitTorque.NEWTON_METRES,
            value=3.14,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[UnitTorqueConversion, Error]]] = (
        await get_torque_unit_conversion.asyncio_detailed(
            client=client,
            input_unit=UnitTorque.NEWTON_METRES,
            output_unit=UnitTorque.NEWTON_METRES,
            value=3.14,
        )
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

    result: Optional[Union[UnitVolumeConversion, Error]] = (
        await get_volume_unit_conversion.asyncio(
            client=client,
            input_unit=UnitVolume.CM3,
            output_unit=UnitVolume.CM3,
            value=3.14,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[UnitVolumeConversion, Error]]] = (
        await get_volume_unit_conversion.asyncio_detailed(
            client=client,
            input_unit=UnitVolume.CM3,
            output_unit=UnitVolume.CM3,
            value=3.14,
        )
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
    response: Response[Optional[Union[User, Error]]] = (
        await get_user_self.asyncio_detailed(
            client=client,
        )
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
    response: Response[Optional[Union[User, Error]]] = (
        await update_user_self.asyncio_detailed(
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

    result: Optional[Union[ApiCallWithPriceResultsPage, Error]] = (
        await user_list_api_calls.asyncio(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[ApiCallWithPriceResultsPage, Error]]] = (
        await user_list_api_calls.asyncio_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


@pytest.mark.skip
def test_get_api_call_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiCallWithPrice, Error]] = get_api_call_for_user.sync(
        client=client,
        id="<uuid>",
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
            id="<uuid>",
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiCallWithPrice, Error]] = (
        await get_api_call_for_user.asyncio(
            client=client,
            id="<uuid>",
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[ApiCallWithPrice, Error]]] = (
        await get_api_call_for_user.asyncio_detailed(
            client=client,
            id="<uuid>",
        )
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

    result: Optional[Union[ApiTokenResultsPage, Error]] = (
        await list_api_tokens_for_user.asyncio(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[ApiTokenResultsPage, Error]]] = (
        await list_api_tokens_for_user.asyncio_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
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
    response: Response[Optional[Union[ApiToken, Error]]] = (
        await create_api_token_for_user.asyncio_detailed(
            client=client,
            label=None,  # Optional[str]
        )
    )


@pytest.mark.skip
def test_get_api_token_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiToken, Error]] = get_api_token_for_user.sync(
        client=client,
        token="<uuid>",
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
            token="<uuid>",
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
        token="<uuid>",
    )

    # OR run async with more info
    response: Response[Optional[Union[ApiToken, Error]]] = (
        await get_api_token_for_user.asyncio_detailed(
            client=client,
            token="<uuid>",
        )
    )


@pytest.mark.skip
def test_delete_api_token_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = delete_api_token_for_user.sync(
        client=client,
        token="<uuid>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Error = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Error]] = delete_api_token_for_user.sync_detailed(
        client=client,
        token="<uuid>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_api_token_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = await delete_api_token_for_user.asyncio(
        client=client,
        token="<uuid>",
    )

    # OR run async with more info
    response: Response[Optional[Error]] = (
        await delete_api_token_for_user.asyncio_detailed(
            client=client,
            token="<uuid>",
        )
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
    response: Response[Optional[Union[ExtendedUser, Error]]] = (
        await get_user_self_extended.asyncio_detailed(
            client=client,
        )
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

    result: Optional[Union[List[AccountProvider], Error]] = (
        await get_oauth2_providers_for_user.asyncio(
            client=client,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[List[AccountProvider], Error]]] = (
        await get_oauth2_providers_for_user.asyncio_detailed(
            client=client,
        )
    )


@pytest.mark.skip
def test_get_user_onboarding_self():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Onboarding, Error]] = get_user_onboarding_self.sync(
        client=client,
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: Onboarding = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[Onboarding, Error]]] = (
        get_user_onboarding_self.sync_detailed(
            client=client,
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_onboarding_self_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Onboarding, Error]] = await get_user_onboarding_self.asyncio(
        client=client,
    )

    # OR run async with more info
    response: Response[Optional[Union[Onboarding, Error]]] = (
        await get_user_onboarding_self.asyncio_detailed(
            client=client,
        )
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
    response: Response[Optional[Union[UserOrgInfo, Error]]] = (
        await get_user_org.asyncio_detailed(
            client=client,
        )
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

    result: Optional[Union[Customer, Error]] = (
        await get_payment_information_for_user.asyncio(
            client=client,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[Customer, Error]]] = (
        await get_payment_information_for_user.asyncio_detailed(
            client=client,
        )
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

    result: Optional[Union[Customer, Error]] = (
        await update_payment_information_for_user.asyncio(
            client=client,
            body=BillingInfo(
                name="<string>",
                phone="<string>",
            ),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[Customer, Error]]] = (
        await update_payment_information_for_user.asyncio_detailed(
            client=client,
            body=BillingInfo(
                name="<string>",
                phone="<string>",
            ),
        )
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

    result: Optional[Union[Customer, Error]] = (
        await create_payment_information_for_user.asyncio(
            client=client,
            body=BillingInfo(
                name="<string>",
                phone="<string>",
            ),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[Customer, Error]]] = (
        await create_payment_information_for_user.asyncio_detailed(
            client=client,
            body=BillingInfo(
                name="<string>",
                phone="<string>",
            ),
        )
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
    response: Response[Optional[Error]] = (
        await delete_payment_information_for_user.asyncio_detailed(
            client=client,
        )
    )


@pytest.mark.skip
def test_get_payment_balance_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CustomerBalance, Error]] = get_payment_balance_for_user.sync(
        client=client,
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
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CustomerBalance, Error]] = (
        await get_payment_balance_for_user.asyncio(
            client=client,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[CustomerBalance, Error]]] = (
        await get_payment_balance_for_user.asyncio_detailed(
            client=client,
        )
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

    result: Optional[Union[PaymentIntent, Error]] = (
        await create_payment_intent_for_user.asyncio(
            client=client,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[PaymentIntent, Error]]] = (
        await create_payment_intent_for_user.asyncio_detailed(
            client=client,
        )
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

    result: Optional[Union[List[Invoice], Error]] = (
        await list_invoices_for_user.asyncio(
            client=client,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[List[Invoice], Error]]] = (
        await list_invoices_for_user.asyncio_detailed(
            client=client,
        )
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

    result: Optional[Union[List[PaymentMethod], Error]] = (
        await list_payment_methods_for_user.asyncio(
            client=client,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[List[PaymentMethod], Error]]] = (
        await list_payment_methods_for_user.asyncio_detailed(
            client=client,
        )
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
    response: Response[Optional[Error]] = (
        await delete_payment_method_for_user.asyncio_detailed(
            client=client,
            id="<string>",
        )
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

    result: Optional[Union[ZooProductSubscriptions, Error]] = (
        await get_user_subscription.asyncio(
            client=client,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[ZooProductSubscriptions, Error]]] = (
        await get_user_subscription.asyncio_detailed(
            client=client,
        )
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

    result: Optional[Union[ZooProductSubscriptions, Error]] = (
        await update_user_subscription.asyncio(
            client=client,
            body=ZooProductSubscriptionsUserRequest(
                modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
            ),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[ZooProductSubscriptions, Error]]] = (
        await update_user_subscription.asyncio_detailed(
            client=client,
            body=ZooProductSubscriptionsUserRequest(
                modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
            ),
        )
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

    result: Optional[Union[ZooProductSubscriptions, Error]] = (
        await create_user_subscription.asyncio(
            client=client,
            body=ZooProductSubscriptionsUserRequest(
                modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
            ),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[ZooProductSubscriptions, Error]]] = (
        await create_user_subscription.asyncio_detailed(
            client=client,
            body=ZooProductSubscriptionsUserRequest(
                modeling_app=ModelingAppIndividualSubscriptionTier.FREE,
            ),
        )
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
    response: Response[Optional[Error]] = (
        await validate_customer_tax_information_for_user.asyncio_detailed(
            client=client,
        )
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

    result: Optional[Union[PrivacySettings, Error]] = (
        await get_user_privacy_settings.asyncio(
            client=client,
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[PrivacySettings, Error]]] = (
        await get_user_privacy_settings.asyncio_detailed(
            client=client,
        )
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

    result: Optional[Union[PrivacySettings, Error]] = (
        await update_user_privacy_settings.asyncio(
            client=client,
            body=PrivacySettings(
                can_train_on_data=False,
            ),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[PrivacySettings, Error]]] = (
        await update_user_privacy_settings.asyncio_detailed(
            client=client,
            body=PrivacySettings(
                can_train_on_data=False,
            ),
        )
    )


@pytest.mark.skip
def test_get_session_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[Session, Error]] = get_session_for_user.sync(
        client=client,
        token="<uuid>",
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
            token="<uuid>",
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
        token="<uuid>",
    )

    # OR run async with more info
    response: Response[Optional[Union[Session, Error]]] = (
        await get_session_for_user.asyncio_detailed(
            client=client,
            token="<uuid>",
        )
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

    result: Optional[Union[TextToCadResultsPage, Error]] = (
        await list_text_to_cad_models_for_user.asyncio(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
            no_models=None,  # Optional[bool]
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[TextToCadResultsPage, Error]]] = (
        await list_text_to_cad_models_for_user.asyncio_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
            no_models=None,  # Optional[bool]
        )
    )


@pytest.mark.skip
def test_get_text_to_cad_model_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[TextToCad, Error]] = get_text_to_cad_model_for_user.sync(
        client=client,
        id="<uuid>",
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
            id="<uuid>",
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_text_to_cad_model_for_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[TextToCad, Error]] = (
        await get_text_to_cad_model_for_user.asyncio(
            client=client,
            id="<uuid>",
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[TextToCad, Error]]] = (
        await get_text_to_cad_model_for_user.asyncio_detailed(
            client=client,
            id="<uuid>",
        )
    )


@pytest.mark.skip
def test_create_text_to_cad_model_feedback():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Error] = create_text_to_cad_model_feedback.sync(
        client=client,
        id="<uuid>",
        feedback=AiFeedback.THUMBS_UP,
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
            id="<uuid>",
            feedback=AiFeedback.THUMBS_UP,
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
        id="<uuid>",
        feedback=AiFeedback.THUMBS_UP,
    )

    # OR run async with more info
    response: Response[Optional[Error]] = (
        await create_text_to_cad_model_feedback.asyncio_detailed(
            client=client,
            id="<uuid>",
            feedback=AiFeedback.THUMBS_UP,
        )
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
    response: Response[Optional[Union[UserResultsPage, Error]]] = (
        await list_users.asyncio_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
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

    result: Optional[Union[ExtendedUserResultsPage, Error]] = (
        await list_users_extended.asyncio(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[ExtendedUserResultsPage, Error]]] = (
        await list_users_extended.asyncio_detailed(
            client=client,
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


@pytest.mark.skip
def test_get_user_extended():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ExtendedUser, Error]] = get_user_extended.sync(
        client=client,
        id="<string>",
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
            id="<string>",
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
        id="<string>",
    )

    # OR run async with more info
    response: Response[Optional[Union[ExtendedUser, Error]]] = (
        await get_user_extended.asyncio_detailed(
            client=client,
            id="<string>",
        )
    )


@pytest.mark.skip
def test_get_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[User, Error]] = get_user.sync(
        client=client,
        id="<string>",
    )

    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    body: User = result
    print(body)

    # OR if you need more info (e.g. status_code)
    response: Response[Optional[Union[User, Error]]] = get_user.sync_detailed(
        client=client,
        id="<string>",
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[User, Error]] = await get_user.asyncio(
        client=client,
        id="<string>",
    )

    # OR run async with more info
    response: Response[Optional[Union[User, Error]]] = await get_user.asyncio_detailed(
        client=client,
        id="<string>",
    )


@pytest.mark.skip
def test_list_api_calls_for_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[ApiCallWithPriceResultsPage, Error]] = (
        list_api_calls_for_user.sync(
            client=client,
            id="<string>",
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
            id="<string>",
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

    result: Optional[Union[ApiCallWithPriceResultsPage, Error]] = (
        await list_api_calls_for_user.asyncio(
            client=client,
            id="<string>",
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[ApiCallWithPriceResultsPage, Error]]] = (
        await list_api_calls_for_user.asyncio_detailed(
            client=client,
            id="<string>",
            sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
            limit=None,  # Optional[int]
            page_token=None,  # Optional[str]
        )
    )


@pytest.mark.skip
def test_get_payment_balance_for_any_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CustomerBalance, Error]] = (
        get_payment_balance_for_any_user.sync(
            client=client,
            id=Uuid("<uuid>"),
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
            id=Uuid("<uuid>"),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_any_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CustomerBalance, Error]] = (
        await get_payment_balance_for_any_user.asyncio(
            client=client,
            id=Uuid("<uuid>"),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[CustomerBalance, Error]]] = (
        await get_payment_balance_for_any_user.asyncio_detailed(
            client=client,
            id=Uuid("<uuid>"),
        )
    )


@pytest.mark.skip
def test_update_payment_balance_for_any_user():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CustomerBalance, Error]] = (
        update_payment_balance_for_any_user.sync(
            client=client,
            id=Uuid("<uuid>"),
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
            id=Uuid("<uuid>"),
            body=UpdatePaymentBalance(),
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_payment_balance_for_any_user_async():
    # Create our client.
    client = ClientFromEnv()

    result: Optional[Union[CustomerBalance, Error]] = (
        await update_payment_balance_for_any_user.asyncio(
            client=client,
            id=Uuid("<uuid>"),
            body=UpdatePaymentBalance(),
        )
    )

    # OR run async with more info
    response: Response[Optional[Union[CustomerBalance, Error]]] = (
        await update_payment_balance_for_any_user.asyncio_detailed(
            client=client,
            id=Uuid("<uuid>"),
            body=UpdatePaymentBalance(),
        )
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
        pool=None,  # Optional[str]
    ) as websocket:

        # Send a message.
        websocket.send(
            WebSocketRequest(
                sdp_offer(
                    offer=RtcSessionDescription(
                        sdp="<string>",
                        type=RtcSdpType.UNSPECIFIED,
                    ),
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
        pool=None,  # Optional[str]
    )

    # Send a message.
    await websocket.send("{}")

    # Get the messages.
    async for message in websocket:
        print(message)
