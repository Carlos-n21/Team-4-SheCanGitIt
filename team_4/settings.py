"""
Django settings for team_4 project.
"""

from pathlib import Path
import os
import dj_database_url # type: ignore
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DEBUG", "True") != "False"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1,.herokuapp.com").split(",")


# Application definition

INSTALLED_APPS = [
    # predefined django apps
    'jazzmin',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'channels',  # for async messaging
    'daphne',  # for async messaging, must be placed before django.contrib.staticfiles
    'django.contrib.staticfiles',

    #cloudinary
    'cloudinary',
    'cloudinary_storage',

    #allauth
    'allauth',
    'allauth.account',
    # 'allauth.socialaccount',
     
    # custom project apps
    'affirmation',
    'chat',
    'her_buddies',
    'her_mentor',
    'her_story',
    'user_profile',
    'home',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default auth backend
    'allauth.account.auth_backends.AuthenticationBackend',  # Django Allauth
]

# Configure Allauth
ACCOUNT_LOGIN_METHODS = ['email']  # Use email instead of username
ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*']
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_SIGNUP_REDIRECT_URL = '/'  # Redirect after sign-up
ACCOUNT_LOGOUT_REDIRECT_URL = '/'  # Redirect after logout
LOGIN_REDIRECT_URL = '/'  # Redirect after login
ACCOUNT_EMAIL_VERIFICATION = 'none'

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@shecangitit.com'

MIDDLEWARE = [
    'allauth.account.middleware.AccountMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.template.context_processors.request',
]

ROOT_URLCONF = 'team_4.urls'

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'team_4.wsgi.application'

ASGI_APPLICATION = 'team_4.asgi.application'

REDIS_URL = os.getenv("REDISCLOUD_URL", "redis://localhost:6379")

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [REDIS_URL],
        },
    },
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = os.getenv("SESSION_COOKIE_SECURE", True)
CSRF_COOKIE_SECURE = os.getenv("CSRF_COOKIE_SECURE", True)

CSRF_TRUSTED_ORIGINS = [
    'https://sparksync-test-baedaeaf485c.herokuapp.com',
    'wss://sparksync-test-baedaeaf485c.herokuapp.com',
    'http://192.168.178.48:8000',
]


# Database Configuration (Using DATABASE_URL)
DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600) if DATABASE_URL else {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static", 
]

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET')
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = 'https://res.cloudinary.com/{}/'.format(os.getenv('CLOUDINARY_CLOUD_NAME'))


# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
