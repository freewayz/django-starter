#!/usr/bin/env python
import os
import sys
from {{ project_name }} import utils

if __name__ == "__main__":
    if utils.is_dev():
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.dev")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.prod")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
