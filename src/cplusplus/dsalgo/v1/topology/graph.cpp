#include <bits/stdc++.h>
using namespace std;

template<typename T>
struct Edge {

public:

T weight, capacity;

Edge(
  T weight=1, T capacity=1
)
: weight(weight),
  capacity(capacity)
{}
};


template<typename T>
struct Node {};


template<typename T>
struct Graph {

public:

Graph(int n=0)
: edges(n), nodes(n)
{}

void add_edge(
  int u, int v,
  T weight=1, T capacity=1
) {
  edges[u].emplace(
    v,
    Edge<T>(weight, capacity)
  );
}

vector<map<int, Edge<T>>>
  edges;

vector<Node<T>> nodes;


vector<int> level;


void bfs(int source=0)
{
  int n = (int)nodes.size();
  level = vector<int>(n, -1);
  level[source] = 0;
  queue<int> que;
  que.push(source);
  while (!que.empty())
  {
    int u = que.front();
    que.pop();
    for (
      const auto& p: edges[u])
    {
      int v = p.first;
      Edge<T> e = p.second;
      if (level[v] != -1)
      {
        continue;
      }
      level[v] = level[u] + 1;
      que.push(v);
    }
  }
}

};

template<typename T>
class ShortestPath {
};

template<typename T>
class FloydWarshall
: public Graph<T>
{

private:

vector<vector<T>> dist;

void make_dist_matrix() {
  int n = (int)nodes.size();
  T inf =
    numeric_limits<T>::max();
  dist = vector<vector<T>>(
    n,
    vector<T>(n, inf>>1)
  )
  for (int u = 0; u < n; u++)
  {
    dist[u][u] = 0;
    for (
      const auto& p: edges[u])
    {
      int v = edges.first;
      Edge e = edges.second;
      d[u][v] = e.weight;
    }
  }
}


void update(
  int src,
  int dst,
  int mid,
) {
  dist[src][dst] = min(
    dist[src][dst],
    dist[src][mid]
      + dist[mid][dst],
  );
}


void update_via_mid(int w) {
  int n = (int)nodes.size();
  for (int u = 0; u < n; u++)
  {
    for (int v = 0; v < n; v++)
    {
      update(u, v, w);
    }
  }
}


public:

vector<vector<T>> compute() {
  make_dist_matrix();
  for (int w = 0; w < n; w++)
  {
    update_via_mid(w);
  }
  return dist;
}
};
