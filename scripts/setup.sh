#!/bin/bash
apt update
apt install -y \
    git \
    neovim \
    software-properties-common \
    curl \
    wget \
    sudo \
    git \
    xclip \
    xsel

rm -rf /var/lib/apt/lists/*
apt clean -y
#   echo "PS1='\w\$ '" >> ~/.bashrc \
#   echo "bind '\"\t\":menu-complete'" >> ~/.bashrc
# cat ./scripts/path_funcs.sh >> ~/.bashrc
