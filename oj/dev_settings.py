# coding=utf-8
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': '172.31.100.180',
        'PORT': 5432,
        'NAME': "onlinejudge",
        'USER': "onlinejudge",
        'PASSWORD': 'onlinejudge'
    }
}

REDIS_CONF = {
    "host": "172.31.100.180",
    "port": "6380"
}


DEBUG = True

ALLOWED_HOSTS = ["*"]

DATA_DIR = f"{BASE_DIR}/data"
