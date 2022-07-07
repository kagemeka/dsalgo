// TODO:

#include <bits/stdc++.h>
using namespace std;

template<typename T> struct Edge {
public:
  T weight, capacity;

  Edge(T weight = 1, T capacity = 1): weight(weight), capacity(capacity) {}
};

template<typename T> struct Node {};

template<typename T> struct Graph {
public:
  Graph(int n = 0): edges(n), nodes(n) {}

  void add_edge(int u, int v, T weight = 1, T capacity = 1) {
    edges[u].emplace(v, Edge<T>(weight, capacity));
  }

  vector<map<int, Edge<T>>> edges;

  vector<Node<T>> nodes;

  vector<int> level;

  void bfs(int source = 0) {
    int n = (int)nodes.size();
    level = vector<int>(n, -1);
    level[source] = 0;
    queue<int> que;
    que.push(source);
    while(!que.empty()) {
      int u = que.front();
      que.pop();
      for(auto const& p: edges[u]) {
        int v = p.first;
        Edge<T> e = p.second;
        if(level[v] != -1) { continue; }
        level[v] = level[u] + 1;
        que.push(v);
      }
    }
  }
};
