#!/bin/bash

setup() {
    SOURCEKIT_TOOLCHAIN_PATH=/usr/local/swift
    SWIFT_VER=5.6.1
    apt update
    DEBIAN_FRONTEND=noninteractive apt install -y \
        binutils \
        git \
        gnupg2 \
        libc6-dev \
        libcurl4 \
        libedit2 \
        libgcc-9-dev \
        libpython2.7 \
        libsqlite3-0 \
        libstdc++-9-dev \
        libxml2 \
        libz3-dev \
        pkg-config \
        tzdata \
        wget \
        zlib1g-dev
    wget -O - https://swift.org/builds/swift-${SWIFT_VER}-release/ubuntu2004/swift-${SWIFT_VER}-RELEASE/swift-${SWIFT_VER}-RELEASE-ubuntu20.04.tar.gz | tar -xzC /usr/local/ \
        --transform=s/-${SWIFT_VER}-RELEASE-ubuntu20.04//
    echo "export \"PATH=/usr/local/swift/usr/bin:$PATH\"" >>~/.bashrc

    # run source ~/.bashrc in console.
}

setup
