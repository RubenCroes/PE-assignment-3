#!/bin/bash

# Run DB migrations
echo "Running database migrations..."
flask db init
flask db migrate -m "Initial Migrations"
flask db upgrade

# Start the app
echo "Starting Flask app..."
exec gunicorn -b 0.0.0.0:8000 app:app
