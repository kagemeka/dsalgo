#!/bin/bash

source ~/.bashrc

gpp_compile() {
	g++ $1 -DCPP_DEBUG -Wall -Wextra -Werror -std=c++17 -O2 -o main
}

gpp() {
	gpp_compile $1 && chmod +x main && time ./main
}

for f in ./dsalgo/*.cpp; do
	echo "next run $f"
	gpp $f
done
