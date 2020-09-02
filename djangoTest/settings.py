"""
Django settings for djangoTest project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os, django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h!4q%@w(s3t=po(e*nf+7-*p3!gosae^l0@$97s@&qo83!5c3k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['https://allan-crm1.herokuapp.com', 'localhost']

# Application definition

INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # own apps
        'accounts.apps.AccountsConfig',
        'django_filters',
        'storages'  # used for AWS S3 buckets storages
        ]

MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware' #to handle heroku for staticfiles
        ]

ROOT_URLCONF = 'djangoTest.urls'

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

WSGI_APPLICATION = 'djangoTest.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'demo_1',
                'USER': 'postgres',
                'PASSWORD': 'enterpwforpostgres',
                'HOST': 'database-1.c418exvvduzm.us-east-2.rds.amazonaws.com',
                'PORT': '5432'

                }
        }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Hong_Kong'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
key1 = '5bJocJ3NHXOM6cEl9lNlj'
key2 = 'AKIA54BDMJ55ALWWBHUH'



STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#
STATIC_URL = '/static/'
MEDIA_URL = '/images/'
STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
        # to find the dir where storing static files
        ]

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

# SMTP setting
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # remember to type it correct
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'djangotestforallan@gmail.com'
EMAIL_HOST_PASSWORD = 'allanfortestdjango'

# S3 BUCKETS CONFIG
AWS_S3_HOST = "s3.us-east-2.amazonaws.com"
AWS_S3_REGION_NAME = "us-east-2"
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_ACCESS_KEY_ID = key1+key2
AWS_SECRET_ACCESS_KEY = 'WmpVwL49tqAorgaotSl'
AWS_STORAGE_BUCKET_NAME = 'allan-crm1-bucket'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

django_heroku.settings(locals())
