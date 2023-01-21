#!/bin/bash

install_java() {
    apt update
    apt install -y openjdk-19-jdk
}

install_java
