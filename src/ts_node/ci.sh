#!/bin/bash

install_nodejs() {
    curl -sL https://deb.nodesource.com/setup_current.x | sudo -E bash -
    apt install -y nodejs

}

install_typescript() {
    npm install -g typescript ts-node
}

setup() {
    apt update
    install_nodejs
    install_typescript
}

setup