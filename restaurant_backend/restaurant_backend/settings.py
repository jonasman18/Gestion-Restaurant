from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-change-me'

DEBUG = True

ALLOWED_HOSTS = ["*"]

# -------------------------------------------------------
# APPS
# -------------------------------------------------------

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # REST Framework
    'rest_framework',

    # CORS
    'corsheaders',

    # Custom apps
    'restaurant',
    'api',
    'pdf',
    'stats',
]

# -------------------------------------------------------
# MIDDLEWARE
# -------------------------------------------------------

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # doit être tout en haut
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------------------------------------------
# CORS pour Angular
# -------------------------------------------------------

CORS_ALLOW_ALL_ORIGINS = True
# OU plus sécurisé :
# CORS_ALLOWED_ORIGINS = ["http://localhost:4200"]

# -------------------------------------------------------
# URLS
# -------------------------------------------------------

ROOT_URLCONF = 'restaurant_backend.urls'

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

WSGI_APPLICATION = 'restaurant_backend.wsgi.application'

# -------------------------------------------------------
# BASE DE DONNÉES PostgreSQL
# -------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'restaurant',
        'USER': 'postgres',
        'PASSWORD': 'jonasman',  # <--- change ceci
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# -------------------------------------------------------
# VALIDATION DES MOTS DE PASSE
# -------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------------------------------------
# LANGUE & TIMEZONE
# -------------------------------------------------------

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Nairobi'  # Madagascar (UTC+3)

USE_I18N = True
USE_TZ = True

# -------------------------------------------------------
# STATIC FILES
# -------------------------------------------------------

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
