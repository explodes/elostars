import os

os.path.sep = os.path.sep

rel = lambda *x: os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', *x))

AUTH_USER_MODEL = 'main.User'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'elostars.main',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Denver'
USE_I18N = True
USE_L10N = True
USE_TZ = True

ROOT_URLCONF = 'elostars.urls'
WSGI_APPLICATION = 'elostars.wsgi.application'

ALLOWED_HOSTS = ['*']

MEDIA_ROOT = rel('media')
MEDIA_URL = '/media/'

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    rel('static'),
)

TEMPLATE_DIRS = (
    rel('templates'),
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'default-snowflake',
    },
    'matchup': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

FACE_DETECTION_ENABLED = False
FACE_DETECTION_CASCADE = None  # /usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml

try:
    from local_settings import *
except ImportError:
    print 'Cannot find local settings. Application will not run with incomplete settings.'