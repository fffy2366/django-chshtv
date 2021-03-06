#-*-coding:utf-8-*- 
"""
Django settings for chshtvp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!_z-qg3uh&vr!uj_j(#o(4@(_@1xj79q4g4-y-&py&t6(-^h9&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cms',
    #'cms.middleware.exceptions',
    'captcha',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.exceptions.ExceptionMiddleware',
)

ROOT_URLCONF = 'chshtvp.urls'

WSGI_APPLICATION = 'chshtvp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'chshtvp',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',                  
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
STATIC_ROOT = os.path.join(os.path.dirname(PROJECT_ROOT),'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    ("backstage",os.path.join(STATIC_ROOT,'backstage')),
    ("css",os.path.join(STATIC_ROOT,'css')),
    ("js",os.path.join(STATIC_ROOT,'js')),
    ("img",os.path.join(STATIC_ROOT,'img')),
    ("video",os.path.join(STATIC_ROOT,'video')),
    ("swf",os.path.join(STATIC_ROOT,'swf')),
    )

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

SITE_NAME = 'CMS'

LOGIN_URL = '/backstage/login'
