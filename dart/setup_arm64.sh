#!/bin/bash

source ~/.bashrc

install_dart() {
    # References
    # https://dart.dev/get-dart#install-a-debian-package
    # https://dart.dev/get-dart/archive

    apt update
    apt install -y unzip wget
    BASE=https://storage.googleapis.com/dart-archive/channels/
    CHANNEL=stable
    DART_VERSION=2.18.7
    PLATFORM=linux
    ARCH=arm64
    FILE_NAME=dartsdk-$PLATFORM-$ARCH-release.zip

    URL=${BASE}${CHANNEL}/release/$DART_VERSION/sdk/$FILE_NAME
    wget $URL
    unzip $FILE_NAME
    rm $FILE_NAME

    DART_PATH=/usr/bin/dart
    DART_BIN=$DART_PATH/bin/

    mv dart-sdk $DART_PATH

    echo "export PATH=$PATH:$DART_BIN" >>~/.bashrc

    export PATH=$PATH:$DART_BIN
    dart --version

    # run source ~/.bashrc on terminal

}

if ! command -v dart &>/dev/null; then
    echo "command not found"
    install_dart
fi
