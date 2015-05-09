import os

rel = lambda *x: os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', *x))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

CDN_URL = "http://localhost:8000"

SECRET_KEY = ''

DATABASES = {
    ## sqlite configuration
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': rel('database.db'),
    }
    ## Postgres configuration
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'mydb',
    #     'USER': 'myuser',
    #     'PASSWORD': 'password',
    #     'HOST': 'localhost',
    #     'PORT': '',
    # }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'loggers': {
        'djsonapi': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

## No face detection
FACE_DETECTION_ENABLED = False
FACE_DETECTION_CASCADE = None

## Face detection
# FACE_DETECTION_ENABLED = True
# FACE_DETECTION_CASCADE = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml"

if not SECRET_KEY:
    raise Exception("You have to configure your SECRET_KEY: ~100 random characters of gibberish")