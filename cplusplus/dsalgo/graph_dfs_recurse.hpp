#pragma once
#include <functional>
using namespace std;
template<typename G, typename F>
auto graph_dfs(const G &g, F f, int src) -> void {
  function<void(int)> dfs;
  dfs = [&](int u) -> void {
    for (auto &v: g[u])
      if (f(u, v))
        dfs(v);
  };
  dfs(src);
}
