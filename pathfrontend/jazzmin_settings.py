"""
Jazzmin settings for enhanced admin UI with focus on permissions and authorizations
"""

# Title and branding
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Path Admin",
    
    # Title on the brand, and login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Path Administration",
    
    # Logo to use for your site, must be present in static files (defaults to site_logo if absent or None)
    "site_logo": "img/logo.png",
    
    # Logo to use for login form (defaults to site_logo if absent or None)
    "login_logo": None,
    
    # Welcome text on the login screen
    "welcome_sign": "Welcome to Pathways  Administration",
    
    # Copyright on the footer
    "copyright": "Path Ltd",
    
    # List of model admins to search from the search bar
    "search_model": ["auth.User", "auth.Group"],
    
    # The model admin to search from the search bar
    "search_model": ["auth.User", "auth.Group", "hall.Hall", "hall.EventType", "hall.Facility"],
    
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,
    
    ############
    # Top Menu #
    ############
    
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
        
        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "hall"},
        
        # External url that opens in a new window (Permissions can be added)
        {"name": "Support", "url": "https://github.com/yourgithub/path/issues", "new_window": True},
    ],
    
    #############
    # User Menu #
    #############
    
    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/yourgithub/path/issues", "new_window": True},
        {"model": "auth.user"}
    ],
    
    #############
    # Side Menu #
    #############
    
    # Whether to display the side menu
    "show_sidebar": True,
    
    # Whether to aut expand the menu
    "navigation_expanded": True,
    
    # List of apps to base side menu ordering off of
    "order_with_respect_to": ["auth", "hall", "dashboard"],
    
    # Custom icons for side menu apps/models (Shown at the top of the sidebar)
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "auth.Permission": "fas fa-key",
        "hall.Hall": "fas fa-building",
        "hall.EventType": "fas fa-calendar-alt",
        "hall.Facility": "fas fa-concierge-bell",
    },
    
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    
    #############
    # UI Tweaks #
    #############
    
    # Render out the modals instead of popups
    "related_modal_active": True,
    
    # Custom CSS for all pages
    "custom_css": None,
    
    # Custom JS for all pages
    "custom_js": None,
    
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
}

# Configure Jazzmin UI settings
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": True
}
