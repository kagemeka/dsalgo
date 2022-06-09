abs_dirpath() {
    echo $(dirname $(readlink -f $1))
}

this_file_dir() {
    abs_dirpath ${BASH_SOURCE[0]}
}

entrypoint_file_dir() {
    abs_dirpath $(realpath $0)
}
