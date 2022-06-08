#include "../../data_structure/graph.cpp"

// TODO cut below

#include <vector>
#include <functional>
#include <queue>
#include <limits>



namespace graph_theory::maximum_flow {
  template <typename T> struct EdmondsKarpData { T capacity; };
  template <typename T> using EdmondsKarpGraph = DenseDirectedGraph<void *, EdmondsKarpData<T>>;
  

  template <typename T> 
  T edmonds_karp(EdmondsKarpGraph<T> g, int src, int sink) {
    int n = g.nodes.size();
    T inf = std::numeric_limits<T>::max();
    std::vector<int> prev(n, -1);
    std::vector<bool> visited(n);
    std::queue<int> fifo_que; 

    std::function<void()> find_path = [&]() -> void {
      std::fill(prev.begin(), prev.end(), -1);
      std::fill(visited.begin(), visited.end(), false);
      visited[src] = true;
      fifo_que.push(src);
      while (!fifo_que.empty()) {
        int u = fifo_que.front(); fifo_que.pop();
        for (int v = 0; v < n; v++) {
          if (visited[v] || g.edges[u][v].capacity == 0) continue;
          visited[v] = true;
          prev[v] = u;
          fifo_que.push(v);
        }          
      }
    };

    std::function<T()> augment_flow = [&]() -> T {
      int u, v = sink;
      T flow = inf;
      while (prev[v] != -1) {
        u = prev[v];
        flow = std::min(flow, g.edges[u][v].capacity);
        v = u;          
      }
      if (flow == inf) return 0;
      v = sink;
      while (prev[v] != -1) {
        u = prev[v];
        g.edges[u][v].capacity -= flow;
        g.edges[v][u].capacity += flow;
        v = u;
      }
      return flow;
    };

    T flow = 0;
    while (1) {
      find_path();
      T f = augment_flow();
      if (f == 0) return flow;
      flow += f;
    }
  }
}
