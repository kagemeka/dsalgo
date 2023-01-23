#pragma once
#include <vector>
using namespace std;
struct union_find {
  vector<int> data;
  union_find(int size): data(size, -1) {}
  auto root(int u) -> int { return data[u] < 0 ? u : data[u] = root(data[u]); }
  auto unite(int u, int v) {
    u = root(u), v = root(v);
    if (u == v)
      return;
    if (data[u] > data[v])
      swap(u, v);
    data[u] += data[v];
    data[v] = u;
  }
  auto size_of(int u) -> int { return -data[root(u)]; }
  auto size() -> int { return data.size(); }
  auto labels() -> vector<int> {
    int n = size();
    vector<int> labels(n, -1);
    int l = 0;
    for (int i = 0; i < n; i++) {
      int r = root(i);
      if (labels[r] == -1) {
        labels[r] = l;
        l++;
      }
      labels[i] = labels[r];
    }
    return labels;
  }
};
