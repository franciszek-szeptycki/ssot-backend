#!/bin/sh

python manage.py migrate

gunicorn django_web_app.wsgi:application -b 0.0.0.0:8000 
