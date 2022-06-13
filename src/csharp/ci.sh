#!/bin/bash

install_dotnet() {
    apt update
    apt install -y wget
    wget \
        https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb \
        -O packages-microsoft-prod.deb
    dpkg -i packages-microsoft-prod.deb
    rm packages-microsoft-prod.deb
}

install_sdk() {
    apt update
    apt install -y apt-transport-https
    apt update
    apt install -y dotnet-sdk-6.0
}

install_runtime() {
    apt install -y aspnetcore-runtime-6.0
}

install_dotnet_script() {
    dotnet tool install -g dotnet-script
}

setup() {
    install_dotnet
    install_sdk
    install_runtime
    install_dotnet_script
}

setup
