#!/bin/bash

apt update
apt install -y curl
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
echo "source $HOME/.poetry/env" >>~/.bashrc
python3 -m pip install -U pip
