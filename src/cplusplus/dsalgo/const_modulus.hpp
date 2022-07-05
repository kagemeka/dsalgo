#pragma once

#include <type_traits>
using namespace std;

template<typename T, T v, enable_if_t<(v > 0)>* = nullptr> struct const_mod {
  static constexpr auto get() -> T { return v; }
};
