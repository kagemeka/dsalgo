#!/bin/bash

source ~/.bashrc

abs_dirpath() {
	echo $(dirname $(readlink -f $1))
}

this_file_dir() {
	abs_dirpath ${BASH_SOURCE[0]}
}

entrypoint_file_dir() {
	abs_dirpath $(realpath $0)
}

setup() {
	apt update
	apt install -y \
		apt-utils \
		build-essential \
		curl \
		shfmt
	curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
	echo "export PATH=\"$HOME/.cargo/bin:$PATH\"" >>~/.bashrc
	source $HOME/.cargo/env
	# please run `source ~/.bashrc` in command line.
}

update_toolchain() {
	rustup toolchain install nightly
	rustup default nightly
	rustup component add rustfmt
	rustup update
	cargo update --verbose

}

test() {
	# https://doc.rust-lang.org/cargo/commands/cargo-test.html
	cargo test
	cargo test \
		--all-features \
		--all-targets \
		--benches \
		--bins \
		--color always \
		--examples \
		--future-incompat-report \
		--locked \
		--manifest-path Cargo.toml \
		--no-fail-fast \
		--release \
		--tests \
		--verbose \
		--workspace \
		-Z unstable-options
	# --frozen \
	# --offline
	# --timings html
	# --unit-graph \
}

format() {
	cargo fmt \
		--all \
		--verbose \
		--manifest-path=Cargo.toml \
		--message-format=human
	# --check
	./../ci.sh
	shfmt *.sh
}

doc() {
	cargo doc \
		--open
}

crean() {
	cargo clean
}

ci() {
	if ! command -v cargo &>/dev/null; then
		echo "command not found"
		setup
	fi

	update_toolchain

	cargo package --list --allow-dirty

	format
	test

	cargo publish --dry-run --allow-dirty

	$@
}

ci $@
