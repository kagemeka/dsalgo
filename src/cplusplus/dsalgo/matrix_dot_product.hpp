#include <vector>

// T: semiring
template <typename T, typename M>
auto matrix_dot(const M& a, const M& b) -> M {
  assert(a[0].size() == b.size());
  int h = a.size(), w = b[0].size();
  M c(h, std::vector<T>(w));
  for (int i = 0; i < h; ++i) {
    for (int j = 0; j < w; ++j) {
      for (int k = 0; k < (int)a[0].size(); ++k) {
        c[i][j] += a[i][k] * b[k][j];
      }
    }
  }
  return c;
}
