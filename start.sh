#!/bin/sh

# make migrations
python3 manage.py makemigrations
python3 manage.py migrate
# run server
python manage.py runserver