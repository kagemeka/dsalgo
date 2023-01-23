// #define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
/* Algebra */
namespace Algebra {
constexpr long long MOD = 1e9 + 7;
// constexpr long long MOD = 998244353;
long double const PI = acos(-1);
constexpr long double EPS = 1e-13;
} // namespace Algebra
using namespace Algebra;
/* Combinatorics */
namespace Combinatorics {
template<typename T> auto next_combination(T s) -> T {
  T x = s & -s, y = s + x;
  return ((s & ~y) / x) >> 1 | y;
}
template<typename T> auto combinations(T a, int r) -> vector<T> {
  int n = a.size();
  vector<T> res;
  if (r > n || r < 0)
    return res;
  vector<int> indices(r);
  for (int i = 0; i < r; i++) indices[i] = i;
  res.push_back(T(a.begin(), a.begin() + r));
  while (true) {
    bool flg = false;
    int i = r - 1;
    for (; i > -1; i--) {
      if (indices[i] != i + n - r) {
        flg = true;
        break;
      }
    }
    if (!flg) {
      return res;
    }
    indices[i]++;
    for (int j = i + 1; j < r; j++) { indices[j] = indices[j - 1] + 1; }
    T tmp(r);
    for (int j = 0; j < r; j++) tmp[j] = a[indices[j]];
    res.push_back(tmp);
  }
  return res;
}
} // namespace Combinatorics
using namespace Combinatorics;
/* Geometry and Topology */
namespace GeometryTopology {
template<typename... T> struct Vector {
public:
  Vector(T... args) {}
};
// to vector crossing algorithm later.
/* Graph */
template<typename T> struct Graph {
public:
  /* Tree Doubling For Finding LCA */
  void find_ancestors() {
    ancestors.push_back(parent);
    for (int i = 0, l = bit_length(*max_element(depth.begin(), depth.end()));
         i < l;
         i++) {
      auto ancestor = *prev(ancestors.end());
      auto nxt_ancestor(N)->vector<int>;
      for (int u = 0; u < N; u++) { nxt_ancestor[u] = ancestor[ancestor[u]]; }
      ancestors.push_back(nxt_ancestor);
    }
  }
  /* Find dist(u, v) on Tree.*/
  auto find_dist(int u, int v) -> T {
    return dist[u] + dist[v] - 2 * dist[find_lca(u, v)];
  }
  auto find_lca(int u, int v) -> int {
    int du = depth[u], dv = depth[v];
    if (du > dv) {
      swap(u, v);
      swap(du, dv);
    }
    int d = dv - du;
    for (int i = 0, l = bit_length(d); i < l; i++) {
      if (d >> i & 1)
        v = ancestors[i][v];
    }
    if (u == v)
      return u;
    for (int i = bit_length(du) - 1; i > -1; i--) {
      int nu = ancestors[i][u], nv = ancestors[i][v];
      if (nu == nv)
        continue;
      u = nu, v = nv;
    }
    return parent[u];
  }
  auto dijkstra(int src) -> vector<T> {
    using P = pair<T, int>;
    priority_queue<P, vector<P>, greater<P>> q;
    q.push(P(0, src));
    paths = vector<int>(N, 0);
    paths[src] = 1;
    vector<T> dist(N, INF / 10);
    dist[src] = 0;
    vector<bool> visited(N, false);
    while (!q.empty()) {
      auto tmp = q.top();
      q.pop();
      T d = tmp.first;
      int u = tmp.second;
      if (visited[u]) {
        continue;
      }
      visited[u] = true;
      for (auto &p: edges[u]) {
        int v = p.first;
        edge e = p.second;
        T dv = d + e.weight;
        if (dv >= dist[v]) {
          if (dv == dist[v]) {
            paths[v] = (paths[v] + paths[u]) % MOD;
          }
          continue;
        }
        paths[v] = paths[u];
        dist[v] = dv;
        q.push(P(dv, v));
      }
    }
    return dist;
  }
  auto shortest_paths(int src) -> vector<int> {
    dijkstra(src);
    return paths;
  }
  void change_cap(int u, int v, T c) { edges[u].find(v)->second.capacity = c; }
  vector<int> lv;
  vector<int> depth;
  T INF = numeric_limits<T>::max();
  vector<T> dist;
  vector<int> parent;
  vector<vector<int>> ancestors;
  vector<int> paths;
};
struct UnionFind {
public:
  UnionFind(int n = 0): parent(n), rank(n), size(n, 1) {
    N = n;
    for (int i = 0; i < n; i++) parent[i] = i;
  }
  auto find(int u) -> int {
    if (parent[u] == u)
      return u;
    return parent[u] = find(parent[u]);
  }
  void unite(int u, int v) {
    u = find(u), v = find(v);
    if (u == v)
      return;
    if (rank[u] < rank[v])
      swap(u, v);
    parent[v] = u;
    size[u] += size[v];
    rank[u] = max(rank[u], rank[v] + 1);
  }
  auto same(int u, int v) -> bool { return find(u) == find(v); }
  vector<int> size;
  vector<int> rank;

private:
  int N;
  vector<int> parent;
};
template<typename T> struct Rectangle {
  T x1, y1, x2, y2;
  Rectangle(T _x1, T _y1, T _x2, T _y2): x1(_x1), y1(_y1), x2(_x2), y2(_y2) {}
  auto operator<(Rectangle const &r) const -> bool {
    if (this->x1 != r.x1) {
      return this->x1 < r.x1;
    }
    if (this->y1 != r.y1) {
      return this->y1 < r.y1;
    }
    if (this->x2 != r.x2) {
      return this->y1 < r.x2;
    }
    if (this->y2 != r.y2) {
      return this->y2 < r.y2;
    }
  }
};
} // namespace GeometryTopology
using namespace GeometryTopology;
namespace Algebra {
template<typename T>
auto bitwise_dot(vector<vector<T>> &a, vector<vector<T>> &b)
    -> vector<vector<T>> {
  int h = a.size(), w = b[0].size(), l = b.size();
  assert((int)a[0].size() == l);
  vector<vector<T>> c(h, vector<T>(w));
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      for (int k = 0; k < l; k++) { c[i][j] ^= a[i][k] & b[k][j]; }
    }
  }
  return c;
}
template<typename T>
auto bitwise_mat_pow(vector<vector<T>> a, T n) -> vector<vector<T>> {
  int m = a.size();
  vector<vector<T>> b = identity<T>(m);
  for (int i = 0; i < m; i++) b[i][i] = numeric_limits<T>::max();
  while (n) {
    if (n & 1)
      b = bitwise_dot(b, a);
    n >>= 1;
    a = bitwise_dot(a, a);
  }
  return b;
}
template<typename T> auto gcd(T a, T b) -> T { return __gcd(a, b); }
template<typename T> auto lcm(T a, T b) -> T { return a / gcd(a, b) * b; }
/* NumberTheory */
namespace NumberTheory {
template<typename T> struct PrimeNumber {
public:
  PrimeNumber(): prime_nums(0) {
    is_prime.set();
    is_prime[0] = is_prime[1] = 0;
    for (T i = 2; i < N; i++) {
      if (!is_prime[i])
        continue;
      for (T j = i * 2; j < N; j += i) is_prime[j] = 0;
    }
    for (T i = 0; i < N; i++) {
      if (is_prime[i])
        prime_nums.emplace_back(i);
    }
  }
  auto operator[](int i) -> T & { return prime_nums[i]; }
  auto operator()(T n) -> bool { return is_prime[n]; }
  auto factorize(T n) -> map<T, int> {
    map<T, int> cnt;
    if (n < 2)
      return cnt;
    for (T &p: prime_nums) {
      if (p * p > n)
        break;
      while (!(n % p)) {
        cnt[p]++;
        n /= p;
      }
      if (n == 1)
        return cnt;
    }
    cnt[n] = 1;
    return cnt;
  }
  auto factorize_factorial(T n) -> map<T, int> {
    map<T, int> cnt;
    for (T i = 2; i < n + 1; i++) {
      for (auto &x: factorize(i)) { cnt[x.first] += x.second; }
    }
    return cnt;
  }

private:
  const T N = 1e7;
  bitset<(T)1e7> is_prime;
  vector<T> prime_nums;
};
