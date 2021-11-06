#!/usr/bin/env sh

set -o errexit
set -o nounset

echo "Run manage.py migrations"
python /usr/app/manage.py makemigrations
python /usr/app/manage.py migrate --noinput

echo "Run server"
exec python -Wd /usr/app/manage.py runserver 0.0.0.0:8000