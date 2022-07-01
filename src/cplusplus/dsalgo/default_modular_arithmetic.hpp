#pragma once
#include "modular_inverse_euclidean.hpp"

template <typename M>
class default_modular_arithmetic {

public:
  constexpr auto static mod() -> int { return M::get(); }

  constexpr auto static norm(int x) -> int {
    if (x < -mod() || mod() <= x) {
      x %= mod();
    }
    return x += (x < 0) * mod();
  }

  constexpr auto static add(int a, int b) -> int { return norm(a + b); }

  constexpr auto static neg(int a) -> int {
    auto v = norm(a);
    return v == 0 ? 0 : mod() - v;
  }

  constexpr auto static mul(int a, int b) -> int {
    return norm((long)a * b % mod());
  }

  constexpr auto static inv(int a) -> int {
    return modular_inverse_euclidean(mod(), norm(a));
  }
};
