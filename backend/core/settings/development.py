"""
Django Settings - Development Configuration
"""

from .base import *

DEBUG = True

# Django Extensions nur hinzufügen wenn installiert
try:
    import django_extensions  # noqa
    INSTALLED_APPS += ['django_extensions']
except ImportError:
    pass

# Erweiterte CORS für lokale Entwicklung
CORS_ALLOWED_ORIGINS += [
    'http://localhost:3001',
]

