import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

SECRET_KEY = '*'

DEBUG = False

ALLOWED_HOSTS = []

MY_APPS = [
    'shop',
    'cart',
    'orders',
    'payment',
    'coupons',
    'rosetta',
    'parler',
    'localflavor',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = MY_APPS + DJANGO_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/'
MEDIA_ROOT = BASE_DIR / ''

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CART_SESSION_ID = 'cart'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STRIPE_PUBLISHABLE_KEY = '*'
STRIPE_SECRET_KEY = '*'
STRIPE_WEBHOOK_SECRET = '*'
STRIPE_API_VERSION = '*'

REDIS_HOST = '*'
REDIS_PORT = 6379
REDIS_DB = 1

LANGUAGES = [
    ('en', _('English')),
    ('ru', _('Russian')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

PARLER_LANGUAGES = {
    None: (
        {'code': 'en'},
        {'code': 'ru'},
    ),
    'default': {
        'fallback': 'en',
        'hide_untranslated': False,
    }
}