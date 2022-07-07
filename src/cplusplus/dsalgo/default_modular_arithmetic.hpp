#pragma once
#include "modular_inverse_euclidean.hpp"
template<typename M> class default_modular_arithmetic {
public:
  constexpr static auto mod() -> int { return M::get(); }
  constexpr static auto norm(int x) -> int {
    if(x < -mod() || mod() <= x) { x %= mod(); }
    return x += (x < 0) * mod();
  }
  constexpr static auto add(int a, int b) -> int { return norm(a + b); }
  constexpr static auto neg(int a) -> int {
    auto v = norm(a);
    return v == 0 ? 0 : mod() - v;
  }
  constexpr static auto mul(int a, int b) -> int {
    return norm((long)a * b % mod());
  }
  constexpr static auto inv(int a) -> int { return modinv(mod(), norm(a)); }
};
