#!/bin/bash

setup() {
	apt update
	apt install -y \
		build-essential \
		clang-format \
		clangd \
		clang-tidy \
		cmake \
		sudo
	install_googletest
}

install_googletest() {
	# https://github.com/google/googletest/tree/main/googletest
	git clone https://github.com/google/googletest.git -b release-1.11.0
	cd googletest # Main directory of the cloned repository.
	mkdir build   # Create a directory to hold the build output.
	cd build
	cmake .. # Generate native build scripts for GoogleTest.
	make
	make install
	cd ../../
	rm -r ./googletest
}

#region
# source `ci.sh` or copy these commands into ~/.bashrc
gpp_compile() {
	g++ $1 -DCPP_DEBUG -Wall -Wextra -Werror -std=c++17 -O2 -g -o main
}

gpp() {
	gpp_compile $1 && chmod +x main && time ./main
}
#endregion

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

clang_format() {
	clang-format \
		-i \
		--sort-includes \
		./**/*.hpp
	./../../scripts/pre-commit.sh
}

ci() {
	setup
	tidy_lint_format
	clang_format
	test
}

# setup
ci
# dump_tidy_config
