#!/bin/bash

setup() {
    apt update
    apt install -y \
        build-essential \
        clang-format \
        clangd \
        clang-tidy \
        cmake
}

#region
# source `ci.sh` or copy these commands into ~/.bashrc
gpp_compile() {
    g++ $1 -DCPP_DEBUG -Wall -Wextra -Werror -std=c++17 -O3 -o main
}

gpp() {
    gpp_compile $1 && chmod +x main && time ./main
}
#endregion

# install_googletest() {
# }

test() {
    cmake -S . -B build
    cmake --build build
    ctest --test-dir build
}

dump_tidy_config() {
    clang-tidy \
        --dump-config \
        --format-style=file \
        -checks=modernize-* \
        --fix \
        --fix-errors \
        ./**/*.[ch]pp

}
tidy_lint_format() {
    clang-tidy \
        --config-file=.clang-tidy \
        ./**/*.[ch]pp
}

format() {
    clang-format \
        -i \
        --sort-includes \
        ./**/*.hpp
    ./../../scripts/pre-commit.sh
}

ci() {
    setup
    tidy_lint_format
    format
    test
}

ci
# dump_tidy_config
