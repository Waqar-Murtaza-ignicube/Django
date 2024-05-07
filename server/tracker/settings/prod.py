from .base import *

DEBUG = False

ALLOWED_HOSTS = ["tracker.vercel.app"]

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tracker',
        'USER': 'admin',
        'PASSWORD': 'admin@12345',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# CORS Settings for Production
CORS_ALLOWED_ORIGINS = [
    "tracker.vercel.app"
]

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
