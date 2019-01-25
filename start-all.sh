#!/bin/bash
set -e

echo "Starting local Redis Server"
./start-local-redis.sh

echo "Initialising local Postgres db"
./start-local-postgres.sh

echo "Starting local Hearts app"
./start-local-hearts.sh

echo "Starting local node client"
./start-local-node.sh
