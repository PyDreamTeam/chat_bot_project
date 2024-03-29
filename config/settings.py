"""
Django settings for chat_bot_project project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta
from typing import Dict, Any

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# environ init
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env() # reading .env file

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS', default=[]))


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djoser', #djoser 
    'corsheaders',  #cors   
    'rest_framework_simplejwt', #JWT authentication backend library
    'rest_framework_simplejwt.token_blacklist',
    'accounts',
    'favorite',
    'platforms',
    'solutions',
    'orders',
    'drf_spectacular', #specification
    'django_celery_beat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # middleware for cors-headers
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'accounts/templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# DATABASE CONFIG
DATABASES = {
    'default': {
        'ENGINE': env.str('DATABASE_ENGINE'),
        'NAME': env.str('DATABASE_NAME'),
        'USER': env.str('DATABASE_USER'),
        'PASSWORD': env.str('DATABASE_PASSWORD'),
        'HOST': env.str('DATABASE_HOST'),
        'PORT': env.str('DATABASE_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {    
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
    'DEFAULT_AUTHENTICATION_CLASSES': [        
        "rest_framework_simplejwt.authentication.JWTAuthentication" #JWT
        #'rest_framework.authentication.TokenAuthentication',  # djoser
        #'rest_framework.authentication.BasicAuthentication',
        #'rest_framework.authentication.SessionAuthentication', 

    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated"
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


#drf-spectacular SPECTACULAR_SETTINGS
SPECTACULAR_SETTINGS: Dict[str, Any] = {
    # path prefix
    'SCHEMA_PATH_PREFIX': r'/api/v[0-9]',
    # swagger settings
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'filter': True,
    },
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
    'ENABLE_LIST_MECHANICS_ON_NON_2XX': True,
    # schema metadata
    'TITLE': 'Chat-Bot API',
    'DESCRIPTION': 'This is a API for a Chat-Bot store',
    'VERSION': '1.0.1',
    'CONTACT': {
        "name": "API Support",
        "url": "http://www.example.com/support",
        "email": "support@example.com"
    },
}


# SMTP CONFIG
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = 'smtp-mail.outlook.com' # 'smtp.mailgun.org'
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER')
DEFAULT_FROM_EMAIL = env.str('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587


# DJOSER CONFIG
DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True, # True is only required re_password
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": False,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "SET_USERNAME_RETYPE": False,
    "SET_PASSWORD_RETYPE": True,
    "USERNAME_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "PASSWORD_RESET_CONFIRM_URL": "change-password?uid={uid}&token={token}",
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "ACTIVATION_URL": "?uid={uid}&token={token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SOCIAL_AUTH_TOKEN_STRATEGY": "djoser.social.token.jwt.TokenStrategy",
    "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": [
        "your redirect url",
        "your redirect url",
    ],
    "SERIALIZERS": {
        "user_create": "djoser.serializers.UserCreateSerializer", 
        'user_create_password_retype': 'accounts.serializers.UserCreatePasswordRetypeSerializer',  # custom serializer
        "user": "djoser.serializers.UserSerializer",
        "current_user": "djoser.serializers.UserSerializer",
        "user_delete": "djoser.serializers.UserSerializer",
        'password_reset': 'accounts.serializers.PasswordResetSerializer', # custom serializer
        'password_reset_confirm': 'djoser.serializers.PasswordResetConfirmSerializer',  
        'password_reset_confirm_retype': 'djoser.serializers.PasswordResetConfirmRetypeSerializer',
        'activation': 'djoser.serializers.ActivationSerializer',   
        'set_password': 'djoser.serializers.SetPasswordSerializer',
        'set_password_retype': 'djoser.serializers.SetPasswordRetypeSerializer',
        'set_username': 'djoser.serializers.SetUsernameSerializer',
        'set_username_retype': 'djoser.serializers.SetUsernameRetypeSerializer',       
        'username_reset': 'djoser.serializers.SendEmailResetSerializer',
        'username_reset_confirm': 'djoser.serializers.UsernameResetConfirmSerializer',
        'username_reset_confirm_retype': 'djoser.serializers.UsernameResetConfirmRetypeSerializer',       
        'token': 'djoser.serializers.TokenSerializer',
        'token_create': 'djoser.serializers.TokenCreateSerializer',  
    },
    "EMAIL": {
        'activation': 'accounts.email.ActivationEmail', # custom
        'confirmation': 'accounts.email.ConfirmationEmail', # custom ConfirmationEmail
        'password_reset': 'accounts.email.PasswordResetEmail', # custom
        'password_changed_confirmation': 'accounts.email.PasswordChangedConfirmationEmail', # custom
        'username_changed_confirmation': 'accounts.email.UsernameChangedConfirmationEmail', # custom
        'username_reset': 'accounts.email.UsernameResetEmail', # custom
    },
    "CONSTANTS": {
        'messages': 'djoser.constants.Messages',
    },
}


# JWT CONFIG
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=1440),  # can be changed
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    
    'AUTH_HEADER_TYPES': ('JWT',),   
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION", 
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}


# CORS CONFIG
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'origin',
    'dnt',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'access-control-allow-methods',
    'content-disposition',
]
# CORS_ALLOWED_ORIGINS = [
#     'http://python.twnsnd.online',
#     'https://python.twnsnd.online',    
# ]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.User' #new model user

CELERY_BROKER_URL = f"redis://{env.str('CELERY_HOST')}:{env.str('CELERY_PORT')}"
CELERY_RESULT_BACKEND = f"redis://{env.str('CELERY_HOST')}:{env.str('CELERY_PORT')}"
CELERY_IMPORTS = ["accounts.tasks"]

SUPERUSER_EMAIL = env.str('SUPERUSER_EMAIL')
SUPERUSER_PASSWORD = env.str('SUPERUSER_PASSWORD')