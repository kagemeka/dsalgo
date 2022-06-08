#include <vector>


namespace graph_theory {
  template<typename T> struct Edge { const int u, v; T data; };


  template<typename T, typename U>
  struct SparseDirectedGraph {
    using E = Edge<U>;  // G::E edge{u, v, data};
    std::vector<T> nodes;
    std::vector<std::vector<E>> edges;    
    SparseDirectedGraph(int n) : nodes(n), edges(n) {}
    void add_edge(const E &e) { edges[e.u].push_back(e); }
  };


  template <typename T, typename U>
  struct DenseDirectedGraph {
    std::vector<T> nodes;
    std::vector<std::vector<U>> edges;
    DenseDirectedGraph(int n) : nodes(n), edges(n, std::vector<U>(n)) {}
    std::vector<U>& operator[](int i) { return edges[i]; } 
  };


  template <typename T, typename U>
  struct UndirectedGraph {
    using E = Edge<U>;
    std::vector<T> nodes;
    std::vector<E> edges;
    UndirectedGraph(int n) : nodes(n) {}
    SparseDirectedGraph<T, U> to_directed() const {
      SparseDirectedGraph<T, U> g(nodes.size());
      g.nodes = nodes;
      for (const E &e : edges) {
        g.add_edge(e);
        g.add_edge(E{e.v, e.u, e.data});
      };
      return g;
    }
  };
};