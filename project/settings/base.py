"""
Django settings for paysensetask project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import json
import os
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.core.exceptions import ImproperlyConfigured
import cloudinary

BASE_DIR = Path(__file__).parents[2]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

def get_secret(setting):
    file_path = str(BASE_DIR / 'project' / 'settings' / 'secrets.json')
    try:
        with open(file_path) as file:
            secrets = json.loads(file.read())
            try:
                return secrets[setting]
            except KeyError:
                error_message = "Set the {0} environment variable".format(setting)
                raise ImproperlyConfigured(error_message)
    except FileNotFoundError:
        error_message = "secrets.json not found in settings folder"
        raise ImproperlyConfigured(error_message)


SECRET_KEY = get_secret("SECRET_KEY")

SECRET_TOKEN = get_secret("SECRET_TOKEN")

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '^b#h7p2)kt861_apojnr$if4727pc4moepuwy0wg(p4x@osofp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["api.example.com"]


# Application definition

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'oauth2_provider',
    'corsheaders',
    'rest_framework_swagger',
    'miscellaneous',
    'social.apps.django_app.default'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    # 'social.backends.facebook.FacebookOAuth2',
    # 'social.backends.google.GoogleOAuth2',
    # 'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)


ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
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

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)

SOCIAL_AUTH_PROVIDERS = ['facebook', 'google-plus']

SOCIAL_AUTH_GOOGLE_PLUS_SCOPE = [
    'openid', 'profile', 'email'
]

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'

# FSM_ADMIN_FORCE_PERMIT = True


WSGI_APPLICATION = 'project.wsgi.application'

#LOGIN_REDIRECT_URL = 'http:localhost:8000/api/web/v1/instagram/token'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DATABASE_NAME'),
        'USER': get_secret('DATABASE_USER'),
        'PASSWORD': get_secret('DATABASE_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'


REST_FRAMEWORK = {
    'PAGE_SIZE': 100,
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M",
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}
# cors headers settings

CORS_ORIGIN_ALLOW_ALL = False


CORS_ALLOW_CREDENTIALS = False
CORS_REPLACE_HTTPS_REFERER = False

CORS_ALLOW_METHODS = (
        'GET',
        'POST',
        'PUT',
        'PATCH',
        'DELETE',
        'OPTIONS'
    )
CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    "http://example.com"
)


OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope'
    },
    'ACCESS_TOKEN_EXPIRE_SECONDS': 343432,
    'REFRESH_TOKEN_EXPIRE_SECONDS': 31232423
}

EXCEPTION_MASKING = False