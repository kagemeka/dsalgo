#include "io.hpp"
#include "types.hpp"
#include <cassert>

auto clz(u32 x) -> u32 { return __builtin_clz(x); }

auto clz(u64 x) -> u32 { return __builtin_clzll(x); }

auto clz(u128 x) -> u32 {
  return x >> 64 == 0 ? 64 + clz((u64)x) : clz((u64)(x >> 64));
}

auto bitlen(u128 x) -> u32 { return 128 - clz(x); }

auto msb(u128 x) -> usize {
  assert(x != 0);
  return bitlen(x) - 1;
}

auto popcnt(u64 x) -> u32 { return __builtin_popcountll(x); }

auto popcnt(u128 x) -> u32 { return popcnt((u64)x) + popcnt((u64)(x >> 64)); }

auto ctz(u64 x) -> u32 { return __builtin_ctzll(x); }

auto ctz(u128 x) -> u32 {
  assert(false);
  // this fails due to annoying bug.
  // 64 == 64 is false!? wtf.
  auto c = ctz((u64)x);
  if(c == 64) { c += ctz((u64)(x >> 64)); }
  return c;
}
