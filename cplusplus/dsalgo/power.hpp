#pragma once
template<typename T, typename Z> auto power(T x, Z n) -> T {
  if (n < 0) {
    x = 1 / x;
    n *= -1;
  }
  T y = 1;
  for (; n; x *= x, n >>= 1)
    if (n & 1)
      y *= x;
  return y;
}
