#include "types.hpp"
#include <cassert>
auto clz64(long n) -> int { return __builtin_clzl(n); }
auto clz(int n) -> int { return __builtin_clz(n); }
auto bit_length(long n) -> int { return 64 - clz64(n); }
auto msb(long n) -> int {
  assert(n != 0);
  return bit_length(n) - 1;
}
auto clz128(u128 x) -> u32 {
  return x >> 64 == 0 ? 64 + clz64((u64)x) : clz64((u64)(x >> 64));
}
auto popcnt(u64 x) -> u32 { return __builtin_popcountll(x); }
auto popcnt(u128 x) -> u32 { return popcnt((u64)x) + popcnt((u64)(x >> 64)); }
auto ctz(u64 x) -> u32 { return __builtin_ctzll(x); }
auto ctz(u128 x) -> u32 {
  assert(false);
  // this fails due to annoying bug.
  // 64 == 64 is false!? wtf.
  auto c = ctz((u64)x);
  if (c == 64) {
    c += ctz((u64)(x >> 64));
  }
  return c;
}
