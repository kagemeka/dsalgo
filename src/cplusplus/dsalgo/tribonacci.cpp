#include <vector>

template <typename T>
std::vector<T> tribonacci_sequence(int n) {
  assert(n >= 3);
  std::vector<T> t(n);
  t[2] = 1;
  for (int i = 3; i < n; i++) t[i] = t[i - 1] + t[i - 2] + t[i - 3];
  return t;
}