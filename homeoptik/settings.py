# -*- coding: utf-8 -*-

from decimal import Decimal as D

import os
import sys

# Path helper
PROJECT_DIR = os.path.dirname(__file__)
location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)
PY3 = sys.version_info >= (3, 0)

USE_TZ = True

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SQL_DEBUG = DEBUG

ALLOWED_HOSTS = ['homeoptik.ru',]

ADMINS = (
    ('Aleksey Zhigulin', 'a.a.zhigulin@yandex.ru'),
)
EMAIL_SUBJECT_PREFIX = '[HomeOptik] '
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'noreply@homeoptik.ru'
EMAIL_HOST_PASSWORD = '2QPr86'
DEFAULT_FROM_EMAIL = 'noreply@homeoptik.ru'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
SERVER_EMAIL = DEFAULT_FROM_EMAIL

CONTACT_FORM_BCC = 'info@homeoptik.ru'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'homeoptik_db',
        'USER': 'homeoptik',
        'PASSWORD': 'kBcwGP',
        'HOST': '',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru_RU'

# Includes all languages that have >50% coverage in Transifex
# Taken from Django's default setting for LANGUAGES
gettext_noop = lambda s: s
LANGUAGES = (
    #('en-gb', gettext_noop('British English')),
    #('zh-cn', gettext_noop('Simplified Chinese')),
    #('nl', gettext_noop('Dutch')),
    #('it', gettext_noop('Italian')),
    #('pl', gettext_noop('Polish')),
    ('ru_RU', gettext_noop('Russian')),
    #('sk', gettext_noop('Slovak')),
    #('pt-br', gettext_noop('Brazilian Portuguese')),
    #('fr', gettext_noop('French')),
    #('de', gettext_noop('German')),
    #('ko', gettext_noop('Korean')),
    #('uk', gettext_noop('Ukrainian')),
    #('es', gettext_noop('Spanish')),
    #('da', gettext_noop('Danish')),
    #('ar', gettext_noop('Arabic')),
    #('ca', gettext_noop('Catalan')),
    #('cs', gettext_noop('Czech')),
    #('el', gettext_noop('Greek')),
)

# ROSETTA_STORAGE_CLASS = 'rosetta.storage.SessionRosettaStorage'
ROSETTA_STORAGE_CLASS = 'rosetta.storage.CacheRosettaStorage'
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
ROSETTA_REQUIRES_AUTH = False
ROSETTA_WSGI_AUTO_RELOAD = True
LOCALE_PATHS = (
    location('locale'),
        location('../forked/newsletter_subscription/locale'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = location("../media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = '/media/admin/'

STATIC_URL = '/static/'
STATIC_ROOT = location('../static')
STATICFILES_DIRS = (
    location('static/'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '9_dh*7ko+n8)@^0^_vhqi^(3v$!*o9h1e&7*qzf(ya@g8y^86j'

# List of callables that know how to import templates from various sources.

TEMPLATE_LOADERS = (
     ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        # needed by django-treebeard for admin (and potentially other libs)
        'django.template.loaders.eggs.Loader',
     )),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    # Oscar specific
    'oscar.apps.search.context_processors.search_form',
    'oscar.apps.promotions.context_processors.promotions',
    'oscar.apps.checkout.context_processors.checkout',
    'oscar.core.context_processors.metadata',
    'oscar.apps.customer.notifications.context_processors.notifications',
    # Custom
    'homeoptik.context_processors.subscribe_form',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.transaction.TransactionMiddleware',
    'forked.flatpages.middleware.FlatpageFallbackMiddleware',
    # Allow languages to be selected
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    # Ensure a valid basket is added to the request instance for every request
    'oscar.apps.basket.middleware.BasketMiddleware',
    # Enable the ProfileMiddleware, then add ?cprofile to any
    # URL path to print out profile details
    'oscar.profiling.middleware.ProfileMiddleware',
)

ROOT_URLCONF = 'homeoptik.urls'

# Add another path to Oscar's templates.  This allows templates to be
# customised easily.
from oscar import OSCAR_MAIN_TEMPLATE_DIR
TEMPLATE_DIRS = (
    location('templates'),
    location('templates/oscar'),
   # OSCAR_MAIN_TEMPLATE_DIR,
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
        },
        'simple': {
            'format': '[%(asctime)s] %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'checkout_file': {
            'level': 'INFO',
            'class': 'oscar.core.logging.handlers.EnvFileHandler',
            'filename': 'checkout.log',
            'formatter': 'verbose'
        },
        'gateway_file': {
            'level': 'INFO',
            'class': 'oscar.core.logging.handlers.EnvFileHandler',
            'filename': 'gateway.log',
            'formatter': 'simple'
        },
        'error_file': {
            'level': 'INFO',
            'class': 'oscar.core.logging.handlers.EnvFileHandler',
            'filename': 'errors.log',
            'formatter': 'verbose'
        },
        'sorl_file': {
            'level': 'INFO',
            'class': 'oscar.core.logging.handlers.EnvFileHandler',
            'filename': 'sorl.log',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
    },
    'loggers': {
        # Django loggers
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'error_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['null'],
            'propagate': False,
            'level': 'DEBUG',
        },
        # Oscar core loggers
        'oscar.checkout': {
            'handlers': ['console', 'checkout_file'],
            'propagate': False,
            'level': 'INFO',
        },
        'oscar.catalogue.import': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'INFO',
        },
        'oscar.alerts': {
            'handlers': ['null'],
            'propagate': False,
            'level': 'INFO',
        },
        # Sandbox logging
        'gateway': {
            'handlers': ['gateway_file'],
            'propagate': True,
            'level': 'INFO',
        },
        # Third party
        'south': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'sorl.thumbnail': {
            'handlers': ['sorl_file'],
            'propagate': True,
            'level': 'INFO',
        },
        # Suppress output of this debug toolbar panel
        'template_timings_panel': {
            'handlers': ['null'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'forked.flatpages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django_extensions',
    # Debug toolbar + extensions
    'debug_toolbar',
    'template_timings_panel',
    'rosetta',          # For i18n testing
    'compressor',
    'widget_tweaks',
    'yandex_money',
    'gunicorn',
    'towel',
    'forked.newsletter_subscription',
    'qwert',
    'homeoptik',
]

from oscar import get_core_apps
INSTALLED_APPS = INSTALLED_APPS + get_core_apps(['forked.checkout',
                                                 'forked.search',
                                                 'forked.catalogue',
                                                 'forked.promotions',
                                                 'forked.dashboard.promotions',
                                                 'forked.dashboard.pages',
                                                 'forked.dashboard.offers',
                                                 'forked.shipping',
                                                 'forked.offer',
                                                 'forked.address',
                                                 'forked.partner',])

# Add Oscar's custom auth backend so users can sign in using their email
# address.
AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.Emailbackend',
    'django.contrib.auth.backends.ModelBackend',
)


LOGIN_REDIRECT_URL = '/'
APPEND_SLASH = True


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr',
        'INCLUDE_SPELLING': True,
        'EXCLUDED_INDEXES': ['forked.search.search_indexes.CoreProductIndex'],
    },
}

# =============
# Debug Toolbar
# =============

# Implicit setup can often lead to problems with circular imports, so we
# explicitly wire up the toolbar

DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'template_timings_panel.panels.TemplateTimings.TemplateTimings',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
INTERNAL_IPS = ['127.0.0.1', '::1']

if PY3:
    # Template timings panel doesn't work with Python 3 atm
    # https://github.com/orf/django-debug-toolbar-template-timings/issues/18
    INSTALLED_APPS.remove('template_timings_panel')
    DEBUG_TOOLBAR_PANELS.remove(
        'template_timings_panel.panels.TemplateTimings.TemplateTimings')


# ==============
# Oscar settings
# ==============

from oscar.defaults import *

# Meta
# ====

OSCAR_SHOP_NAME = 'Home Optik'
OSCAR_SHOP_TAGLINE = 'оптика на дом'
OSCAR_RECENTLY_VIEWED_PRODUCTS = 20
OSCAR_ALLOW_ANON_CHECKOUT = True
OSCAR_DEFAULT_CURRENCY = 'RUB'
OSCAR_CURRENCY_FORMAT = u'#,##0 ¤'


OSCAR_PRODUCTS_PER_PAGE = 12
OSCAR_OFFERS_PER_PAGE = 12
OSCAR_REVIEWS_PER_PAGE = 12
OSCAR_NOTIFICATIONS_PER_PAGE = 12
OSCAR_EMAILS_PER_PAGE = 12
OSCAR_ORDERS_PER_PAGE = 12
OSCAR_ADDRESSES_PER_PAGE = 12
OSCAR_STOCK_ALERTS_PER_PAGE = 12
OSCAR_DASHBOARD_ITEMS_PER_PAGE = 12

OSCAR_REQUIRED_ADDRESS_FIELDS = ('first_name', 'line1', 'city')

OSCAR_FROM_EMAIL = 'noreply@homeoptik.ru'

# Promotions
OSCAR_PROMOTION_POSITIONS = (('page', 'Page'),
                             ('right', 'Right-hand sidebar'),
                             ('left', 'Left-hand sidebar'),
                             ('home_slides', 'Slides on home page'),
                             ('bottom', 'Bottom'))

# Shipping
OSCAR_SHIPPING_PICKUP_EXCL_TAX = D('0.00')
OSCAR_SHIPPING_PICKUP_INCL_TAX = D('0.00')

OSCAR_SHIPPING_COURIER_EXCL_TAX = D('250.00')
OSCAR_SHIPPING_COURIER_INCL_TAX = D('250.00')

OSCAR_SHIPPING_POST_INCL_TAX = D('390.00')
OSCAR_SHIPPING_POST_EXCL_TAX = D('390.00')

OSCAR_SEARCH_FACETS = {
    'queries': OrderedDict([
        ('price_range',
         {
             'name': gettext_noop('Цена'),
             'field': 'price',
             'queries': [
                 # This is a list of (name, query) tuples where the name will
                 # be displayed on the front-end.
                 (gettext_noop('от 0 до 1000 руб.'), u'[0 TO 1000]'),
                 (gettext_noop('от 1000 до 3000 руб.'), u'[1000 TO 3000]'),
                 (gettext_noop('от 3000 до 5000 руб.'), u'[3000 TO 5000]'),
                 (gettext_noop('от 5000 руб.'), u'[5000 TO *]'),
             ]
         }),
    ]),
    'fields': OrderedDict([
        ('brand', {'name': gettext_noop('Бренд'), 'field': 'brand'}),
        ('purpose', {'name': gettext_noop('Назначение'), 'field': 'purpose'}),
        ('lenses_type', {'name': gettext_noop('Тип линз'), 'field': 'lenses_type'}),
        ('material', {'name': gettext_noop('Материал'), 'field': 'material'}),
        ('properties', {'name': gettext_noop('Свойства'), 'field': 'properties'}),
        ('index', {'name': gettext_noop('Индекс уточнения'), 'field': 'index'}),
        ('cover', {'name': gettext_noop('Покрытие'), 'field': 'cover'}),
        ('reflex', {'name': gettext_noop('Остаточный рефлекс'), 'field': 'reflex'}),


        # ('product_class', {'name': gettext_noop('Type'), 'field': 'product_class'}),
        # ('astigmatic', {'name': gettext_noop('Возможность заказал астигматичных линз'), 'field': 'astigmatic'}),
        # ('color', {'name': gettext_noop('Цвет линзы'), 'field': 'color'}),
        # ('design', {'name': gettext_noop('Дизайн'), 'field': 'design'}),
        # ('rating', {'name': gettext_noop('Rating'), 'field': 'rating'}),
        # ('glass_style', {'name': gettext_noop('Form'), 'field': 'glass_style'}),
    ]),
}

PAYMENT_METHODS = (
            ('CASH', u'Наличными курьеру'),
            ('POST', u'Наложенным платежем'),
)

# This is added to each template context by the core context processor.  It is
# useful for test/stage/qa sites where you want to show the version of the site
# in the page title.
DISPLAY_VERSION = False


# Order processing
# ================

# Some sample order/line status settings
OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
    'Processed': (),
}


# LESS/CSS/statics
# ================

# We default to using CSS files, rather than the LESS files that generate them.
# If you want to develop Oscar's CSS, then set USE_LESS=True and
# COMPRESS_ENABLED=False in your settings_local module and ensure you have
# 'lessc' installed.  You can do this by running:
#
#    pip install -r requirements_less.txt
#
# which will install node.js and less in your virtualenv.

USE_LESS = False

COMPRESS_ENABLED = False
# COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',  'compressor.filters.cssmin.CSSMinFilter']
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)
COMPRESS_OFFLINE_CONTEXT = {
    'STATIC_URL': 'STATIC_URL',
    'use_less': USE_LESS,
}

# We do this to work around an issue in compressor where the LESS files are
# compiled but compression isn't enabled.  When this happens, the relative URL
# is wrong between the generated CSS file and other assets:
# https://github.com/jezdez/django_compressor/issues/226
COMPRESS_OUTPUT_DIR = 'oscar'

# Logging
# =======

LOG_ROOT = location('../logs')
# Ensure log root exists
if not os.path.exists(LOG_ROOT):
    os.mkdir(LOG_ROOT)

# Sorl
# ====

THUMBNAIL_DEBUG = True
THUMBNAIL_KEY_PREFIX = 'oscar'

# Use a custom KV store to handle integrity error
# THUMBNAIL_KVSTORE = 'oscar.sorl_kvstore.ConcurrentKVStore'

# Django 1.6 has switched to JSON serializing for security reasons, but it does not
# serialize Models. We should resolve this by extending the
# django/core/serializers/json.Serializer to have the `dumps` function. Also
# in tests/config.py
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
CACHE_MIDDLEWARE_KEY_PREFIX = 'homeoptik'

#YANDEX MONEY KIT
YANDEX_MONEY_DEBUG = False
YANDEX_MONEY_SCID = 12345
YANDEX_MONEY_SHOP_ID = 56789
YANDEX_MONEY_SHOP_PASSWORD = 'password'
YANDEX_MONEY_FAIL_URL = 'http://9dd05044.ngrok.io/checkout/fail-payment/'
YANDEX_MONEY_SUCCESS_URL = 'http://9dd05044.ngrok.io/checkout/success-payment/'
# информировать о случаях, когда модуль вернул Яндекс.Кассе ошибку
YANDEX_MONEY_MAIL_ADMINS_ON_PAYMENT_ERROR = True

# Try and import local settings which can be used to override any of the above.
try:
    from settings_local import *
except ImportError:
    pass
