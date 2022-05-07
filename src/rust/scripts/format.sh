#!/bin/bash

cargo fmt \
    --all \
    --verbose \
    --manifest-path=Cargo.toml \
    --message-format=human
# --check
