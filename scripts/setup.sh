#!/bin/bash
apt update
apt install -y \
    git \
    neovim

cat ./scripts/path_funcs.sh >> ~/.bashrc
