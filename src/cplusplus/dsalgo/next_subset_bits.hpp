#pragma once
#include <cassert>
// find next t \subseteq s
template<typename T> auto next_subset_bits(const T& s, T t) -> T {
  assert(t > 0);
  return --t & s;
}
