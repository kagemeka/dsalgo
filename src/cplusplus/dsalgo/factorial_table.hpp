#ifndef FACTORIAL_TABLE_HPP
#define FACTORIAL_TABLE_HPP

#include "./accumulate.hpp"
#include "./ops.hpp"
#include "rust_types.hpp"
#include <cassert>
#include <numeric>
#include <vector>

template <typename S>
auto factorial_table(unsigned long int size) -> std::vector<S> {
  assert(size > 0);
  std::vector<S> v(size);
  std::iota(v.begin(), v.end(), 0);
  v[0] = 1;
  return accumulate<S, mul<S>>(v);
}

#endif // FACTORIAL_TABLE_HPP
