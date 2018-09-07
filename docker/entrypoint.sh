export DOCKER=100
DJANGO_SETTINGS_MODULE=question.settings

django-admin migrate


echo Starting Gunicorn
exec gunicorn question.wsgi:application \
     --bind=0.0.0.0:8000 \
     --workers 2 \
     --timeout 300 \
     --log-level=debug \
     "$@"


