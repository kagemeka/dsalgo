
#pragma once

namespace z_algorithm {
#include "types.hpp"
  using namespace types;

  template <typename A>
  auto z_algorithm(const A& a) -> vec<int> {
    int n = a.size();
    vec<int> lcp(n, 0);
    for (int i = 1, l = 0; i < n; ++i) {
      auto r = l + lcp[l];
      auto d = r <= i ? 0 : std::min(lcp[i - l], r - i);
      while (i + d < n && a[i + d] == a[d]) ++d;
      lcp[i] = d;
      if (r < i + d) l = i;
    }
    lcp[0] = n;
    return lcp;
  }
} // namespace z_algorithm
