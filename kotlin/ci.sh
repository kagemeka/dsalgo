#!/bin/bash

source ~/.bashrc

install_sdkman() {
    # https://sdkman.io/install
    apt update
    apt install -y \
        curl \
        unzip \
        zip

    curl -s https://get.sdkman.io | bash
    echo "source $HOME/.sdkman/bin/sdkman-init.sh" >>~/.bashrc
    source $HOME/.sdkman/bin/sdkman-init.sh
    sdk version
}

install_java() {
    # https://linuxhint.com/install-java-ubuntu-22-04/

    apt update
    apt install -y openjdk-18-jdk
}

install_kotlin() {
    # https://kotlinlang.org/docs/command-line.html

    if ! command -v sdk &>/dev/null; then
        echo "command not found"
        install_sdkman
    fi

    if ! command -v java &>/dev/null; then
        echo "command not found"
        install_java
    fi

    sdk install kotlin
    kotlin -version

    # run source ~/.bashrc in console.
}

ci() {
    if ! command -v kotlin &>/dev/null; then
        echo "command not found"
        install_kotlin
    fi

}

ci
