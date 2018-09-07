import os
from django.core.exceptions import ImproperlyConfigured
__author__ = "peter"


def get_env(env=None):
    try:
        return os.getenv(env)
    except KeyError:
        raise ImproperlyConfigured("Cant find the environment variable")

def is_dev():
    dev =  get_env(env='ENV')
    return dev == "dev" or dev == "development"

def is_prod():
    return not is_dev()

def deployment_type():
    return os.getenv('DEPLOYMENT', None)

def is_docker():
    deployment_type() == 'DOCKER'

def is_heroku():
    deployment_type() == 'HEROKU'

