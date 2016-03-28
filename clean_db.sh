#!/bin/bash

echo 'Cleaning database'
rm -f tmp.db db.sqlite3
rm -r api/migrations
python manage.py makemigrations api
python manage.py migrate