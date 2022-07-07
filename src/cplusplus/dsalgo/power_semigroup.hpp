#pragma once
template<typename G, typename T, typename Z> auto pow_semigroup(T x, Z n) -> T {
  assert(n >= 1);
  T y = x;
  while(--n) {
    if(n & 1) y = G::op(y, x);
    x = G::op(x, x);
    n >>= 1;
  }
  return y;
}
