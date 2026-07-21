from enum import Enum


class Feature(str, Enum):
    """Feature-like switches determined by environment, rules, and overrides."""  # noqa: E501

    """# When enabled, auth is restricted to only employees."""  # noqa: E501

    AUTH_RESTRICTED_TO_EMPLOYEES = "auth_restricted_to_employees"

    """# Enables emitting telemetry to BigQuery, otherwise received telemetry is just dropped."""  # noqa: E501

    BIG_QUERY_TELEMETRY = "big_query_telemetry"

    """# Stripe related features are enabled."""  # noqa: E501

    BILLING = "billing"

    """# Disable signup through email or OAuth."""  # noqa: E501

    DISALLOW_SELF_SIGNUP = "disallow_self_signup"

    """# Email sending is handled by AWS SES."""  # noqa: E501

    EMAIL_WITH_S_E_S = "email_with_s_e_s"

    """# Enables the Z0006 lint, for converting to new face api syntax in Zoo Design Studio."""  # noqa: E501

    ENABLE_Z0006_LINT = "enable_z0006_lint"

    """# Enables the Factory portal."""  # noqa: E501

    FACTORY_PORTAL = "factory_portal"

    """# New KCL lexer and parser."""  # noqa: E501

    KCL_NEW_LEXER_PARSER = "kcl_new_lexer_parser"

    """# Immediately redirect to our Govcloud environment (zoogov.dev)."""  # noqa: E501

    REDIRECT_TO_GOVCLOUD = "redirect_to_govcloud"

    """# Requires SAML auth and orgs for all users."""  # noqa: E501

    REQUIRE_SAML_AUTH = "require_saml_auth"

    """# Only to be used only for local development. Allows bypassing certain features or makes local dev easier."""  # noqa: E501

    LOCAL_DEV = "local_dev"

    """# Enables customers to subscribe to our newsletter."""  # noqa: E501

    NEWSLETTER = "newsletter"

    """# Prefix email subjects with the environment so we can better identify the source."""  # noqa: E501

    PREFIX_EMAIL_SUBJECT = "prefix_email_subject"

    """# Enterprise-only CockroachDB features (like `REGIONAL BY ROW`) are enabled in this environment."""  # noqa: E501

    ENTERPRISE_COCKROACH = "enterprise_cockroach"

    """# Always use cookies with same-site=none."""  # noqa: E501

    SAME_SITE_NONE_COOKIES = "same_site_none_cookies"

    """# Notify us via slack if we're missing tax info for a customer."""  # noqa: E501

    VALIDATE_TAX_INFO = "validate_tax_info"

    """# Enables modeling dialogs in Zoo Design Studio."""  # noqa: E501

    MODELING_DIALOGS = "modeling_dialogs"

    """# Enables plugins in Zoo Design Studio."""  # noqa: E501

    PLUGINS = "plugins"

    """# Grants access to the beta proprietary-to-KCL conversion endpoint."""  # noqa: E501

    PROPRIETARY_TO_KCL_CONVERSION_BETA = "proprietary_to_kcl_conversion_beta"

    """# Enables the topological segments-based region API for point-and-click in Zoo Design Studio."""  # noqa: E501

    SEGMENTS_BASED_REGIONS = "segments_based_regions"

    """# Enables sketch solve experimental features in Zoo Design Studio."""  # noqa: E501

    SKETCH_EXPERIMENTAL_FEATURES = "sketch_experimental_features"

    """# Enables cloud storage for web and desktop. Yes desktop too, the name is old and will go away soon."""  # noqa: E501

    WEB_APP_FILE_BROWSER = "web_app_file_browser"

    """# Enables private Zookeeper Pro mode access in ML Copilot."""  # noqa: E501

    ZOOKEEPER_PRO_MODE = "zookeeper_pro_mode"

    """# Allow creating a session via an existing API key"""  # noqa: E501

    UNSAFE_ALLOW_API_KEY_AUTH = "unsafe_allow_api_key_auth"

    """# Allow shortlinks to have a domain of localhost."""  # noqa: E501

    UNSAFE_ALLOW_LOCALHOST_SHORTLINKS = "unsafe_allow_localhost_shortlinks"

    """# Enable ZooCorp OAuth2. This adds https://auth.corp.zoo.dev as an OAuth2 provider."""  # noqa: E501

    ZOO_CORP_AUTH = "zoo_corp_auth"

    def __str__(self) -> str:
        return str(self.value)
