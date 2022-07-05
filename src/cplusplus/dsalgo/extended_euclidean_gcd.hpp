#include <tuple>

template<typename T> auto extended_euclidean_gcd(T a, T b)
  -> std::tuple<T, T, T> {
  using std::swap;
  T x00 = 1, x01 = 0, x10 = 0, x11 = 1;
  while(b != 0) {
    T q = a / b;
    a %= b, swap(a, b);
    x00 -= q * x01, swap(x00, x01);
    x10 -= q * x11, swap(x10, x11);
  }
  return {a, x00, x10};
}
