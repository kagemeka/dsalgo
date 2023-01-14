#!/bin/bash

GO_VERSION=1.18.1
apt update
apt install -y wget
wget -O - https://dl.google.com/go/go${GO_VERSION}.linux-amd64.tar.gz | tar -xzC /usr/local/
echo "export GOPATH=/usr/local/go" >>~/.bashrc
source ~/.bashrc
echo "export PATH=${PATH}:${GOPATH}/bin" >>~/.bashrc
source ~/.bashrc
