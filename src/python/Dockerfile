FROM python:3.10-slim-buster
SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /root/
RUN \
  apt update \
  && apt install -y \
  apt-utils \
  curl \
  git \
  && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
  && echo 'source $HOME/.poetry/env' >> ~/.bashrc \
  && python3 -m pip install -U pip
