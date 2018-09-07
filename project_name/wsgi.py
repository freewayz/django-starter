"""
WSGI config for {{ project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.conf.global_settings import STATIC_ROOT
from .utils  import (
    is_prod,
    is_dev,
    is_heroku,
    is_docker
)


if is_dev():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.dev")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.prod")

application = get_wsgi_application()

"""
Use WhiteNoise as our static assets server if we are doing our
deployment on Heroku.

This basically check if export DEPLOYMENT=HEROKU
"""
if is_heroku():
    from whitenoise import WhiteNoise
    application = WhiteNoise(application, root=STATIC_ROOT)

if is_docker():
    """You might want to use NGINX to handle serving of static files
        which has been configured in the docker section
    """
    pass
