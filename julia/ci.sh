#!/bin/bash

setup() {
    MAJOR=1
    MINOR=7
    PATCH=3

    MAJOR_MINOR="${MAJOR}.${MINOR}"
    JULIA_VERSION="${MAJOR_MINOR}.${PATCH}"

    apt update
    apt install -y wget

    wget -O - \
        https://julialang-s3.julialang.org/bin/linux/x64/${MAJOR_MINOR}/julia-${JULIA_VERSION}-linux-x86_64.tar.gz | tar \
        -xvzC /usr/local \
        --transform=s/-${JULIA_VERSION}//
    ln -fns /usr/local/julia/bin/julia /usr/bin/julia
}

setup
