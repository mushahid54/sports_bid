__author__ = 'MushahidKhan'

from ..local import *

EXCEPTION_MASKING = False
# INSTALLED_APPS.remove('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'summerlabel',
        'PASSWORD': 'admin123',
        'HOST': '127.0.0.1',
        'PORT': '5432',  # you can change this like: DATABASES['default']['PORT'] = 'some_other_port'
    }
}