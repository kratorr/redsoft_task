#!/bin/bash


echo "Start memory checker"
python3 memory_check.py &

echo "Collect static files"
python3 manage.py collectstatic --noinput

echo "Apply database migrations"
python3 manage.py migrate


echo "Create OpenAPI schema"
python3 manage.py spectacular --color --file schema.yml

echo "Starting server"
python3 manage.py runserver 0.0.0.0:8000
