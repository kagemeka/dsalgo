// TODO: test
#pragma once
#include "rust_types.hpp"
#include <cassert>
#include <vector>

namespace dsalgo::tribonacci_sequence {
  using namespace rust_types;

  template <typename T>
  auto tribonacci_sequence(usize size) -> vec<T> {
    assert(size >= 3);
    vec<T> t(size);
    t[0] = 1, t[1] = 1, t[2] = 2;
    for (usize i = 3; i < size; i++) t[i] = t[i - 1] + t[i - 2] + t[i - 3];
    return t;
  }

} // namespace dsalgo::tribonacci_sequence
