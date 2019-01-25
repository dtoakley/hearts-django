#!/bin/bash
set -e

if [ ! -f ./local-dev-config.sh ]; then
    echo "ERROR You must create config file ./local-dev-config.sh with your local config."
    echo "ERROR See ./local-dev-config.sh.dist for an example."
    exit 1;
fi

source local-dev-config.sh

docker pull node:9.6.1

if [ ! "$(docker network list | grep hearts-local-dev)"  ]; then
    docker network create -d bridge hearts-local-dev
fi

# If the container is already running, remove it.
docker rm --force local-dev-node > /dev/null 2>&1 || true

docker run \
    --hostname local-dev-node \
    --name local-dev-node \
    --network "hearts-local-dev" \
    --publish 3000:3000 \
    --volume ${HOST_MOUNT_TARGET}:${DOCKER_MOUNT_DIR}:cached \
    --detach \
    node:9.6.1 \
    /bin/bash -c "cd ${DOCKER_MOUNT_DIR}/hearts-django; ./run-local-hearts-client.sh"
