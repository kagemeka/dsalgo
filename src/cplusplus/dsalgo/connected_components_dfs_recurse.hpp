#pragma once

#include <functional>
#include <vector>
using namespace std;

template<typename G> auto connected_components(const G& g) -> vector<int> {
  int n = g.size();
  vector<int> ids(n, -1);
  int id = 0;
  function<void(int)> dfs;
  dfs = [&](int u) {
    ids[u] = id;
    for(auto& v: g[u]) {
      if(ids[v] != -1) continue;
      dfs(v);
    }
  };
  for(int i = 0; i < n; i++) {
    if(ids[i] != -1) continue;
    dfs(i);
    id++;
  }
  return ids;
}
