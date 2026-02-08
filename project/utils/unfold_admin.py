from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


UNFOLD = {
    "SITE_TITLE": "Custom suffix in <title> tag",
    "SITE_HEADER": "Appears in sidebar at the top",
    "SITE_SUBHEADER": "Appears under SITE_HEADER",
    "SITE_DROPDOWN": [
        {
            "icon": "diamond",
            "title": _("My site"),
            "link": "https://example.com",
        },
        # ...
    ],
    "SITE_URL": "/",
    "SITE_ICON": {
        "light": lambda request: static("icon-light.svg"),  # light mode
        "dark": lambda request: static("icon-dark.svg"),  # dark mode
    },
    # "SITE_LOGO": lambda request: static("logo.svg"),  # both modes, optimise for 32px height
    "SITE_LOGO": {
        "light": lambda request: static("logo-light.svg"),  # light mode
        "dark": lambda request: static("logo-dark.svg"),  # dark mode
    },
    "SITE_SYMBOL": "speed",  # symbol from icon setf
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("favicon.svg"),
        },
    ],
    "SHOW_HISTORY": True,  # show/hide "History" button, default: True
    "SHOW_VIEW_ON_SITE": True,  # show/hide "View on site" button, default: True
    "SHOW_BACK_BUTTON": False,  # show/hide "Back" button on changeform in header, default: False
    # ENVIRONMENT
    # "ENVIRONMENT": "sample_app.environment_callback",  # environment name in header
    # "ENVIRONMENT_TITLE_PREFIX": "sample_app.environment_title_prefix_callback",  # environment name prefix in title tag
    # "DASHBOARD_CALLBACK": "sample_app.dashboard_callback",
    # =============================
    "THEME": "dark",  # Force theme: "dark" or "light". Will disable theme switcher
    "LOGIN": {
        "image": lambda request: static("sample/login-bg.jpg"),
        "redirect_after": lambda request: reverse_lazy("admin:APP_MODEL_changelist"),
        # Inherits from `unfold.forms.AuthenticationForm`
        # "form": "apps.forms.CustomLoginForm",
    },
    "STYLES": [
        lambda request: static("css/style.css"),
    ],
    "SCRIPTS": [
        lambda request: static("js/script.js"),
    ],
    "BORDER_RADIUS": "6px",
    "COLORS": {
        "base": {
            "50": "oklch(98.5% .002 247.839)",
            "100": "oklch(96.7% .003 264.542)",
            "200": "oklch(92.8% .006 264.531)",
            "300": "oklch(87.2% .01 258.338)",
            "400": "oklch(70.7% .022 261.325)",
            "500": "oklch(55.1% .027 264.364)",
            "600": "oklch(44.6% .03 256.802)",
            "700": "oklch(37.3% .034 259.733)",
            "800": "oklch(27.8% .033 256.848)",
            "900": "oklch(21% .034 264.665)",
            "950": "oklch(13% .028 261.692)",
        },
        "primary": {
            "50": "oklch(97.7% .014 308.299)",
            "100": "oklch(94.6% .033 307.174)",
            "200": "oklch(90.2% .063 306.703)",
            "300": "oklch(82.7% .119 306.383)",
            "400": "oklch(71.4% .203 305.504)",
            "500": "oklch(62.7% .265 303.9)",
            "600": "oklch(55.8% .288 302.321)",
            "700": "oklch(49.6% .265 301.924)",
            "800": "oklch(43.8% .218 303.724)",
            "900": "oklch(38.1% .176 304.987)",
            "950": "oklch(29.1% .149 302.717)",
        },
        "font": {
            "subtle-light": "var(--color-base-500)",  # text-base-500
            "subtle-dark": "var(--color-base-400)",  # text-base-400
            "default-light": "var(--color-base-600)",  # text-base-600
            "default-dark": "var(--color-base-300)",  # text-base-300
            "important-light": "var(--color-base-900)",  # text-base-900
            "important-dark": "var(--color-base-100)",  # text-base-100
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "fr": "🇫🇷",
                "nl": "🇧🇪",
            },
        },
    },
    "SIDEBAR": {
        "show_search": False,  # Search in applications and models names
        "command_search": False,  # Replace the sidebar search with the command search
        "show_all_applications": False,  # Dropdown with all applications and models
        "navigation": [
            {
                "title": _("Dashboard"),
                "separator": False,
                "collapsible": False,
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:index"),
                        # "badge": "apps.badge_callback",
                        # "badge_variant": "info",  # info, success, warning, primary, danger
                        # "badge_style": "solid",  # background fill style
                        "permission": lambda request: request.user.is_superuser,
                    },
                ],
            },
            {
                "title": _("Users & Profiles"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "people",
                        "link": reverse_lazy("admin:users_user_changelist"),
                    },
                    {
                        "title": _("User Profiles"),
                        "icon": "person",
                        "link": reverse_lazy("admin:users_userprofile_changelist"),
                    },
                    {
                        "title": _("Password Reset OTPs"),
                        "icon": "lock_reset",
                        "link": reverse_lazy("admin:users_passwordresetotp_changelist"),
                    },
                    # rest_framework_simplejwt.token_blacklist pages
                    {
                        "title": _("Token Blacklist"),
                        "icon": "vpn_key_off",
                        "link": reverse_lazy(
                            "admin:token_blacklist_blacklistedtoken_changelist"
                        ),
                    },
                    {
                        "title": _("Outstanding Tokens"),
                        "icon": "key_off",
                        "link": reverse_lazy(
                            "admin:token_blacklist_outstandingtoken_changelist"
                        ),
                    },
                ],
            },
            {
                "title": _("CMS"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Pages"),
                        "icon": "article",
                        "link": reverse_lazy("admin:cms_page_changelist"),
                    },
                    {
                        "title": _("Page Sections"),
                        "icon": "view_sidebar",
                        "link": reverse_lazy("admin:cms_pagesection_changelist"),
                    },
                    {
                        "title": _("Feature Items"),
                        "icon": "star",
                        "link": reverse_lazy("admin:cms_featureitem_changelist"),
                    },
                ],
            },
            {
                "title": _("System Settings"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("General Settings"),
                        "icon": "settings",
                        "link": reverse_lazy(
                            "admin:system_settings_generalsetting_changelist"
                        ),
                    },
                    {
                        "title": _("Social Media"),
                        "icon": "share",
                        "link": reverse_lazy(
                            "admin:system_settings_socialmedia_changelist"
                        ),
                    },
                    {
                        "title": _("Privacy Policy"),
                        "icon": "privacy_tip",
                        "link": reverse_lazy(
                            "admin:system_settings_privacypolicy_changelist"
                        ),
                    },
                ],
            },
            {
                "title": _("Contact & Support"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Contact Us Messages"),
                        "icon": "support_agent",
                        "link": reverse_lazy(
                            "admin:contact_support_contactus_changelist"
                        ),
                    },
                ],
            },
            {
                "title": _("Subscriptions"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Plans"),
                        "icon": "local_offer",
                        "link": reverse_lazy("admin:subscriptions_plan_changelist"),
                    },
                    {
                        "title": _("Features"),
                        "icon": "star_border",
                        "link": reverse_lazy("admin:subscriptions_feature_changelist"),
                    },
                ],
            },
        ],
    },
}
