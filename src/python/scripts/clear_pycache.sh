#!/bin/bash

find . | grep -E "__pycache__$" | xargs rm -rf
