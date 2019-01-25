#!/bin/bash
set -e

if [ ! -f ./local-dev-config.sh ]; then
    echo "ERROR You must create config file ./local-dev-config.sh with your local config."
    echo "ERROR See ./local-dev-config.sh.dist for an example."
    exit 1;
fi

source local-dev-config.sh

docker pull postgres:10.2

if [ ! "$(docker network list | grep local-dev-network)"  ]; then
    docker network create -d bridge local-dev-network
fi

docker run \
    --env POSTGRES_USER=${POSTGRES_USER} \
    --env POSTGRES_RPASSWORD=${POSTGRES_PASSWORD} \
    --env POSTGRES_DB=${POSTGRES_DB} \
    --hostname local-dev-postgres \
    --name local-dev-postgres \
    --network "local-dev-network" \
    --publish 5432:5432 \
    --detach \
    postgres:10.2
