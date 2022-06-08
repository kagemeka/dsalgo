#!/bin/bash

install_pre-commit() {
    apt update
    apt install -y python3-pip
    pip install -U pip
    pip install pre-commit
}

pre-commit() {
    if ! command -v pre-commit &>/dev/null; then
        echo "command not found"
        ./scripts/install_pre-commit.sh
    fi

    pre-commit run --all-files

}

pre-commit
