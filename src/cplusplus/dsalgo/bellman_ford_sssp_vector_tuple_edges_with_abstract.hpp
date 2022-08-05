#pragma once
#include "bellman_ford_abstract.hpp"
#include <vector>
using namespace std;
template<typename G, typename T>
auto bellman_ford_sssp(const T& inf, int n, const G& edges, int src)
  -> vector<T> {
  vector<T> dist(n, inf);
  dist[src] = 0;
  long iter_cnt = 0;
  int m = edges.size();
  auto f = [&](tuple<int, int, T> const& e) -> bool {
    iter_cnt++;
    int loop = (iter_cnt + m - 1) / m;
    auto& [u, v, w] = e;
    if(dist[u] == inf) return false;
    auto dv = dist[u] == -inf ? -inf : dist[u] + w;
    if(dv >= dist[v]) return false;
    dist[v] = loop >= n ? -inf : dv;
    return true;
  };
  bellman_ford_abstract(edges, f);
  return dist;
}
