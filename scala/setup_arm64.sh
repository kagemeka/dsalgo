#!/bin/bash

install_java() {
    apt update
    apt install -y openjdk-19-jdk
}

install_scala() {
    # https://docs.scala-lang.org/getting-started/index.html
    apt update
    apt install -y curl
    install_java

    ARCH=aarch64

    curl -fL https://github.com/coursier/launchers/raw/master/cs-$ARCH-pc-linux.gz | gzip -d >cs && chmod +x cs && yes | ./cs setup

    rm cs

    # https://techviewleo.com/how-to-install-scala-on-ubuntu-linux/
    BIN=$HOME/.local/share/coursier/bin/
    echo "export PATH=$PATH:$BIN" >>~/.bashrc

    export PATH=$PATH:$BIN
    scala -version
    # run source ~/.bashrc in terminal
}

install_scala
