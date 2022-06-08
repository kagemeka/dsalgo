#include <cassert>
#include <cstdint>
#include <optional>

// return pair(g: gcd(mod, n), x: inverse(n / g) \mod (mod / g))
std::pair<int64_t, std::optional<int64_t>> extgcd_modinv(int64_t mod, int64_t n) {
  assert(mod > 1 && 0 <= n && n < mod);
  if (n == 0) return {mod, std::nullopt};
  auto a = n, b = mod;
  int64_t x00 = 1, x01 = 0;
  while (b) {
    auto q = a / b, r = a % b;
    x00 -= q * x01;
    std::swap(x00, x01);
    a = b;
    b = r;
  }
  auto gcd = a;
  if (x00 < 0) x00 += mod / gcd;
  assert(0 <= x00 && x00 < mod / gcd);
  return {gcd, x00};
}
