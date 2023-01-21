#!/bin/bash
source ~/.bashrc

# install_swift() {
#     ./setup.sh
#     source ~/.bashrc
# }

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
