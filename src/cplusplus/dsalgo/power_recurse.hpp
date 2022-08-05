#pragma once
template<typename T, typename N> auto power(T x, N n) -> T {
  if(n == 1) return x;
  auto y = power(x, n >> 1);
  y *= y;
  if(n & 1) y *= x;
  return y;
}
