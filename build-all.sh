#!/bin/bash
set -e

if [ ! -f ./local-dev-config.sh ]; then
    echo "ERROR You must create config file ./local-dev-config.sh with your local config."
    echo "ERROR See ./local-dev-config.sh.dist for an example."
    exit 1;
fi

echo "Building Hearts App"

docker pull python:3.6

source local-dev-config.sh

if [ ! "$(docker network list | grep hearts-local-dev)"  ]; then
    docker network create -d bridge hearts-local-dev
fi

# If the container is already running, remove it.
docker rm --force local-dev-hearts > /dev/null 2>&1 || true

docker run \
    --hostname local-dev-hearts \
    --name local-dev-hearts \
    --network "hearts-local-dev" \
    --volume ${HOST_MOUNT_TARGET}:${DOCKER_MOUNT_DIR}:cached \
    --publish 8000:8000 \
    --detach \
    python:3.6 \
    /bin/bash -c "cd ${DOCKER_MOUNT_DIR}/hearts-django; ./build-local-hearts.sh"


echo "Building Node Hearts client"
./build-local-hearts-client.sh
