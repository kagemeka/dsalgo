#!/bin/bash

install_pre-commit() {
    apt update
    apt install -y python3-pip
    pip install -U pip
    pip install pre-commit
}

precommit() {
    if ! command -v pre-commit &>/dev/null; then
        echo "command not found"
        install_pre-commit
    fi

    pre-commit run --all-files

}

chmod -R +x ./**/*.sh

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

precommit
