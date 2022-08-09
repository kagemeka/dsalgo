#pragma once
template<typename T, typename N> auto power(T x, N n) -> T {
  T y = 1;
  for(; n; x *= x, n >>= 1)
    if(n & 1) y *= x;
  return y;
}
