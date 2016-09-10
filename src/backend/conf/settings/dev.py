# -*- coding: utf-8 -*-

from .base import Base

class Dev(Base):
    DEBUG = True

    SECRET_KEY='123456789abcdefghijklmnopqrsutvwxyz'

    # django-debug-toolbar
    MIDDLEWARE_CLASSES = Base.MIDDLEWARE_CLASSES + [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]

    INSTALLED_APPS = Base.INSTALLED_APPS + [
        'debug_toolbar',
    ]

    DEBUG_TOOLBAR_CONFIG = {
        'DISABLE_PANELS': [
            'debug_toolbar.panels.redirects.RedirectsPanel',
        ],
        'SHOW_TEMPLATE_CONTEXT': True,
    }

    TEST_RUNNER = 'django.test.runner.DiscoverRunner'



    # We should use JSON API, but we have encountered some issues
    REST_FRAMEWORK = {
        'DEFAULT_PARSER_CLASSES': (
            'rest_framework.parsers.JSONParser',
            'rest_framework.parsers.FormParser',
            'rest_framework.parsers.MultiPartParser'
        ),
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        'TEST_REQUEST_DEFAULT_FORMAT' : 'json'
    }
