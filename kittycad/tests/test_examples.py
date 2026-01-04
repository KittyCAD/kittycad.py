import datetime
from pathlib import Path
from typing import Dict, List

import pytest

from kittycad import AsyncKittyCAD, KittyCAD
from kittycad.models import (
    AccountProvider,
    ApiCallQueryGroup,
    ApiCallWithPrice,
    ApiToken,
    AppClientInfo,
    AsyncApiCall,
    AsyncApiCallOutput,
    AuthApiKeyResponse,
    CodeOutput,
    Conversation,
    CreateShortlinkResponse,
    Customer,
    CustomerBalance,
    CustomModel,
    DatasetS3Policies,
    DiscountCode,
    ExtendedUser,
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
    Org,
    OrgAdminDetails,
    OrgDataset,
    OrgDatasetConversionStatsResponse,
    OrgDatasetFileConversion,
    OrgDatasetFileConversionDetails,
    OrgDatasetFileConversionSummary,
    OrgMember,
    PaymentIntent,
    PaymentMethod,
    Pong,
    SamlIdentityProvider,
    ServiceAccount,
    Session,
    Shortlink,
    SubscriptionPlanPriceRecord,
    TextToCad,
    TextToCadIteration,
    TextToCadMultiFileIteration,
    TextToCadResponse,
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
    UserAdminDetails,
    UserFeatureList,
    UserOrgInfo,
    VerificationTokenResponse,
    WebSocketRequest,
    ZooProductSubscriptions,
)
from kittycad.models.add_org_member import AddOrgMember
from kittycad.models.api_call_query_group_by import ApiCallQueryGroupBy
from kittycad.models.api_call_status import ApiCallStatus
from kittycad.models.api_token_uuid import ApiTokenUuid
from kittycad.models.base64data import Base64Data
from kittycad.models.billing_info import BillingInfo
from kittycad.models.code_language import CodeLanguage
from kittycad.models.code_option import CodeOption
from kittycad.models.conversion_params import ConversionParams
from kittycad.models.conversion_sort_mode import ConversionSortMode
from kittycad.models.create_custom_model import CreateCustomModel
from kittycad.models.create_org_dataset import CreateOrgDataset
from kittycad.models.create_shortlink_request import CreateShortlinkRequest
from kittycad.models.created_at_sort_mode import CreatedAtSortMode
from kittycad.models.crm_data import CrmData
from kittycad.models.email_authentication_form import EmailAuthenticationForm
from kittycad.models.event import Event, OptionModelingAppEvent
from kittycad.models.fbx_storage import FbxStorage
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
from kittycad.models.ml_copilot_client_message import OptionHeaders, OptionUser
from kittycad.models.ml_copilot_tool import MlCopilotTool
from kittycad.models.ml_feedback import MlFeedback
from kittycad.models.modeling_app_event_type import ModelingAppEventType
from kittycad.models.org_dataset_source import OrgDatasetSource
from kittycad.models.org_details import OrgDetails
from kittycad.models.output_format3d import OptionFbx, OutputFormat3d
from kittycad.models.plan_interval import PlanInterval
from kittycad.models.post_effect_type import PostEffectType
from kittycad.models.price_upsert_request import PriceUpsertRequest
from kittycad.models.privacy_settings import PrivacySettings
from kittycad.models.rtc_ice_candidate_init import RtcIceCandidateInit
from kittycad.models.saml_identity_provider_create import SamlIdentityProviderCreate
from kittycad.models.service_account_uuid import ServiceAccountUuid
from kittycad.models.session_uuid import SessionUuid
from kittycad.models.source_position import SourcePosition
from kittycad.models.source_range import SourceRange
from kittycad.models.source_range_prompt import SourceRangePrompt
from kittycad.models.storage_provider import StorageProvider
from kittycad.models.store_coupon_params import StoreCouponParams
from kittycad.models.subscribe import Subscribe
from kittycad.models.subscription_plan_billing_model import SubscriptionPlanBillingModel
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
from kittycad.models.update_custom_model import UpdateCustomModel
from kittycad.models.update_member_to_org_body import UpdateMemberToOrgBody
from kittycad.models.update_org_dataset import UpdateOrgDataset
from kittycad.models.update_payment_balance import UpdatePaymentBalance
from kittycad.models.update_shortlink_request import UpdateShortlinkRequest
from kittycad.models.update_user import UpdateUser
from kittycad.models.user_identifier import UserIdentifier
from kittycad.models.user_org_role import UserOrgRole
from kittycad.models.uuid import Uuid
from kittycad.models.web_socket_request import OptionTrickleIce
from kittycad.models.zoo_product_subscriptions_org_request import (
    ZooProductSubscriptionsOrgRequest,
)
from kittycad.models.zoo_product_subscriptions_user_request import (
    ZooProductSubscriptionsUserRequest,
)


@pytest.mark.skip
def test_get_schema():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result = client.meta.get_schema()

    print(result)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_schema_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result = await client.meta.get_schema()


@pytest.mark.skip
def test_get_ipinfo():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: IpAddrInfo = client.meta.get_ipinfo()

    body: IpAddrInfo = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_ipinfo_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: IpAddrInfo = await client.meta.get_ipinfo()


@pytest.mark.skip
def test_create_text_to_cad():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: TextToCad = client.ml.create_text_to_cad(
        output_format=FileExportFormat.FBX,
        kcl=None,
        body=TextToCadCreateBody(
            prompt="<string>",
        ),
    )

    body: TextToCad = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_text_to_cad_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: TextToCad = await client.ml.create_text_to_cad(
        output_format=FileExportFormat.FBX,
        kcl=None,
        body=TextToCadCreateBody(
            prompt="<string>",
        ),
    )


@pytest.mark.skip
def test_get_api_call_metrics():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[ApiCallQueryGroup] = client.api_calls.get_api_call_metrics(
        group_by=ApiCallQueryGroupBy.EMAIL
    )

    body: List[ApiCallQueryGroup] = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_metrics_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[ApiCallQueryGroup] = await client.api_calls.get_api_call_metrics(
        group_by=ApiCallQueryGroupBy.EMAIL
    )


@pytest.mark.skip
def test_list_api_calls():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    item: ApiCallWithPrice
    for item in client.api_calls.list_api_calls(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    ):
        print(item)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_api_calls_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    iterator = client.api_calls.list_api_calls(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )
    item: ApiCallWithPrice
    async for item in iterator:
        print(item)


@pytest.mark.skip
def test_get_api_call():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPrice = client.api_calls.get_api_call(id="<string>")

    body: ApiCallWithPrice = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPrice = await client.api_calls.get_api_call(id="<string>")


@pytest.mark.skip
def test_apps_github_callback():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.apps.apps_github_callback()


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_apps_github_callback_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.apps.apps_github_callback()


@pytest.mark.skip
def test_apps_github_consent():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: AppClientInfo = client.apps.apps_github_consent()

    body: AppClientInfo = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_apps_github_consent_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: AppClientInfo = await client.apps.apps_github_consent()


@pytest.mark.skip
def test_apps_github_webhook():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.apps.apps_github_webhook(body=bytes("some bytes", "utf-8"))


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_apps_github_webhook_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.apps.apps_github_webhook(body=bytes("some bytes", "utf-8"))


@pytest.mark.skip
def test_list_async_operations():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    item: AsyncApiCall
    for item in client.api_calls.list_async_operations(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        status=ApiCallStatus.QUEUED,
        limit=None,
        page_token=None,
    ):
        print(item)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_async_operations_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    iterator = client.api_calls.list_async_operations(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        status=ApiCallStatus.QUEUED,
        limit=None,
        page_token=None,
    )
    item: AsyncApiCall
    async for item in iterator:
        print(item)


@pytest.mark.skip
def test_get_async_operation():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: AsyncApiCallOutput = client.api_calls.get_async_operation(id="<string>")

    body: AsyncApiCallOutput = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_async_operation_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: AsyncApiCallOutput = await client.api_calls.get_async_operation(
        id="<string>"
    )


@pytest.mark.skip
def test_auth_api_key():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: AuthApiKeyResponse = client.hidden.auth_api_key()

    body: AuthApiKeyResponse = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_auth_api_key_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: AuthApiKeyResponse = await client.hidden.auth_api_key()


@pytest.mark.skip
def test_auth_email():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: VerificationTokenResponse = client.hidden.auth_email(
        body=EmailAuthenticationForm(
            email="<string>",
        )
    )

    body: VerificationTokenResponse = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_auth_email_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: VerificationTokenResponse = await client.hidden.auth_email(
        body=EmailAuthenticationForm(
            email="<string>",
        )
    )


@pytest.mark.skip
def test_auth_email_callback():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.hidden.auth_email_callback(
        email="<string>", token="<string>", callback_url=None
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_auth_email_callback_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.hidden.auth_email_callback(
        email="<string>", token="<string>", callback_url=None
    )


@pytest.mark.skip
def test_get_auth_saml_by_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.hidden.get_auth_saml_by_org(org_id=Uuid("<string>"), callback_url=None)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_auth_saml_by_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.hidden.get_auth_saml_by_org(org_id=Uuid("<string>"), callback_url=None)


@pytest.mark.skip
def test_get_auth_saml():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.hidden.get_auth_saml(provider_id=Uuid("<string>"), callback_url=None)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_auth_saml_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.hidden.get_auth_saml(provider_id=Uuid("<string>"), callback_url=None)


@pytest.mark.skip
def test_post_auth_saml():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.hidden.post_auth_saml(
        provider_id=Uuid("<string>"), body=bytes("some bytes", "utf-8")
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_post_auth_saml_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.hidden.post_auth_saml(
        provider_id=Uuid("<string>"), body=bytes("some bytes", "utf-8")
    )


@pytest.mark.skip
def test_community_sso():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.meta.community_sso(sig="<string>", sso="<string>")


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_community_sso_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.meta.community_sso(sig="<string>", sso="<string>")


@pytest.mark.skip
def test_create_debug_uploads():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[str] = client.meta.create_debug_uploads()

    body: List[str] = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_debug_uploads_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[str] = await client.meta.create_debug_uploads()


@pytest.mark.skip
def test_create_event():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.meta.create_event(
        body=Event(
            OptionModelingAppEvent(
                created_at=datetime.datetime.now(),
                event_type=ModelingAppEventType.SUCCESSFUL_COMPILE_BEFORE_CLOSE,
                project_name="<string>",
                source_id="<string>",
                user_id="<string>",
            )
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_event_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.meta.create_event(
        body=Event(
            OptionModelingAppEvent(
                created_at=datetime.datetime.now(),
                event_type=ModelingAppEventType.SUCCESSFUL_COMPILE_BEFORE_CLOSE,
                project_name="<string>",
                source_id="<string>",
                user_id="<string>",
            )
        )
    )


@pytest.mark.skip
def test_create_file_center_of_mass():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileCenterOfMass = client.file.create_file_center_of_mass(
        output_unit=UnitLength.CM,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    body: FileCenterOfMass = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_center_of_mass_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileCenterOfMass = await client.file.create_file_center_of_mass(
        output_unit=UnitLength.CM,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_conversion_options():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileConversion = client.file.create_file_conversion_options(
        body=ConversionParams(
            output_format=OutputFormat3d(
                OptionFbx(
                    storage=FbxStorage.ASCII,
                )
            ),
            src_format=InputFormat3d(
                OptionSldprt(
                    split_closed_faces=False,
                )
            ),
        ),
        file_attachments={
            "main.kcl": Path("path/to/main.kcl"),
            "helper.kcl": Path("path/to/helper.kcl"),
        },
    )

    body: FileConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_conversion_options_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileConversion = await client.file.create_file_conversion_options(
        body=ConversionParams(
            output_format=OutputFormat3d(
                OptionFbx(
                    storage=FbxStorage.ASCII,
                )
            ),
            src_format=InputFormat3d(
                OptionSldprt(
                    split_closed_faces=False,
                )
            ),
        ),
        file_attachments={
            "main.kcl": Path("path/to/main.kcl"),
            "helper.kcl": Path("path/to/helper.kcl"),
        },
    )


@pytest.mark.skip
def test_create_file_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileConversion = client.file.create_file_conversion(
        output_format=FileExportFormat.FBX,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    body: FileConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_conversion_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileConversion = await client.file.create_file_conversion(
        output_format=FileExportFormat.FBX,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_density():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileDensity = client.file.create_file_density(
        material_mass=3.14,
        material_mass_unit=UnitMass.G,
        output_unit=UnitDensity.LB_FT3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    body: FileDensity = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_density_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileDensity = await client.file.create_file_density(
        material_mass=3.14,
        material_mass_unit=UnitMass.G,
        output_unit=UnitDensity.LB_FT3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_execution():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CodeOutput = client.executor.create_file_execution(
        lang=CodeLanguage.GO, output=None, body=bytes("some bytes", "utf-8")
    )

    body: CodeOutput = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_execution_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CodeOutput = await client.executor.create_file_execution(
        lang=CodeLanguage.GO, output=None, body=bytes("some bytes", "utf-8")
    )


@pytest.mark.skip
def test_create_file_mass():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileMass = client.file.create_file_mass(
        material_density=3.14,
        material_density_unit=UnitDensity.LB_FT3,
        output_unit=UnitMass.G,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    body: FileMass = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_mass_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileMass = await client.file.create_file_mass(
        material_density=3.14,
        material_density_unit=UnitDensity.LB_FT3,
        output_unit=UnitMass.G,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_surface_area():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileSurfaceArea = client.file.create_file_surface_area(
        output_unit=UnitArea.CM2,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    body: FileSurfaceArea = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_surface_area_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileSurfaceArea = await client.file.create_file_surface_area(
        output_unit=UnitArea.CM2,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_create_file_volume():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileVolume = client.file.create_file_volume(
        output_unit=UnitVolume.CM3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )

    body: FileVolume = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_file_volume_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: FileVolume = await client.file.create_file_volume(
        output_unit=UnitVolume.CM3,
        src_format=FileImportFormat.FBX,
        body=bytes("some bytes", "utf-8"),
    )


@pytest.mark.skip
def test_internal_get_api_token_for_discord_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiToken = client.meta.internal_get_api_token_for_discord_user(
        discord_id="<string>"
    )

    body: ApiToken = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_internal_get_api_token_for_discord_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiToken = await client.meta.internal_get_api_token_for_discord_user(
        discord_id="<string>"
    )


@pytest.mark.skip
def test_logout():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.hidden.logout()


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_logout_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.hidden.logout()


@pytest.mark.skip
def test_list_ml_prompts():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    item: MlPrompt
    for item in client.ml.list_ml_prompts(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    ):
        print(item)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_ml_prompts_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    iterator = client.ml.list_ml_prompts(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )
    item: MlPrompt
    async for item in iterator:
        print(item)


@pytest.mark.skip
def test_get_ml_prompt():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: MlPrompt = client.ml.get_ml_prompt(id="<string>")

    body: MlPrompt = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_ml_prompt_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: MlPrompt = await client.ml.get_ml_prompt(id="<string>")


@pytest.mark.skip
def test_list_conversations_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    item: Conversation
    for item in client.ml.list_conversations_for_user(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    ):
        print(item)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_conversations_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    iterator = client.ml.list_conversations_for_user(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )
    item: Conversation
    async for item in iterator:
        print(item)


@pytest.mark.skip
def test_create_proprietary_to_kcl():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: KclModel = client.ml.create_proprietary_to_kcl(code_option=CodeOption.PARSE)

    body: KclModel = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_proprietary_to_kcl_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: KclModel = await client.ml.create_proprietary_to_kcl(
        code_option=CodeOption.PARSE
    )


@pytest.mark.skip
def test_create_custom_model():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomModel = client.ml.create_custom_model(
        body=CreateCustomModel(
            dataset_ids=[Uuid("<string>")],
            name="<string>",
        )
    )

    body: CustomModel = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_custom_model_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomModel = await client.ml.create_custom_model(
        body=CreateCustomModel(
            dataset_ids=[Uuid("<string>")],
            name="<string>",
        )
    )


@pytest.mark.skip
def test_get_custom_model():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomModel = client.ml.get_custom_model(id=Uuid("<string>"))

    body: CustomModel = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_custom_model_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomModel = await client.ml.get_custom_model(id=Uuid("<string>"))


@pytest.mark.skip
def test_update_custom_model():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomModel = client.ml.update_custom_model(
        id=Uuid("<string>"), body=UpdateCustomModel()
    )

    body: CustomModel = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_custom_model_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomModel = await client.ml.update_custom_model(
        id=Uuid("<string>"), body=UpdateCustomModel()
    )


@pytest.mark.skip
def test_list_org_datasets_for_model():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[OrgDataset] = client.ml.list_org_datasets_for_model(
        id=Uuid("<string>")
    )

    body: List[OrgDataset] = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_org_datasets_for_model_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[OrgDataset] = await client.ml.list_org_datasets_for_model(
        id=Uuid("<string>")
    )


@pytest.mark.skip
def test_create_kcl_code_completions():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: KclCodeCompletionResponse = client.ml.create_kcl_code_completions(
        body=KclCodeCompletionRequest(
            extra=KclCodeCompletionParams(
                language="<string>",
                trim_by_indentation=False,
            ),
            prompt="<string>",
            stop=["<string>"],
            stream=False,
            suffix="<string>",
        )
    )

    body: KclCodeCompletionResponse = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_kcl_code_completions_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: KclCodeCompletionResponse = await client.ml.create_kcl_code_completions(
        body=KclCodeCompletionRequest(
            extra=KclCodeCompletionParams(
                language="<string>",
                trim_by_indentation=False,
            ),
            prompt="<string>",
            stop=["<string>"],
            stream=False,
            suffix="<string>",
        )
    )


@pytest.mark.skip
def test_create_text_to_cad_iteration():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: TextToCadIteration = client.ml.create_text_to_cad_iteration(
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
        )
    )

    body: TextToCadIteration = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_text_to_cad_iteration_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: TextToCadIteration = await client.ml.create_text_to_cad_iteration(
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
        )
    )


@pytest.mark.skip
def test_create_text_to_cad_multi_file_iteration():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: TextToCadMultiFileIteration = (
        client.ml.create_text_to_cad_multi_file_iteration(
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
            file_attachments={
                "main.kcl": Path("path/to/main.kcl"),
                "helper.kcl": Path("path/to/helper.kcl"),
            },
        )
    )

    body: TextToCadMultiFileIteration = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_text_to_cad_multi_file_iteration_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: TextToCadMultiFileIteration = (
        await client.ml.create_text_to_cad_multi_file_iteration(
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
            file_attachments={
                "main.kcl": Path("path/to/main.kcl"),
                "helper.kcl": Path("path/to/helper.kcl"),
            },
        )
    )


@pytest.mark.skip
def test_delete_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.orgs.delete_org()


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.orgs.delete_org()


@pytest.mark.skip
def test_get_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Org = client.orgs.get_org()

    body: Org = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Org = await client.orgs.get_org()


@pytest.mark.skip
def test_create_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Org = client.orgs.create_org(
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        )
    )

    body: Org = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Org = await client.orgs.create_org(
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        )
    )


@pytest.mark.skip
def test_update_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Org = client.orgs.update_org(
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        )
    )

    body: Org = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Org = await client.orgs.update_org(
        body=OrgDetails(
            billing_email="<string>",
            name="<string>",
            phone="<string>",
        )
    )


@pytest.mark.skip
def test_org_list_api_calls():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    item: ApiCallWithPrice
    for item in client.api_calls.org_list_api_calls(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    ):
        print(item)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_org_list_api_calls_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    iterator = client.api_calls.org_list_api_calls(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )
    item: ApiCallWithPrice
    async for item in iterator:
        print(item)


@pytest.mark.skip
def test_get_api_call_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPrice = client.api_calls.get_api_call_for_org(id="<string>")

    body: ApiCallWithPrice = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_for_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPrice = await client.api_calls.get_api_call_for_org(
        id="<string>"
    )


@pytest.mark.skip
def test_org_dataset_s3_policies():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: DatasetS3Policies = client.orgs.org_dataset_s3_policies(
        role_arn="<string>", uri="<string>"
    )

    body: DatasetS3Policies = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_org_dataset_s3_policies_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: DatasetS3Policies = await client.orgs.org_dataset_s3_policies(
        role_arn="<string>", uri="<string>"
    )


@pytest.mark.skip
def test_list_org_datasets():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    item: OrgDataset
    for item in client.orgs.list_org_datasets(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    ):
        print(item)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_org_datasets_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    iterator = client.orgs.list_org_datasets(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )
    item: OrgDataset
    async for item in iterator:
        print(item)


@pytest.mark.skip
def test_create_org_dataset():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgDataset = client.orgs.create_org_dataset(
        body=CreateOrgDataset(
            name="<string>",
            source=OrgDatasetSource(
                access_role_arn="<string>",
                provider=StorageProvider.S3,
                uri="<string>",
            ),
        )
    )

    body: OrgDataset = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_org_dataset_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgDataset = await client.orgs.create_org_dataset(
        body=CreateOrgDataset(
            name="<string>",
            source=OrgDatasetSource(
                access_role_arn="<string>",
                provider=StorageProvider.S3,
                uri="<string>",
            ),
        )
    )


@pytest.mark.skip
def test_delete_org_dataset():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.orgs.delete_org_dataset(id=Uuid("<string>"))


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_org_dataset_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.orgs.delete_org_dataset(id=Uuid("<string>"))


@pytest.mark.skip
def test_get_org_dataset():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgDataset = client.orgs.get_org_dataset(id=Uuid("<string>"))

    body: OrgDataset = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_dataset_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgDataset = await client.orgs.get_org_dataset(id=Uuid("<string>"))


@pytest.mark.skip
def test_update_org_dataset():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgDataset = client.orgs.update_org_dataset(
        id=Uuid("<string>"), body=UpdateOrgDataset()
    )

    body: OrgDataset = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_dataset_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgDataset = await client.orgs.update_org_dataset(
        id=Uuid("<string>"), body=UpdateOrgDataset()
    )


@pytest.mark.skip
def test_list_org_dataset_conversions():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    item: OrgDatasetFileConversionSummary
    for item in client.orgs.list_org_dataset_conversions(
        id=Uuid("<string>"),
        sort_by=ConversionSortMode.CREATED_AT_ASCENDING,
        limit=None,
        page_token=None,
    ):
        print(item)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_org_dataset_conversions_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    iterator = client.orgs.list_org_dataset_conversions(
        id=Uuid("<string>"),
        sort_by=ConversionSortMode.CREATED_AT_ASCENDING,
        limit=None,
        page_token=None,
    )
    item: OrgDatasetFileConversionSummary
    async for item in iterator:
        print(item)


@pytest.mark.skip
def test_get_org_dataset_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgDatasetFileConversionDetails = client.orgs.get_org_dataset_conversion(
        conversion_id=Uuid("<string>"), id=Uuid("<string>")
    )

    body: OrgDatasetFileConversionDetails = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_dataset_conversion_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgDatasetFileConversionDetails = (
        await client.orgs.get_org_dataset_conversion(
            conversion_id=Uuid("<string>"), id=Uuid("<string>")
        )
    )


@pytest.mark.skip
def test_retry_org_dataset_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgDatasetFileConversion = client.orgs.retry_org_dataset_conversion(
        conversion_id=Uuid("<string>"), id=Uuid("<string>")
    )

    body: OrgDatasetFileConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_retry_org_dataset_conversion_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgDatasetFileConversion = await client.orgs.retry_org_dataset_conversion(
        conversion_id=Uuid("<string>"), id=Uuid("<string>")
    )


@pytest.mark.skip
def test_rescan_org_dataset():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgDataset = client.orgs.rescan_org_dataset(id=Uuid("<string>"))

    body: OrgDataset = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_rescan_org_dataset_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgDataset = await client.orgs.rescan_org_dataset(id=Uuid("<string>"))


@pytest.mark.skip
def test_get_org_dataset_conversion_stats():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgDatasetConversionStatsResponse = (
        client.orgs.get_org_dataset_conversion_stats(id=Uuid("<string>"))
    )

    body: OrgDatasetConversionStatsResponse = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_dataset_conversion_stats_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgDatasetConversionStatsResponse = (
        await client.orgs.get_org_dataset_conversion_stats(id=Uuid("<string>"))
    )


@pytest.mark.skip
def test_list_org_members():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    item: OrgMember
    for item in client.orgs.list_org_members(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        role=UserOrgRole.ADMIN,
        limit=None,
        page_token=None,
    ):
        print(item)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_org_members_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    iterator = client.orgs.list_org_members(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        role=UserOrgRole.ADMIN,
        limit=None,
        page_token=None,
    )
    item: OrgMember
    async for item in iterator:
        print(item)


@pytest.mark.skip
def test_create_org_member():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgMember = client.orgs.create_org_member(
        body=AddOrgMember(
            email="<string>",
            role=UserOrgRole.ADMIN,
        )
    )

    body: OrgMember = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_org_member_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgMember = await client.orgs.create_org_member(
        body=AddOrgMember(
            email="<string>",
            role=UserOrgRole.ADMIN,
        )
    )


@pytest.mark.skip
def test_delete_org_member():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.orgs.delete_org_member(user_id=Uuid("<string>"))


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_org_member_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.orgs.delete_org_member(user_id=Uuid("<string>"))


@pytest.mark.skip
def test_get_org_member():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgMember = client.orgs.get_org_member(user_id=Uuid("<string>"))

    body: OrgMember = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_member_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgMember = await client.orgs.get_org_member(user_id=Uuid("<string>"))


@pytest.mark.skip
def test_update_org_member():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgMember = client.orgs.update_org_member(
        user_id=Uuid("<string>"),
        body=UpdateMemberToOrgBody(
            role=UserOrgRole.ADMIN,
        ),
    )

    body: OrgMember = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_member_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgMember = await client.orgs.update_org_member(
        user_id=Uuid("<string>"),
        body=UpdateMemberToOrgBody(
            role=UserOrgRole.ADMIN,
        ),
    )


@pytest.mark.skip
def test_delete_payment_information_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.payments.delete_payment_information_for_org()


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_payment_information_for_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.payments.delete_payment_information_for_org()


@pytest.mark.skip
def test_get_payment_information_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = client.payments.get_payment_information_for_org()

    body: Customer = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_information_for_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = await client.payments.get_payment_information_for_org()


@pytest.mark.skip
def test_create_payment_information_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = client.payments.create_payment_information_for_org(
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        )
    )

    body: Customer = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_payment_information_for_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = await client.payments.create_payment_information_for_org(
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        )
    )


@pytest.mark.skip
def test_update_payment_information_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = client.payments.update_payment_information_for_org(
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        )
    )

    body: Customer = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_payment_information_for_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = await client.payments.update_payment_information_for_org(
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        )
    )


@pytest.mark.skip
def test_get_payment_balance_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = client.payments.get_payment_balance_for_org(
        include_total_due=False
    )

    body: CustomerBalance = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = await client.payments.get_payment_balance_for_org(
        include_total_due=False
    )


@pytest.mark.skip
def test_create_payment_intent_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PaymentIntent = client.payments.create_payment_intent_for_org()

    body: PaymentIntent = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_payment_intent_for_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PaymentIntent = await client.payments.create_payment_intent_for_org()


@pytest.mark.skip
def test_list_invoices_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[Invoice] = client.payments.list_invoices_for_org()

    body: List[Invoice] = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_invoices_for_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[Invoice] = await client.payments.list_invoices_for_org()


@pytest.mark.skip
def test_list_payment_methods_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[PaymentMethod] = client.payments.list_payment_methods_for_org()

    body: List[PaymentMethod] = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_payment_methods_for_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[PaymentMethod] = await client.payments.list_payment_methods_for_org()


@pytest.mark.skip
def test_delete_payment_method_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.payments.delete_payment_method_for_org(id="<string>")


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_payment_method_for_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.payments.delete_payment_method_for_org(id="<string>")


@pytest.mark.skip
def test_get_org_subscription():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = client.payments.get_org_subscription()

    body: ZooProductSubscriptions = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_subscription_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = await client.payments.get_org_subscription()


@pytest.mark.skip
def test_create_org_subscription():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = client.payments.create_org_subscription(
        body=ZooProductSubscriptionsOrgRequest(
            modeling_app="<string>",
        )
    )

    body: ZooProductSubscriptions = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_org_subscription_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = await client.payments.create_org_subscription(
        body=ZooProductSubscriptionsOrgRequest(
            modeling_app="<string>",
        )
    )


@pytest.mark.skip
def test_update_org_subscription():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = client.payments.update_org_subscription(
        body=ZooProductSubscriptionsOrgRequest(
            modeling_app="<string>",
        )
    )

    body: ZooProductSubscriptions = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_subscription_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = await client.payments.update_org_subscription(
        body=ZooProductSubscriptionsOrgRequest(
            modeling_app="<string>",
        )
    )


@pytest.mark.skip
def test_validate_customer_tax_information_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.payments.validate_customer_tax_information_for_org()


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_validate_customer_tax_information_for_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.payments.validate_customer_tax_information_for_org()


@pytest.mark.skip
def test_get_org_privacy_settings():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PrivacySettings = client.orgs.get_org_privacy_settings()

    body: PrivacySettings = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_privacy_settings_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PrivacySettings = await client.orgs.get_org_privacy_settings()


@pytest.mark.skip
def test_update_org_privacy_settings():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PrivacySettings = client.orgs.update_org_privacy_settings(
        body=PrivacySettings(
            can_train_on_data=False,
        )
    )

    body: PrivacySettings = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_privacy_settings_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PrivacySettings = await client.orgs.update_org_privacy_settings(
        body=PrivacySettings(
            can_train_on_data=False,
        )
    )


@pytest.mark.skip
def test_delete_org_saml_idp():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.orgs.delete_org_saml_idp()


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_org_saml_idp_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.orgs.delete_org_saml_idp()


@pytest.mark.skip
def test_get_org_saml_idp():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: SamlIdentityProvider = client.orgs.get_org_saml_idp()

    body: SamlIdentityProvider = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_saml_idp_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: SamlIdentityProvider = await client.orgs.get_org_saml_idp()


@pytest.mark.skip
def test_create_org_saml_idp():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: SamlIdentityProvider = client.orgs.create_org_saml_idp(
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=IdpMetadataSource(
                OptionUrl(
                    url="<string>",
                )
            ),
            technical_contact_email="<string>",
        )
    )

    body: SamlIdentityProvider = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_org_saml_idp_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: SamlIdentityProvider = await client.orgs.create_org_saml_idp(
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=IdpMetadataSource(
                OptionUrl(
                    url="<string>",
                )
            ),
            technical_contact_email="<string>",
        )
    )


@pytest.mark.skip
def test_update_org_saml_idp():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: SamlIdentityProvider = client.orgs.update_org_saml_idp(
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=IdpMetadataSource(
                OptionBase64EncodedXml(
                    data=Base64Data(b"<bytes>"),
                )
            ),
            technical_contact_email="<string>",
        )
    )

    body: SamlIdentityProvider = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_saml_idp_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: SamlIdentityProvider = await client.orgs.update_org_saml_idp(
        body=SamlIdentityProviderCreate(
            idp_entity_id="<string>",
            idp_metadata_source=IdpMetadataSource(
                OptionBase64EncodedXml(
                    data=Base64Data(b"<bytes>"),
                )
            ),
            technical_contact_email="<string>",
        )
    )


@pytest.mark.skip
def test_list_service_accounts_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    item: ServiceAccount
    for item in client.service_accounts.list_service_accounts_for_org(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    ):
        print(item)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_service_accounts_for_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    iterator = client.service_accounts.list_service_accounts_for_org(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )
    item: ServiceAccount
    async for item in iterator:
        print(item)


@pytest.mark.skip
def test_create_service_account_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ServiceAccount = client.service_accounts.create_service_account_for_org(
        label=None
    )

    body: ServiceAccount = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_service_account_for_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ServiceAccount = (
        await client.service_accounts.create_service_account_for_org(label=None)
    )


@pytest.mark.skip
def test_delete_service_account_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.service_accounts.delete_service_account_for_org(
        token=ServiceAccountUuid("<string>")
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_service_account_for_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.service_accounts.delete_service_account_for_org(
        token=ServiceAccountUuid("<string>")
    )


@pytest.mark.skip
def test_get_service_account_for_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ServiceAccount = client.service_accounts.get_service_account_for_org(
        token=ServiceAccountUuid("<string>")
    )

    body: ServiceAccount = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_service_account_for_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ServiceAccount = await client.service_accounts.get_service_account_for_org(
        token=ServiceAccountUuid("<string>")
    )


@pytest.mark.skip
def test_get_org_shortlinks():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    item: Shortlink
    for item in client.orgs.get_org_shortlinks(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    ):
        print(item)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_org_shortlinks_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    iterator = client.orgs.get_org_shortlinks(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )
    item: Shortlink
    async for item in iterator:
        print(item)


@pytest.mark.skip
def test_list_orgs():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    item: Org
    for item in client.orgs.list_orgs(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    ):
        print(item)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_orgs_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    iterator = client.orgs.list_orgs(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )
    item: Org
    async for item in iterator:
        print(item)


@pytest.mark.skip
def test_get_any_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Org = client.orgs.get_any_org(id=Uuid("<string>"))

    body: Org = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_any_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Org = await client.orgs.get_any_org(id=Uuid("<string>"))


@pytest.mark.skip
def test_org_admin_details_get():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgAdminDetails = client.orgs.org_admin_details_get(id=Uuid("<string>"))

    body: OrgAdminDetails = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_org_admin_details_get_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: OrgAdminDetails = await client.orgs.org_admin_details_get(
        id=Uuid("<string>")
    )


@pytest.mark.skip
def test_get_payment_balance_for_any_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = client.payments.get_payment_balance_for_any_org(
        include_total_due=False, id=Uuid("<string>")
    )

    body: CustomerBalance = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_any_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = await client.payments.get_payment_balance_for_any_org(
        include_total_due=False, id=Uuid("<string>")
    )


@pytest.mark.skip
def test_update_payment_balance_for_any_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = client.payments.update_payment_balance_for_any_org(
        id=Uuid("<string>"), include_total_due=False, body=UpdatePaymentBalance()
    )

    body: CustomerBalance = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_payment_balance_for_any_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = await client.payments.update_payment_balance_for_any_org(
        id=Uuid("<string>"), include_total_due=False, body=UpdatePaymentBalance()
    )


@pytest.mark.skip
def test_update_org_subscription_for_any_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = (
        client.payments.update_org_subscription_for_any_org(
            id=Uuid("<string>"),
            body=ZooProductSubscriptionsOrgRequest(
                modeling_app="<string>",
            ),
        )
    )

    body: ZooProductSubscriptions = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_org_subscription_for_any_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = (
        await client.payments.update_org_subscription_for_any_org(
            id=Uuid("<string>"),
            body=ZooProductSubscriptionsOrgRequest(
                modeling_app="<string>",
            ),
        )
    )


@pytest.mark.skip
def test_ping():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Pong = client.meta.ping()

    body: Pong = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_ping_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Pong = await client.meta.ping()


@pytest.mark.skip
def test_get_pricing_subscriptions():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Dict = client.meta.get_pricing_subscriptions()

    body: Dict = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_pricing_subscriptions_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Dict = await client.meta.get_pricing_subscriptions()


@pytest.mark.skip
def test_create_store_coupon():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: DiscountCode = client.store.create_store_coupon(
        body=StoreCouponParams(
            percent_off=10,
        )
    )

    body: DiscountCode = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_store_coupon_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: DiscountCode = await client.store.create_store_coupon(
        body=StoreCouponParams(
            percent_off=10,
        )
    )


@pytest.mark.skip
def test_upsert_subscription_plan_price():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: SubscriptionPlanPriceRecord = (
        client.payments.upsert_subscription_plan_price(
            slug="<string>",
            body=PriceUpsertRequest(
                active=False,
                billing_model=SubscriptionPlanBillingModel.FLAT,
                cadence=PlanInterval.DAY,
                unit_amount=3.14,
            ),
        )
    )

    body: SubscriptionPlanPriceRecord = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_upsert_subscription_plan_price_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: SubscriptionPlanPriceRecord = (
        await client.payments.upsert_subscription_plan_price(
            slug="<string>",
            body=PriceUpsertRequest(
                active=False,
                billing_model=SubscriptionPlanBillingModel.FLAT,
                cadence=PlanInterval.DAY,
                unit_amount=3.14,
            ),
        )
    )


@pytest.mark.skip
def test_get_angle_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitAngleConversion = client.unit.get_angle_unit_conversion(
        input_unit=UnitAngle.DEGREES, output_unit=UnitAngle.DEGREES, value=3.14
    )

    body: UnitAngleConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_angle_unit_conversion_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitAngleConversion = await client.unit.get_angle_unit_conversion(
        input_unit=UnitAngle.DEGREES, output_unit=UnitAngle.DEGREES, value=3.14
    )


@pytest.mark.skip
def test_get_area_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitAreaConversion = client.unit.get_area_unit_conversion(
        input_unit=UnitArea.CM2, output_unit=UnitArea.CM2, value=3.14
    )

    body: UnitAreaConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_area_unit_conversion_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitAreaConversion = await client.unit.get_area_unit_conversion(
        input_unit=UnitArea.CM2, output_unit=UnitArea.CM2, value=3.14
    )


@pytest.mark.skip
def test_get_current_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitCurrentConversion = client.unit.get_current_unit_conversion(
        input_unit=UnitCurrent.AMPERES, output_unit=UnitCurrent.AMPERES, value=3.14
    )

    body: UnitCurrentConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_current_unit_conversion_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitCurrentConversion = await client.unit.get_current_unit_conversion(
        input_unit=UnitCurrent.AMPERES, output_unit=UnitCurrent.AMPERES, value=3.14
    )


@pytest.mark.skip
def test_get_energy_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitEnergyConversion = client.unit.get_energy_unit_conversion(
        input_unit=UnitEnergy.BTU, output_unit=UnitEnergy.BTU, value=3.14
    )

    body: UnitEnergyConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_energy_unit_conversion_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitEnergyConversion = await client.unit.get_energy_unit_conversion(
        input_unit=UnitEnergy.BTU, output_unit=UnitEnergy.BTU, value=3.14
    )


@pytest.mark.skip
def test_get_force_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitForceConversion = client.unit.get_force_unit_conversion(
        input_unit=UnitForce.DYNES, output_unit=UnitForce.DYNES, value=3.14
    )

    body: UnitForceConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_force_unit_conversion_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitForceConversion = await client.unit.get_force_unit_conversion(
        input_unit=UnitForce.DYNES, output_unit=UnitForce.DYNES, value=3.14
    )


@pytest.mark.skip
def test_get_frequency_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitFrequencyConversion = client.unit.get_frequency_unit_conversion(
        input_unit=UnitFrequency.GIGAHERTZ,
        output_unit=UnitFrequency.GIGAHERTZ,
        value=3.14,
    )

    body: UnitFrequencyConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_frequency_unit_conversion_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitFrequencyConversion = await client.unit.get_frequency_unit_conversion(
        input_unit=UnitFrequency.GIGAHERTZ,
        output_unit=UnitFrequency.GIGAHERTZ,
        value=3.14,
    )


@pytest.mark.skip
def test_get_length_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitLengthConversion = client.unit.get_length_unit_conversion(
        input_unit=UnitLength.CM, output_unit=UnitLength.CM, value=3.14
    )

    body: UnitLengthConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_length_unit_conversion_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitLengthConversion = await client.unit.get_length_unit_conversion(
        input_unit=UnitLength.CM, output_unit=UnitLength.CM, value=3.14
    )


@pytest.mark.skip
def test_get_mass_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitMassConversion = client.unit.get_mass_unit_conversion(
        input_unit=UnitMass.G, output_unit=UnitMass.G, value=3.14
    )

    body: UnitMassConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_mass_unit_conversion_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitMassConversion = await client.unit.get_mass_unit_conversion(
        input_unit=UnitMass.G, output_unit=UnitMass.G, value=3.14
    )


@pytest.mark.skip
def test_get_power_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitPowerConversion = client.unit.get_power_unit_conversion(
        input_unit=UnitPower.BTU_PER_MINUTE,
        output_unit=UnitPower.BTU_PER_MINUTE,
        value=3.14,
    )

    body: UnitPowerConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_power_unit_conversion_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitPowerConversion = await client.unit.get_power_unit_conversion(
        input_unit=UnitPower.BTU_PER_MINUTE,
        output_unit=UnitPower.BTU_PER_MINUTE,
        value=3.14,
    )


@pytest.mark.skip
def test_get_pressure_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitPressureConversion = client.unit.get_pressure_unit_conversion(
        input_unit=UnitPressure.ATMOSPHERES,
        output_unit=UnitPressure.ATMOSPHERES,
        value=3.14,
    )

    body: UnitPressureConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_pressure_unit_conversion_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitPressureConversion = await client.unit.get_pressure_unit_conversion(
        input_unit=UnitPressure.ATMOSPHERES,
        output_unit=UnitPressure.ATMOSPHERES,
        value=3.14,
    )


@pytest.mark.skip
def test_get_temperature_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitTemperatureConversion = client.unit.get_temperature_unit_conversion(
        input_unit=UnitTemperature.CELSIUS,
        output_unit=UnitTemperature.CELSIUS,
        value=3.14,
    )

    body: UnitTemperatureConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_temperature_unit_conversion_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitTemperatureConversion = (
        await client.unit.get_temperature_unit_conversion(
            input_unit=UnitTemperature.CELSIUS,
            output_unit=UnitTemperature.CELSIUS,
            value=3.14,
        )
    )


@pytest.mark.skip
def test_get_torque_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitTorqueConversion = client.unit.get_torque_unit_conversion(
        input_unit=UnitTorque.NEWTON_METRES,
        output_unit=UnitTorque.NEWTON_METRES,
        value=3.14,
    )

    body: UnitTorqueConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_torque_unit_conversion_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitTorqueConversion = await client.unit.get_torque_unit_conversion(
        input_unit=UnitTorque.NEWTON_METRES,
        output_unit=UnitTorque.NEWTON_METRES,
        value=3.14,
    )


@pytest.mark.skip
def test_get_volume_unit_conversion():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitVolumeConversion = client.unit.get_volume_unit_conversion(
        input_unit=UnitVolume.CM3, output_unit=UnitVolume.CM3, value=3.14
    )

    body: UnitVolumeConversion = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_volume_unit_conversion_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UnitVolumeConversion = await client.unit.get_volume_unit_conversion(
        input_unit=UnitVolume.CM3, output_unit=UnitVolume.CM3, value=3.14
    )


@pytest.mark.skip
def test_delete_user_self():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.users.delete_user_self()


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_user_self_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.users.delete_user_self()


@pytest.mark.skip
def test_get_user_self():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: User = client.users.get_user_self()

    body: User = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_self_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: User = await client.users.get_user_self()


@pytest.mark.skip
def test_update_user_self():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: User = client.users.update_user_self(
        body=UpdateUser(
            company="<string>",
            discord="<string>",
            first_name="<string>",
            github="<string>",
            image="<string>",
            last_name="<string>",
            phone="<string>",
        )
    )

    body: User = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_user_self_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: User = await client.users.update_user_self(
        body=UpdateUser(
            company="<string>",
            discord="<string>",
            first_name="<string>",
            github="<string>",
            image="<string>",
            last_name="<string>",
            phone="<string>",
        )
    )


@pytest.mark.skip
def test_user_list_api_calls():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    item: ApiCallWithPrice
    for item in client.api_calls.user_list_api_calls(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    ):
        print(item)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_user_list_api_calls_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    iterator = client.api_calls.user_list_api_calls(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )
    item: ApiCallWithPrice
    async for item in iterator:
        print(item)


@pytest.mark.skip
def test_get_api_call_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPrice = client.api_calls.get_api_call_for_user(id="<string>")

    body: ApiCallWithPrice = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_call_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiCallWithPrice = await client.api_calls.get_api_call_for_user(
        id="<string>"
    )


@pytest.mark.skip
def test_list_api_tokens_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    item: ApiToken
    for item in client.api_tokens.list_api_tokens_for_user(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    ):
        print(item)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_api_tokens_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    iterator = client.api_tokens.list_api_tokens_for_user(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )
    item: ApiToken
    async for item in iterator:
        print(item)


@pytest.mark.skip
def test_create_api_token_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiToken = client.api_tokens.create_api_token_for_user(label=None)

    body: ApiToken = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_api_token_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiToken = await client.api_tokens.create_api_token_for_user(label=None)


@pytest.mark.skip
def test_delete_api_token_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.api_tokens.delete_api_token_for_user(token=ApiTokenUuid("<string>"))


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_api_token_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.api_tokens.delete_api_token_for_user(token=ApiTokenUuid("<string>"))


@pytest.mark.skip
def test_get_api_token_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiToken = client.api_tokens.get_api_token_for_user(
        token=ApiTokenUuid("<string>")
    )

    body: ApiToken = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_api_token_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ApiToken = await client.api_tokens.get_api_token_for_user(
        token=ApiTokenUuid("<string>")
    )


@pytest.mark.skip
def test_patch_user_crm():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.users.patch_user_crm(body=CrmData())


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_patch_user_crm_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.users.patch_user_crm(body=CrmData())


@pytest.mark.skip
def test_get_user_self_extended():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ExtendedUser = client.users.get_user_self_extended()

    body: ExtendedUser = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_self_extended_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ExtendedUser = await client.users.get_user_self_extended()


@pytest.mark.skip
def test_user_features_get():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UserFeatureList = client.users.user_features_get()

    body: UserFeatureList = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_user_features_get_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UserFeatureList = await client.users.user_features_get()


@pytest.mark.skip
def test_put_user_form_self():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.users.put_user_form_self(
        body=InquiryForm(
            email="<string>",
            first_name="<string>",
            inquiry_type=InquiryType.PILOT_INQUIRY,
            last_name="<string>",
            message="<string>",
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_put_user_form_self_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.users.put_user_form_self(
        body=InquiryForm(
            email="<string>",
            first_name="<string>",
            inquiry_type=InquiryType.PILOT_INQUIRY,
            last_name="<string>",
            message="<string>",
        )
    )


@pytest.mark.skip
def test_get_oauth2_providers_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[AccountProvider] = client.users.get_oauth2_providers_for_user()

    body: List[AccountProvider] = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_oauth2_providers_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[AccountProvider] = await client.users.get_oauth2_providers_for_user()


@pytest.mark.skip
def test_get_user_org():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UserOrgInfo = client.orgs.get_user_org()

    body: UserOrgInfo = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_org_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UserOrgInfo = await client.orgs.get_user_org()


@pytest.mark.skip
def test_delete_payment_information_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.payments.delete_payment_information_for_user()


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_payment_information_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.payments.delete_payment_information_for_user()


@pytest.mark.skip
def test_get_payment_information_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = client.payments.get_payment_information_for_user()

    body: Customer = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_information_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = await client.payments.get_payment_information_for_user()


@pytest.mark.skip
def test_create_payment_information_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = client.payments.create_payment_information_for_user(
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        )
    )

    body: Customer = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_payment_information_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = await client.payments.create_payment_information_for_user(
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        )
    )


@pytest.mark.skip
def test_update_payment_information_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = client.payments.update_payment_information_for_user(
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        )
    )

    body: Customer = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_payment_information_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Customer = await client.payments.update_payment_information_for_user(
        body=BillingInfo(
            name="<string>",
            phone="<string>",
        )
    )


@pytest.mark.skip
def test_get_payment_balance_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = client.payments.get_payment_balance_for_user(
        include_total_due=False
    )

    body: CustomerBalance = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = await client.payments.get_payment_balance_for_user(
        include_total_due=False
    )


@pytest.mark.skip
def test_create_payment_intent_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PaymentIntent = client.payments.create_payment_intent_for_user()

    body: PaymentIntent = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_payment_intent_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PaymentIntent = await client.payments.create_payment_intent_for_user()


@pytest.mark.skip
def test_list_invoices_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[Invoice] = client.payments.list_invoices_for_user()

    body: List[Invoice] = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_invoices_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[Invoice] = await client.payments.list_invoices_for_user()


@pytest.mark.skip
def test_list_payment_methods_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[PaymentMethod] = client.payments.list_payment_methods_for_user()

    body: List[PaymentMethod] = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_payment_methods_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: List[PaymentMethod] = await client.payments.list_payment_methods_for_user()


@pytest.mark.skip
def test_delete_payment_method_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.payments.delete_payment_method_for_user(id="<string>", force=False)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_payment_method_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.payments.delete_payment_method_for_user(id="<string>", force=False)


@pytest.mark.skip
def test_set_default_payment_method_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.payments.set_default_payment_method_for_user(id="<string>")


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_set_default_payment_method_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.payments.set_default_payment_method_for_user(id="<string>")


@pytest.mark.skip
def test_get_user_subscription():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = client.payments.get_user_subscription()

    body: ZooProductSubscriptions = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_subscription_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = await client.payments.get_user_subscription()


@pytest.mark.skip
def test_create_user_subscription():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = client.payments.create_user_subscription(
        body=ZooProductSubscriptionsUserRequest(
            modeling_app="<string>",
        )
    )

    body: ZooProductSubscriptions = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_user_subscription_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = await client.payments.create_user_subscription(
        body=ZooProductSubscriptionsUserRequest(
            modeling_app="<string>",
        )
    )


@pytest.mark.skip
def test_update_user_subscription():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = client.payments.update_user_subscription(
        body=ZooProductSubscriptionsUserRequest(
            modeling_app="<string>",
        )
    )

    body: ZooProductSubscriptions = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_user_subscription_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = await client.payments.update_user_subscription(
        body=ZooProductSubscriptionsUserRequest(
            modeling_app="<string>",
        )
    )


@pytest.mark.skip
def test_validate_customer_tax_information_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.payments.validate_customer_tax_information_for_user()


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_validate_customer_tax_information_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.payments.validate_customer_tax_information_for_user()


@pytest.mark.skip
def test_get_user_privacy_settings():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PrivacySettings = client.users.get_user_privacy_settings()

    body: PrivacySettings = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_privacy_settings_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PrivacySettings = await client.users.get_user_privacy_settings()


@pytest.mark.skip
def test_update_user_privacy_settings():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PrivacySettings = client.users.update_user_privacy_settings(
        body=PrivacySettings(
            can_train_on_data=False,
        )
    )

    body: PrivacySettings = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_user_privacy_settings_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: PrivacySettings = await client.users.update_user_privacy_settings(
        body=PrivacySettings(
            can_train_on_data=False,
        )
    )


@pytest.mark.skip
def test_get_session_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Session = client.users.get_session_for_user(token=SessionUuid("<string>"))

    body: Session = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_session_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: Session = await client.users.get_session_for_user(
        token=SessionUuid("<string>")
    )


@pytest.mark.skip
def test_get_user_shortlinks():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    item: Shortlink
    for item in client.users.get_user_shortlinks(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    ):
        print(item)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_shortlinks_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    iterator = client.users.get_user_shortlinks(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )
    item: Shortlink
    async for item in iterator:
        print(item)


@pytest.mark.skip
def test_create_user_shortlink():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CreateShortlinkResponse = client.users.create_user_shortlink(
        body=CreateShortlinkRequest(
            restrict_to_org=False,
            url="<string>",
        )
    )

    body: CreateShortlinkResponse = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_user_shortlink_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CreateShortlinkResponse = await client.users.create_user_shortlink(
        body=CreateShortlinkRequest(
            restrict_to_org=False,
            url="<string>",
        )
    )


@pytest.mark.skip
def test_delete_user_shortlink():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.users.delete_user_shortlink(key="<string>")


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_user_shortlink_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.users.delete_user_shortlink(key="<string>")


@pytest.mark.skip
def test_redirect_user_shortlink():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.hidden.redirect_user_shortlink(key="<string>")


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_redirect_user_shortlink_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.hidden.redirect_user_shortlink(key="<string>")


@pytest.mark.skip
def test_update_user_shortlink():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.users.update_user_shortlink(
        key="<string>",
        body=UpdateShortlinkRequest(
            restrict_to_org=False,
        ),
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_user_shortlink_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.users.update_user_shortlink(
        key="<string>",
        body=UpdateShortlinkRequest(
            restrict_to_org=False,
        ),
    )


@pytest.mark.skip
def test_list_text_to_cad_parts_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    item: TextToCadResponse
    for item in client.ml.list_text_to_cad_parts_for_user(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        conversation_id=Uuid("<string>"),
        limit=None,
        page_token=None,
        no_models=None,
        no_parts=None,
    ):
        print(item)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_text_to_cad_parts_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    iterator = client.ml.list_text_to_cad_parts_for_user(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        conversation_id=Uuid("<string>"),
        limit=None,
        page_token=None,
        no_models=None,
        no_parts=None,
    )
    item: TextToCadResponse
    async for item in iterator:
        print(item)


@pytest.mark.skip
def test_get_text_to_cad_part_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: TextToCadResponse = client.ml.get_text_to_cad_part_for_user(id="<string>")

    body: TextToCadResponse = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_text_to_cad_part_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: TextToCadResponse = await client.ml.get_text_to_cad_part_for_user(
        id="<string>"
    )


@pytest.mark.skip
def test_create_text_to_cad_part_feedback():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.ml.create_text_to_cad_part_feedback(
        id="<string>", feedback=MlFeedback.THUMBS_UP
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_text_to_cad_part_feedback_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.ml.create_text_to_cad_part_feedback(
        id="<string>", feedback=MlFeedback.THUMBS_UP
    )


@pytest.mark.skip
def test_list_users():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    item: User
    for item in client.users.list_users(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    ):
        print(item)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_users_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    iterator = client.users.list_users(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )
    item: User
    async for item in iterator:
        print(item)


@pytest.mark.skip
def test_list_users_extended():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    item: ExtendedUser
    for item in client.users.list_users_extended(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    ):
        print(item)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_users_extended_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    iterator = client.users.list_users_extended(
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING, limit=None, page_token=None
    )
    item: ExtendedUser
    async for item in iterator:
        print(item)


@pytest.mark.skip
def test_get_user_extended():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ExtendedUser = client.users.get_user_extended(id=UserIdentifier("<string>"))

    body: ExtendedUser = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_extended_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ExtendedUser = await client.users.get_user_extended(
        id=UserIdentifier("<string>")
    )


@pytest.mark.skip
def test_get_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: User = client.users.get_user(id=UserIdentifier("<string>"))

    body: User = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: User = await client.users.get_user(id=UserIdentifier("<string>"))


@pytest.mark.skip
def test_user_admin_details_get():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UserAdminDetails = client.users.user_admin_details_get(
        id=UserIdentifier("<string>")
    )

    body: UserAdminDetails = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_user_admin_details_get_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: UserAdminDetails = await client.users.user_admin_details_get(
        id=UserIdentifier("<string>")
    )


@pytest.mark.skip
def test_list_api_calls_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    item: ApiCallWithPrice
    for item in client.api_calls.list_api_calls_for_user(
        id=UserIdentifier("<string>"),
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,
        page_token=None,
    ):
        print(item)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_list_api_calls_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Iterate through all pages automatically
    iterator = client.api_calls.list_api_calls_for_user(
        id=UserIdentifier("<string>"),
        sort_by=CreatedAtSortMode.CREATED_AT_ASCENDING,
        limit=None,
        page_token=None,
    )
    item: ApiCallWithPrice
    async for item in iterator:
        print(item)


@pytest.mark.skip
def test_get_payment_balance_for_any_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = client.payments.get_payment_balance_for_any_user(
        id=UserIdentifier("<string>"), include_total_due=False
    )

    body: CustomerBalance = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_payment_balance_for_any_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = await client.payments.get_payment_balance_for_any_user(
        id=UserIdentifier("<string>"), include_total_due=False
    )


@pytest.mark.skip
def test_update_payment_balance_for_any_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = client.payments.update_payment_balance_for_any_user(
        id=UserIdentifier("<string>"),
        include_total_due=False,
        body=UpdatePaymentBalance(),
    )

    body: CustomerBalance = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_payment_balance_for_any_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: CustomerBalance = await client.payments.update_payment_balance_for_any_user(
        id=UserIdentifier("<string>"),
        include_total_due=False,
        body=UpdatePaymentBalance(),
    )


@pytest.mark.skip
def test_update_subscription_for_user():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = client.users.update_subscription_for_user(
        id=UserIdentifier("<string>"),
        body=ZooProductSubscriptionsUserRequest(
            modeling_app="<string>",
        ),
    )

    body: ZooProductSubscriptions = result
    print(body)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_update_subscription_for_user_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    result: ZooProductSubscriptions = await client.users.update_subscription_for_user(
        id=UserIdentifier("<string>"),
        body=ZooProductSubscriptionsUserRequest(
            modeling_app="<string>",
        ),
    )


@pytest.mark.skip
def test_put_public_form():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.users.put_public_form(
        body=InquiryForm(
            email="<string>",
            first_name="<string>",
            inquiry_type=InquiryType.PILOT_INQUIRY,
            last_name="<string>",
            message="<string>",
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_put_public_form_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.users.put_public_form(
        body=InquiryForm(
            email="<string>",
            first_name="<string>",
            inquiry_type=InquiryType.PILOT_INQUIRY,
            last_name="<string>",
            message="<string>",
        )
    )


@pytest.mark.skip
def test_put_public_subscribe():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    client.users.put_public_subscribe(
        body=Subscribe(
            email="<string>",
        )
    )


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_put_public_subscribe_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    await client.users.put_public_subscribe(
        body=Subscribe(
            email="<string>",
        )
    )


@pytest.mark.skip
def test_create_executor_term():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Connect to the websocket.
    with client.executor.create_executor_term() as websocket:
        # Send a message.
        websocket.send("{}")

        # Get the messages.
        for message in websocket:
            print(message)


# OR run async
@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_executor_term_async():
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Connect to the websocket.
    websocket = await client.executor.create_executor_term()

    # Send a message.
    await websocket.send("{}")

    # Get the messages.
    async for message in websocket:
        print(message)


@pytest.mark.skip
def test_ml_copilot_ws():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Connect to the websocket.
    with client.ml.ml_copilot_ws(
        conversation_id=None, replay=None, pr=None
    ) as websocket:
        # Send a message.
        websocket.send(
            MlCopilotClientMessage(
                OptionUser(
                    content="<string>",
                    current_files={"<string>": b"<bytes>"},
                    forced_tools=[MlCopilotTool.EDIT_KCL_CODE],
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
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Connect to the websocket.
    websocket = await client.ml.ml_copilot_ws(
        conversation_id=None, replay=None, pr=None
    )

    # Send a message.
    await websocket.send("{}")

    # Get the messages.
    async for message in websocket:
        print(message)


@pytest.mark.skip
def test_ml_reasoning_ws():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Connect to the websocket.
    with client.ml.ml_reasoning_ws(id="<string>") as websocket:
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
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Connect to the websocket.
    websocket = await client.ml.ml_reasoning_ws(id="<string>")

    # Send a message.
    await websocket.send("{}")

    # Get the messages.
    async for message in websocket:
        print(message)


@pytest.mark.skip
def test_modeling_commands_ws():
    client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Connect to the websocket.
    with client.modeling.modeling_commands_ws(
        fps=10,
        order_independent_transparency=False,
        post_effect=PostEffectType.PHOSPHOR,
        show_grid=False,
        unlocked_framerate=False,
        video_res_height=10,
        video_res_width=10,
        webrtc=False,
        api_call_id=None,
        pool=None,
        replay=None,
        pr=None,
    ) as websocket:
        # Send a message.
        websocket.send(
            WebSocketRequest(
                OptionTrickleIce(
                    candidate=RtcIceCandidateInit(
                        candidate="<string>",
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
    client = AsyncKittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable

    # Connect to the websocket.
    websocket = await client.modeling.modeling_commands_ws(
        fps=10,
        order_independent_transparency=False,
        post_effect=PostEffectType.PHOSPHOR,
        show_grid=False,
        unlocked_framerate=False,
        video_res_height=10,
        video_res_width=10,
        webrtc=False,
        api_call_id=None,
        pool=None,
        replay=None,
        pr=None,
    )

    # Send a message.
    await websocket.send("{}")

    # Get the messages.
    async for message in websocket:
        print(message)
