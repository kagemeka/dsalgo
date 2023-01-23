#!/bin/bash

install_python() {
	apt update

	# PYVER=3.11
	# add-apt-repository -y ppa:deadsnakes/ppa
	# apt update
	# apt install -y \
	#     python$PYVER \
	#     python$PYVER-distutils \
	#     python$PYVER-dev
	# ln -fns /usr/bin/python$PYVER /usr/bin/python3
	# ln -fns /usr/bin/python3 /usr/bin/python

	apt install -y \
		software-properties-common \
		python3-pip
}

install_poetry() {
	apt install -y curl
	curl -sSL https://install.python-poetry.org | python3 -
	echo 'export PATH=$HOME/.local/bin:$PATH' >>~/.bashrc
	export PATH=$HOME/.local/bin:$PATH
	# run source ~/.bashrc in terminal

	poetry --version # check poetry command
	poetry self update
}

update_toolchain() {
	poetry update
	poetry install
}

setup() {
	install_python
	install_poetry
	update_toolchain
}

lint() {
	poetry run mypy .
	poetry run flake8 .
}

format() {
	poetry run isort .
	poetry run black .
	./../ci.sh
}

test() {
	poetry run pytest
	#     poetry run pytest \
	#         --asyncio-mode=strict \
	#         --verbose . \
	#         --ignore=docs \
	#         --ignore=src/dsalgo_numba \
	#         --ignore=src/dsalgo_numpy \
	#         --ignore=prime_text
	#     # --testpaths="**/src/dsalgo/*.py"
	#     # --testpaths=tests/
	#     # --python

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

ci() {
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
