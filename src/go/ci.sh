#!/bin/bash

setup() {

    GO_VERSION=1.18.3
    apt update
    apt install -y wget
    wget -O - https://dl.google.com/go/go${GO_VERSION}.linux-amd64.tar.gz | tar -xzC /usr/local/
    GOPATH="/usr/local/go"
    echo "export GOPATH=${GOPATH}" >>~/.bashrc
    source ~/.bashrc
    echo "export PATH=${PATH}:${GOPATH}/bin" >>~/.bashrc
    # run source ~/.bashrc in console.
}

help() {
    go help
}

ci() {
    if ! command -v go &>/dev/null; then
        echo "go command not found"
        setup
        source ~/.bashrc
    fi

    go fmt -n -x ./...
    ./../../scripts/pre-commit.sh
    go test -v ./...
}

ci
