#pragma once

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

// void _test_pow() {
//   const int m = 1000000007;

//   struct G {
//     static auto op(long x, long y) -> long { return x * y % m; }
//     static auto e() -> long { return 1; }
//     static auto inv(long x) -> long { return pow<G>(x, m - 2); }
//   };

//   assert(pow(2, 10) == 1024);
//   assert(pow<G>(2, -1) == 500000004);
//   assert(pow_r<G>(2, -1) == 500000004);
//   _passed("pow");
// }
