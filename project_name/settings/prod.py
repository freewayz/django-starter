from base import *
from {{ project_name | lower }}.utils import is_heroku
import dj_database_url


PRODUCTION_APP = [
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
]

PRODUCTION_MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

MIDDLEWARE_CLASSES = DEV_MIDDLEWARE_CLASSES + PRODUCTION_MIDDLEWARE + PROJECT_MIDDLEWARE_CLASSES

DEBUG = False


# use the heroku postgres database
if is_heroku():
    django_database_config = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(django_database_config)
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(
    BASE_DIR, 'assets'
)

STATICFILES_DIRS = [
    os.path.join(
        BASE_DIR, 'static'
    )
]


