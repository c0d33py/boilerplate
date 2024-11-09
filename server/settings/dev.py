from .base import *

DEBUG = True

# Development settings
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INTERNAL_IPS = ['127.0.0.1']

# Security settings & CORS
X_FRAME_OPTIONS = 'SAMEORIGIN'
CSRF_COOKIE_SAMESITE = 'strict'
CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:5500',
]

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5500',
]
CORS_ALLOW_CREDENTIALS = True
