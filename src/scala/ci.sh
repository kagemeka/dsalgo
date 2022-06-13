#!/bin/bash

setup() {
    apt update
    apt install -y default-jdk scala
}

setup
