#pragma once
#include <queue>
using namespace std;

template<typename G, typename F> auto graph_bfs(const G& g, F f, int src)
  -> void {
  queue<int> que;
  que.push(src);
  while(que.size()) {
    int u = que.front();
    que.pop();
    for(auto& v: g[u])
      if(f(u, v)) que.push(v);
  }
}
