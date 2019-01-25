#!/bin/bash
set -e

pip3.6 install virtualenv
virtualenv virtualenv

source virtualenv/bin/activate
export HEARTS_ENV_CONFIG_FILE="local_dev_env_config.ini"

echo "Installing python requirements"
pip3.6 install -r requirements.txt

echo "migrating models"
python manage.py migrate

echo "Creating superuser"
python manage.py create_initial_superuser
