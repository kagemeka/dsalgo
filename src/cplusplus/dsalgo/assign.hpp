#include <algorithm>

template<typename T, typename F> auto assign(F f, T& a, const T& b) -> void {
  a = f(a, b);
}

template<typename T> auto chmin(T& a, const T& b) -> void {
  assign([](T a, T b) -> T { return std::min(a, b); }, a, b);
}

template<typename T> auto chmax(T& a, const T& b) -> void {
  assign([](T a, T b) -> T { return std::max(a, b); }, a, b);
}
