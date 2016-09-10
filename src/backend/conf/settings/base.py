# -*- coding: utf-8 -*-
import os
from configurations import Configuration, values


class Base(Configuration):

    # APP CONFIGURATION
    # -------------------------------------------------------------------------
    DJANGO_APPS = [
        # Default Django apps:
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

    THIRD_PARTY_APPS = [
        'rest_framework',
    ]

    # Apps specific for this project go here.
    LOCAL_APPS = [
        'api.accounts',
    ]

    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

    MIDDLEWARE_CLASSES = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_DIR = '../../..'#environ.Path(__file__) - 3
    APPS_DIR = '../../../api'# ROOT_DIR.path('api')

    DATABASES = values.DatabaseURLValue()

    ROOT_URLCONF = 'conf.urls'
    WSGI_APPLICATION = 'conf.wsgi.application'

    AUTH_USER_MODEL = 'accounts.Account'
    LOGIN_REDIRECT_URL = '/'

    STATIC_URL = '/assets/'

    SECRET_KEY = values.SecretValue()

    # Internationalization
    # https://docs.djangoproject.com/en/dev/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True
