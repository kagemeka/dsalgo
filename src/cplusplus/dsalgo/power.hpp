#include <cstdint>

template <typename S, typename G>
auto pow_semigroup_recurse(const S& s, uint64_t n) -> S {
  assert(n > 0);
  if (n == 1) return s;
  S x = pow_semigroup_recurse<S, G>(s, n >> 1);
  x = G::operate(x, x);
  if (n & 1) x = G::operate(x, s);
  return x;
}

template <typename S, typename G>
auto pow_semigroup(S s, uint64_t n) -> S {
  assert(n > 0);
  S x = s;
  --n;
  while (n > 0) {
    if (n & 1) x = G::operate(x, s);
    s = G::operate(s, s);
    n >>= 1;
  }
  return x;
}

template <typename S, typename M>
auto pow_monoid(const S& s, uint64_t n) -> S {
  if (n == 0) return M::identity();
  return pow_semigroup<S, M>(s, n);
}

template <typename S, typename G>
auto pow_group(const S& s, int64_t n) -> S {
  return n >= 0 ? pow_monoid<S, G>(s, n) : pow_monoid<S, G>(G::invert(s), -n);
}
