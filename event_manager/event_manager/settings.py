from pathlib import Path
import environ
import ldap
from django_auth_ldap.config import (
    LDAPSearch,
    LDAPGroupQuery,
    GroupOfNamesType,
    PosixGroupType,
)

from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(BASE_DIR / ".env")
env = environ.Env(
    DEBUG=(bool, False),  # cast to boolean, default is False
)

MESSAGE_TAGS = {
    messages.DEBUG: "alert-secondary",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

# install django-environ and set the .env File
SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "events",
    "crispy_forms",
    "crispy_bootstrap5",
    "pages",
    "rest_framework",
    "rest_framework.authtoken",  # will generate DB table
    "drf_spectacular",
    "drf_spectacular_sidecar",
]

CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = ("bootstrap5",)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    INSTALLED_APPS.extend([
        "debug_toolbar",
        "django_extensions",
    ])

    MIDDLEWARE.extend([
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ])

    DEBUG_TOOLBAR_CONFIG = {
        "INTERCEPT_REDIRECTS": False,
    }
    INTERNAL_IPS = ("127.0.0.1",)


ROOT_URLCONF = 'event_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "event_manager" / "templates"],
        'APP_DIRS': True,  # look in the apps for template-directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Event Manager API',
    'DESCRIPTION': 'Django Event manager',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',

    # OTHER SETTINGS
}


WSGI_APPLICATION = 'event_manager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LOGIN_REDIRECT_URL = '/'  # go there after login
LOGOUT_REDIRECT_URL = '/' # go there after logout

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'  # de-de

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# LDAP SETTINGS
AUTH_LDAP_SERVER_URI = 'ldap://192.168.178.40'
AUTH_LDAP_BIND_DN = 'cn=admin,dc=example,dc=com'
AUTH_LDAP_BIND_PASSWORD = 'secret_password'
AUTH_LDAP_USER_SEARCH = LDAPSearch('dc=example,dc=com',ldap.SCOPE_SUBTREE, '(uid=%(user)s)')
AUTH_LDAP_GROUP_SEARCH = LDAPSearch('dc=example,dc=com',ldap.SCOPE_SUBTREE, '(objectClass=top)')
AUTH_LDAP_GROUP_TYPE = PosixGroupType(name_attr="cn")

# Populate the Django user from the LDAP directory.
AUTH_LDAP_REQUIRE_GROUP = "cn=enabled+gidNumber=501,ou=groups,dc=example,dc=com"
AUTH_LDAP_MIRROR_GROUPS = True

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
    "username": "uid",
    "password": "userPassword",
}

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=active+gidNumber=500,ou=groups,dc=example,dc=com",
    "is_staff": "cn=staff+gidNumber=503,ou=groups,dc=example,dc=com",
    "is_superuser": "cn=superuser+gidNumber=502,ou=groups,dc=example,dc=com"
}

AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_TIMEOUT = 3600

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',  # ldap auth
    'django.contrib.auth.backends.ModelBackend', # standard auth
)