#!/bin/bash

source local-dev-config.sh

docker exec -it local-dev-hearts /bin/bash -c "cd ${DOCKER_MOUNT_DIR}/hearts-django;
                                               export HEARTS_ENV_CONFIG_FILE=local_dev_env_config.ini;
                                               source ./virtualenv/bin/activate;
                                               python manage.py test"

