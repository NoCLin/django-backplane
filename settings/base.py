from pathlib import Path
import sys

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / 'data'
sys.path.insert(0, str(BASE_DIR / 'apps'))
sys.path.insert(0, str(BASE_DIR / 'ext_apps'))

SECRET_KEY = ''

DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'apps.common.django_suit.config.SuitConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'gunicorn',

    'rest_framework',
    'drf_yasg',
    'import_export',
    'silk',

    'apps.common',

]

MIDDLEWARE = [

    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    # ref: http://whitenoise.evans.io/en/stable/django.html
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'silk.middleware.SilkyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 统一异常处理
    'common.restframework.unified_response.middleware.ExceptionHandlerMiddleware',

]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
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

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = DATA_DIR / 'collected_static'
STATIC_ROOT.mkdir(parents=True, exist_ok=True)
STATICFILES_DIRS = (BASE_DIR / 'static',)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = DATA_DIR / 'media'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

LOG_ROOT = DATA_DIR / 'log'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] '
                      '[%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
    },
    'filters': {
    },
    'handlers': {

        'sql': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_ROOT / 'sql.log',
            'formatter': 'standard'},

        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT / 'all.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT / 'error.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },

        'request_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT / 'requests.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'scripts_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT / 'script.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': False
        },
        'django.request': {
            'handlers': ['scripts_handler'],
            'level': 'INFO',
            'propagate': False,
        },
        'scripts': {
            'handlers': ['scripts_handler'],
            'level': 'INFO',
            'propagate': False
        }
    }
}

# 拆分配置，但是区分开发环境与生产环境的不拆分

# noinspection PyUnresolvedReferences
from common.settings import *

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
            # "PASSWORD": "",
        }
    }
}

SITE_HEADER = "YOUR SITE"
SITE_FOOTER = "YOUR SITE"
