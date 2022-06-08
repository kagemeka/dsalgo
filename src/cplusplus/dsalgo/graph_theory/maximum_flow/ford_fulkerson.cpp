#include "../../data_structure/graph.cpp"

// TODO cut below

#include <vector>
#include <functional>
#include <limits>


namespace graph_theory {
  namespace maximum_flow {
    template <typename T> struct FordFulkersonData { T capacity; };
    template <typename T> using FordFulkersonGraph = DenseDirectedGraph<void *, FordFulkersonData<T>>;

    template <typename T>
    T ford_fulkerson(FordFulkersonGraph<T> g, int src, int sink) {
      int n = g.nodes.size();
      T inf = std::numeric_limits<T>::max();
      std::vector<bool> visited(n);

      std::function<T(int, T)> augment_flow = [&](int u, T flow_in) -> T {
        visited[u] = true;
        if (u == sink) return flow_in;
        for (int v = 0; v < n; v++) {
          auto &data = g.edges[u][v];
          if (visited[v] || data.capacity == 0) continue;
          T flow = augment_flow(v, std::min(flow_in, data.capacity));
          if (flow == 0) continue;
          data.capacity -= flow;
          g.edges[v][u].capacity += flow;
          return flow;
        }
        return 0;
      };

      T flow = 0;
      while (1) {
        std::fill(visited.begin(), visited.end(), false);
        T f = augment_flow(src, inf);
        if (f == 0) return flow;
        flow += f;
      }
    }
  };
};
