#pragma once
#include "types.hpp"

namespace z_algorithm_findall_substr {
  using namespace types;
  template <typename A>
  auto z_algorithm_findall(const A& a, const A& pattern) -> vec<usize> {
    using concat_sequence::concat;
    using z_algorithm::z_algorithm;
    int n = a.size(), m = pattern.size();
    auto z = z_algorithm(concat(pattern, a));
    vec<usize> indices;
    for (int i = 0; i < n; ++i) {
      if (z[m + i] >= m) indices.push_back(i);
    }
    return indices;
  }
} // namespace z_algorithm_findall_substr
