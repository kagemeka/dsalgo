#!/bin/bash

setup() {
    apt update
    apt install -y haskell-platform
    curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh
    curl -sSL https://get.haskellstack.org/ | sh

    echo "export PATH=/root/.local/bin:$PATH" >>~/.bashrc

}
# ghc

setup
