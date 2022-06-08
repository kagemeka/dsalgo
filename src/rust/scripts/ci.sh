#!/bin/bash

source ~/.bashrc

setup() {
    apt update
    apt install -y \
        apt-utils \
        build-essential \
        curl
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
    echo "export PATH=\"$HOME/.cargo/bin:$PATH\"" >>~/.bashrc
}

update_toolchain() {
    rustup toolchain install nightly
    rustup default nightly
    rustup component add rustfmt
    rustup update
    cargo update --verbose

}

test() {
    # https://doc.rust-lang.org/cargo/commands/cargo-test.html
    cargo test
    cargo test \
        --all-features \
        --all-targets \
        --benches \
        --bins \
        --color always \
        --examples \
        --future-incompat-report \
        --locked \
        --manifest-path Cargo.toml \
        --no-fail-fast \
        --release \
        --tests \
        --verbose \
        --workspace \
        -Z unstable-options
    # --frozen \
    # --offline
    # --timings html
    # --unit-graph \
}

format() {
    cargo fmt \
        --all \
        --verbose \
        --manifest-path=Cargo.toml \
        --message-format=human
    # --check

    ./scripts/pre-commit.sh
}

ci() {
    if ! command -v cargo &>/dev/null; then
        echo "command not found"
        setup
    fi
    source $HOME/.cargo/env

    update_toolchain

    cargo package --list --allow-dirty

    format
    test

    cargo publish --dry-run --allow-dirty
}

ci
