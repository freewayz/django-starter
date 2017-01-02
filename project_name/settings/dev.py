from base import *
from {{ project_name }}.utils import get_env

DATABASES = {
    "default" : {
        "ENGINE" : "django.db.backends.postgresql_psycopg2",
        "NAME" : "{{ project_name|lower }}",
        "USER" : get_env(env='DB_USER'),
        "PASSWORD" : get_env(env='DB_PASS'),
        "HOST" : "localhost",
        "PORT" : get_env(env='DB_PORT')
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]