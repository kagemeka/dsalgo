#!/bin/bash

source ~/.bashrc

./scripts/update_toolchain.sh
cargo update --verbose
cargo package --list --allow-dirty

./scripts/format.sh
./scripts/test.sh

cargo publish --dry-run --allow-dirty

pre-commit run --all-files
