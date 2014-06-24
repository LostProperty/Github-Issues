"""Dev site settings."""

from __future__ import absolute_import

from os.path import join

from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'feedback',
        'PASSWORD': 'foosh4ohThaiqu', # TODO: move to environment variable
        'USER': 'feedback',
        'HOST': 'feedback.c7cu5t2zxzhk.eu-west-1.rds.amazonaws.com',
        'PORT': '5432',
        'TEST_NAME': 'feedback_test',
    }
}

STATIC_ROOT = '/srv/static/feedback/'

# TODO: add logging here (use sentry?)
