# noinspection PyUnresolvedReferences
from .base import *

ALLOWED_HOSTS = ['*', ]
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'form',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'pgsql',
        'PORT': '5432',
    }
}

OAUTH_CALLBACK_BASE_URL = "http://localhost:8000"

# NOTE: change it
SECRET_KEY = '9h!41r$lc-$iq5h^v=8)ftfnvzon%=e@(ak^)7@x*a6ns3@ds6'
