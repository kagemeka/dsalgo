#!/bin/bash

source ~/.bashrc

cargo update --verbose
cargo package --list --allow-dirty

./scripts/format.sh
./scripts/test.sh

cargo publish --dry-run --allow-dirty
