#!/bin/bash

source virtualenv/bin/activate

export HEARTS_ENV_CONFIG_FILE="local_dev_env_config.ini"
export WERKZEUG_DEBUG_PIN="off"

echo "Starting Hearts App..."

python manage.py runserver 0.0.0.0:8000
