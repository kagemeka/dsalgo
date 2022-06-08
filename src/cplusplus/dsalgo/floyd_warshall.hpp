#include <stdexcept>
#include <vector>

template <typename T>
std::vector<std::vector<T>> floyd_warshall(const std::vector<std::vector<T>>& min_edge_matrix) {
  auto dist = min_edge_matrix;
  unsigned long int n = dist.size();
  for (unsigned long int i = 0; i < n; ++i) assert(dist[i].size() == n);
  for (unsigned long int i = 0; i < n; ++i) {
    dist[i][i] = std::min(dist[i][i], 0);
  }
  for (unsigned long int k = 0; k < n; ++k) {
    for (unsigned long int i = 0; i < n; ++i) {
      for (unsigned long int j = 0; j < n; ++j) {
        dist[i][j] = std::min(dist[i][j], dist[i][k] + dist[k][j]);
      }
    }
  }
  for (unsigned long int i = 0; i < n; ++i) {
    if (dist[i][i] < 0) {
      throw std::logic_error("negative cycle found.");
    }
  }
  return dist;
}