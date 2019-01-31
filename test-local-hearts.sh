#!/bin/bash

docker exec -it hearts-django_web_1 /bin/bash -c "cd /srv/www;
                                               export HEARTS_ENV_CONFIG_FILE=local_dev_env_config.ini;
                                               source ./virtualenv/bin/activate;
                                               python manage.py test"
