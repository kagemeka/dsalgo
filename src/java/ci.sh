#!/bin/bash

setup() {
    apt update
    apt install -y default-jre
}

setup