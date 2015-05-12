"""Prod site settings."""

from __future__ import absolute_import

from os import environ

from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'feedback',
        'PASSWORD': environ.get('DB_PASSWORD'),
        'USER': 'feedback',
        'HOST': 'feedback.c7cu5t2zxzhk.eu-west-1.rds.amazonaws.com',
        'PORT': '5432',
        'TEST_NAME': 'feedback_test',
    }
}

STATIC_ROOT = '/srv/github_issues/static/'

########## GITHUB ISSUES CONFIGURATION
SOCIAL_AUTH_GITHUB_KEY = 'af784628317f37b22dba'
SOCIAL_AUTH_GITHUB_SECRET = environ.get('GITHUB_CLIENT_SECRET')
