#!/bin/bash

# Attendre que MySQL soit prêt
echo "Waiting for MySQL to be ready..."
while ! nc -z mysql 3306; do
  sleep 1
done

echo "MySQL is ready. Initializing database..."
python app.py init

echo "Starting Flask application..."
python app.py