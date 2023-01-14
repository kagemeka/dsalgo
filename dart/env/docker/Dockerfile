FROM ubuntu:20.04
SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND=noninteractive
RUN \
  apt -q=2 update \
  && apt install -yq=2 \
  apt-utils \
  apt-transport-https \
  gnupg2 \
  wget \
  xclip \
  xsel \
  && wget -qO - \
  https://dl-ssl.google.com/linux/linux_signing_key.pub \
  | apt-key add - \
  && wget -qO - \
  https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list \
  > /etc/apt/sources.list.d/dart_stable.list \
  && apt -q=2 update \
  && apt -yq=2 install dart \
  && echo \
  'export PATH="$PATH:/usr/lib/dart/bin"' \
  >> ~/.bashrc
