#pragma once

#include <type_traits>

template <typename T, T v, std::enable_if_t<2 <= v>* = nullptr>
struct const_modulus {
  static constexpr auto get() -> T { return v; }
};
