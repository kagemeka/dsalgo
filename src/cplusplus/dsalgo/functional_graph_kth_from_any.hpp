#pragma once
#include "functional_graph_doubling_table.hpp"

class functional_graph_kth_from_any {
  vector<vector<int>> table;

public:
  // k <= 2^exp
  functional_graph_kth_from_any(const vector<int>& f, int max_exp)
      : table(functional_graph_doubling_table(f, max_exp)) {}

  auto operator()(int src, long k) -> int {
    int i = src;
    for (int j = 0; j < (int)table.size(); j++) {
      if (~k >> j & 1) continue;
      i = table[j][i];
    }
    return i;
  }
};
