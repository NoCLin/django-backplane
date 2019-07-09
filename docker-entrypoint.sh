#!/usr/bin/env sh

set -o errexit
set -o nounset

postgres_ready () {
  # don't forget to set the correct db host
  sh "./scripts/wait-for-command.sh" -t 5 -s 0 52 -c "curl pgsql:5432"
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
done

# It is also possible to wait for other services as well: redis, elastic, etcd
>&2 echo "Postgres is up - continuing..."


python manage.py migrate --noinput
python manage.py collectstatic --noinput

export PYTHONIOENCODING="UTF-8"

gunicorn application.wsgi:application --env DJANGO_SETTINGS_MODULE=settings.prod -c ./gunicorn_config.py

