#pragma once

template<typename T, typename N> auto power(T x, N n) -> T {
  T y = 1;
  while(n) {
    if(n & 1) y *= x;
    x *= x;
    n >>= 1;
  }
  return y;
}
