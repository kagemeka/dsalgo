#pragma once
#include "power_monoid.hpp"
#include "power_semigroup.hpp"

template <typename G, typename T, typename Z>
auto pow_group(T x, Z n) -> T {
  return n >= 0 ? pow_monoid<G>(x, n) : pow_semigroup<G>(G::inv(x), -n);
}
