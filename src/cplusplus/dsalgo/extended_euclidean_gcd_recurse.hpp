#include <tuple>

template<typename T> auto extended_euclidean_gcd_recurse(T a, T b)
  -> std::tuple<T, T, T> {
  if(b == 0) { return {a, 1, 0}; }
  auto [g, x, y] = extended_euclidean_gcd_recurse(b, a % b);
  return {g, y, x - a / b * y};
}
