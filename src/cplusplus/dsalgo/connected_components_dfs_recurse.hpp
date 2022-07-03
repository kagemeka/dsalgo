#pragma once

#include <functional>
#include <vector>
using namespace std;

template <typename G>
auto connected_components(const G& g) -> vector<int> {
  int n = g.size();
  vector<int> labels(n, -1);
  int l = 0;
  function<void(int)> dfs;
  dfs = [&](int u) {
    labels[u] = l;
    for (auto& v : g[u]) {
      if (labels[v] != -1) continue;
      dfs(v);
    }
  };
  for (int i = 0; i < n; i++) {
    if (labels[i] != -1) continue;
    dfs(i);
    l++;
  }
  return labels;
}
