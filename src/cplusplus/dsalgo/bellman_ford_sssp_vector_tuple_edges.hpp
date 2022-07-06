#pragma once

#include <vector>
using namespace std;

template<typename T, typename G>
auto bellman_ford(const T& inf, int n, const G& edges, int src) -> vector<T> {
  vector<T> dist(n, inf);
  dist[src] = 0;
  for(int i = 0; i < 2 * (n - 1); i++) {
    for(auto& [u, v, w]: edges) {
      if(dist[u] == inf) continue;
      T dv = dist[u] == -inf ? -inf : dist[u] + w;
      if(dv >= dist[v]) continue;
      dist[v] = i >= n - 1 ? -inf : dv;
    }
  }
  return dist;
}
