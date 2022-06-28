#pragma once
#include "types.hpp"

namespace morris_pratt_table_1_indexed {
  using namespace types;
  template <typename A>
  auto morris_pratt_table(const A& a) -> vec<int> {
    int n = a.size();
    vec<int> lb(n + 1, 0);
    lb[0] = -1;
    for (int i = 0, d = -1; i < n; ++i) {
      while (d != -1 && a[d] != a[i]) d = lb[d];
      ++d;
      lb[i + 1] = d;
    }
    return lb;
  }
} // namespace morris_pratt_table_1_indexed
