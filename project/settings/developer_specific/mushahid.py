__author__ = 'MushahidKhan'

EXCEPTION_MASKING = False
# INSTALLED_APPS.remove('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'datebase',
        'USER': 'database_user',
        'PASSWORD': '32232',
        'HOST': '127.0.0.1',
        'PORT': '5432',  # you can change this like: DATABASES['default']['PORT'] = 'some_other_port'
    }
}