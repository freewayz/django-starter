from base import *
from {{ project_name }}.utils import get_env

DATABASES = {
    "default" : {
        "ENGINE" : "django.db.backends.mysql",
        "NAME" : "{{ project_name }}",
        "USER" : "root",
        "PASSWORD" : get_env(env='DB_PASS'),
        "HOST" : "localhost"
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]