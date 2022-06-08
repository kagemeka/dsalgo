#include "./modular.hpp"

template <typename mint> struct mod_mul {
  static mint operate(const mint& a, const mint& b) { return a * b; }
  static mint identity() { return 1; }
  static mint invert(const mint& a) { return 1 / a; }
};
