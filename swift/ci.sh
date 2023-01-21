#!/bin/bash
source ~/.bashrc


install_swift() {
    # references
    # https://www.swift.org/getting-started/
    # https://www.swift.org/download/
    # https://github.com/apple/swift-docker/blob/59e3cc2532e57bb75b406bb9c589b62bd12edd5c/5.7/ubuntu/22.04/Dockerfile

    apt update
    export DEBIAN_FRONTEND=noninteractive

    # don't use apt!
    apt-get install -y \
        binutils \
        git \
        gnupg2 \
        libc6-dev \
        libcurl4-openssl-dev \
        libedit2 \
        libgcc-9-dev \
        libpython3.8 \
        libsqlite3-0 \
        libstdc++-9-dev \
        libxml2-dev \
        libz3-dev \
        pkg-config \
        tzdata \
        unzip \
        zlib1g-dev

    SWIFT_PLATFORM=ubuntu22.04
    SWIFT_VERSION_NUMBER=5.7.3
    SWIFT_BRANCH=swift-$SWIFT_VERSION_NUMBER-release
    SWIFT_VERSION=swift-$SWIFT_VERSION_NUMBER-RELEASE
    SWIFT_WEBROOT=https://download.swift.org

    # check processor architecture
    # e.g.
    # Ubuntu on Intel CPU: amd64(x86_64, x64)
    # M1 Macbook: arm64(aarch64)
    set -e
    ARCH_NAME="$(dpkg --print-architecture)"
    url=
    case "${ARCH_NAME##*-}" in
    'amd64')
        OS_ARCH_SUFFIX=''
        ;;
    'arm64')
        OS_ARCH_SUFFIX='-aarch64'
        ;;
    *)
        echo >&2 "error: unsupported architecture: '$ARCH_NAME'"
        exit 1
        ;;
    esac

    SWIFT_WEBDIR="$SWIFT_WEBROOT/$SWIFT_BRANCH/$(echo $SWIFT_PLATFORM | tr -d .)$OS_ARCH_SUFFIX"
    FILE_NAME="$SWIFT_VERSION-$SWIFT_PLATFORM$OS_ARCH_SUFFIX"
    SWIFT_BIN_URL="$SWIFT_WEBDIR/$SWIFT_VERSION/$FILE_NAME.tar.gz"

    apt install -y wget

    wget -O - "$SWIFT_BIN_URL" | tar -xzC /usr/local/ \
        --transform=s/$FILE_NAME/swift/

    echo 'export PATH=/usr/local/swift/usr/bin:$PATH' >>~/.bashrc

    # run source ~/.bashrc in terminal

    export PATH=/usr/local/swift/usr/bin:$PATH
    swift --version
}


install_swiftlint() {
    git clone https://github.com/realm/SwiftLint.git
    p=$(pwd) # snapshot
    cd SwiftLint
    swift build -c release
    mv .build/release/swiftlint /usr/local/bin/
    cd $p
    rm -r SwiftLint
}

install_swift-format() {
    BRANCH=release/5.7
    git clone -b $BRANCH https://github.com/apple/swift-format.git
    p=$(pwd)
    cd swift-format
    swift build -c release
    mv .build/release/swift-format /usr/local/bin/
    cd $p
    rm -r swift-format
}

setup_toolchains() {
    if ! command -v swift &>/dev/null; then
        echo "command not found"
        install_swift
    fi

    if ! command -v swiftlint &>/dev/null; then
        echo "command not found"
        install_swiftlint
    fi

    if ! command -v swift-format &>/dev/null; then
        echo "command not found"
        install_swift-format
    fi
}

format() {
    swift-format format \
        --parallel \
        --recursive \
        --in-place \
        --configuration .swift-format \
        .
    # ./../ci.sh
}

lint() {
    swiftlint lint
    # check options by: swiftlint lint --help
}

ci() {
    setup_toolchains

    lint
    format
}

ci
