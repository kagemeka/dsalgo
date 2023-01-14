#pragma once
template<typename T, typename F> auto replace(F f, T& a, const T& b) -> void {
  a = f(a, b);
}
