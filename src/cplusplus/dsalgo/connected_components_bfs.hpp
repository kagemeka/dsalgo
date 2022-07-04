#pragma once
#include <queue>
#include <vector>
using namespace std;

template <typename G>
auto connected_components(const G& g) -> vector<int> {
  int n = g.size();
  queue<int> que;
  vector<int> ids(n, -1);
  int id = 0;
  for (int i = 0; i < n; i++) {
    if (ids[i] != -1) continue;
    que.push(i);
    while (!que.empty()) {
      int u = que.front();
      que.pop();
      ids[u] = id;
      for (auto& v : g[u]) {
        if (ids[v] == -1) que.push(v);
      }
    }
    id++;
  }
  return ids;
}