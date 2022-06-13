#!/bin/bash

install_gdc() {
    echo "TODO"
}
install_ldc() {
    echo "TODO"
}
install_dmd() {
    apt update
    apt install -y curl
    curl https://dlang.org/install.sh | bash -s

    # for activate dmd,
    # source ~/dlang/dmd-2.100.0/activate
    # update compiler version manually.
    # run `deactivate` for exit.
    # https://dlang.org/install.html#activate

    # run main.d file.
    # rdmd main.d
    # https://tour.dlang.org/tour/en/welcome/run-d-program-locally
}

setup() {
    install_dmd
}

setup
