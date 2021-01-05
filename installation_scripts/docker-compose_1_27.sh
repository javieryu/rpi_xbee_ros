#!/bin/sh
# Download the current stable release of docker compose
# in this case 1.27.4
curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Symbolic link to docker-compose exec
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose