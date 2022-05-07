#!/bin/bash

apt update
apt install -y apt-utils git

./scripts/install_poetry.sh
./scripts/update_env.sh
poetry install
