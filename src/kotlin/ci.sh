#!/bin/bash

setup() {
    apt update
    apt install -y \
        unzip \
        zip

    curl -s https://get.sdkman.io | bash
    echo "source $HOME/.sdkman/bin/sdkman-init.sh" >>~/.bashrc
    source $HOME/.sdkman/bin/sdkman-init.sh
    sdk install kotlin
    # run source ~/.bashrc in console.
}

setup
