#!/bin/bash

setup() {
    CLOJURE_VERSION=1.11.1.1124
    # check latest version
    # https://clojure.org/guides/install_clojure

    apt update
    apt install -y rlwrap

    install_sh="linux-install-${CLOJURE_VERSION}.sh"
    curl -O https://download.clojure.org/install/${install_sh}
    chmod +x ${install_sh}
    sudo ./${install_sh}
    rm ${install_sh}
}
setup
