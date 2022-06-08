#ifndef INVERSE_FACTORIAL_TABLE_HPP
#define INVERSE_FACTORIAL_TABLE_HPP

#include "./accumulate.hpp"
#include "./factorial_table.hpp"
#include <numeric>
#include <vector>

template <typename S> std::vector<S> inverse_factorial_table(unsigned long int size) {
  std::vector<S> v(size);
  std::iota(v.begin(), v.end(), 1);
  v[size - 1] = 1 / factorial_table<S>(size)[size - 1];
  reverse(v.begin(), v.end());
  v = accumulate<S, mul<S>>(v);
  reverse(v.begin(), v.end());
  return v;
}
#endif // INVERSE_FACTORIAL_TABLE_HPP
