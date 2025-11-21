"""
Django Settings - Production Configuration
"""

from .base import *
import dj_database_url

DEBUG = False

# Allowed Hosts für Railway
ALLOWED_HOSTS = [
    '.railway.app',
    'lorchpro.up.railway.app',
] + config('DJANGO_ALLOWED_HOSTS', default='').split(',')

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    'https://*.railway.app',
]

# Railway Proxy-Header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Security Settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# WhiteNoise für Static Files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Database mit SSL (Railway)
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=600,
        ssl_require=True
    )

