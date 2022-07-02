#pragma once

template <typename T>
auto modular_inverse_euclidean(T mod, T n) -> T {
  auto [g, inv] = euclidean_modular_gcd_inv(mod, n);
  assert(g == 1);
  return inv;
}
