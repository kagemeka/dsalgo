#pragma once
#include <queue>
#include <vector>
using namespace std;

template <typename G>
auto connected_components(const G& g) -> vector<int> {
  int n = g.size();
  queue<int> que;
  vector<int> labels(n, -1);
  int l = 0;
  for (int i = 0; i < n; i++) {
    if (labels[i] != -1) continue;
    que.push(i);
    while (!que.empty()) {
      int u = que.front();
      que.pop();
      labels[u] = l;
      for (auto& v : g[u]) {
        if (labels[v] == -1) que.push(v);
      }
    }
    l++;
  }
  return labels;
}