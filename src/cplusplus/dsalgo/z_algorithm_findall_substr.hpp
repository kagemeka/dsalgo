#pragma once
#include "concat_sequence.hpp"
#include "types.hpp"
#include "z_algorithm.hpp"

template<typename A>
auto z_algorithm_findall_substr(const A& a, const A& pattern) -> vec<usize> {
  using concat_sequence::concat;
  int n = a.size(), m = pattern.size();
  auto z = z_algorithm(concat(pattern, a));
  vec<usize> indices;
  for(int i = 0; i < n; ++i) {
    if(z[m + i] >= m) indices.push_back(i);
  }
  return indices;
}
