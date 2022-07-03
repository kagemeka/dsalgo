#pragma once
#include "power_semigroup.hpp"

template <typename G, typename T, typename Z>
auto pow_monoid(T x, Z n) -> T {
  assert(n >= 0);
  return n == 0 ? G::e() : pow_semigroup<G>(x, n);
}
