#pragma once
#include "types.hpp"

namespace kmp_table_1_indexed {
  using namespace types;
  template <typename A>
  auto kmp_table(const A& a) -> vec<int> {
    int n = a.size();
    vec<int> f(n + 1, 0);
    f[0] = -1;
    for (int i = 0, d = -1; i < n; ++i) {
      while (d != -1 && a[d] != a[i]) d = f[d];
      ++d;
      f[i + 1] = i + 1 < n && a[d] == a[i + 1] ? f[d] : d;
    }
    return f;
  }
} // namespace kmp_table_1_indexed
