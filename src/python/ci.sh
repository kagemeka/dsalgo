#!/bin/bash
source ~/.bashrc

# apt install -y \
#     python3-neovim \
#     python3-pip
# PYVER=3.9
# add-apt-repository -y ppa:deadsnakes/ppa
# apt update
# apt install -y \
#     python$PYVER \
#     python$PYVER-distutils \
#     python$PYVER-dev
# ln -fns /usr/bin/python$PYVER /usr/bin/python3
# ln -fns /usr/bin/python3 /usr/bin/python

install_poetry() {
    apt update
    apt install -y curl
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    echo "source $HOME/.poetry/env" >>~/.bashrc
    python3 -m pip install -U pip
    source $HOME/.poetry/env
    # please run `source ~/.bashrc` in command line.
}

update_toolchain() {
    poetry update
}

setup() {
    apt update
    apt install -y apt-utils git
    ln -fns /usr/bin/python3 /usr/bin/python
    install_poetry
    update_toolchain
    poetry install
}

lint() {
    poetry run mypy .
    poetry run pflake8 .
}

publish_dry() {
    poetry publish \
        --build \
        --username kagemeka \
        --verbose \
        --version \
        -n \
        --dry-run
}

format() {
    poetry run isort .
    poetry run black .
    ./../../scripts/pre-commit.sh
}

test() {
    poetry run pytest \
        --asyncio-mode=strict \
        --verbose . \
        --ignore=docs \
        --ignore=src/dsalgo_numba \
        --ignore=src/dsalgo_numpy \
        --ignore=prime_text
    # --testpaths="**/src/dsalgo/*.py"
    # --testpaths=tests/
    # --python

}

# region extra commands

clear_cache() {
    poetry cache clear pypi --all
    find . | grep -E "__pycache__$" | xargs rm -rf
}

update_docs() {
    apt update
    apt install -y make
    poetry install -E docs
    ./scripts/generate_sphinx_docs_headers.sh
    ./scripts/build_sphinx_docs.sh

}

# endregion

ci() {
    source ~/.bashrc
    if ! command -v poetry &>/dev/null; then
        echo "command not found"
        setup
    fi

    update_toolchain
    format
    lint
    test

    $@
}

ci $@
