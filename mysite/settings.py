"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'app',
    'accounts',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'ec',
    'appointment',
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

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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

AUTH_USER_MODEL = 'accounts.CustomUser'
ACCOUNT_ADAPTER = 'accounts.adapter.AccountAdapter'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_EMAIL_VERIFICATION = 'none'

# 画像
MEDIA_URL = '/app/static/img/'

# Stripe
STRIPE_SECRET_KEY = 'sk_test_51HbJXRA2iF7L75ITTqxYqvhZfpTpb6ewZbRz50QKWldxpdHIOh9bdSeoPmQOU2tEYtXZyGRR3uc13PCdz9gOKNEO00Ls75qgVD'

# デプロイ設定
DEBUG = False

try:
    from .local_settings import *
except ImportError:
    pass

# ローカル環境設定
if DEBUG:
    ALLOWED_HOSTS = ['*']
    # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'app/static/img/')
else:
    import environ
    env = environ.Env()
    env.read_env(os.path.join(BASE_DIR, '.env'))

    SECRET_KEY = env('SECRET_KEY')
    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    # EMAIL_HOST = 'smtp.gmail.com'
    # EMAIL_PORT = 587
    # EMAIL_HOST_USER = 'xxx@gmail.com'
    # EMAIL_HOST_PASSWORD = 'xxx'
    # EMAIL_USE_TLS = True

    STATIC_ROOT = '/usr/share/nginx/html/static'
    MEDIA_ROOT = '/user/share/nginx/html/app/static/img/'