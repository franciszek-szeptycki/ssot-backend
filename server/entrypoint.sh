#!/bin/sh

#check is postgres up (all credentials from .env file)
while ! nc -z db 5432; do
  echo "Waiting for Postgres to start..."
  sleep 1
done

python manage.py migrate
python manage.py seed_admin

python manage.py runserver 0.0.0.0:80
