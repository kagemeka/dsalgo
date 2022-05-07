#!/bin/bash

apt update
apt install -y apt-utils git
ln -fns /usr/bin/python3 /usr/bin/python

./scripts/install_poetry.sh
./scripts/update_env.sh
poetry install
