# -*- coding: UTF-8 -*-
"""
Django settings for myBlog project.

Generated by 'django-admin startproject' using Django 1.9

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
from django.conf.global_settings import STATICFILES_DIRS

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=%@(+89m7w&$o5m*9(4b=y*jrs%zgq%p#h1wu#8y1xett=h5*f'

# SECURITY WARNING: don't run with debug turned on in production!
# 正式部署的时候更改为false
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'personal',
    'easy_thumbnails',
    'wechat',
    'rest_framework',
    'blogapi',
]

# 1.10之前，中间件的key为MIDDLEWARE_CLASSES, 1.10之后，为MIDDLEWARE
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+'/templates'],
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

WSGI_APPLICATION = 'myBlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/
# en-us:英语环境
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# 通过 AUTH_USER_MODEL 指定自定义用户模型所在的位置
AUTH_USER_MODEL = 'personal.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

# 七牛云存储相关配置 pip install django-qiniu-storage
QINIU_ACCESS_KEY = 'y8_ShQVjyL9IB2hebzp2HnD0PYvZfqxcGRWP0Ev7'
QINIU_SECRET_KEY = '59Pf8MxWLnLAfzqJdZGRpLZdXnjl4Bets-212d0T'
QINIU_BUCKET_NAME = 'wj5633'
QINIU_BUCKET_DOMAIN = 'ompehspge.bkt.clouddn.com/'
QINIU_SECURE_URL = False      # 使用http 

PREFIX_URL = 'http://'

# MEDIA_URL = PREFIX_URL + QINIU_BUCKET_DOMAIN + '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\','/')

# DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuMediaStorage' 

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\','/')
IMAGE_PREFIX = 'gallery'

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)


# 配置缩略图大小，方便在模板中使用
THUMBNAIL_ALIASES = {
  '': {
    'thumbnail' : {'size': (150,150), 'crop':True},
  },
}
