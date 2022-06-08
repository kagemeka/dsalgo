#include <vector>

template<typename T>
std::vector<T> longest_increasing_sequence(const std::vector<T>& a) {
  T inf = std::numeric_limits<T>::max();
  std::vector<T> lis(a.size(), inf);
  for (const T& x: a) *std::lower_bound(lis.begin(), lis.end(), x) = x;
  auto i = std::lower_bound(lis.begin(), lis.end(), inf);
  return std::vector<T>(lis.begin(), i);
}
