#include "./modular.hpp"

template <typename mint>
struct mod_mul {
  static auto operate(const mint& a, const mint& b) -> mint { return a * b; }
  static auto identity() -> mint { return 1; }
  static auto invert(const mint& a) -> mint { return 1 / a; }
};
