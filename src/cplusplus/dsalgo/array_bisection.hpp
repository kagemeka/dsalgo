#include <algorithm>

template <typename T, typename A>
auto lower_bound(A a, T x) -> int {
  return std::lower_bound(a.begin(), a.end(), x) - a.begin();
}

template <typename T, typename A>
auto upper_bound(A a, T x) -> int {
  return std::upper_bound(a.begin(), a.end(), x) - a.begin();
}
