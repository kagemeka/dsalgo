#!/bin/bash

install_swift() {
    SOURCEKIT_TOOLCHAIN_PATH=/usr/local/swift
    SWIFT_VER=5.6.2
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
    source ~/.bashrc
}

install_swiftlint() {
    git clone https://github.com/realm/SwiftLint.git
    p=$(pwd)
    cd SwiftLint
    swift build -c release
    mv .build/release/swiftlint /usr/local/bin/
    cd $p
    rm -r SwiftLint
}

install_swift-format() {
    BRANCH=release/5.6
    git clone -b $BRANCH https://github.com/apple/swift-format.git
    p=$(pwd)
    cd swift-format
    swift build -c release
    mv .build/release/swift-format /usr/local/bin/
    cd $p
    rm -r swift-format
}

setup() {
    install_swift
    install_swiftlint
    install_swift-format
}

format() {
    swift-format -p -r -i .
    ./../../scripts/pre-commit.sh
}
ci() {
    # setup
    format
    swiftlint

}

ci
