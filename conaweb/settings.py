"""
Django settings for conaweb project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import sys
import dj_database_url
from django.core.management.utils import get_random_secret_key


from django.urls import reverse_lazy
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-$wl44v2skgyz$&hev=a5i(5k)=d02m2v@zt&)_(-t_h$+q#^29'
#[label django_app/settings.py]
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())
# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
#[label django_app/settings.py]
DEBUG = os.getenv("DEBUG", "False") == "True"
#[label django_app/settings.py]
DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"

#ALLOWED_HOSTS = ['arcane-bayou-67214.herokuapp.com','127.0.0.1','https://www.mlcalc.com/', 'clownfish-app-jmsml.ondigitalocean.app','134.122.52.247']
#[label django_app/settings.py]
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
#archivos staticos
DIR_STATIC=os.path.join(BASE_DIR, "conabom/pages/static/")
STATICFILES_DIRS=[DIR_STATIC]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'conabom',
    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conaweb.urls'
DIR_TEMPLATES=os.path.join(BASE_DIR, "conabom/pages/")


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [DIR_TEMPLATES],
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

WSGI_APPLICATION = 'conaweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
#
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'coopnabomberos',
#        'USER': 'conabomadmin',
#        'PASSWORD': 'CoopNaBomberos2021',
#        'HOST': 'localhost',
#        'PORT': '',
#    }
#}
#import dj_database_url
#db_from_env = dj_database_url.config(conn_max_age=600)
#DATABASES["default"].update(db_from_env)
#[label django_app/settings.py]
if DEVELOPMENT_MODE is True:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    if os.getenv("DATABASE_URL", None) is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es-DO'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST="smtp.gmail.com"
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER='cristophermartinez1989@gmail.com'
EMAIL_HOST_PASSWORD="jvkhmmzuoemqrvdp"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'userIndex'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL='login'

MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL = "/media/"


# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'