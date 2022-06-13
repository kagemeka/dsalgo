#!/bin/bash

# TODO: fix installation error.
setup() {
    apt update
    apt install -y curl
    curl https://nim-lang.org/choosenim/init.sh -sSf | sh
    echo "export PATH=/root/.nimble/bin:$PATH" >>~/.bashrc
}

setup
