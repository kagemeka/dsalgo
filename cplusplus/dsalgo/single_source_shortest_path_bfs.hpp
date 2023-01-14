#pragma once
#include "graph_bfs.hpp"
template<typename T, typename G>
auto bfs_sssp(const T& inf, const G& g, int src) -> vector<T> {
  int n = g.size();
  vector<T> dist(n, inf);
  dist[src] = 0;
  auto f = [&](int u, int v) -> bool {
    if(dist[v] != inf) return false;
    dist[v] = dist[u] + 1;
    return true;
  };
  graph_bfs(g, f, src);
  return dist;
}
