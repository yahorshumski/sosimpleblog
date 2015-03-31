"""
Django settings for blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
import dj_database_url

if socket.gethostname().startswith('precise32'):
    LIVEHOST = False
else: 
    LIVEHOST = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y#&d5ypjc$edx!an=(r4uxxeul+93tau@81kjz3s#bd7us^-8&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogengine',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.syndication',

)

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'blog.urls'

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


if LIVEHOST:
    # DEBUG = True
    # PREPEND_WWW = False
    # MEDIA_URL = 'http://static1.grsites.com/'
    DATABASES = {}
    DATABASES['default'] =  dj_database_url.config()
    DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = 'staticfiles'
    STATIC_URL = '/static/'
    TEMPLATE_DIRS = '/app/templates/'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

else:
    DEBUG = True
    TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

    # PREPEND_WWW = False
    # MEDIA_URL = 'http://localhost:8000/static/'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'blogdb',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'shumski',
            'PASSWORD': 'qwert123',
            'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
            'client_encoding': 'UTF8',
        }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Template directory

INSTALLED_APPS += ('django_jenkins',)
JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    # 'django_jenkins.tasks.with_coverage',
)
PROJECT_APPS = ['blogengine']