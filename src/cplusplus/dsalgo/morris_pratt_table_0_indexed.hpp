#pragma once
#include "types.hpp"

namespace morris_pratt_table_0_indexed {
  using namespace types;
  template <typename A>
  auto morris_pratt_table(const A& a) -> vec<int> {
    int n = a.size();
    vec<int> lb(n, 0); // longest border
    for (int i = 1, d = 0; i < n; ++i) {
      while (d != 0 && a[d] != a[i]) d = lb[d - 1];
      if (a[d] == a[i]) ++d;
      lb[i] = d;
    }
    return lb;
  }
} // namespace morris_pratt_table_0_indexed
