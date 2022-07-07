#pragma once

template<typename G, typename T, typename Z>
auto pow_semigroup_recurse(T x, Z n) -> T {
  assert(n >= 1);
  if(n == 1) return x;
  auto y = pow_semigroup_recurse<G>(x, n >> 1);
  y = G::op(y, y);
  if(n & 1) y = G::op(y, x);
  return y;
}
