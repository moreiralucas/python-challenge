#!/usr/bin/sh
RETRIES=5
until psql -h $POSTGRES_SERVICE -U $POSTGRES_USER -d $POSTGRES_DB -c "select 1" > /dev/null 2>&1 || [ $RETRIES -eq 0 ]; do
  echo "Waiting for postgres server, $((RETRIES)) remaining attempts..."
  RETRIES=$((RETRIES-=1))
  sleep 1
done

python manage.py migrate
python manage.py runserver 0.0.0.0:8000
