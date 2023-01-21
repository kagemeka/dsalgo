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
    mv dart-sdk /usr/lib/dart/

    echo 'export PATH=$PATH:/usr/lib/dart/bin' >>~/.bashrc

    source ~/.bashrc
    dart --version

}

install_dart
