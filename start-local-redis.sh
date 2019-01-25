#!/bin/bash
set -e

if [ ! -f ./local-dev-config.sh ]; then
    echo "ERROR You must create config file ./local-dev-config.sh with your local config."
    echo "ERROR See ./local-dev-config.sh.dist for an example."
    exit 1;
fi

source local-dev-config.sh

docker pull redis:4.0

if [ ! "$(docker network list | grep local-dev-network)"  ]; then
    docker network create -d bridge local-dev-network
fi

docker run \
    --hostname local-dev-redis \
    --name local-dev-redis \
    --network "local-dev-network" \
    --publish 6379:6379 \
    --detach \
    redis:4.0
