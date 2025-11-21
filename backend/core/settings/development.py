"""
Django Settings - Development Configuration
"""

from .base import *

DEBUG = True

INSTALLED_APPS += [
    'django_extensions',
]

# Erweiterte CORS für lokale Entwicklung
CORS_ALLOWED_ORIGINS += [
    'http://localhost:3001',
]

