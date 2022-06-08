source $HOME/.cargo/env

rustup toolchain install nightly
rustup default nightly
rustup update

rustup component add rustfmt
