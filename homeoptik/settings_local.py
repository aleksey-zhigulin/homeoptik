__author__ = 'aleksey'

import os
import dj_database_url

DEBUG = True
TEMPLATE_DEBUG = True
SQL_DEBUG = True

location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)

# DATABASES = {'default': dj_database_url.config(default='postgres://homeoptik:kBcwGP@185.58.204.167:5432/homeoptik_db')}
# Use a Sqlite database by default
DATABASES = {'default': dj_database_url.config(default='postgres://kbnzibvwndmgwt:5kFaSFUdgzkGpJrVwZSuVMarim@ec2-54-243-149-147.compute-1.amazonaws.com:5432/dehb58j6jcp7tg')}

DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'

MEDIA_ROOT = location("public/media")
STATIC_ROOT = location('public/static')
LOG_ROOT = location('logs')

COMPRESS_ENABLED = False

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}