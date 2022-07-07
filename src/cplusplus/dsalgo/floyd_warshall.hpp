#pragma once

template<typename G, typename F> auto floyd_warshall(G g, F f) -> G {
  int n = g.size();
  for(int k = 0; k < n; ++k) {
    for(int i = 0; i < n; ++i) {
      for(int j = 0; j < n; ++j) { g[i][j] = f(g[i][j], g[i][k], g[k][j]); }
    }
  }
  return g;
}
