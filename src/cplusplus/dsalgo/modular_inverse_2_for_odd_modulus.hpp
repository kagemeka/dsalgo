#pragma once

template<typename T> auto inverse_2_for_odd_modulus(T mod) -> T {
  return (mod + 1) >> 1;
}
