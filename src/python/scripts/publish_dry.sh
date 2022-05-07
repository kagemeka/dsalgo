#!/bin/bash

poetry publish \
    --build \
    --username kagemeka \
    --verbose \
    --version \
    -n \
    --dry-run
