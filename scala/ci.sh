#!/bin/bash

setup() {
    apt update
    apt install -y curl

    # https://www.scala-lang.org/download/
    curl -fL https://github.com/coursier/launchers/raw/master/cs-x86_64-pc-linux.gz | gzip -d > cs && chmod +x cs && yes | ./cs setup

    rm cs

    # https://techviewleo.com/how-to-install-scala-on-ubuntu-linux/
    echo 'export PATH="$PATH:$HOME/.local/share/coursier/bin/"' >> ~/.bashrc

    # check to be installed
    source ~/.bashrc
    scala -version
}

setup
