// TODO:

#include "../../data_structure/graph.cpp"

// TODO cut below

#include <functional>
#include <limits>
#include <queue>
#include <vector>

namespace graph_theory::maximum_flow {
  template <typename T>
  struct DinicData {
    T capacity;
  };
  template <typename T>
  using DinicGraph = SparseDirectedGraph<void*, DinicData<T>>;

  template <typename T>
  auto dinic(DinicGraph<T> g, int src, int sink) -> T {
    int n = g.nodes.size();
    std::vector<int> level(n, -1);
    std::function<void()> update_level = [&]() -> void {
      for (int i = 0; i < n; i++) level[i] = -1;
      level[src] = 0;
      std::queue<int> fifo_que;
      fifo_que.push(src);
      while (!fifo_que.empty()) {
        int u = fifo_que.front();
        fifo_que.pop();
        for (const auto& e : g.edges[u]) {
          if (level[e.v] != -1 || e.data.capacity == 0) continue;
          level[e.v] = level[u] + 1;
          fifo_que.push(e.v);
        }
      }
    };

    std::function<T(int, T)> flow_to_sink = [&](int u, T flow_in) -> T {
      if (u == sink) return flow_in;
      if (flow_in == 0) return 0;
      T flow_out = 0;
      auto edges = g.edges[u];
      g.edges[u].clear();
      for (auto& e : edges) {
        if (e.data.capacity == 0) continue;
        if (level[e.v] <= level[u]) {
          g.add_edge(e);
          continue;
        }
        T flow = flow_to_sink(e.v, std::min(flow_in, e.data.capacity));
        if ((e.data.capacity -= flow) > 0) g.add_edge(e);
        if (flow > 0) g.add_edge({e.v, u, {flow}});
        flow_in -= flow;
        flow_out += flow;
      }
      return flow_out;
    };

    T inf = std::numeric_limits<T>::max();
    T flow = 0;
    while (true) {
      update_level();
      if (level[sink] == -1) return flow;
      flow += flow_to_sink(src, inf);
    }
  };
  // e.g. using G = graph_theory::maximum_flow::DinicGraph<long long>;
} // namespace graph_theory::maximum_flow
