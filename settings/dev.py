# noinspection PyUnresolvedReferences
from .base import *

ALLOWED_HOSTS = ['*', ]
DEBUG = True
SECRET_KEY = '9h!41r$lc-$iq5h^v=8)ftfnvzon%=e@(ak^)7@x*a6ns3@ds6'

# TODO: read password from env
DATABASES = {
    'default':
        {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': "./data/db.sqlite3",
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:16379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
            # "PASSWORD": "",
        }
    }
}

# TODO: django-constance
