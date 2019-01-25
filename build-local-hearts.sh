#!/bin/bash
#!/usr/bin/env python3

virtualenv -p python3.6 virtualenv

source ./virtualenv/bin/activate

echo "Installing python requirements"
pip install -r requirements.txt

export HEARTS_ENV_CONFIG_FILE="local_dev_env_config.ini"

echo "Migrating models"
python manage.py migrate

echo "Creating initial superuser"
python manage.py create_initial_superuser




