#pragma once
#include "extended_euclidean_gcd_recurse.hpp"

template <typename T>
auto euclidean_modular_gcd_inv(T mod, T n) -> std::pair<T, T> {
  auto [g, x, _] = extended_euclidean_gcd_recurse(n, mod);
  auto u = mod / g;
  assert(0 <= (x += (x < 0) * u) && x <= u);
  return {g, x};
}