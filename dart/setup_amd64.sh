#!/bin/bash

source ~/.bashrc

install_dart() {
    # https://dart.dev/get-dart#install-using-apt-get
    sudo apt update
    sudo apt install -y \
        apt-transport-https \
        wget \
        sudo
    wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo gpg --dearmor -o /usr/share/keyrings/dart.gpg
    echo 'deb [signed-by=/usr/share/keyrings/dart.gpg arch=amd64] https://storage.googleapis.com/download.dartlang.org/linux/debian stable main' | sudo tee /etc/apt/sources.list.d/dart_stable.list

    apt update
    apt install -y dart

    dart --version

    # onother installation method
    # https://dart.dev/get-dart#install-a-debian-package
}

install_dart
