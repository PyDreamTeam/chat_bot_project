#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "wait db"

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "run db "
fi

python manage.py migrate

exec "$@"