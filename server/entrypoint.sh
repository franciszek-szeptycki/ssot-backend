#!/bin/sh

#check is postgres up (all credentials from .env file)
while ! nc -z db 5432; do
  echo "Waiting for Postgres to start..."
  sleep 1
done

python manage.py migrate

python manage.py collectstatic --noinput

python manage.py seed_admin

gunicorn server.wsgi --bind 0.0.0.0:8000