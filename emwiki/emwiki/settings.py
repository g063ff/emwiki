"""
Django settings for emwiki project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

env = environ.Env(
    DEBUG=(bool, False)
)
env.read_env(os.path.join(BASE_DIR, '.env'))


# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY is written at localsettings.py
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'contents.contents.apps.ContentsConfig',
    'contents.symbol.apps.SymbolConfig',
    'contents.article.apps.ArticleConfig',
    'home.apps.HomeConfig',
    'search.apps.SearchConfig',
    'accounts.apps.AccountsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'emwiki.urls'

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

WSGI_APPLICATION = 'emwiki.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': env.db()
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = '/'

AUTH_USER_MODEL = 'accounts.User'

if DEBUG is True:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

STATIC_ROOT = '/code/static'


ARTICLE_DIR = os.path.join(BASE_DIR, 'contents', 'article')
SYMBOL_DIR = os.path.join(BASE_DIR, 'contents', 'symbol')
CONTENTS_DIR = os.path.join(BASE_DIR, 'contents', 'contents')


RAW_MIZFILE_DIR = os.path.join(BASE_DIR, 'contents', 'mizarfiles', 'mml')
COMMENTED_MIZFILE_DIR = os.path.join(BASE_DIR, 'contents', 'mizarfiles', 'mml_commented')

RAW_HTMLIZEDMML_DIR = os.path.join(BASE_DIR, 'contents', 'mizarfiles', 'htmlized_mml')
PRODUCT_HTMLIZEDMML_DIR = os.path.join(BASE_DIR, 'static', 'htmlized_mml')

PRODUCT_SYMBOLHTML_DIR = os.path.join(BASE_DIR, 'static', 'symbol_html')

STATIC_ARTICLES_URL = STATIC_URL + "htmlized_mml/"
STATIC_SYMBOLS_URL = STATIC_URL + "symbol_html/"


TEST_DATA_DIR = os.path.join(BASE_DIR, 'testdata')

TEST_CACHE_DIR = os.path.join(TEST_DATA_DIR, 'cachedata')

TEST_RAW_MIZFILE_DIR = os.path.join(TEST_DATA_DIR, 'mml')
TEST_COMMENTED_MIZFILE_DIR = os.path.join(TEST_DATA_DIR, 'mml_commented')

TEST_RAW_HTMLIZEDMML_DIR = os.path.join(TEST_DATA_DIR, 'raw_htmlized_mml')
TEST_PRODUCT_HTMLIZEDMML_DIR = os.path.join(TEST_DATA_DIR, 'product_htmlized_mml')
