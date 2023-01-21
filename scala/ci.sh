install_java() {
    apt update
    apt install -y openjdk-19-jdk
}

install_scala() {
    # https://docs.scala-lang.org/getting-started/index.html
    apt update
    apt install -y curl
    install_java

    set -e
    ARCH_NAME="$(dpkg --print-architecture)"
    url=
    case "${ARCH_NAME##*-}" in
    'amd64')
        ARCH='x86_64'
        ;;
    'arm64')
        ARCH='aarch64'
        ;;
    *)
        echo >&2 "error: unsupported architecture: '$ARCH_NAME'"
        exit 1
        ;;
    esac

    curl -fL https://github.com/coursier/launchers/raw/master/cs-$ARCH-pc-linux.gz | gzip -d >cs && chmod +x cs && yes | ./cs setup

    rm cs

    # https://techviewleo.com/how-to-install-scala-on-ubuntu-linux/
    BIN=$HOME/.local/share/coursier/bin/
    echo "export PATH=$PATH:$BIN" >>~/.bashrc

    export PATH=$PATH:$BIN
    scala -version
    # run source ~/.bashrc in terminal

}

setup() {
    if ! command -v scala &>/dev/null; then
        echo "command not found"
        install_scala
    fi
}

ci() {
    setup

}

ci
