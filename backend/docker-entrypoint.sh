#!/bin/bash

echo "Collect Static files"
python manage.py collectstatic --noinput

echo "Apply database migrations"
python manage.py makemigrations users
python manage.py makemigrations decks
python manage.py makemigrations cards
python manage.py makemigrations
python manage.py migrate users
python manage.py migrate decks
python manage.py migrate cards
python manage.py migrate

echo "Starting server"
gunicorn backend.wsgi:application --bind 0.0.0.0:8000