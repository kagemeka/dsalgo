// test: passed
// TODO: more test cases.

#include "./rust_types.hpp"
#include <cassert>

namespace dsalgo::euclidean_modular_gcd_inv {
using namespace dsalgo::rust_types;

// return pair(g: gcd(mod, n), x: inverse(n / g) \mod (mod / g))
auto euclidean_mod_gcd_inv(u64 mod, u64 n) -> std::pair<u64, u64> {
  assert(0 < n && n < mod);
  i64 a = n, b = mod;
  i64 x00 = 1, x01 = 0;
  while (b) {
    x00 -= a / b * x01;
    std::swap(x00, x01);
    a %= b;
    std::swap(a, b);
  }
  u64 gcd = a;
  u64 u = mod / gcd;
  if (x00 < 0) x00 += u;
  assert(0 <= x00 && x00 < (i64)u);
  return {gcd, x00};
}

} // namespace dsalgo::euclidean_modular_gcd_inv
