#!/bin/bash

apt update
pip install -U pip
pip install pre-commit
pre-commit run --all-files
