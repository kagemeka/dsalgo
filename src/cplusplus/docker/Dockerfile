FROM ubuntu:latest
SHELL ["/bin/bash", "-c"]
ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /root/
RUN \
  apt -q=2 update \
  && apt -yq=2 install \
  apt-utils \
  build-essential \
  neovim \
  software-properties-common \
  xclip \
  xsel \
  && rm -rf /var/lib/apt/lists/* \
  && apt clean -y \
  && echo "PS1='\w\$ '" >> ~/.bashrc \
  && echo "bind '\"\t\":menu-complete'" >> ~/.bashrc
