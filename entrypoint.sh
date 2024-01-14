#!/bin/sh
action=$1
if [ "$action" = "runserver" ]; then
  python manage.py collectstatic --no-input &&
  python manage.py migrate &&
  gunicorn \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --error-logfile - \
    --access-logfile - \
    --timeout 60 \
    --reload \
    application.wsgi:application
elif [ "$action" = "loadtest" ]; then
    locust
fi
