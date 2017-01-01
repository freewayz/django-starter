"""
WSGI config for {{ project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import utils

from django.core.wsgi import get_wsgi_application
from django.conf.global_settings import STATIC_ROOT
if utils.is_dev():        
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.dev")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.prod")

application = get_wsgi_application()
if utils.is_prod():
    from whitenoise import WhiteNoise
    application = WhiteNoise(application, root=STATIC_ROOT)