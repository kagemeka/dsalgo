# Contributing to DsAlgo (Rust)

## module naming rule

* basically,
  * <theme>_<algorithm/data_structure>_<ext>.rs
    * if theme is trivial, it can be omitted.
    * for example, `floyd_warshall` is a algorithm only used for shortest path.
    * extentional impl section should be separeted with absolute core API.

## project rules

* do not introduce additional directory depth for this project.
* instead, split files into small pieces, and connect them by `use` keyword.
* run ./script/ci.sh before commit and push.
* by defining abstract algebra and precice traits, preserve strict `DRY` principle and beautiful codes.
