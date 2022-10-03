#!/bin/bash

install_nodejs() {
    curl -sL https://deb.nodesource.com/setup_current.x | sudo -E bash -
    apt install -y nodejs

}

install_typescript() {
    npm install -g typescript ts-node
}

install_jest() {
    npm install --save-dev jest ts-jest @types/jest
}

install_prettier() {
    npm install --save-dev prettier
}

install_node_modules() {
    npm install --save-dev @types/node
}

setup() {
    apt update
    install_nodejs
    install_typescript
    install_jest
    install_prettier
    install_node_modules
}

setup
