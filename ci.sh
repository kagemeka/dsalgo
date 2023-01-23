#!/bin/bash

install_pre-commit() {
    apt update
    apt install -y git python3-pip
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

apt update
apt install -y \
    git \
    neovim \
    shfmt

shfmt -w **/*.sh
precommit
