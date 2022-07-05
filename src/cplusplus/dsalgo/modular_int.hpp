#pragma once
#include <iostream>
using namespace std;

template<typename M> struct modint {
  using T = typename std::decay<decltype(M::get())>::type;

  T value;

  using Self = modint;

  constexpr static auto m() -> T { return M::get(); }

  template<typename U> constexpr static auto norm(const U& x) -> T {
    T v = x;
    if(v < -m() || m() <= v) v %= m();
    return v + (v < 0) * m();
  }

  constexpr modint(): value() {}

  template<typename U> modint(const U& x): value(norm(x)) {}

  auto operator()() -> const T& { return value; }

  template<typename T> explicit operator T() const {
    return static_cast<T>(value);
  }

  auto operator+=(Self const& rhs) -> Self& {
    value += rhs.value;
    value -= (value >= m()) * m();
    return *this;
  }

  auto operator-() const -> Self {
    return Self(value == 0 ? value : m() - value);
  }

  auto operator*=(Self const& rhs) -> Self& {
    value *= rhs.value;
    if(value >= m()) value %= m();
    return *this;
  }

  [[nodiscard]] auto inv() const -> Self { return Self(modinv(m(), value)); }

  auto operator-=(Self const& rhs) -> Self& { return *this += -rhs; }

  auto operator/=(Self const& rhs) -> Self& { return *this *= rhs.inv(); }

  auto operator++() -> Self& { return *this += 1; }

  auto operator--() -> Self& { return *this -= 1; }

  auto operator++(int) -> Self {
    Self res(*this);
    *this += 1;
    return res;
  }

  auto operator--(int) -> Self {
    Self res(*this);
    *this -= 1;
    return res;
  }

  friend auto operator+(Self const& lhs, Self const& rhs) -> Self {
    return Self(lhs) += rhs;
  }

  friend auto operator-(Self const& lhs, Self const& rhs) -> Self {
    return Self(lhs) -= rhs;
  }

  friend auto operator*(Self const& lhs, Self const& rhs) -> Self {
    return Self(lhs) *= rhs;
  }

  friend auto operator/(Self const& lhs, Self const& rhs) -> Self {
    return Self(lhs) /= rhs;
  }

  friend auto operator==(Self const& lhs, Self const& rhs) -> bool {
    return lhs.value == rhs.value;
  }

  friend auto operator!=(Self const& lhs, Self const& rhs) -> bool {
    return lhs.value != rhs.value;
  }

  friend auto operator>>(std::istream& stream, Self& x) -> std::istream& {
    T v;
    stream >> v;
    x.value = norm(v);
    return stream;
  }

  friend auto operator<<(std::ostream& stream, Self const& x) -> std::ostream& {
    return stream << x.value;
  }
};
