#!/bin/bash

setup() {
    apt update
    apt install -y \
        apt-transport-https \
        gnupg2 \
        wget
    wget -O - \
        https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
    wget -O - \
        https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list \
        >/etc/apt/sources.list.d/dart_stable.list
    apt update
    apt install -y dart
    echo "export PATH=\"$PATH:/usr/lib/dart/bin\"" >>~/.bashrc

}
setup
