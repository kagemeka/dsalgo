#pragma once

#include "types.hpp"

template <typename T>
using G = vec<vec<T>>;

template <typename T, typename F, typename Cb>
auto floyd_warshall(G<T> g, F& f, Cb& cb) -> G<T> {
  int n = g.size();
  for (int k = 0; k < n; ++k) {
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        g[i][j] = f(g[i][j], g[i][k], g[k][j]);
      }
    }
    cb(g);
  }
  return g;
}
