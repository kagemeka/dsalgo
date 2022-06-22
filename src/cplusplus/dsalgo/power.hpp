#include <cstdint>
// pow on Group like structure.
template <typename G, typename T, typename Z>
auto pow(T x, Z n) -> T {
  if (n == 0) return G::e();
  if (n < 0) {
    x = G::inv(x);
    n = -n;
  }
  T y = x;
  --n;
  while (n) {
    if (n & 1) y = G::op(y, x);
    x = G::op(x, x);
    n >>= 1;
  }
  return y;
}

// recursive
template <typename G, typename T, typename Z>
auto pow_r(T x, Z n) -> T {
  if (n == 0) return G::e();
  if (n < 0) {
    return pow_r<G>(G::inv(x), -n);
  }
  if (n == 1) return x;
  auto y = pow_r<G>(x, n >> 1);
  y = G::op(y, y);
  if (n & 1) y = G::op(y, x);
  return y;
}

// pow on Fp
template <typename T, typename Z>
auto pow(T x, Z n) -> T {
  T y = 1;
  while (n) {
    if (n & 1) y *= x;
    x *= x;
    n >>= 1;
  }
  return y;
}

auto _test_pow() {
  const int m = 1000000007;

  struct G {
    static auto op(i64 x, i64 y) -> i64 { return x * y % m; }
    static auto e() -> i64 { return 1; }
    static auto inv(i64 x) -> i64 { return pow<G>(x, m - 2); }
  };

  assert(pow(2, 10) == 1024);
  assert(pow<G>(2, -1) == 500000004);
  assert(pow_r<G>(2, -1) == 500000004);
  _passed("pow");
}
