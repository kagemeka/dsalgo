#pragma once

template<typename G, typename F> auto bellman_ford_abstract(const G& edges, F f)
  -> void {
  while(true) {
    bool updated = false;
    for(auto& e: edges) { updated |= f(e); }
    if(!updated) break;
  }
}
