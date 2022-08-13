#pragma once
template<typename A> auto zeta(A f) -> A {
  int n = f.size();
  for(int i = 1; i < n; i++) {
    for(int j = i << 1; j < n; j += i) f[i] += f[j];
  }
  return f;
}
template<typename A> auto mobius(A f) -> A {
  int n = f.size();
  for(int i = n - 1; i > 0; i--) {
    for(int j = i << 1; j < n; j += i) f[i] -= f[j];
  }
  return f;
}
