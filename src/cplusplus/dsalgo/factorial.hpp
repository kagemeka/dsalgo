
#include "./accumulate.hpp"
#include "./ops.hpp"
#include "rust_types.hpp"
#include <cassert>
#include <numeric>
#include <vector>

template <typename S>
auto factorials(usize n) -> vec<S> {
  assert(n > 0);
  vec<S> a(n);
  std::iota(entire(a), 0);
  a[0] = 1;
  return arr::accum<S>([](S a, S b) { return a * b; }, a);
}

template <typename S>
auto inv_factorials(usize n) -> vec<S> {
  vec<S> a(n);
  std::iota(entire(a), 1);
  a[n - 1] = 1 / factorials<S>(n)[n - 1];
  reverse(entire(a));
  a = arr::accum<S, mul<S>>(a);
  reverse(entire(a));
  return a;
}

template <typename S>

auto invs(usize n) -> vec<S> {}